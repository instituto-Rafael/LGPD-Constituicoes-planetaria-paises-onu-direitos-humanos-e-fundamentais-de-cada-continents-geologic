# Auditoria de proveniência V2 — César Reis × Reis Office × BLAKE3-team × fork RMR
Data da pesquisa: 2026-10-29 (BRT). Escopo: 1996–2026. Estado: EVIDENCE_PARTIAL / DRAFT-HOLD / claim_allowed=false.

**Fronteira:** SOURCE ≠ ARTIFACT ≠ EXECUTION ≠ EVIDENCE ≠ CLAIM. Este documento registra observações e lacunas, não atesta fraude, autoria de algoritmo, implantação comum, identidade física de servidor ou manipulação de arquivos.

## 1. Escopo de hosts e esquemas (oito URLs, homepage)

| URL consultada | Observação direta via leitor web em 2026-10-29 | Limite |
| --- | --- | --- |
| http://cesarreis.com.br/ | NOT_RETRIEVED | O leitor normalizou/tentou HTTPS; nenhum status HTTP original certificado |
| https://cesarreis.com.br/ | NOT_RETRIEVED | Não prova inexistência |
| http://www.cesarreis.com.br/ | NOT_RETRIEVED | Não comprova redirecionamento nem queda |
| https://www.cesarreis.com.br/ | NOT_RETRIEVED | Não comprova redirecionamento nem queda |
| http://reisoffice.com.br/ | TEXT_RETRIEVED | Leitor apresentou página em https://reisoffice.com.br/; header HTTP/redirect não foi preservado |
| https://reisoffice.com.br/ | TEXT_RETRIEVED | Site comercial atual; HTML bruto não preservado |
| http://www.reisoffice.com.br/ | TEXT_RETRIEVED | Leitor apresentou https://www.reisoffice.com.br/; sem captura de headers |
| https://www.reisoffice.com.br/ | TEXT_RETRIEVED | Página comercial atual; bytes não comparados |

**Não confundir:** conteúdos textuais iguais renderizados pelo leitor ≠ SHA-256 de HTML igual ≠ mesmo endereço IP ≠ mesmo binding IIS ≠ mesmo `physicalPath`.
Fonte 2026: https://reisoffice.com.br/ e https://www.reisoffice.com.br/.

## 2. Fonte histórica recuperada

- Captura efetivamente aberta e examinada: https://web.archive.org/web/20051215052151/http://www.cesarreis.com.br/ ; timestamp da URL = 2005-12-15T05:21:51Z; URL arquivada = HTTP com www; Wayback indica 326 capturas da URL de 2000-08-18 até 2023-08-30. Esse número refere-se à URL exibida, não necessariamente aos subdomínios e protocolos correlatos.
- Conteúdo textual observado em 2005: GED, OCR, workflows, impressão variável, gerenciamento remoto e monitoramento LAN/WAN. Esses termos são serviços comerciais/tecnologias da época, não uma implementação demonstrada do algoritmo BLAKE3.
- Captura de /arquiv/empresa.asp informada em investigação anterior: https://web.archive.org/web/20051218050441/http://www.cesarreis.com.br/arquiv/empresa.asp. **Nesta rodada o replay dessa página não foi recuperado**.
- Contexto anterior de duas árvores ASP (/arquiv/ e /Telas/) e aplicações expostas por IP: registrado no dossiê de investigação local; a replay não foi revalidada nesta rodada. Não classificar como manipulação.
- Tentativas de recuperar para 2005 variantes HTTPS, sem-www ou `reisoffice.com.br`: NOT_RETRIEVED pelo leitor web. NÃO inferir não existência de captura. O endpoint CDX não devolveu índice recuperável neste ambiente.
- 1996–1999: TOKEN_VAZIO_UNOBSERVED. A Wayback existir desde 1996 não demonstra presença desses domínios naquele ano.

## 3. Marcos GitHub com commits e proveniência

| Fonte | Instante UTC observado | SHA / identificador | Conteúdo verificável |
| --- | --- | --- | --- |
| BLAKE3-team/BLAKE3 | 2019-12-02T21:52:56Z | 4d0d2ccd9932f0ae0e34dd2634a0da86a5d63ed9 | "initial commit", README inicial |
| BLAKE3-team/BLAKE3 | 2019-12-09T02:45:49Z | d0a6e9ecb2b077feea316979d7b19b47d3f82cfe | código C importado de veorq/BLAKE3-c; relação de origem declarada no commit |
| BLAKE3-team/BLAKE3 | 2019-12-12T18:18:57Z | 7cf6b8f1747137eb1145dcb212a5168185936b58 | b3sum inicial |
| BLAKE3-team/BLAKE3 | 2026-08-20T08:50:34Z | f3149ec5bb5449af877ba20377a11008ff499fa2 | release 1.8.7 |
| BLAKE3-team/BLAKE3 | 2026-10-01T19:59:11Z | f55849f89cd85083c1c9daa2c5de20766f309c00 | reparo de curto-circuito para saída AVX-512 de zero blocos e teste |
| rafaelmeloreisnovo/BLAKE3 | 2026-10-27T15:08:35Z | 718a8f8e200c42aecfdf5ffedcab6d130ed3dcfb | merge PR#183: componente RMR de evidência/revisão prospectiva |

