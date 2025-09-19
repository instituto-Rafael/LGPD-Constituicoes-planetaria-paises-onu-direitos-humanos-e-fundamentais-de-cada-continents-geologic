import os, hashlib, time, subprocess, threading, queue
from datetime import datetime

RAFA_SIGIL = "RAFAELIA-GCΩ-"+str(int(time.time()))
HONEYSTR = "∆GC-CRIME-Ω-SECRET-"+RAFA_SIGIL
HONEYFILE = f"/sdcard/{RAFA_SIGIL}.txt"
REPORT = f"/sdcard/report_{RAFA_SIGIL}.txt"
SUMMARY = f"/sdcard/summary_{RAFA_SIGIL}.txt"

KEYWORDS = [
    RAFA_SIGIL, "GC-CRIME", "SECRET", "deleted", "backup", "shadow", "upload", "cache",
    "voice", "image", "audio", "persist", "deadletter", "archive", "temp", "analytics",
    "send", "log", "outbox", "draft", "conversation", "media", "root", "hold"
]

APPS = [
    "com.whatsapp","com.google.android.inputmethod.latin","com.google.android.gms","com.facebook.orca",
    "com.instagram.android","com.facebook.katana","com.snapchat.android","com.google.android.apps.messaging",
    "com.google.android.apps.photos","com.dropbox.android","com.microsoft.office.outlook","com.twitter.android",
    "com.skype.raider","com.google.android.apps.docs","com.google.android.keep","com.spotify.music"
]

DIRS_MEDIA = [
    "/sdcard/WhatsApp/Backups", "/sdcard/Download", "/sdcard/Documents", "/sdcard/Android/data",
    "/sdcard/WhatsApp/Media", "/sdcard/DCIM", "/sdcard/Music", "/sdcard/Audio", "/sdcard/Recordings"
]

SEVERITY = {
    "SECRET": "CRÍTICO",
    "deleted": "ALTO",
    "backup": "ALTO",
    "shadow": "ALTO",
    "upload": "ALTO",
    "deadletter": "ALTO",
    "archive": "MÉDIO",
    "cache": "MÉDIO",
    "voice": "MÉDIO",
    "audio": "MÉDIO",
    "image": "MÉDIO",
    "persist": "MÉDIO",
    "temp": "BAIXO",
    "log": "BAIXO",
    "analytics": "BAIXO",
    "draft": "BAIXO",
    "outbox": "BAIXO",
    "conversation": "BAIXO",
    "media": "BAIXO",
    "root": "CRÍTICO",
    "hold": "ALTO"
}

def inject_honeyfile():
    with open(HONEYFILE,"w") as f:
        f.write(HONEYSTR)
    print(f"[+] Honeyfile criado: {HONEYFILE}")

def hash_file(path):
    with open(path, "rb") as f:
        return hashlib.sha512(f.read()).hexdigest()

def scan_dir(dirs, keywords, out_q):
    for d in dirs:
        if not os.path.exists(d): continue
        for root, _, files in os.walk(d):
            for fn in files:
                path = os.path.join(root, fn)
                try:
                    with open(path, errors='ignore') as f:
                        content = f.read()
                        for kw in keywords:
                            if kw in content:
                                out_q.put((path, kw))
                except: continue

def scan_packages(packages, keywords, out_q):
    for pkg in packages:
        datadir = f"/data/data/{pkg}/"
        if not os.path.exists(datadir): continue
        for root, _, files in os.walk(datadir):
            for fn in files:
                path = os.path.join(root, fn)
                try:
                    with open(path, errors='ignore') as f:
                        content = f.read()
                        for kw in keywords:
                            if kw in content:
                                out_q.put((path, pkg, kw))
                except: continue

def scan_logcat(keywords, out_q):
    out = subprocess.getoutput("logcat -d -v brief | tail -n 5000")
    for line in out.splitlines():
        for kw in keywords:
            if kw in line:
                out_q.put((line, kw))

def auto_classify(findings):
    classified = {}
    for path, kw in findings:
        sev = SEVERITY.get(kw,"BAIXO")
        if sev not in classified: classified[sev]=[]
        classified[sev].append((path, kw))
    return classified

