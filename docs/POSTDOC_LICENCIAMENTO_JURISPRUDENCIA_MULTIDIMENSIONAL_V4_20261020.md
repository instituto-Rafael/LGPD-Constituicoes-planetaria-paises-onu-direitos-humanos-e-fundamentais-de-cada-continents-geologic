# RAFAELIA Ω — Projeto pós-doutoral multidimensional: justiça do licenciamento computacional — V4

**Data:** 2026-10-20 · **Responsável pela hipótese:** ΔRafaelVerboΩ · **Estado:** PRERREGISTRO_DE_PESQUISA / REVISAO_HUMANA_PENDENTE / NO_MERGE / claim_allowed=false.
**Proveniência e filiação:** V1 `CPU_SMT_LICENSING_CROSS_BORDER_FAIRNESS_V1.md` → V2 `CPU_SMT_LICENSING_ANTITRUST_EVIDENCE_V2_20261020.md` → V3 `CPU_CORE_PURO_MULTICORE_BUFFER_POLICY_V3_20261020.md` → **V4** jurídico-doutrinário-jurisprudencial. Título é PROPOSTA DE INVESTIGAÇÃO pós-doutoral, não matrícula, título, credenciamento, chancela acadêmica ou parecer jurídico.
**Contratos:** SOURCE≠ARTIFACT≠EXECUTION≠EVIDENCE≠CLAIM; `TOKEN_VAZIO != 0`; `IMPLEMENTED_UNTESTED != PASS`; documentação não implica culpa; distinguir norma aplicável, analogia, doutrina, jurisprudência, medida técnica e reivindicação político-legislativa.

## 1. Delimitação epistêmica, hipótese e perguntas
Título proposto: **“Licenciamento de software em arquiteturas multicore, SMT e virtuais: convergência entre direito contratual, autoral, concorrencial, consumidor, penal e prova técnica comparada.”**
Problema: fornecedores podem contratar por *package*, core físico, hardware thread, vCPU, instância, usuário, organização ou capacidade computacional. Como distinguir métricas materialmente transparentes, aceitas e legítimas da duplicação de cobrança incompatível com o instrumento e, quando comprovado poder de mercado, do abuso anticoncorrencial?
H1 (proposta): existe uma subclasse identificável de contratos e práticas em que recursos lógicos foram contados como novos recursos físicos, apesar da métrica de promessa e de fatura se referirem a hardware físico; a anomalia pode gerar tutela contratual e, somente com requisitos adicionais, consumidor/concorrencial.
H0 (contra-hipótese): cobrança por thread/vCPU pode ser expressamente pactuada, transparente e remunerar escala de uso, suporte ou desempenho; não é injusta por definição física. Contrato pode prever mínimos por socket/core.
H2 (tecnologia): métrica por buffer privado tipado pode servir como **indicador experimental** de arquitetura, mas não é ontologia de core, nem preço justo universal (Cortex-M0 refuta o requisito necessário de cache).
H3 (direito comparado): direito autoral protege o código/expressão, enquanto regras de concorrência e contratos condicionam modalidades de exploração; nenhum tratado geral impõe “uma licença por processador”.
Critério de rejeição: dados do contrato autorizam a unidade, implementação técnica é fiel, mercado apresenta justificativas econômicas legítimas, ou falta posição dominante/efeito para reivindicação concorrencial.

## 2. Matriz ortogonal de subsistemas jurídicos (convergências e contradições)

