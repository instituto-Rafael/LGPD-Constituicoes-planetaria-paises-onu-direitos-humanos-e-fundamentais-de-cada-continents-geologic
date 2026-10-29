# BLAKR Ω — Evidências datadas BLAKE3 × Reis Office × César Reis (V2)
Data da consulta: 2026-10-29. Source class: PUBLIC (sanitizado). Branch: HOLD, sem merge, sem imputação.
Parent: `2026-10-29_BLAKR_ATLAS_SESSOES_UNIFICADAS_V1.md`.
SOURCE ≠ ARTIFACT ≠ EXECUTION ≠ EVIDENCE ≠ CLAIM. TOKEN_VAZIO ≠ 0.

## 1 — GitHub BLAKE3: cronologia com fontes primárias
Fonte: [BLAKE3-team/BLAKE3](https://github.com/BLAKE3-team/BLAKE3); API de releases `https://api.github.com/repos/BLAKE3-team/BLAKE3/releases?per_page=100&page=1` (32 itens consultados). `published_at` é timestamp de lançamento no GitHub, não a data de nascimento do algoritmo.
Repositório oficial `created_at=2019-11-10T11:15:44Z`; fork `rafaelmeloreisnovo/BLAKE3` `created_at=2025-11-24T23:56:51Z`; API confirma `parent/source=BLAKE3-team/BLAKE3` e `master` como branch padrão. **Commits pré-fork aparecem no grafo histórico do fork por herança**, e não por produção independente retroativa.
| Ano | Releases oficiais observados, data UTC |
|---|---|
| 2022 | 1.3.0 (2022-01-08), 1.3.1 (2022-02-14), 1.3.2 (2022-11-20), 1.3.3 (2022-11-26) |
| 2023 | 1.4.0 (2023-06-08), 1.4.1 (2023-07-06), 1.5.0 (2023-09-21) |
| 2024 | 1.5.1 (2024-03-12), 1.5.2 (2024-07-12), 1.5.3 (2024-07-15), 1.5.4 (2024-08-19), 1.5.5 (2024-11-27) |
| 2025 | 1.6.0 (2025-02-17), 1.6.1 (2025-02-27), 1.7.0 (2025-03-18), 1.8.0 (2025-03-31), 1.8.1 (2025-04-03), 1.8.2 (2025-04-21) |
| 2026 até 29/10 | 1.8.3 (2026-01-08), 1.8.4 (2026-03-30), 1.8.5 (2026-04-25), 1.8.6 (2026-08-05), 1.8.7 (2026-08-20) |

Endpoints de consulta `GET /repos/BLAKE3-team/BLAKE3/commits?until=<YYYY>-12-31T23:59:59Z&per_page=1`. **São snapshots até a data, não diffs de todo o ano**:
- 2022-12-13T23:56:08Z [e366618d225679e750232bfabe63191e14657289](https://github.com/BLAKE3-team/BLAKE3/commit/e366618d225679e750232bfabe63191e14657289)
- 2023-12-30T07:28:33Z [4d32708f511fd85c6b0fb131295cc73224246738](https://github.com/BLAKE3-team/BLAKE3/commit/4d32708f511fd85c6b0fb131295cc73224246738)
- 2024-11-27T02:38:04Z [5c8b350b3531102359b89e9f0a3367e6de4a43f4](https://github.com/BLAKE3-team/BLAKE3/commit/5c8b350b3531102359b89e9f0a3367e6de4a43f4)
- 2025-12-09T19:38:21Z [890050cb9b89448a25e067349aed9734a3b03d5e](https://github.com/BLAKE3-team/BLAKE3/commit/890050cb9b89448a25e067349aed9734a3b03d5e)
- 2026-10-01T19:59:11Z [f55849f89cd85083c1c9daa2c5de20766f309c00](https://github.com/BLAKE3-team/BLAKE3/commit/f55849f89cd85083c1c9daa2c5de20766f309c00)

Fork último commit consultado até 2025-12-31: [890050cb9b89448a25e067349aed9734a3b03d5e](https://github.com/rafaelmeloreisnovo/BLAKE3/commit/890050cb9b89448a25e067349aed9734a3b03d5e), igual ao oficial no instante de referência de 2025-12-09. A igualdade desse SHA **não demonstra** igualdade do fork durante todo 2025.

## 2 — Divergências verificadas ou previamente documentadas
- Documento precursor [crosswalk público](./2026-10-29_BREAKTRACE_BLAKE3_CESARREIS_REISALVES_CROSSWALK_V1.md) pinou em 2026-10-29 oficial `f55849f...` e fork `718a8f8...`: Git compare `ahead_by=1060`, `behind_by=29`, com merge-base `890050cb...`. Divergência de histórico Git ≠ manipulação.
- Drive privado de pesquisa BLAKE3/RMR em 2026-10-27 compara 22 blobs compartilhados distintos em refs fixados e identifica risco técnico em `c/blake3.h` (restrict/alias), `c/blake3_neon.c` (símbolo externo), `c/blake3_avx512_x86-64_unix.S` (ramo alterado), `c/blake3_dispatch.c` (hint), `c/blake3_impl.h` (CYGWIN). Esses são **alvos de testes**, não defeitos ou intenção comprovados.
- Histórico de 2022, 2023 e 2024 deve ser comparado **oficial vs versão oficial capturada naquela época**, não contra uma suposta existência pública do fork em anos anteriores a 2025.
- Nenhum conteúdo WARC/Wayback para o GitHub foi recuperado nesta rodada. O Git e a data de release vêm do provedor GitHub, não do Wayback.

## 3 — Reis Office e César Reis: webmaster, robots, imagens
### Fonte institucional atual observada
- [Site atual](https://www.reisoffice.com.br/) apresenta menus, produtos, serviços, certificações e links para arquivos de imagem; [empresa](https://reisoffice.com.br/empresa) declara criação empresarial em **1984** e certificação ISO em **2005**. Essas datas são **declarações institucionais**, não timestamps de captura arquivada.
- Site atual (recurso explicitamente identificado em link HTML, mas imagem bytes não obtidos): `https://reisoffice.com.br/images/logo-reisoffice-novo.png` e `https://reisoffice.com.br/images/visual/footer/sistemaGestao14001.png`.
- O site atual lista página de **Museu** (`https://reisoffice.com.br/empresa/museu`) e imagens institucionais: bom ponto para comparar caminhos/arquivos históricos, mas nenhuma versão 2005 foi recuperada.
- Registro WHOIS **reproduzido por terceiro** numa página de relatório com data interna 2019-12-13 informa `reisoffice.com.br created:20050805` e DNS próprios no período. Fonte secundária: https://reisoffice.com.br.cutestat.com/ . Isso não prova servidor IIS compartilhado nem autoriza inferir registro histórico de `cesarreis.com.br`.

### Wayback/robots/sitemap: tentativas e estado
| Target | Operação e resultado | Estado |
|---|---|---|
| `https://web.archive.org/web/20051215052151/http://www.cesarreis.com.br/` | URL 2005 fornecida pelo usuário; nesta consulta a abertura retornou erro interno de acesso, sem HTTP capture/HTML | LOCATOR_ONLY |
| `https://web.archive.org/web/20051215052151/http://www.cesarreis.com.br/robots.txt` | abertura falhou; não inferir existência de captura de robots nesta data | NOT_RETRIEVED |
| `https://web.archive.org/web/20260915000000*/www.reisoffice.com.br` | abertura falhou; URL de calendário não é carimbo de captura individual | NOT_RETRIEVED |
| `https://www.reisoffice.com.br/robots.txt` | abertura falhou nesta ferramenta; **status HTTP do servidor não obtido** | NOT_RETRIEVED |
| `https://reisoffice.com.br/robots.txt` | idem | NOT_RETRIEVED |
| `https://loja.reisoffice.com.br/robots.txt` | idem | NOT_RETRIEVED |
| `https://loja.reisoffice.com.br/sitemap.xml` | idem | NOT_RETRIEVED |
| `https://index.commoncrawl.org/CC-MAIN-2024-51-index?url=www.reisoffice.com.br%2Frobots.txt&output=json` | API da coleção não retornou resultado legível no ambiente | NOT_RETRIEVED |

**Importante:** zero bytes lidos de `robots.txt`, `sitemap.xml`, meta-`webmaster`, HTML Wayback, imagens antigas ou logs IIS. Não escrever `404`, `robots bloqueou`, `foi removido` ou `manipulação` sem cabeçalho/arquivo observado. A página atual com imagens não prova que sejam os mesmos arquivos de 1999–2017.

### Pesquisa prescrita, não executada
Para cada `cesarreis.com.br` e `reisoffice.com.br`, cruzar `http`/`https`, raiz/`www`/`ww`/`wwww`/`mobile`/`portal`, `robots.txt`, `sitemap.xml`, `images/`, `img/`, `webmaster`, GIF/JPG/PNG, CSS, ASP/ASPX, HTML, redirects e `Server` header quando existir. Buscar CDX por **anos** (1996–2026), preservar `timestamp,original,statuscode,mimetype,digest,length` e WARC. Lacunas não devem ser preenchidas. Preferir fonte primária Internet Archive; Common Crawl e Arquivo.pt são alternativas independentes, sem transferência automática de prova.

## 4 — Fronteira cruzada e destino
- **Nenhuma ligação causal** encontrada entre commits do BLAKE3 2022–2026 e versões dos websites; os conjuntos são timelines ortogonais até surgir deployment chain documentado.
- O literal `Officevix` não foi localizado como pasta/repo do projeto nas contas de Drive e GitHub pesquisadas. Uma empresa pública com esse nome é entidade distinta e **não será tomada como destino por coincidência nominal**. ROUTE_STATE=BLOCKED para esse destino.
- [GitHub LGPD](https://github.com/instituto-Rafael/LGPD-Constituicoes-planetaria-paises-onu-direitos-humanos-e-fundamentais-de-cada-continents-geologic) recebe apenas este crosswalk público sanitizado na branch de auditoria. Google Drive privada recebe o material documental de referência. Nenhum dado de terceiros ou dossiê pessoal é copiado a este repositório público.

## 5 — Critério de prova (GATE)
Para alegação de arquivo historicamente idêntico: `(URL, Memento timestamp, response/status, raw bytes, SHA256, corpo)` do mesmo recurso, depois comparação de digest em duas capturas. Para servidor/IIS compartilhado: prova primária IP histórico/host headers/config/IIS + arquivo/assinatura. Para relação causal com commits: referência de build, deploy e logs. **Sem isso: `claim_allowed=false`.**

## R3 / receipt
`MU-BLAKR-BLAKE3-WAYBACK-ROBOTS-20261029-V2 | source=GitHub official releases+commits, Reis Office institucional, tools archive attempts, prior crosswalk | parent=MU-BLAKR-SESSION-UNIFICATION-20261029-V1 | kind=SCOPED_EVIDENCE_INDEX | Δ=cronologia 2022–2026 pinada; rotas robots/imagens listadas; Wayback NOT_RETRIEVED | routes=L,O,P,C,R,I,E | evidence=GitHub URLs + site URL + this Git SHA | gap=CDX, WARC, robots contents, IIS, Officevix dest | next=raw snapshots + metadata preservation, independent QA | claim_allowed=false`

R3 = <GIT timeline e imagens atuais observadas, arquivo histórico/robots bloqueados à observação, preservar capturas brutas e diff por recurso>.