def gen_report(honeyfile, found1, found2, found3, found4, logcat, sniff=None):
    with open(REPORT,"w") as r:
        r.write(f"GC-FORENSE-MAX PRO | Selo: {RAFA_SIGIL}\n")
        r.write(f"Honeyfile: {honeyfile}\nHASH: {hash_file(honeyfile)}\n")
        r.write(f"\n[1] Storage público:\n")
        for p,kw in found1: r.write(f"  {p} [chave: {kw}]\n")
        r.write(f"\n[2] Data/data apps:\n")
        for p,pkg,kw in found2: r.write(f"  {p} [APP: {pkg}] [chave: {kw}]\n")
        r.write(f"\n[3] Backups/media/voice:\n")
        for p,kw in found3: r.write(f"  {p} [chave: {kw}]\n")
        for p,kw in found4: r.write(f"  {p} [chave: {kw}]\n")
        r.write(f"\n[4] LOGCAT (últimas 5000 linhas):\n")
        for line,kw in logcat: r.write(f"  {kw}: {line}\n")
        if sniff:
            r.write(f"\n[5] Dump de tráfego salvo: {sniff}\n")
    print(f"[✔] Relatório salvo: {REPORT}\n")

def gen_summary(found1, found2, found3, found4, logcat):
    # Agrupar por severidade e tipo/app
    classified = auto_classify(found1 + found3 + found4)
    apps_viol = {}
    for p,pkg,kw in found2:
        sev = SEVERITY.get(kw,"BAIXO")
        if pkg not in apps_viol: apps_viol[pkg]=[]
        apps_viol[pkg].append((p, kw, sev))
    # Gerar sumário
    with open(SUMMARY,"w") as s:
        s.write(f"=== GC-FORENSE-MAX PRO SUMMARY [{RAFA_SIGIL}] ===\n")
        s.write(f"Horário: {datetime.now()}\n\n")
        s.write(">>> RESUMO GERAL DOS CRIMES DETECTADOS:\n")
        for sev in ["CRÍTICO","ALTO","MÉDIO","BAIXO"]:
            if sev in classified:
                s.write(f"\n[{sev}] {len(classified[sev])} ocorrências:\n")
                for p,kw in classified[sev]:
                    s.write(f"  {p} [chave: {kw}]\n")
        s.write("\n>>> VIOLAÇÕES POR APP:\n")
        for app in apps_viol:
            s.write(f"\n[APP: {app}] {len(apps_viol[app])} achados:\n")
            for p,kw,sev in apps_viol[app]:
                s.write(f"  ({sev}) {p} [chave: {kw}]\n")
        s.write("\n>>> EXTRATO DE LOGCAT:\n")
        for line,kw in logcat[:15]:
            s.write(f"  {kw}: {line}\n")
    print(f"[√] Sumário executivo salvo: {SUMMARY}\n")

def run_multithreaded_scan():
    print("[*] Iniciando varredura paralela...")
    q1, q2, q3, q4, ql = queue.Queue(), queue.Queue(), queue.Queue(), queue.Queue(), queue.Queue()
    threads = []
    # Storage comum
    t1 = threading.Thread(target=scan_dir, args=([["/sdcard/"]], KEYWORDS, q1))
    # Data/data
    t2 = threading.Thread(target=scan_packages, args=(APPS, KEYWORDS, q2))
    # Backups/mídia/voz
    t3 = threading.Thread(target=scan_dir, args=(DIRS_MEDIA, KEYWORDS, q3))
    # LOGCAT
    t4 = threading.Thread(target=scan_logcat, args=(KEYWORDS, ql))
    for t in [t1, t2, t3, t4]: t.start(); threads.append(t)
    for t in threads: t.join()
    found1, found2, found3, found4, logcat = [], [], [], [], []
    while not q1.empty(): found1.append(q1.get())
    while not q2.empty(): found2.append(q2.get())
    while not q3.empty(): found3.append(q3.get())
    while not ql.empty(): logcat.append(ql.get())
    # Média/voice scan extra (redundância)
    t5 = threading.Thread(target=scan_dir, args=([["/sdcard/Music","/sdcard/Audio","/sdcard/Recordings"]], KEYWORDS, q4))
    t5.start(); t5.join()
    while not q4.empty(): found4.append(q4.get())
    return found1, found2, found3, found4, logcat

if __name__=="__main__":
    inject_honeyfile()
    time.sleep(2)
    found1, found2, found3, found4, logcat = run_multithreaded_scan()
    #sniff = sniff_traffic(30) # Descomente se quiser captura de tráfego
    gen_report(HONEYFILE, found1, found2, found3, found4, logcat)
    gen_summary(found1, found2, found3, found4, logcat)
    print("[√] EXECUÇÃO COMPLETA! Relatório e sumário prontos para denúncia, mídia, README, petição judicial.")
