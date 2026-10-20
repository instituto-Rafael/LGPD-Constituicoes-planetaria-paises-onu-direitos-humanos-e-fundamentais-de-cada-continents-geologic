# Núcleo físico, SMT e justiça no licenciamento computacional — Dossiê V1

**Autor da hipótese:** ΔRafaelVerboΩ / RAFAELIA · **Data:** 2026-10-20 · **Estado:** PROPOSTA_JURÍDICA_TÉCNICA / REVISÃO_HUMANA_PENDENTE · **claim_allowed:** false.

## 0. Invariantes de método
SOURCE ≠ ARTIFACT ≠ EXECUTION ≠ EVIDENCE ≠ CLAIM. TOKEN_VAZIO ≠ 0. Lei ≠ tratado ≠ doutrina ≠ contrato ≠ arquitetura de hardware ≠ política proposta. Material de pesquisa: **não** é parecer jurídico, decisão de autoridade, constatação de crime nem regra internacional vigente. Sem publicação como parecer definitivo, denúncias nominativas, incorporação em main, treinamentos, ou submissões sem revisão humana e evidências específicas.

## 1. Pergunta-raiz e tese reformulada
**Pergunta:** sob quais condições é juridicamente justificável contar threads SMT, vCPUs ou núcleos lógicos como unidades adicionais de licença, quando compartilham recursos físicos com outro contexto de execução?

**Tese normativa defendida, ainda não direito positivo:** preferir contagem por unidade física efetivamente relevante, quando o produto/contrato afirmar licenciar capacidade de execução física independente. Exigir divulgação inteligível das condições que justifiquem uma métrica por thread, vCPU, socket, instância, usuário ou core. `LICENÇA_FÍSICA_PREFERIDA` é proposta contratual e não obrigação legal universal.

**Contra-hipótese:** software pode oferecer valor, paralelismo de threads, suporte ou escala computacional mesmo sem cache privada adicional; em contratos claros, e quando lícitos, outros modelos de licença podem ser válidos. Não presumir que preço por thread seja enriquecimento sem causa, conluio, fraude, violação constitucional ou ilícito concorrencial.

## 2. Tecnologia: separações indispensáveis
`physical_package` (socket/SoC) ≠ `physical_core` (núcleo físico) ≠ `logical_processor` (SMT/hardware thread) ≠ `vCPU` (exposição/atribuição virtual) ≠ `cache_instance` (identidade/compartilhamento de cache) ≠ `buffer` (estruturas distintas) ≠ `licensed_unit` (definição contratual).

A cache L1 não é critério único de existência de núcleo nem existe garantia de exatamente um buffer físico por core. Há L1 de instruções e de dados e múltiplas estruturas de buffer; cores e caches podem diferir por microarquitetura. Intel confirma que Hyper-Threading conserva estado arquitetural próprio por thread e compartilha outros recursos (caches, barramentos, unidades de execução). Igualdade `P=L` ou `P=C` não é teorema técnico-jurídico.

Definir por dispositivo: `P` núcleos físicos, `L` threads lógicas, `V` vCPUs alocadas, `K` topologia de caches, `B` buffers tipados (NÃO cardinalidade única), `C` unidades cobradas por contrato, `M` base expressa na cláusula. `ratio=C/P` serve apenas como sinal de auditoria, não inferência de ilicitude; para `P=0|UNKNOWN` ratio=TOKEN_VAZIO (nunca divisão/zero sintético).

Medir por fabricante/modelo/SKU, CPUID/MIDR, SMT siblings, cache shared_cpu_map, NUMA/topologia, hipervisor, afinidade, licenças ativadas e versão de OS. `/sys/devices/system/cpu`, CPUID, documentação de fabricante, lscpu/OS e hipergerenciador podem divergir; colecionar capturas autenticáveis e limitações da observação. Medidas Android/ARM/x86 não são intercambiáveis sem gate.

### Falsificadores técnicos
FT1: dois CPUs com topologia L1 comparável possuem números distintos de cores; refuta tamanho/quantidade de L1 como definição universal de processador.
FT2: SMB/SMT com dois logical_processors no mesmo core e estado arquitetural parcial duplicado; refuta `thread=core físico`.
FT3: workload com SMT produz throughput adicional, ainda com L1 compartilhada; refuta `sem L1 nova => nenhum valor incremental`.
FT4: vCPU virtual pode representar tempo compartilhado/agendamento remoto; refuta correspondência universal `vCPU=core físico exclusivo`.

