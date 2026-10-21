# Suplemento probatório Ω V2 — Licenças por SMT, soquete, núcleo e mercados
**Data de referência:** 2026-10-20 | **Estado:** RESEARCH_ADDENDUM / DRAFT_NO_MERGE / claim_allowed=false
**Parent:** docs/CPU_SMT_LICENSING_CROSS_BORDER_FAIRNESS_V1.md | **Autor da hipótese:** ΔRafaelVerboΩ
**Princípio:** SOURCE ≠ ARTIFACT ≠ EXECUTION ≠ EVIDENCE ≠ CLAIM; TOKEN_VAZIO ≠ 0.

## 1. Formulação precisa do pedido e força de prova
A proposição do autor é **uma licença por processador físico/package**, sem criar nova licença só porque o mesmo processador apresenta threads SMT; é distinta de **uma licença por núcleo físico**, pois um package pode ter vários núcleos. Ambas são políticas possíveis, não regras universais dos tratados.
A tese jurídico-econômica passível de contestação: há possível *cobrança duplicada/contratualmente incompatível* quando a oferta promete licenciar o mesmo recurso físico uma vez, a documentação/fatura multiplica unidades por threads e não há cláusula autorizadora; sob outras circunstâncias, preços por threads são válidos e geram valor adicional.
O termo técnico universal `cache_L1_one_buffer_one_processor` permanece FALSIFICÁVEL: cache L1 não é critério necessário/suficiente para identificar socket, core, thread ou preço.

## 2. Fontes comerciais primárias — evidência direta da variabilidade
| Fonte | Regra observável | Peso para tese | Limite |
|---|---|---|---|
| Microsoft, Core-based licensing: https://www.microsoft.com/licensing/guidance/Core-based-licensing-models | SQL Server OSE físico: contar núcleos **físicos**; hyper-threading **não afeta** contagem; mínimo quatro licenças por processador físico | Fortíssimo contra premissa de que todo logical processor necessariamente cria licença | Não cria regra geral um package=uma licença; mínimo contratual impede essa inferência |
| Microsoft, SQL Server Terms pt-BR: https://www.microsoft.com/licensing/spur/pt-BR/productoffering/sqlserver/all | Modo OSE virtual: cobrar núcleos virtuais; se virtual core mapeia em múltiplos hardware threads, a licença pode considerar cada thread | Contraevidência de regra universal "nenhuma thread jamais licenciável" | Condições de versão/assinatura, contrato e virtualização precisam ser verificadas |
| IBM PVU pt-BR: https://www.ibm.com/br-pt/software/passportadvantage/pvu-licensing-for-customers | Para PVU define processador como cada **núcleo de processador** dentro do chip; dual core = dois núcleos para PVU; cálculo depende tecnologia/modelo | Refuta equivalência automática package=1 unidade em todos os modelos | PVU é uma medida contratual própria, não lei |
| Oracle OLSA BR histórico: https://www.oracle.com/br/corporate/olsa/contract-license-olsa-v031609/ | Modelo usa contagem de núcleos × fator; versões Standard antigas podem usar soquete ocupado | Mostra opção real socket versus core | É documento histórico; verificar contrato vigente, versão, produto e descontos antes de qualquer comparação |
| Intel HT guide: https://www.intel.com/content/www/us/en/developer/articles/guide/hyper-thread-tuning-guide-for-video-ai-workload.html | Duas threads lógicas no mesmo core compartilham execução/cache/barramento; estados arquiteturais distintos | Prova técnica de não equivalência thread/core físico | Compartilhamento não implica throughput idêntico nem eliminação de valor marginal |

## 3. Jurisdição, tutela e hipótese de concorrência
**BR Constituição:** art. 173 §4 estabelece repressão legal ao abuso do poder econômico voltado a dominar mercados, eliminar concorrência e aumentar arbitrariamente lucros: https://www4.planalto.gov.br/legislacao/portal-legis/legislacao-1/constituicao

**BR Lei 12.529/2011 art. 36:** indícios dependem de mercado relevante, posição/capacidade de afetar condições de mercado e objeto/efeito potencial; §3 X trata discriminação injustificada de adquirentes por preços/condições quando preenchido o caput. Art. 47 permite ação de cessação e perdas/danos nos termos legais; o ressarcimento dobrado do §1 tem condições e recorte específico (incisos I/II do §3 art.36), **não** é consequência geral da mera cobrança por SMT. Fonte: https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12529.htm

