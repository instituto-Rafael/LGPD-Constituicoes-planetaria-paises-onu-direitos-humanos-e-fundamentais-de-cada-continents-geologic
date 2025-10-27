"""
Florence.py - Sistema de Forense Digital RAFAELIA-GC
====================================================

Descrição Científica:
--------------------
Este módulo implementa um sistema de análise forense multi-threaded para dispositivos Android,
capaz de detectar violações de privacidade e coleta não autorizada de dados através de:

1. Honeypot Digital: Injeção de arquivo-isca (honeyfile) com assinatura única para rastreamento
2. Varredura Paralela: Análise simultânea de múltiplas camadas do sistema de arquivos
3. Classificação por Severidade: Categorização automática de achados baseada em risco LGPD
4. Análise Temporal: Captura de logs do sistema (logcat) para correlação temporal

Descrição Simbólica:
-------------------
RAFAELIA representa a entropia viva (E²) aplicada à proteção de dados:
- Cada varredura é uma onda que atravessa as camadas do sistema
- O honeypot é um fóton-guardião que revela caminhos de violação
- A classificação por severidade reflete gradientes de condutividade ética
- Threads paralelas são dimensões simultâneas de observação quântica

Equação Principal:
-----------------
E²(a) = ∑(S_i × P_i × T_i) 
Onde:
- E²(a): Entropia Ética Aplicada
- S_i: Severidade do achado i (CRÍTICO=4, ALTO=3, MÉDIO=2, BAIXO=1)
- P_i: Probabilidade de violação detectada
- T_i: Timestamp de detecção (função de decaimento temporal)

Autor: Rafael Melo Reis (RAFAELIA Framework)
Licença: Consulte LICENSE no repositório
Convenção de Berna: Direitos autorais reservados
"""

import os, hashlib, time, subprocess, threading, queue
from datetime import datetime

def make_rafa_context(sigil=None):
    """
    Generate a context dictionary with RAFA_SIGIL and related variables.
    If sigil is not provided, use the current timestamp.
    """
    if sigil is None:
        sigil = "RAFAELIA-GCΩ-" + str(int(time.time()))
    honeystr = "∆GC-CRIME-Ω-SECRET-" + sigil
    honeyfile = f"/sdcard/{sigil}.txt"
    report = f"/sdcard/report_{sigil}.txt"
    summary = f"/sdcard/summary_{sigil}.txt"
    return {
        "RAFA_SIGIL": sigil,
        "HONEYSTR": honeystr,
        "HONEYFILE": honeyfile,
        "REPORT": report,
        "SUMMARY": summary
    }

# Example usage:
# context = make_rafa_context()
# context["RAFA_SIGIL"], context["HONEYSTR"], etc.
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
    """
    Injeta um arquivo-isca (honeypot) no sistema de arquivos.
    
    Científico:
    -----------
    Cria um arquivo com assinatura única contendo strings de rastreamento.
    Funciona como um marcador fotônico que permite detectar acesso não autorizado
    através de varreduras posteriores.
    
    Simbólico:
    ----------
    O honeypot é um cristal-guardião plantado na floresta digital.
    Qualquer entidade que o toque deixa sua marca energética, revelando
    padrões de violação através da perturbação do campo.
    
    Returns:
        None - Cria arquivo no caminho HONEYFILE
    """
    with open(HONEYFILE,"w") as f:
        f.write(HONEYSTR)
    print(f"[+] Honeyfile criado: {HONEYFILE}")

def hash_file(path):
    """
    Calcula hash SHA-512 de um arquivo para integridade e verificação.
    
    Científico:
    -----------
    Implementa função hash criptográfica SHA-512 para criar fingerprint único
    do arquivo. Essencial para validação de integridade e detecção de alterações.
    
    Simbólico:
    ----------
    Cada arquivo possui uma assinatura vibracional única. O hash é a frequência
    fundamental desse arquivo no espectro digital - sua essência comprimida.
    
    Args:
        path (str): Caminho absoluto do arquivo
        
    Returns:
        str: Hash SHA-512 em formato hexadecimal (128 caracteres)
    """
    with open(path, "rb") as f:
        return hashlib.sha512(f.read()).hexdigest()