## 3. Fontes normativas e hierarquia (verificar vigência/jurisdição sempre)
| Âmbito | Fonte e pertinência real | Limite |
| --- | --- | --- |
| TRIPS/OMC | Arts. 9–10: programas em fonte/objeto protegidos por copyright; ideias, métodos e conceitos matemáticos não protegidos como tais | Não define unidade licenciável por hardware |
| OMPI/WCT | Art. 4: proteção de programas como obras literárias | Não fixa preço por cache/SMT |
| Brasil — Constituição | Art. 5º, XXII, XXVII, XXXII e art. 170, IV/V: propriedade, autoria, consumidor e concorrência | Princípios precisam de norma, fatos e aplicação concreta |
| Brasil — Lei 9.609/1998 | Arts. 1–2, 9–10: proteção e licenciamento de software | Não obriga licença única por core |
| Brasil — Código Civil | Arts. 421/422: função social/boa-fé; 884–886: enriquecimento sem causa e subsidiariedade | Exige situação sem justa causa, dano/deslocamento e remédio adequado |
| Brasil — CDC | Arts. 6, 39, 46, 51: informação, práticas e cláusulas abusivas, quando incide relação de consumo | Não presumir relação de consumo B2B |
| Brasil — Lei 12.529/2011 | Art. 36: efeitos nocivos à concorrência, domínio/abuso e lucro arbitrário; competência do CADE | Exige mercado relevante e prova da conduta/efeitos previstos |
| Brasil — LGPD | Lei 13.709/2018 arts. 5–6, 7, 18, 37, 46: tratamento de dados, não regulação geral de preços | Aplica-se a dados pessoais em telemetria, contratos e cobrança |
| EUA — 1ª Emenda | expressão e petição contra restrições estatais em seus contornos | Não proíbe por si preço de fornecedor privado |
| EUA — 4ª Emenda | buscas/apreensões governamentais, fronteira de acesso a logs | Não determina quantos cores são licenciáveis |
| EUA — 5ª Emenda | due process e expropriação estatal com requisitos próprios | Não é causa automática contra preço privado |
| EUA — Sherman/FTC Act | antitrust/unfair methods/unfair or deceptive acts, requisitos dependentes do caso | Preço elevado isolado não prova infração |
| UE — Dir. 2009/24/CE | copyright de software, exceções e atos reservados | Não escolhe uma métrica universal |
| UE — art. 102 TFUE | abuso de posição dominante sujeito a elementos específicos | Domínio de mercado deve ser demonstrado |

**Nota CAD:** “CAD Trust Trade Fair” não foi identificado como uma autoridade/regime normativo único pelas fontes examinadas. Possíveis referentes distintos: **CADE** (Brasil), *antitrust* e regras de *fair trade/unfair competition* (territorialmente definidas). Manter `CAD_ACRONYM=TOKEN_VAZIO` até identificação documental.

## 4. Matriz probatória por caso concreto
| ID | Evidência mínima | Método / contraprova | Estado |
| --- | --- | --- | --- |
| E01 | EULA, SLA, order forms e política de licença com versões/datas | Verificar cláusula específica `C` e aceite | TOKEN_VAZIO |
| E02 | FATURAS, pagamentos, recibos, quantitativo ativado | Reconciliação preço × unidade × período e descontos | TOKEN_VAZIO |
| E03 | CPU SKU, SMT, cache hierarchy e alocação VM | Captura técnica reproduzível e contraprova do fabricante | TOKEN_VAZIO |
| E04 | Oferta e publicidade comercial sobre métrica | Contrastar promessas, riscos de omissão e contrato | TOKEN_VAZIO |
| E05 | Mercado relevante, substitutos, barreiras, efeito sobre consumidores/concorrentes | Teoria do dano concorrencial, alternativas, eficiência | TOKEN_VAZIO |
| E06 | Relação de consumo, jurisdição, escolha de foro/lei, execução | Parecer de advogado habilitado em cada foro | TOKEN_VAZIO |
| E07 | Bases legais e DPIA/RIPD se houver telemetria pessoal | Data minimization, retenção, segurança, acessos | TOKEN_VAZIO |

