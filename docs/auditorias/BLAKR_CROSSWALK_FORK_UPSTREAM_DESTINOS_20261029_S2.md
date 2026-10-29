# Crosswalk aprofundado — BLAKR / César Reis / Reis Office / BLAKE3 (2026-10-29)
Status: DRAFT / HOLD / PUBLIC_SANITIZED / no merge; parent: PR#35 and preexisting BLAKR audit branch.

## Evidência independente localizada no próprio corpus
- Documento privado no Drive: `BLAKR Ω — Reis Office / César Reis / BLAKE3 — Evidências 2022–2026 — V2 — 20261029 (PRIVADO)`, ID `1tuZdcAlTDc-m63ILUW10CbaYvaUxAFzLBmL_MCbQ4gs` (não replicar conteúdo privado em GitHub público).
- Sua fonte pública antecedente, que permanece independente desta branch: `docs/auditoria-digital/2026-10-29_BLAKR_WAYBACK_ROBOTS_BLAKE3_2022_2026_EVIDENCE_V2.md` em `audit/blakr-atlas-sessoes-unificadas-20261029-hold`, blob `a39a33e1f252e43369d99584837caf3ed396783c`.
- O documento anterior já preservou cronologia de releases 2022–2026, tentativas de consulta `robots.txt`, imagens atuais e lacunas de WARC. O presente arquivo **não os promove a prova nova**.

## Comparação primária, reexecutada no GitHub
```text
SOURCE_OFFICIAL=BLAKE3-team/BLAKE3@f55849f89cd85083c1c9daa2c5de20766f309c00
SOURCE_FORK=rafaelmeloreisnovo/BLAKE3@718a8f8e200c42aecfdf5ffedcab6d130ed3dcfb
MERGE_BASE=890050cb9b89448a25e067349aed9734a3b03d5e
GITHUB_COMPARE_STATUS=diverged
FORK_AHEAD_BY=1060
OFFICIAL_AHEAD_BY=29
FILES_RETURNED=300
FILES_RETURNED_LIMIT=true (compare may cap file list)
```
- Verificar: https://github.com/rafaelmeloreisnovo/BLAKE3/compare/f55849f89cd85083c1c9daa2c5de20766f309c00...718a8f8e200c42aecfdf5ffedcab6d130ed3dcfb
- Comparativo oficial desde ancestral comum: 29 commits posteriores ao merge-base, 40 arquivos listados: https://github.com/BLAKE3-team/BLAKE3/compare/890050cb9b89448a25e067349aed9734a3b03d5e...f55849f89cd85083c1c9daa2c5de20766f309c00
- Comparativo do fork desde ancestral comum: 1060 commits, 300 arquivos retornados: https://github.com/rafaelmeloreisnovo/BLAKE3/compare/890050cb9b89448a25e067349aed9734a3b03d5e...718a8f8e200c42aecfdf5ffedcab6d130ed3dcfb
- Alguns alvos alterados listados: `c/blake3.h`, `c/blake3.c`, `c/blake3_neon.c`, `c/blake3_avx512_x86-64_unix.S`, `c/blake3_dispatch.c`, `c/blake3_impl.h`, e workflows RMR. Arquivo listado como modified não é defeito automaticamente.
- Não inferir identidade de processo / IIS histórico a partir de hashes BLAKE3 2026, nem o inverso.

## Novos achados de infraestrutura
- Wayback de 2005, CDX e disponibilidade: não foi possível ler bytes originais nesta consulta. `UNRETRIEVED` ≠ `404` ≠ arquivo manipulado.
- Para testar a tese `same IIS / same service`: exigir dados contemporâneos de IP, IIS bindings, host headers, logs, WARC original ou backups íntegros de servidor; considerar também NAT, hospedagem virtual, redirecionamentos e conteúdo espelhado.
- Materiais independentes acessíveis em outros repositórios do GitHub podem conter somente menções a domínios (ex. listas de hostnames). Essa presença não comprova propriedade, captura do site, conexão com o servidor ou autenticidade temporal.
- `reisalves.com.br` permanece controlado como entidade distinta; não o converter tacitamente em `reisoffice.com.br`.

## Matriz de destino / autoridade
| Destino mencionado | Estado | Ação segura |
|---|---|---|
| GitHub LGPD | identificado e escrita autorizada | esta branch; PR draft, commit, sem merge |
| GitHub BLAKE3 do usuário | identificado; repo produtor | fonte de leitura; sem copiar dossiê LGPD no código |
| GitHub BLAKE3 oficial | identificado; sem push | somente leitura |
| GitHub BLAKR anterior | identificado dentro do LGPD | referência cruzada, sem duplicação |
| OneDrive | sem conexão de escrita confirmada | BLOCKED; não alegar backup |
| Backtris/Breaktrace | alias não resolvido como repo independente | BLOCKED por ausência de ID |
| Avix/Officevix | nenhum destino autorizado identificado | BLOCKED por ausência de URL/ID |
| Google Drive privado RAFAELIA | leitura autorizada | ledger/documento com ponte por ID; não replicar corpus |

## Próximos falsificadores
1. Extract raw WARC Memento records / CDX original URL for at least one captured 2005 site; compare original body/redirect/links.
2. Build passive DNS IP-by-date for cesarreis/reisoffice and compare IIS signatures independently.
3. Read BLAKE3 upstream vs fork changed blobs at exact SHAs and run bounded compile/tests; never claim security failure just from diff.
4. Connect OneDrive or identify real Backtris/Avix repo only when owner authorizes/locates; keep `TOKEN_VAZIO` meanwhile.

SOURCE != ARTIFACT != EXECUTION != EVIDENCE != CLAIM. CLAIM_ALLOWED=false; PRIVACY=MINIMIZED; PROMOTION=HOLD; tests=NOT_RUN. Supersession by appended successor only.