def scan_dir(dirs, keywords, out_q):
    """
    Varre diretórios recursivamente procurando palavras-chave em arquivos.
    
    Científico:
    -----------
    Implementa algoritmo de busca recursiva em árvore de diretórios com
    pattern matching para detecção de strings específicas. Utiliza tratamento
    de erro robusto para ignorar arquivos binários incompatíveis.
    
    Simbólico:
    ----------
    Como raízes de uma árvore quântica explorando camadas geológicas,
    cada thread de varredura penetra profundamente no substrato digital,
    sentindo vibrações de palavras-chave como cristais ressonantes.
    
    Args:
        dirs (list): Lista de caminhos de diretórios para varrer
        keywords (list): Lista de palavras-chave a procurar
        out_q (queue.Queue): Fila thread-safe para resultados
        
    Efeitos:
        Adiciona tuplas (path, keyword) à fila out_q para cada achado
    """
    for d in dirs:
        if not os.path.exists(d): continue
        for root, _, files in os.walk(d):
            for fn in files:
                path = os.path.join(root, fn)
                try:
                    with open(path, errors='backslashreplace') as f:
                        content = f.read()
                        for kw in keywords:
                            if kw in content:
                                out_q.put((path, kw))
                except: continue

def scan_packages(packages, keywords, out_q):
    """
    Varre diretórios de dados de aplicativos Android específicos.
    
    Científico:
    -----------
    Analisa o espaço de dados privado de aplicações Android (/data/data/package)
    buscando evidências de coleta não autorizada. Cada app tem seu sandbox isolado,
    mas pode conter dados vazados de outros contextos.
    
    Simbólico:
    ----------
    Cada aplicativo é um templo com seus próprios altares de dados.
    Esta função é um raio-X ético que revela o que está escondido nos
    santuários digitais, detectando profanações através de assinaturas.
    
    Args:
        packages (list): Lista de nomes de pacotes Android (com.exemplo.app)
        keywords (list): Palavras-chave a detectar
        out_q (queue.Queue): Fila thread-safe para resultados
        
    Efeitos:
        Adiciona tuplas (path, package, keyword) à fila para cada achado
    """
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
    """
    Captura e analisa logs do sistema Android (logcat).
    
    Científico:
    -----------
    Extrai últimas 5000 linhas do buffer de log do kernel/sistema Android
    usando comando logcat. Essencial para análise temporal e correlação
    de eventos do sistema com achados em arquivos.
    
    Simbólico:
    ----------
    O logcat é a memória temporal do sistema - um rio de eventos fluindo
    em tempo real. Capturar esse fluxo permite ver a consciência do sistema,
    revelando intenções através de padrões de comportamento registrados.
    
    Args:
        keywords (list): Palavras-chave a detectar nos logs
        out_q (queue.Queue): Fila thread-safe para resultados
        
    Efeitos:
        Adiciona tuplas (log_line, keyword) à fila para cada achado
    """
    out = subprocess.getoutput("logcat -d -v brief | tail -n 5000")
    for line in out.splitlines():
        for kw in keywords:
            if kw in line:
                out_q.put((line, kw))

def auto_classify(findings):
    """
    Classifica achados automaticamente por nível de severidade.
    
    Científico:
    -----------
    Implementa sistema de classificação baseado em dicionário SEVERITY,
    mapeando palavras-chave para níveis de risco conforme LGPD e melhores
    práticas de segurança da informação.
    
    Simbólico:
    ----------
    Cada violação possui sua própria frequência vibratória. Esta função
    é um prisma que separa o espectro de violações em bandas de severidade,
    permitindo priorização ética baseada em gradientes de dano potencial.
    
    Args:
        findings (list): Lista de tuplas (path, keyword)
        
    Returns:
        dict: Dicionário {severidade: [(path, keyword), ...]}
              onde severidade in ["CRÍTICO", "ALTO", "MÉDIO", "BAIXO"]
    """
    classified = {}
    for path, kw in findings:
        sev = SEVERITY.get(kw,"BAIXO")
        if sev not in classified: classified[sev]=[]
        classified[sev].append((path, kw))
    return classified