Sem `E01+E02+E03`: **não quantificar enriquecimento ou dano**. Sem `E05`: não alegar antitrust. Sem `E06`: não afirmar violação final. Controvérsias/contraprovas devem ser preservadas como arestas, não apagadas.

## 5. Teste de falsificação jurídico e econômico
FJ1: texto contratual prevê licenciamento por logical processor, foi claramente informado, aceito e não é abusivo segundo a lei aplicável -> enfraquece tese de pagamento sem causa.
FJ2: capacidade/benefícios mensuráveis por SMT mesmo com recursos compartilhados -> enfraquece premissa de ausência total de contraprestação.
FJ3: ausência de mercado dominante e existência de substitutos -> enfraquece caminho do abuso de posição dominante, sem excluir outras causas.
FJ4: cliente empresarial sem tutela do CDC no caso concreto -> exige fundamentação civil/concorrencial independente.
FJ5: prova de omissão material, divergência de faturamento ou alteração unilateral injustificada -> aumenta viabilidade de revisão contratual; não condena automaticamente.

## 6. Arquitetura federada e tratamento de dados
`LGPD_CONSTITUICOES` (fonte produtora de crosswalk legal, dados normativos e hipóteses) → `Mapa` (roteador semântico e tipos de evidência) → `Google Drive` (governança documental/ledger) ↔ `alphaXiv` (papers como material científico, não lei) → `avaliação humana externa`.

Permitir somente dados técnicos desidentificados nos repositórios públicos. Documentos comerciais, invoices, IDs e contratos potencialmente confidenciais permanecem em armazenamento privado autorizado, sem push automático. Hash atesta igualdade de bytes, não licitude ou verdade. Nunca autorizar contorno de EULA nem coleta clandestina.

## 7. Gates para promoção
G0 Identidade e autoridade dos objetos.
G1 Fontes primárias e vigência cruzadas.
G2 Taxonomia de CPU falsificada contra arquiteturas heterogêneas e virtualizadas.
G3 Cláusula + fatura + medição + contraparte reprodutíveis.
G4 Jurisdição, legitimidade, aplicabilidade do CDC/antitrust.
G5 Revisão independente de Direito contratual, Direito Econômico, PI e Eng. da Computação.
G6 CI exato de schema/documentação; aceite humano explícito antes de promover.
No momento: `G0=PARTIAL`, `G1=SCOPED_SOURCE_CHECK`; `G2..G6=TOKEN_VAZIO`; `claim_allowed=false`; `NO_MERGE`.

## 8. Fontes primárias e literatura
- https://www.intel.com/content/www/us/en/support/articles/000098959.html
- https://edc.intel.com/content/www/us/en/design/ipla/software-development-platforms/client/platforms/alder-lake-desktop/12th-generation-intel-core-processors-datasheet-volume-1-of-2/001/intel-hyper-threading-technology/
- https://www.wto.org/ENGLISH/docs_e/legal_e/31bis_trips_04_e.htm
- https://www.wipo.int/en/web/treaties/ip/wct/index
- https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm
- https://www.planalto.gov.br/ccivil_03/leis/l9609.htm
- https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm
- https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm
- https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12529.htm
- https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm
- https://www.law.cornell.edu/constitution/first_amendment
- https://www.law.cornell.edu/constitution/fourth_amendment
- https://www.law.cornell.edu/constitution/fifth_amendment
- https://www.ftc.gov/enforcement/anticompetitive-practices
- https://eur-lex.europa.eu/legal-content/en/TXT/?uri=CELEX:32009L0024
- https://www.alphaxiv.org/abs/2608.23165 (CPU/cache; paper não define licenciamento)
- https://www.alphaxiv.org/abs/2403.14927 (licenciamento; não trata diretamente da tese SMT)

## R3
F_ok = hipótese registrada e delimitada, fontes oficiais identificadas e crosswalk separa jurisdição/força/prova.
F_gap = E01–E07 desconhecidos e competência/acrônimo CAD ambíguo; nenhum caso individual comprovado.
F_next = colher contrato+fatura+topologia mínima autorizados → auditoria econômico-jurídica em versão protegida → revisão independente e falsificadores.