**BR CADE — interpretação oficial:** "O preço ou aumento excessivo por si só não pode ser considerado uma prática lesiva à concorrência"; tipos distintos: preços meramente exploratórios vs abusos excludentes. A lei não torna toda desvantagem aritmética automaticamente infração: https://www.gov.br/cade/pt-br/acesso-a-informacao/perguntas-frequentes/perguntas-sobre-infracoes-a-ordem-economica

**BR Código Civil art. 884–886:** sem justa causa, enriquecimento à custa de outrem e subsidiariedade do remédio; contrato claro e causa jurídica podem enfraquecer a tese. Fonte: https://legis.senado.gov.br/norma/552282/publicacao/34620807

**BR precedente de proximidade limitada:** CADE 23/04/2025, caso Ericsson/Motorola/Lenovo sobre licenciamento de **patentes essenciais SEP 5G**; identificados indícios de discriminação e condições injustas, determinando aprofundamento. **Não prova infração em licenças de software por thread**, nem converte política FRAND de SEP em padrão geral para licenças CPU. Fonte: https://www.gov.br/cade/pt-br/assuntos/noticias/cade-determina-abertura-de-inquerito-para-investigar-a-ericsson-por-pratica-anticoncorrencial

**UE TFUE art. 102(a),(c),(d):** preços não equitativos, condições desiguais para prestações equivalentes e obrigações suplementares desconectadas, somente se demonstrado abuso de dominante com os pressupostos da jurisdição: https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:12016E102
**EUA FTC / Sherman:** a FTC explica que monopólio ou preço alto por si só não são automaticamente ilícitos; métodos irrazoáveis de manutenção/conquista de monopólio são analisados. Fontes: https://www.ftc.gov/advice-guidance/competition-guidance/guide-antitrust-laws/single-firm-conduct e https://www.ftc.gov/enforcement/anticompetitive-practices . Caso Intel/FTC 2010 mostra aplicação antitrust real a mercado de CPUs, mas **não é decisão sobre preço de software por SMT**: https://www.ftc.gov/legal-library/browse/cases-proceedings/061-0247-intel-corporation-matter

**"Trade Trust"** não é identificador confirmado de tratado ou tribunal antitrust internacional; `TRADE_TRUST_ENTITY=TOKEN_VAZIO`. Se pretendido "antitrust" EUA, a autoridade pode envolver FTC/DOJ e Sherman/Clayton/FTC Acts; Brasil = CADE/SBDC. Não afirmar competência mundial do CADE ou da FTC.

## 4. Teste de monotonicidade controlada
Definir `S(x)`=escopo contratual/qualidade de serviço/licenças por CPU, `R(x)`=capacidade física certificada e `price(x)`=total pago comparável (mesma versão, edição, data, moeda, suporte, região, descontos e escopo de utilização).
Proposta de **justiça comercial**, não teorema legal:
Se `S(A)=S(B)` e `R(A) <= R(B)` em todas as dimensões contratuais materiais, mas `price(A)>price(B)` **unicamente** porque foram contadas duas threads SMT de um só core como "dois processadores físicos", há anomalia tarifária a esclarecer: `ANOMALY_INVERSION`.
Isso não demonstra, isoladamente, lucro arbitrário nem ausência de justa causa; preço de software não é função física obrigatoriamente monotônica. Comparação entre CPUs distintas exige cuidado: performance, arquitetura, instruções, memória, energia, latência, suporte e nível de licença podem divergir.

**Exemplos H0/H1 hipotéticos, NÃO faturas:**
- A: 1 package, 1 core, 2 SMT threads; B: 1 package, 2 cores, 2 threads, sem SMT. Política "por package" -> 1 unidade em A e 1 em B. Política "por core físico" -> 1 em A e 2 em B (sujeito a mínimos); política "por thread" -> 2 em ambos. Nenhuma dessas tabelas demonstra ilicitude por si.
- A: 1 package, 1 core, 2 SMT threads. Fornecedor anuncia licença "por processador físico", mas fatura 2 unidades por contagem de logical CPUs: discrepância material se termos e fatos confirmados; investigar cobrança contratual indevida.
- A: mesma CPU com SMT desabilitado vs habilitado, mesmo contrato e workload: comparar preço, licença, throughput e recursos hardware. Valor marginal `ΔQ=Q_SMT_ON-Q_SMT_OFF`; mesmo se ΔQ positivo, nova L1/novo core continuam inexistentes. Não derivar preço justo diretamente de ΔQ.