### A. Direito civil/contratual/empresarial (Brasil)
- **Fontes:** CC Lei 10.406/2002 arts. 113 (interpretação), 187 (abuso de direito), 421/421-A (liberdade contratual, intervenção mínima e revisão excepcional, presunções B2B), 422 (boa-fé), 423/424 (adesão), 317/478–480 (revisão/resolução sob pressupostos), 884–886 (enriquecimento sem causa e subsidiariedade). https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm
- **A favor investigável:** “processador físico” prometido como métrica enquanto uso real fatura threads lógicas; informação ambígua, surpresa e cálculo inconsistente.
- **Contraditório:** autonomia privada, presunção de paridade B2B e causa jurídica contratual; mero lucro/markup não constitui ausência de causa. Alteração extraordinária/imprevisível exigida no art. 478 não pode ser presumida pela existência de SMT.
- **Precedente STJ:** REsp 1.803.627/SP, j. 23/06/2020, explica subsidiariedade do enriquecimento sem causa e relevância da existência de causa jurídica (caso previdência, **analogia de instituto**, não software): https://scon.stj.jus.br/SCON/jurisprudencia/toc.jsp?livre=1803627
- **Doutrina em confronto:** vedação ao enriquecimento por prestação vs enriquecimento por intervenção (*lucro da intervenção*); critérios de prova de enriquecimento distinto de dano. STJ REsp 1.698.701/RJ (uso de imagem e lucro da intervenção, outra matéria): https://scon.stj.jus.br/SCON/jurisprudencia/toc.jsp?livre=1698701
- **Gate:** exigir EULA versionada + oferta + notas fiscais + CPU real + descontos/SKU + causa contratual. Não confundir inconformidade da cobrança com ilegalidade do modelo em abstrato.

### B. Propriedade intelectual / direito autoral
- **Brasil:** Lei 9.609/1998 arts. 2, 7–12; especialmente art. 9: uso de software no País é objeto de contrato de licença; art. 10 tem hipóteses específicas de nulidade para contratos de comercialização de software de origem externa; art. 12 tipifica violação de direitos autorais de programa. https://planalto.gov.br/ccivil_03/leis/l9609.htm ; Lei 9.610/1998: https://www.planalto.gov.br/ccivil_03/leis/l9610.htm
- **STJ REsp 443.119/RJ**, j. 08/05/2003: natureza autoral e indenização em contrafação/comercialização não autorizada. Prova que titular tem direitos, não que sua política de licenças é imune a contestação civil/concorrencial: https://scon.stj.jus.br/SCON/pesquisar.jsp?b=ACOR&fr=veja&i=1&livre=%28%27RESP%27+INPATH%28CLAS%29+AND+%27443119%27+INPATH%28NUM%29%29
- **STJ REsp 991.721/PR**, j. 25/08/2009: discussão sobre **limites do quantum indenizatório** na utilização sem licença; registro possui notícia de EDcl com efeitos modificativos, razão para **não promover conclusão sem cotejo do inteiro teor atualizado**. https://scon.stj.jus.br/SCON/jurisprudencia/toc.jsp?livre=991721
- **TRIPS art. 9(2), 10(1):** proteção de expressão, não ideias/métodos, programa como obra literária em código-fonte e objeto. https://www.wto.org/english/docs_e/legal_e/trips_e.htm
- **TJUE UsedSoft v Oracle C-128/11**, 03/07/2012: exaustão de distribuição de cópia de software em licença por tempo indeterminado com características da venda; limites em fracionamento de licenças, especialmente multiusuário; **não** regula CPU SMT: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62011CJ0128
- **TJUE SAS Institute v World Programming C-406/10**, 02/05/2012: funcionalidade, linguagem e formatos de arquivos não são protegidos enquanto expressão do programa; leitura conforme fundamento da decisão; não legitima cópia de código/manual protegido: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62010CJ0406
- **Diretiva 2009/24/EC**, arts. 5–8, observação/teste e interoperabilidade sob condições; há disposições contratuais nulas em conflitos específicos com proteção legal, não em qualquer cobrança. https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32009L0024

