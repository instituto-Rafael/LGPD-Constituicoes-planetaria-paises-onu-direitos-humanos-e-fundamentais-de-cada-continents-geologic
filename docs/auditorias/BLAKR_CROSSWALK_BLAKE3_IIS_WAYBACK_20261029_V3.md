# BLAKR Ω — Cruzamento aprofundado BLAKE3 × César Reis × Reis Alves × Reis Office — V3
**Estado:** PUBLIC_SANITIZED · DRAFT · HOLD · NO_MERGE · CLAIM_ALLOWED=false  
**Data de observação:** 2026-10-29; granularidade de data, não hora de coleta certificada.  
**Rota de origem:** [LGPD PR #35](https://github.com/instituto-Rafael/LGPD-Constituicoes-planetaria-paises-onu-direitos-humanos-e-fundamentais-de-cada-continents-geologic/pull/35) · [Auditoria BLAKR predecessora](https://github.com/instituto-Rafael/LGPD-Constituicoes-planetaria-paises-onu-direitos-humanos-e-fundamentais-de-cada-continents-geologic/blob/audit/blakr-atlas-sessoes-unificadas-20261029-hold/docs/auditoria-digital/2026-10-29_BLAKR_WAYBACK_ROBOTS_BLAKE3_2022_2026_EVIDENCE_V2.md). 
Sem cópia de documentos privados para este branch público.

## O que foi efetivamente executado nesta rodada
1. Consulta autenticada do GitHub `compare_commits`, usando **`rafaelmeloreisnovo/BLAKE3`**, base `BLAKE3-team:master` e head `master`. Resultado: `status=diverged`, `ahead_by=1060`, `behind_by=29`, `merge_base_commit=890050cb9b89448a25e067349aed9734a3b03d5e`, base SHA `f55849f89cd85083c1c9daa2c5de20766f309c00`. A resolução do head é a observação do provedor em 2026-10-29, não promessa de estabilidade.
2. Persistência, no mesmo PR, de **300 registros de arquivos** retornados pelo compare em `data/auditorias/BLAKE3_COMPARE_UPSTREAM_VS_RMR_20261029_FILE_SAMPLE.csv`. **A API limita essa listagem**; 300 entradas NÃO são inventário completo nem 300 alterações de código criptográfico. De 300 entradas, 28 têm status `modified`; as outras possuem outros estados. Números de commits e número de arquivos são grandezas diferentes.
3. Recuperação dos arquivos de proveniência BLAKR já existentes na branch `audit/blakr-atlas-sessoes-unificadas-20261029-hold`: dois arquivos de autoria do mesmo projeto, indexados por refs Git, NÃO importados para a branch nova, prevenindo duplicação.
4. Tentativas de acessar a captura indicada `20051215052151/http://www.cesarreis.com.br/`, CDX da Wayback, índice CDX do Arquivo.pt para César Reis e Reis Office, índice Common Crawl 2015 de Reis Office: ferramenta retornou `not accessible` / erro interno. Sem resposta HTTP autenticada nem payload WARC para aqueles URLs.
5. Leitura da lista pública `https://index.commoncrawl.org/collinfo.json`, em que constam coleções 2026 e anteriores; isso prova existência de um catálogo independente, **não captura de nenhum domínio-alvo**.

## Identidade, tempo e inferência
| Nó | Evidência | Limite |
|---|---|---|
| `cesarreis.com.br` | referência externa de fotografias em 2003; locator Wayback 15/12/2005 fornecido pelo usuário | captura 2005 não recuperada |
| `reisoffice.com.br` | Reis Office atual declara origem empresarial como César Reis Comércio de Máquinas em 03/07/1984; alteração de razão social em documentação oficial de 2007; portal de revendas distinto | mesmo IIS/IP/vhost em 1999–2017 não provado |
| `reisalves.com.br` | autodescrição como rede farmacêutica iniciada em Dracena em 1996 | sem ligação técnica/societária confirmada com Reis Office |
| `BLAKE3-team/BLAKE3` | upstream: projeto Git moderno; HEAD observado em 01/10/2026 | não pode ser deploy identificado de página de 2005 sem ponte independente |
| `rafaelmeloreisnovo/BLAKE3` | fork/ramo moderno, merge-base de dez/2025 | histórico pré-fork herdado de upstream; não prova autorias retroativas |
| `Backtris` / `Breaktrace` | termos orais de projeto, sem repo confirmado na instalação GitHub | `TOKEN_VAZIO_ALIAS`; não identificar silenciosamente como BLAKE3 |
| `Avix` / `Officevix` | nenhum destino autorizado específico localizado nesta rodada | `ROUTE_STATE=BLOCKED`; não escrever em empresa homônima |
| OneDrive | acesso de escrita em OneDrive não confirmado neste contexto | `ROUTE_STATE=BLOCKED`; Drive Google já tem ledger, não é OneDrive |

## Cronologia comparável: release Git versus históricos de website
**1999–2017**: somente timeline documental da infraestrutura César Reis/Reis Office/Reis Alves. Capturas e logs ausentes não equivalem a ausência de serviço.  
**2019-11-10**: criação do repositório upstream BLAKE3 segundo registro GitHub citado na auditoria predecessora.  
**2022–2024**: releases upstream e commits de fim de ano já indexados no documento predecessor; sem atribuir esses eventos a uma instalação de 1999.  
**2025-11-24**: criação do fork RMR, segundo metadado GitHub registrado no documento predecessor; data de criação do fork ≠ data dos commits herdados.  
**2025-12-09**: último ponto comum `890050cb…` observado na comparação atual.  
**2026-10-01**: commit oficial `f55849f…`.  
**2026-10-27**: commit observado do fork `718a8f8…`, merge PR#183.  
**2026-10-29**: comparação `diverged`, 1060 ahead / 29 behind, CSV de 300 registros. 
Uma ordem temporal não é uma relação causal. Nenhuma evidência de transferência de código para website de 1999–2017, de adulteração de replays ou de propriedade de IIS foi obtida.

## Arquivos-chave do código para investigação controlada
Segundo o crosswalk predecessor, hashes Git de `c/blake3.c`, `src/lib.rs`, `src/portable.rs` e `test_vectors/test_vectors.json` coincidiam entre o fork e upstream em refs pinados; `c/blake3_neon.c` e `Cargo.toml` divergiam. Essa afirmação é **PREVIOUS_EVIDENCE_AT_PINNED_REFS**, não comparação de conteúdo repetida nesta rodada. Próximo passo técnico seria analisar diff exato desses caminhos, interface/ABI, compilação e vetores de teste nos SHAs registrados, sem alegar modificação maliciosa.

## Metodologia de arquivo independente e os pontos de falha
| Plataforma | Endpoint público de referência | Dado que pode fornecer | Resultado para estes domínios |
|---|---|---|---|
| Wayback | `https://web.archive.org/cdx/search/cdx?url=www.cesarreis.com.br/&output=json&from=1999&to=2017` | `timestamp/original/status/digest` | NOT_RETRIEVED |
| Wayback replay | `https://web.archive.org/web/20051215052151/http://www.cesarreis.com.br/` | HTML/cabeçalhos de captura, se disponíveis | NOT_RETRIEVED |
| Arquivo.pt CDX | `https://arquivo.pt/wayback/cdx?url=www.cesarreis.com.br` | índice de capturas independente | NOT_RETRIEVED |
| Arquivo.pt Memento | `https://arquivo.pt/wayback/timemap/json/http://www.cesarreis.com.br/` | time-map alternativo | NOT_RUN |
| Common Crawl | `https://index.commoncrawl.org/collinfo.json` | inventário de coleções | CATALOG_READ / DOMAIN_NOT_VERIFIED |
| Common Crawl 2015 | `https://index.commoncrawl.org/CC-MAIN-2015-06-index?url=www.reisoffice.com.br%2F&output=json` | URL/offset/compressed WARC quando indexado | NOT_RETRIEVED |

Fontes metodológicas: [Arquivo.pt CDX](https://dados.gov.pt/en/datasets/cdx-server-api-url-search), [Arquivo.pt Memento](https://dados.gov.pt/en/datasets/memento-api-url-search), [Common Crawl indices](https://commoncrawl.org/cdxj-index), [Common Crawl collection catalog](https://index.commoncrawl.org/collinfo.json), [Archive-It CDX](https://support.archive-it.org/hc/en-us/articles/115001790023-Access-Archive-It-s-Wayback-index-with-the-CDX-C-API).

**Questão central:** canonicalização SURT pode aproximar `www`, esquema ou variantes. Para testar âncoras, salvar **URL original** de cada record, redirects e corpo bruto; não deduzir identidade de servidor pela chave do índice. Distinguir data de publicação, timestamp de captura, timestamp do commit Git, hora de observação, e clocks em UTC/BRT.

## Plano de verificação e falsificação por camada
- **DNS e IIS:** consultar DNS passivo histórico (A/AAAA/CNAME/MX/NS) e certificados TLS históricos quando aplicáveis. Capturar `Server`, `X-Powered-By`, cookies, ASP session e pistas de `web.config` apenas quando expostas legalmente. Mesmo IP não necessariamente é a mesma instância IIS.
- **HTML e imagens:** recursos `/robots.txt`, `/sitemap.xml`, `/images/`, `/img/`, `/mobile/`, `/portal/`, arquivos `.asp/.aspx/.php/.gif/.jpg/.png`. Preservar digests e bytes apenas em destino com autoridade e licença; este repo público guarda localizadores e hashes não pessoais.
- **Links e e-mails:** `href/src/action`, `mailto:`, domínios de destino, data da captura, URL original e URL reescrita. Contatos de pessoas e e-mails individuais NÃO entram no index público.
- **Algoritmo/replay:** controles negativos com domínio terceiro inalterado; comparativo `id_` vs replay transformado. Sem divergência de WARC e documento externo, suspeita de manipulação permanece H1 não comprovada.
- **Git-versus-site:** somente evento de deploy com commit SHA, build hash, servidor/path e timestamp fecha ponte causal; sem isso linhas de tempo são ortogonais.
- **Evidência negativa:** erro de acesso `INACCESSIBLE_FROM_TOOL` não deve ser materializado como HTTP 404, robots deny, exclusão de acervo ou fraude.

## Fronteira LGPD e rotas
Este é repositório público: **sem** conteúdo do dossiê Drive privado, dados pessoais, correspondência, logs de conta, credenciais ou dumps íntegros sem direito/licença. 
**GitHub** recebe docs, índices e scripts sob PR Draft/HOLD. **Drive** recebe μWRITE e referência de custódia. **OneDrive/Avix** aguardam destino identificável e ligação autorizada, sem gravação fictícia.
Dossiês anteriores ficam preservados em sua branch original. Nada é fundido sem revisão independente.

## Controle/receipt
`MU-BLAKR-AUDIT-V3-20261029 | kind=CROSSWALK_UPSTREAM_VS_ARCHIVES | parent=LGPD-PR35-V1 + BLAKR-predecessor-V2 | status=DRAFT/HOLD | evidence=github:compare_commit stats+300 file rows; CommonCrawl catalog; link-based institutional references | gap=WARC, HTTP original, actual server logs, OneDrive and Avix target | claim_allowed=false | next=metadata raw capture/pDNS and source-specific review | rollback=close Draft PR + preserve predecessors`.