Indicador de auditoria (NÃO dívida legal):
`delta_units = invoice_units - contract_justified_units`, apenas se ambas contagens observadas e interpretadas. `candidate_overcharge = sum(delta_units * applicable_net_unit_price)` apenas se a mesma SKU e demais condições permitem calcular; descontos e tributação separados; dano indenizável = TOKEN_VAZIO até causa, elementos e perícia.

## 5. Diferenciação CADE: monopólio / oligopólio / cartel
- **Monopólio:** único fornecedor no mercado relevante; não automaticamente ilícito.
- **Oligopólio:** poucos fornecedores; não demonstra por si acordo.
- **Cartel:** acordo/coordenação ilícita entre concorrentes, precisa prova de acordo ou indícios probatórios adequados, não mera semelhança de preços.
- **Abuso unilateral:** conduta anticompetitiva de agente em posição dominante, sem necessidade de cartel.
- **Enriquecimento sem causa:** controvérsia privada com elementos de direito civil, não se confunde com cartel.
Definir mercado relevante por produto/geografia/temporalidade, substitutos, switching/lock-in, dependência de interoperabilidade, efeitos, barreiras, política contratual, participação de mercado. `market_power=TOKEN_VAZIO` até estudo empírico.

## 6. Matriz de prova / refutação e prioridade
| Prioridade | Hipótese | Prova pró necessária | Falsificador/causa de rejeição |
|---|---|---|---|
| P0 | "cobrança duplicada não contratada" | EULA/versionamento + invoice + contrato que define físico + hardware | cláusula trata cada thread e foi válida/aplicável |
| P0 | "hardware lógico apresentado como físico" | topologia verificável e marketing/fatura comparáveis | produto só anuncia métrica virtual e a descreve sem ambiguidade |
| P1 | "conduta discriminatória" | compradores equivalentes, mesmas condições, diferenças injustificadas | diferenciação objetiva legítima de edição/escopo/suporte |
| P1 | "abuso posição dominante" | mercado definido, barreiras, poder e causalidade dos efeitos | mercado competitivo, substitutos efetivos, explicação de eficiência |
| P1 | "cartel" | prova de coordenação/ajustes entre concorrentes | decisões independentes de precificação |
| P2 | "ausência de justa causa" | recebimento, ônus, ausência da causa, subsidiariedade | base contratual válida ou outra via legal prioritária |

## 7. Cadeia de custódia e conclusão epistemológica
Nenhum fornecedor foi responsabilizado/denunciado, nenhum preço foi periciado, nenhum consumidor identificado e nenhuma decisão foi alcançada. Fontes acima: documentos oficiais verificados pelo pesquisador em 2026-10-20; caminhos online podem mudar.
**EVIDÊNCIA CONFIRMADA:** Intel SMT compartilha recursos; Microsoft conta núcleos físicos sem acréscimo de HT nesse modo; IBM define PVU por core; Oracle histórica admite modelos core/socket; CADE examina abusos de licenciamento PI e distingue preço excessivo de infração anticompetitiva.
**HIPÓTESE NÃO COMPROVADA:** existe cobrança individual específica incompatível com contrato, abuso dominante, cartel, preço discriminatório injustificado ou enriquecimento sem causa.
**claim_allowed=false; IMPLEMENTED_DOCUMENT_ONLY; EXACT_HEAD_CI=TOKEN_VAZIO; INDEPENDENT_REVIEW=TOKEN_VAZIO; NO_MERGE.**
Próximas etapas: evidência de EULA+invoice+hardware autorizada e privada; estudo de mercado de produto/geografia; falsificadores e parecer jurídico independente com contraprovas; nunca promover denúncia sem indícios suficientes.
R3 = <fontes diretas e norma comparada, fatos específicos e revisão ausentes, testar caso de faturamento com variáveis isoladas>.