### C. Concorrencial — CADE, UE, EUA
- **Brasil:** CF art. 173 §4; Lei 12.529/2011 art. 36 (conduta/efeitos), mercado relevante, poder de mercado, fechamento/exclusão e/ou discriminação injustificada; art. 47 tutela civil autônoma com requisitos. https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12529.htm
- **CADE IBM/Red Hat** AC 08700.001908/2019-73, decisão 13/11/2019 APROVADO SEM RESTRIÇÕES quanto à concentração, análise de incentivos/capacidade e rivalidade; caso separado de gun jumping; usar como **controle negativo**: https://www.gov.br/cade/pt-br/assuntos/noticias/compra-da-red-hat-pela-ibm-e-aprovada-sem-restricoes/
- **CADE Google AdWords** investigação de cláusulas para programa de interoperabilidade, arquivada por ausência de características anticompetitivas: **controle negativo de licenciamento**. https://www.gov.br/cade/pt-br/assuntos/noticias/cade-arquiva-investigacao-sobre-clausulas-em-contratos-para-anuncio-no-google-adwords/
- **CADE Ericsson/Motorola/Lenovo SEP 5G**, 23/04/2025, aprofundamento investigatório envolvendo licenciamento de patentes essenciais e alegações de discriminação: não é condenação nem software per-core. https://www.gov.br/cade/pt-br/assuntos/noticias/cade-determina-abertura-de-inquerito-para-investigar-a-ericsson-por-pratica-anticoncorrencial
- **UE Microsoft v Commission T-201/04**, 17/09/2007, abuso relativo à interoperabilidade e tying; demonstra exame concorrencial de práticas com software/IP, **não é decisão sobre vCPU/caches**. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62004TJ0201 ; TFUE art. 102 https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:12016E102
- **EUA U.S. v Microsoft, 253 F.3d 34**, D.C. Cir. 2001, manutenção monopolística da plataforma/entrada de concorrentes, não per-core. https://www.justice.gov/atr/microsoft-tunney-act-comment-litigating-states-california-connecticut-florida-iowa-kansas
- **Doutrina empírica:** Martins & Santos, *Abuso de posição dominante segundo a jurisprudência do Cade*, Revista de Defesa da Concorrência 8(2), 2020; examina aproximadamente vinte precedentes (2009–2019), regra da razão/poder de mercado; é **artigo doutrinário**, não súmula vinculante. https://revista.cade.gov.br/index.php/revistadedefesadaconcorrencia/article/view/498
- **Regra de controle:** monopólio ≠ cartel ≠ oligopólio ≠ ilícito; CADE não é regulador universal de preços privados; preço exagerado isolado não demonstra infração.

### D. Consumidor e vulnerabilidade B2B
- **CDC** arts. 2, 4, 6, 39 V, 46, 51 IV, X: informação, cláusulas excessivas, alteração unilateral de preço, observada EXISTÊNCIA de relação de consumo. https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm
- **STJ REsp 476.428/SC** (2005), teoria finalista mitigada para pessoa jurídica vulnerável, exige situação concreta: https://www.stj.jus.br/websecstj/cgi/revista/REJ.cgi/ITA?dt=20050509&formato=HTML&nreg=200201456245&salvar=false&seq=542170&tipo=0
- **STJ REsp 1.195.642/RJ** (2012), emprego de teoria finalista aprofundada sob vulnerabilidade, não aplicação universal B2B: https://www.stj.jus.br/websecstj/cgi/revista/REJ.cgi/ITA?dt=20121121&formato=HTML&nreg=201000943916&salvar=false&seq=1194152&tipo=0
- **STJ REsp 1.975.128/MS**, julgamento 05/05/2026, informativo 21/07/2026: nega CDC a pessoa jurídica não destinatária final e sem vulnerabilidade comprovada; distribuição dinâmica probatória CPC art. 373 §1 depende de fundamentação concreta. **Controle negativo 2026**: https://processo.stj.jus.br/jurisprudencia/externo/informativo/?acao=pesquisarumaedicao&livre=%270032E%27.cod.

### E. Direito penal e responsabilidade administrativa: não criminalizar divergência técnica
- Lei 9.609/1998 art. 12 criminaliza condutas específicas de violação de direitos de autor sobre programas. O contrato controverso, precificação elevada, threading SMT, oligopólio e "enriquecimento sem causa" **não são, por si sós, tipos penais**.
- Examinar, apenas se houver fatos documentados, possível pertinência de CP art. 171 (fraude e elementos subjetivos), Lei 8.137/1990 art. 4 (infrações contra ordem econômica, requisitos e participação) e eventual relevância dos arts. 12 da Lei 9.609/1998 para cópia não autorizada. **Nenhum crime identificado.**
- **Falsificador penal:** negócio informado e executado conforme contrato, ausência de dolo, erro de identificação de CPU, comportamento sem tipicidade: afastam imputação automática. Crime requer estrita tipicidade, autoria, elemento subjetivo, provas e garantias processuais. Precedentes criminais ESPECÍFICOS per-SMT: TOKEN_VAZIO.

