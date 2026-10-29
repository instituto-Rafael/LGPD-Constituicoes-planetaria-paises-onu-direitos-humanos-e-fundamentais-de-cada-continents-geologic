# Crosswalk preliminar — Breaktrace / BLAKE3 × César Reis × Reis Alves × Reis Office

- μID: MU-CROSSWALK-BREAKTRACE-CESARREIS-REISALVES-20261029-V1
- Data da consulta: 2026-10-29 (America/Sao_Paulo)
- Fonte: endpoints públicos do GitHub; páginas institucionais públicas; tentativa de consulta Wayback/CDX.
- Escopo: comparação **documental e técnica**, sem atribuição de culpa, controle societário ou fraude.
- Estado: PARTIAL_EVIDENCE / claims de manipulação **NÃO autorizados**.
- Fronteira: SOURCE ≠ ARTIFACT ≠ EXECUTION ≠ EVIDENCE ≠ CLAIM.
- Privacidade: somente identificadores de repositório, domínios e documentos públicos; não importa documentação privada de outros repositórios.

## Identidades — não presumir equivalência

| Alvo | Fonte pública | Situação |
| --- | --- | --- |
| `cesarreis.com.br` | Listagem pública identifica `www.cesarreis.com.br` para César Reis Office Products; https://br.todosnegocios.com/pt/cesar-reis-office-products-11-2442-2600 | Evidência **secundária** de referência histórica de domínio, site atual não obtido |
| `reisoffice.com.br` | https://www.reisoffice.com.br/ ; https://reisoffice.com.br/empresa ; https://intranet.reisoffice.com.br/informacoes | Institucional vigente; intranet publicada declara início em 03/07/1984 sob nome `César Reis Comércio de Máquinas` |
| `reisalves.com.br` | https://www.reisalves.com.br/ ; https://www.reisalves.com.br/historia.php | Grupo Reis Alves, rede farmacêutica que declara origem em Dracena/SP em 1996; **não há elo técnico corroborado** com Reis Office |
| `Breaktrace` | Pesquisa de repositórios acessíveis por nome; sem correspondência exata na instalação GitHub consultada | **TOKEN_VAZIO** quanto ao repo/owner. Não substituir silenciosamente por BLAKE3 |
| `BLAKE3-team/BLAKE3` | https://github.com/BLAKE3-team/BLAKE3 | Projeto oficial BLAKE3, repositório criado em 10/11/2019 |
| `rafaelmeloreisnovo/BLAKE3` | https://github.com/rafaelmeloreisnovo/BLAKE3 | Fork acessível com permissão de escrita; **não presumir que seja Breaktrace** |

## Marcos documentais não-Git

- Página institucional da Reis Office informa criação em 1984; https://reisoffice.com.br/empresa
- Informação institucional publicada em `https://intranet.reisoffice.com.br/informacoes` declara antigo nome `César Reis Comércio de Máquinas`; captura da resposta atual não preservada neste registro.
- Notícia institucional `24/11/2017`, relativa ao negócio de café: https://www.reisoffice.com.br/noticias/ver/213/empresa%2Bespecializada%2Bem%2Boutsourcing%2Be%2Bsolucoes%2Bde%2Btecnologia%2Bpassa%2Ba%2Bcomercializar%2Bcapsulas%2Bde%2Bcafe.html
- Página vigente do Grupo Reis Alves: https://www.reisalves.com.br/ (autodescrição como rede de farmácias).
- As datas em páginas correntes não são equivalentes a timestamps Wayback nem provam retrospectivamente o conteúdo no ano citado.

## Comparação Git auditada em 2026-10-29

Oficial:
- Repo: `BLAKE3-team/BLAKE3`
- HEAD observado: `f55849f89cd85083c1c9daa2c5de20766f309c00` (commit de 2026-10-01)
- URL: https://github.com/BLAKE3-team/BLAKE3/commit/f55849f89cd85083c1c9daa2c5de20766f309c00

Fork:
- Repo: `rafaelmeloreisnovo/BLAKE3`
- HEAD observado: `718a8f8e200c42aecfdf5ffedcab6d130ed3dcfb` (commit de 2026-10-27)
- URL: https://github.com/rafaelmeloreisnovo/BLAKE3/commit/718a8f8e200c42aecfdf5ffedcab6d130ed3dcfb
- `compare` do fork, base no oficial HEAD `f55849f...`, head `master`: `status=diverged`, `ahead_by=1060`, `behind_by=29`.
- `merge_base_commit`: `890050cb9b89448a25e067349aed9734a3b03d5e` (último ponto comum observado, dezembro/2025).
- Diferentes commits não implicam automaticamente alteração do algoritmo, e os primeiros 300 arquivos do comparador NÃO constituem inventário completo (resultado paginado/limitado).

SHA Git **blob** no estado consultado, comparado fork vs upstream atual:

