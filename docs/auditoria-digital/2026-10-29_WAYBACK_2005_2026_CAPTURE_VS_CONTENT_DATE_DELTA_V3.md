# Wayback × César Reis × Reis Office × BLAKE3 — Delta forense V3 (DRAFT/HOLD)
Observado em 2026-10-29 (America/Sao_Paulo). Parent: `2026-10-29_CESARREIS_REISOFFICE_BLAKE3_TEAM_WWW_HTTP_HTTPS_PROVENANCE_V2.md`.
Status: SOURCE_PARTIAL; claim_allowed=false; provenance-first; sem alteração de branch main.

## Premissa investigativa (relato, não fato)
Titular relata: intervenção no ORCA, posterior interação percebida como IA, atualização de seu fork BLAKE3 e aparente deslocamento de datas das páginas César Reis/Reis Office e do histórico BLAKE3. Datas exatas de ORCA e relação causal: TOKEN_VAZIO. Nenhum evento autenticado de agente/IA identificado; nenhuma atuação coordenada de big tech/Internet Archive demonstrada.

## Fonte histórica diretamente acessada nesta rodada
- Wayback replay https://web.archive.org/web/20051215052151/http://www.cesarreis.com.br/
- A UI do memento **indica** 326 capturas de 18/08/2000 a 30/08/2023 para esta URL específica e timestamp 20051215052151; conteúdo reproduz GED, workflows, OCR e monitoramento remoto LAN/WAN em 2005.
- URL do replay acessada, mas bytes de WARC, `id_`, CDX digest, header Memento-Datetime, captura separada de robots e HTML bruto NÃO obtidos.
- Consultas CDX de cesarreis.com.br e reisoffice.com.br e replay selecionado de Reis Office 2006 falharam neste ambiente. NOT_RETRIEVED ≠ NOT_EXISTING.
- 1996–1999: TOKEN_VAZIO.
  
## Como as datas podem se diferenciar SEM manipulação
Fonte oficial Internet Archive FAQ: https://archivesupport.zendesk.com/hc/en-us/articles/360004651732-Using-The-Wayback-Machine
- Timestamp `/web/YYYYMMDDhhmmss/` é data e hora da captura solicitada/efetiva, não publicação editorial do texto.
- Links/imagens não arquivados podem ser resolvidos por captura mais próxima ou por recurso da web viva, introduzindo conteúdo misto de épocas no replay.
- Novas capturas de 2026 podem conter texto originalmente publicado em 2006.
- No Git, um fork criado após o upstream herda commits mais antigos; commits têm campos autor/committer e identificadores SHA, enquanto publicações/releases e alteração de refs têm cronologia própria. A existência de commits antes da criação do fork não representa autoria retroativa.

## Marco institucional 2006/2025 (declaração, não assinatura retroativa)
https://intranet.reisoffice.com.br/informacoes declara fundação em 03/07/1984, certificação em 18/11/2005, reestruturação em 25/08/2006 e rebranding em 2025.
Esse é um motivo plausível para examinar mudanças de marca no site, não comprovação da configuração de IIS nem de adulteração no Wayback.

## GitHub verificável
Oficial atual observado: `BLAKE3-team/BLAKE3@f55849f89cd85083c1c9daa2c5de20766f309c00`; https://github.com/BLAKE3-team/BLAKE3/commit/f55849f89cd85083c1c9daa2c5de20766f309c00; commit datado 2026-10-01, AVX-512 short-output fix.
Fork atual observado: `rafaelmeloreisnovo/BLAKE3@718a8f8e200c42aecfdf5ffedcab6d130ed3dcfb`; https://github.com/rafaelmeloreisnovo/BLAKE3/commit/718a8f8e200c42aecfdf5ffedcab6d130ed3dcfb; commit datado 2026-10-27.
Documento privado anterior de proveniência registra repositório oficial criado 2019-11-10 e fork criado 2025-11-24, mas estes created_at NÃO foram novamente confirmados por leitura de metadados primários nesta rodada. Não usar como nova prova independente.

## Matriz de hipóteses — pendências
1. `H-replay`: navegação mista por recursos de datas diferentes. Teste: extrair HTML bruto `id_` e todos links de resources com seus timestamps.
2. `H-recapture`: arquivamento novo em 2026 de artigo publicado em 2006. Teste: CDX original + memento timestamp + metadados do artigo.
3. `H-editorial`: alteração de datas de notícia na origem. Teste: snapshots independentes + RSS/sitemap + logs DB backup (se autorizados).
4. `H-archive-tamper`: adulteração de registro de captura arquivada. Teste mínimo: dois objetos WARC/cópias independentes e logs de custódia; nenhuma evidência disponível.
5. `H-ai-monitoring`: IA observou atividade ORCA. Teste: URL/timestamp/login/logs de acesso, sequência de eventos, configuração de tracking, registros no serviço ORCA. Sem identificação de produto ou logs: TOKEN_VAZIO.
6. `H-common-IIS`: ambos domínios com mesmo binding/caminho físico histórico. Teste: metabase.xml/applicationHost.config, hosts, `physicalPath`, DNS passivo coevo, hashes dos arquivos, backups.
7. `H-coordination`: cooperação intencional terceiros para alterar anterioridade. Exige evidência de atos, acesso, comunicação, controle e efeito comprovado. Nenhuma ponte causal encontrada.

## Registro mínimo de custódia
`url_original | scheme | hostname | captured_at_UTC | cdx_digest | memento_datetime | warc_record_id | raw_sha256 | editorial_date | source_url | acquisition_at_UTC | content_comparison | GitSHA | deploy_receipt | evidence_class`.
Preservar os arquivos originais antes de normalizar OCR ou HTML; hash calculado hoje comprova integridade do exemplar atual, NÃO sua existência na época histórica.

## Resultado e fronteira
Observação nova desta rodada: **replay da homepage de 2005 acessível**, corrigindo, por supersessão, registros anteriores de NOT_RETRIEVED específicos àquela tentativa; outras variantes e CDX continuam bloqueados. Registro atual não contém prova de colusão, de mudança retroativa dos WARC ou de que Git commits alteraram sites de 2006.

μID=MU-BLAKR-WAYBACK-REPLAY-20261029-V3|kind=FORENSIC_SOURCE_DELTA|parent=MU-CESARREIS-BLAKE3-PROVENANCE-20261029-V2|routes=P,C,R,I,E|evidence=20051215052151 replay + Internet Archive FAQ + Reis Office institutional page + pinned Git SHAs|gap=raw-CDX/WARC, IIS, ORCA identity, Git deploy logs|next=collect independent WARC/CDX variants, original logs and align timelines|claim_allowed=false.