### F. Tributário, processual, prova pericial, dados e internacional privado
- **STF ADI 1945 e ADI 5659** (2021) ISS, não ICMS, no licenciamento/cessão de uso de software; **RE 688.223 (Tema 590)** (2021) ISS também para software personalizado, modulação; decisões tributárias, não fórmula de license fee: https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=461122 e https://portal.stf.jus.br/processos/detalhe.asp?incidente=4245695
- **CPC** art. 369 prova lícita e 373 carga/distribuição dinâmica; 464–480 prova pericial técnica; fonte https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm. Preservar cadeia de custódia técnica do CPU model/serial redigido, CPUID/SoC TRM, snapshot, firmware, hypervisor, contrato datado, fatura e logs, SHA-256; laudo pericial não se reduz a screenshot de "N processors" no SO.
- **LGPD** art. 6 finalidade/necessidade/transparência, art. 46 segurança: minimizar captura de dados pessoais de faturas e licenças; separar repositórios públicos de dossiês privados. https://planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm
- **TRIPS/Berna** dão proteção internacional de software em PI; não são código comercial uniforme de cobrança por núcleo. Lei aplicável, foro/arbitragem, mercado afetado e cláusulas de eleição precisam de avaliação para cada litígio transfronteiriço. `TRADE_TRUST` referido pelo autor continua autoridade ambígua/TOKEN_VAZIO; não o substituir por instituição inventada.

## 3. Doutrinas e métodos que precisam conviver
1. **Boa-fé objetiva / função social / autonomia privada:** controlar assimetrias de informação sem invalidar automaticamente livre fixação de preços e modelos por uso.
2. **Vedação ao enriquecimento sem causa:** demonstrar ausência de causa e subsidiariedade; distinguir desequilíbrio, dano emergente, lucros cessantes, lucro de intervenção e repetição de indébito contratual.
3. **Direitos autorais e exaustão:** distinção entre suporte, licença, reprodução, uso, transferência, interoperabilidade, sublicenciamento e exaustão por jurisdição.
4. **Regra da razão / efeitos concorrenciais / mercado relevante:** testar economias de escala, switching costs, lock-in, interoperabilidade, substitutos, poder de mercado, diferenciação lícita.
5. **Direito penal mínimo, taxatividade e presunção de inocência:** contraditar inflacionamento de ilícitos penais a partir de equações de cobrança.
6. **Acesso à justiça, contraditório, prova pericial, proporcionalidade de remédios:** cada claim tem fonte, pressupostos fáticos, precedente aplicável e contraprova.

## 4. Programa científico falsificável, transversal (sem treinamento ou decisão automática)
**WP1 Técnica (Arquiteto de Computação + Perito):** casos bare-metal CPU single-core, package multicore, SMT on/off, BIG.little, cache privada/compartilhada, vCPU sobrecomissionada; classificar `package/core/thread/buffer/cache` por identidade; ARM Cortex-M0 cacheless falsifica "core=buffer". Entradas firmadas `hardware_snapshot_hash`.
**WP2 Contratos (Civilista + Economista):** amostrar EULAs e termos históricos, anúncios e notas fiscais de mesmas SKUs; classificar unidade, mínimos, regras para virtualização, preço líquido, descontos, escopo e status B2B/CDC.
**WP3 Jurisprudência (Acadêmico de Direito Comparado + Processualista):** extrair *ratio decidendi*; nível hierárquico/órgão/data/jurisdição; `DIRECT|ANALOGICAL|NEGATIVE_CONTROL`; verificar distinguishing/overruling/modulação de efeitos. Estabelecer corpus positivo e negativo, não cherry-picking.
**WP4 Concorrência (Antitruste + Econometria):** definir mercados substituíveis, elasticidade, HHI apenas com dados verificáveis, lock-in; estimar métricas de efeitos com controles antes/depois se factíveis; nunca inferir cartel por preços semelhantes.
**WP5 Penal & Compliance (Criminalista + Autorista + DPO):** red flags separadas, tipicidade/grau de evidência, secret partition de documentos, minimizar dados pessoais e cláusulas confidenciais.
**WP6 Síntese & Reprodutibilidade (Métodos + Revisores):** preregistro H0/H1/H2, falsificadores, tabela de decisões (inclusive adversas), conjunto de testes sintéticos aberto, replicação cega e revisão humana. Resultados podem refutar a tese do autor.