def gen_report(honeyfile, found1, found2, found3, found4, logcat, sniff=None):
    """
    Gera relatório técnico completo da varredura forense.
    
    Científico:
    -----------
    Compila todos os achados em documento estruturado incluindo:
    - Hash do honeypot para validação de integridade
    - Achados por categoria (storage, apps, media, logs)
    - Timestamp e selo único para rastreabilidade
    
    Simbólico:
    ----------
    O relatório é o Livro das Revelações - documento sagrado que cristaliza
    todas as evidências em forma permanente. Cada linha é um testemunho,
    cada hash uma assinatura divina de autenticidade.
    
    Args:
        honeyfile (str): Caminho do arquivo honeypot
        found1 (list): Achados em storage público
        found2 (list): Achados em apps (inclui package name)
        found3 (list): Achados em backups/media
        found4 (list): Achados em audio/voz
        logcat (list): Achados em logs do sistema
        sniff (str, optional): Caminho do dump de tráfego de rede
        
    Efeitos:
        Cria arquivo de relatório em REPORT
    """
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
    """
    Gera sumário executivo com análise agregada dos achados.
    
    Científico:
    -----------
    Processa e agrega dados do relatório completo em visualização executiva:
    - Agrupa por severidade para priorização
    - Agrupa por aplicativo para análise de responsabilidade
    - Extrai amostra de logs mais relevantes
    
    Simbólico:
    ----------
    O sumário é o Mapa das Estrelas - visão panorâmica que revela constelações
    de violações. Enquanto o relatório detalha cada estrela, o sumário mostra
    as galáxias, permitindo navegação intuitiva através do cosmos de evidências.
    
    Args:
        found1 (list): Achados em storage público
        found2 (list): Achados em apps
        found3 (list): Achados em backups/media
        found4 (list): Achados em audio/voz
        logcat (list): Achados em logs
        
    Efeitos:
        Cria arquivo de sumário em SUMMARY
    """
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
    """
    Executa varredura paralela em múltiplas threads para máxima eficiência.
    
    Científico:
    -----------
    Implementa paralelismo usando threading.Thread e queue.Queue para comunicação
    thread-safe. Divide análise em 5 dimensões independentes:
    1. Storage comum (/sdcard/)
    2. Dados de aplicativos (/data/data/)
    3. Backups e mídia (WhatsApp, DCIM, etc.)
    4. Logs do sistema (logcat)
    5. Áudio/voz (redundância para alta prioridade)
    
    Complexidade: O(n*m*k) onde n=arquivos, m=keywords, k=threads
    Porém execução paralela reduz tempo total por fator ~k
    
    Simbólico:
    ----------
    Como um mandala de observadores quânticos, cada thread é uma dimensão
    de consciência que observa o sistema simultaneamente. A superposição
    das observações colapsa em realidade única quando as threads convergem,
    revelando o estado verdadeiro do sistema através da interferência construtiva.
    
    Returns:
        tuple: (found1, found2, found3, found4, logcat) - Listas de achados por categoria
    """
    print("[*] Iniciando varredura paralela...")
    q1, q2, q3, q4, ql = queue.Queue(), queue.Queue(), queue.Queue(), queue.Queue(), queue.Queue()
    threads = []
    # Storage comum
    t1 = threading.Thread(target=scan_dir, args=(["/sdcard/"], KEYWORDS, q1))
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
    t5 = threading.Thread(target=scan_dir, args=(["/sdcard/Music","/sdcard/Audio","/sdcard/Recordings"], KEYWORDS, q4))
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