| Arquivo | SHA igual? | Observação |
| --- | --- | --- |
| `c/blake3.c` | SIM | `00f91f444922df7c8e7b5ff69343852cbbf4c613` |
| `src/lib.rs` | SIM | `6f652071de0ad06626c427e40354e7ee4872be76` |
| `src/portable.rs` | SIM | `acf48e4a60366b551948efcca7cde9360bcb5fd6` |
| `test_vectors/test_vectors.json` | SIM | `f6da91792c6cdf5c6a0f6dad01803045bb204a68` |
| `c/blake3_neon.c` | NÃO | Fork `53ce83c3b6f351087c26952ab1d37f633b0a7d2d`; oficial `794ea80f4715c63aa5d8593ad2cf21fe427089a9` |
| `Cargo.toml` | NÃO | Fork `e494ebc8ee6301db3d0cac984d731a9a9ca5823b`; oficial `dfde8104a5d60679081b3c459ef5da0278b5bc67` |

Esses SHA são identificadores de objeto Git, **não** hashes extraídos de capturas Wayback. A igualdade comprova conteúdo binário Git idêntico somente para os arquivos examinados nesses refs.

## Limite histórico: 1999–2017 versus Git BLAKE3

A existência das empresas e domínios na década anterior não constitui relação causal com repositório BLAKE3, criado em 2019. Para cruzar eventos de 1999–2017 são necessárias fontes registrárias, DNS/WHOIS históricos e capturas de páginas da época. Uma coincidência de nomes, datas ou palavras não comprova vínculo operacional.

## Wayback/CDX: falha de recuperação, não ausência de captura

- Foram feitas tentativas de abrir o calendário/replay e CDX dos domínios citados via acesso web; o ambiente retornou falhas de acesso.
- Nenhum HTML/arquivo WARC, cabeçalho `Memento-Datetime`, digest CDX ou status HTTP de captura foi recuperado e validado nessa execução.
- `TOKEN_VAZIO`: datas de capturas entre 1999 e 2026, redirects históricos, headers, diferenças de página, donos de domínio em período histórico.
- Variantes a levantar por alvo: esquema `http`/`https`; hosts raiz, `www`, `ww`, `wwww`, `mobile`, `portal`; não assumir que cada variante existiu.
- Ferramenta a consultar quando disponível: `https://web.archive.org/cdx/search/cdx?url=*.cesarreis.com.br/*&output=json&filter=statuscode:200`, com consulta análoga para os outros domínios e repetição por protocolo. URL é um **roteiro de pesquisa**, não comprovante de captura.

## Hipóteses e testes de refutação

- H1: houve diferença real de conteúdo histórico? Exigir par `(url_original,timestamp,digest,response_status,body)` com cadeia de obtenção.
- H2: diferença é efeito de redirecionamento, normalização `http/https`, recursos não arquivados ou bloqueio do archive? Comparar CDX, cabeçalhos e replay bruto.
- H3: um commit causou alteração em domínio brasileiro? Exigir ponte identificável entre repo, deploy, sistema, commit SHA e operação de publicação. **Nenhuma ponte identificada**.
- H4: `Breaktrace` é BLAKE3? **Não confirmado**. Exigir URL GitHub, owner ou identificador verificável.
- H5: Reis Alves é operado pela mesma pessoa jurídica que César Reis/Reis Office? **Não demonstrado** pelos documentos consultados.

## Protocolo de próxima coleta

1. Exportar inventário CDX/WARC com `timestamp`, `original`, `statuscode`, `digest`, `mimetype`, `length`, guardando URL exata de consulta e horário UTC.
2. Para capturas válidas, preservar HTML bruto e resposta memento, calcular SHA-256 ou BLAKE3 sobre o mesmo conjunto de bytes, documentando ferramenta e versão.
3. Confrontar publicações datadas com commits Git e eventuais fontes comprovadas de deploy, sem converter correlação temporal em causalidade.
4. Resolvido o identificador do repo `Breaktrace`, coletar commits daquele repo separadamente; até lá `ROUTE_STATE=BLOCKED` apenas para essa trilha.
5. Se necessário, guardar documentos societários identificáveis somente em destino autorizado e com acesso adequado, não neste repo público.

## μWRITE / Receipt

`MU-CROSSWALK-BREAKTRACE-CESARREIS-REISALVES-20261029-V1|2026-10-29|GitHub-public + sites-public|none|auditoria-preliminar|identidades separadas; divergência Git verificável; Wayback inacessível|P,C,R,E|links e SHAs acima|Breaktrace-repo=TOKEN_VAZIO; WARC=TOKEN_VAZIO|CDX bruto + repo exato|commit da escrita na trilha Git`

R3 = <fontes públicas e SHA Git comparados, Wayback e identidade Breaktrace não verificados, obter capturas brutas e ponte repo-deploy>.