Fontes canônicas: https://github.com/BLAKE3-team/BLAKE3/commits/master/ ; https://github.com/BLAKE3-team/BLAKE3/commit/d0a6e9ecb2b077feea316979d7b19b47d3f82cfe ; https://github.com/BLAKE3-team/BLAKE3/commit/f55849f89cd85083c1c9daa2c5de20766f309c00 ; https://github.com/rafaelmeloreisnovo/BLAKE3/commit/718a8f8e200c42aecfdf5ffedcab6d130ed3dcfb .

Criação do repositório oficial em 2019-11-10 consta de indexador secundário https://awesome.ecosyste.ms/projects/github.com%2FBLAKE3-team%2FBLAKE3 ; não é o mesmo marco que commit de 02/12/2019. A especificação técnica é referenciada em https://datatracker.ietf.org/doc/html/draft-aumasson-blake3-00 .

## 4. Comparação exata Git entre oficial e fork

Pares examinados: oficial HEAD f55849f89cd85083c1c9daa2c5de20766f309c00 ↔ fork master 718a8f8e200c42aecfdf5ffedcab6d130ed3dcfb.
GitHub compare na direção oficial -> fork: diverged; ahead_by=1060; behind_by=29; merge_base=890050cb9b89448a25e067349aed9734a3b03d5e; **300 caminhos** devolvidos pelo endpoint, não o inventário exaustivo de commits/arquivos.

| Caminho | Blob Git oficial | Blob Git fork | Resultado |
| --- | --- | --- | --- |
| c/blake3.c | 00f91f444922df7c8e7b5ff69343852cbbf4c613 | mesmo | SAME |
| src/lib.rs | 6f652071de0ad06626c427e40354e7ee4872be76 | mesmo | SAME |
| c/blake3_avx512_x86-64_unix.S | ae15eaed7ab0531c2935177646d917987aaa7fad | 9642e413a3ad0f959449e0089dfd672fbff9fb86 | DIFFERENT |
| src/test.rs | 26672f4268c3302dff013e25ca697060fbcc88a8 | 9bb6c4a716044e4cbb0fdab5687a3f6f941c7e3b | DIFFERENT |

No commit oficial de 01/10/2026 há alteração em `c/blake3_avx512_x86-64_unix.S` e novo teste `test_xof_many_rounds_down`. O teste identificado **está presente** em `src/test.rs` oficial e **ausente** no arquivo do fork examinado. Isso demonstra uma lacuna de paridade pontual, NÃO teste de segurança em runtime no fork. Comparação de blobs é verificável somente nesses refs, não das páginas de 2005.

## 5. Hipóteses e falsificadores

- H-SERVER: `cesarreis` e `reisoffice` operaram no mesmo IIS com os mesmos arquivos. Pendente: bindings/host headers no metabase.xml ou applicationHost.config histórico, `physicalPath`, registros DNS/IP na mesma data e bytes dos arquivos.
- H-ARCHIVE: versões de páginas ou datas foram alteradas. Pendente: pares de Mementos com `original`, `timestamp`, `statuscode`, `digest`, bytes brutos/WARC, preservando CDX/WARC e fonte de obtenção.
- H-GIT: um commit BLAKE3 impactou uma página dos domínios. Pendente: elo primário repo -> build -> deploy -> hostname -> timestamp. **Nenhum elo observado.**
- H-IP: IPs distintos exibidos no site 2005 provam servidores físicos distintos. NÃO; o fato não resolve topologia nem prova servidor único.
- H-ANTERIORIDADE: 2005 < 2019 demonstra que web empresarial existia antes do repositório BLAKE3. TRUE apenas para presença documental e tecnologias descritas; FALSE como prova de precedência do algoritmo BLAKE3.
- H-REDIRECT: HTTP -> HTTPS e sem-www -> www eram iguais historicamente. NOT_OBSERVED. Precisam de registros históricos independentes por esquema e hostname.

## 6. Matriz de custódia (preenchimento futuro)

Campos para cada captura: `capture_id,scheme,hostname,original_url,wayback_timestamp_utc,memento_datetime,source_archive,warc_record_id,http_status,location_header,mime,cdx_digest,raw_sha256,normalized_text_sha256,body_length,extraction_tool,extraction_time_utc,anomaly_type,claim_gate`.
Para cada commit: `repo,ref,commit_sha,git_author_date,git_committer_date,verified_at_utc,blob_path,blob_sha,comparison_base,comparison_head,deploy_receipt`.
Não equiparar datas em postagens/editoriais a timestamps de captura ou autoria Git.

## 7. μWRITE e próxima ação

`MU-CESAR-REIS-BLAKE3-WWW-HTTP-HTTPS-20261029-V2|2026-10-29|Wayback:20051215052151+GitHub BLAKE3-team+fork+site atual|MU-CROSSWALK-BREAKTRACE-CESARREIS-REISALVES-20261029-V1|PROVENANCE_DELTA|8 variantes classificadas; commits oficiais datados; blob AVX-512 fork diverge; nenhum vínculo repo-deploy|P,C,R,I,E|links+SHAs+comparador GitHub|CDX/WARC/IIS/redirects=TOKEN_VAZIO|coletar WARC/CDX e arquivos de configuração IIS|branch DRAFT-HOLD`

R3 = <captura 2005 e Git SHAs/commits comparados, ausência de WARC e IIS bindings, coleta preservada das variantes e teste do fork por autoridade após revisão>.

**Política:** relatório de pesquisa em ramo de auditoria isolado; não mesclar no main automaticamente. Alterações de dados públicos em 2026 não são, sem cadeia de evidência, manipulação maliciosa.