**Desfechos pré-definidos:**
- `D_contract`: unidades efetivamente faturadas – unidades lícitas e contratualmente justificadas; só calcular com contrato e nota verificáveis.
- `A_tech`: distorção factual entre métrica anunciada e topologia real (sem implicar dano).
- `H_competition`: mercado + poder + conduta + efeito; campo `UNKNOWN` quando lacunar.
- `C_copyright`: existência de direito autoral e autorização contratual de uso.
- `P_criminal`: tipicidade/elemento subjetivo, **NÃO_INFERIDO_AUTOMATICAMENTE**.

**Desenho de comparação experimental:** mesma máquina/OS/versão/edição/SKU/suporte/prazo + SMT on/off; core count físico fixo; bytes privados cache tipados; comparar `L_bill`, `L_contract`, `Q_throughput`, `R_resources`. Comparar máquina monocore vs multicore com CPU de mesmo ISA quando possível; heterogeneidade vendor/modelo exige efeitos fixos e variáveis de confusão. Teste de monotonicidade é hipótese normativa, não teorema de preço justo.
**Critérios de confiabilidade:** duplo coding jurídico cego + divergências registradas, matriz de robustez, análise de sensibilidade por jurisdição/época, intervalos de confiança somente após dataset suficiente; falsificar extensão indevida de precedente em domínio distinto.
**Padrão de depósito:** cada precedente recebe link oficial/permalink, ementa/inteiro teor, origem, data, regra, premissas, resultado, `scope`, contraprova, hash de captura se autorizado, correspondência com litígio e risco de supergeneralização.
**Publicações possíveis (NÃO prometidas):** artigo doutrinário comparado; artigo técnico de normalização de topologia; artigo empírico antitruste/contratos; repositório de benchmarks e dataset sem PII; tese de política legislativa separada de afirmações de direito vigente.

## 5. Grafo transversal e gates de promoção
`CPU_RESOURCE` -> `MEASURED_TOPOLOGY` -> `LICENSE_METRIC` -> `CONTRACT` -> `INVOICE` -> `LEGAL_REGIME` -> `MARKET` -> `PRECEDENT_SCOPE` -> `EVIDENCE` -> `FALSIFIER` -> `REVIEW` -> `CLAIM`.
Separar *source* jurisprudência de *artefato* matriz, *execução* benchmark e *evidência* do caso; jurista não presume CPU, perito não declara crime. 
Gate G0 registro hipótese = PASS_SOURCE; G1 citações normativas e decisões oficiais = SOURCE_ONLY_SAMPLE; G2 pesquisa doutrinária sistemática = INCOMPLETE; G3 corpus amostral com controle negativo = PRELIMINARY; G4 observação em hardware real = TOKEN_VAZIO; G5 contrato real + nota + auditoria = TOKEN_VAZIO; G6 acordo entre revisores, causalidade/mercado = TOKEN_VAZIO; G7 revisão humana/institucional/autorização acadêmica = TOKEN_VAZIO. `claim_allowed=false` e `NO_MERGE` até autorização expressa.
**R3:** F_ok = estrutura jurídica comparada, precedentes favoráveis e contrários, método e falsificadores; F_gap = corpus integral e atualização editorial dos precedentes, amostra de contratos, hardware e mercado, elegibilidade acadêmica institucional, revisão independente; F_next = (1) construir codingbook e fichar decisões com inteiros teores (2) testar custos/contagem em cenários controlados e licenciamentos reais autorizados (3) validar proposta com orientador, jurisprudencialista e economista antitruste antes de qualquer claim/denúncia.
