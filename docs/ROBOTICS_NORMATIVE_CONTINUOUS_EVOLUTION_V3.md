# ROBOTICS NORMATIVE CONTINUOUS EVOLUTION V3

**Estado:** `AUDITABLE / VERSIONED / NON_REGRESSION / PROVENANCE_FIRST / FAIL_CLOSED`

**Data de corte:** `2026-08-26`

## 1. Objeto

Este protocolo governa a evolução jurídica, regulatória e técnico-normativa do framework Robotics. Seu objetivo é impedir três falhas recorrentes:

1. norma antiga permanecer tratada como atual;
2. orientação, standard ou certificação ser elevada indevidamente à condição de lei;
3. atualização normativa apagar direitos, lacunas, contraditórios ou a cadeia de custódia anterior.

Robotics não é categoria jurídica positivada. É uma abstração operacional para sistemas automatizados que coletam, inferem, classificam, ranqueiam, recomendam, decidem, agem, transmitem, retêm ou eliminam informação sobre pessoas.

## 2. Regra-mãe

```text
FONTE
→ AUTORIDADE
→ JURISDIÇÃO
→ VERSÃO/DATA
→ ESCOPO
→ ARTIGO/REQUISITO
→ CONTROLE
→ IMPLEMENTAÇÃO
→ EXECUÇÃO
→ EVIDÊNCIA
→ CLAIM
```

Qualquer aresta ausente produz `TOKEN_VAZIO` no ponto exato da ruptura.

```text
TOKEN_VAZIO != NÃO
TOKEN_VAZIO != ZERO
TOKEN_VAZIO != LICENÇA PARA INFERIR
```

## 3. Hierarquia tipada — não uma hierarquia universal de conflitos

Cada fonte recebe tipo:

- Constituição/direito fundamental;
- tratado aplicável;
- lei;
- regulamento;
- decisão de regulador;
- decisão judicial;
- contrato juridicamente válido;
- norma técnica;
- Best Current Practice;
- framework;
- guia/orientação;
- política interna;
- preferência do usuário.

Essa classificação **não resolve sozinha conflito de leis**. Conflitos reais dependem de jurisdição, competência, matéria, vigência e fatos.

## 4. Brasil — baseline jurídico mínimo

### 4.1 Constituição

O desenho deve preservar, conforme aplicabilidade, privacidade, intimidade, sigilo de comunicações/dados e o direito fundamental à proteção de dados pessoais, inclusive nos meios digitais.

### 4.2 LGPD

Artigos nucleares para Robotics:

| Artigo | Função no sistema |
|---|---|
| 1º–2º | finalidade protetiva e fundamentos da disciplina de dados |
| 6º | princípios: finalidade, adequação, necessidade, livre acesso, qualidade, transparência, segurança, prevenção, não discriminação, responsabilização |
| 7º | bases legais de dados pessoais |
| 8º | consentimento quando utilizado; prova, especificidade e revogação |
| 9º | acesso facilitado a informações claras, adequadas e ostensivas |
| 10 | legítimo interesse sob necessidade, transparência e salvaguardas |
| 11 | dados sensíveis |
| 14 | crianças e adolescentes, dentro da redação e regime aplicáveis |
| 17–18 | direitos do titular |
| 20 | revisão/informações sobre decisões unicamente automatizadas que afetem interesses, dentro do escopo legal |
| 33–36 | transferências internacionais |
| 37 | registro das operações |
| 38 | RIPD quando requerido/aplicável |
| 40 | interoperabilidade/portabilidade e padrões definidos pela ANPD |
| 41 | encarregado |
| 44 | irregularidade do tratamento e segurança esperada |
| 46 | segurança técnica/administrativa desde concepção até execução |
| 48 | comunicação de incidente nas hipóteses legais/regulatórias |
| 49–51 | sistemas, boas práticas, governança e padrões técnicos |
| 52 | sanções e critérios, inclusive governança/correção |

### 4.3 Resoluções ANPD já vigentes e materialmente relevantes

- **Resolução 15/2024** — comunicação de incidentes de segurança;
- **Resolução 18/2024** — atuação do encarregado;
- **Resolução 19/2024** — transferência internacional de dados e cláusulas-padrão contratuais, com retificação posterior;
- **Resolução 30/2025** — Mapa de Temas Prioritários 2026–2027;
- **Resolução 31/2025** — atualização da Agenda Regulatória 2025–2026;
- **Resolução 32/2026** — adequação da União Europeia para fins de transferência internacional.

## 5. Mudanças materiais de 2025–2026

### 5.1 ECA Digital

A Lei 15.211/2025 instituiu o Estatuto Digital da Criança e do Adolescente. A Lei 15.352/2026 fixou sua entrada em vigor em **17 de março de 2026** e alterou a estrutura jurídica relacionada à ANPD.

Para Robotics isso cria uma classe de risco própria para serviços acessíveis a crianças/adolescentes, incluindo, conforme o caso:

- aferição/garantia de idade;
- supervisão parental;
- design apropriado à idade;
- publicidade;
- prevenção/mitigação de riscos;
- tratamento de dados para mecanismos de proteção.

### 5.2 Agenda e fiscalização ANPD

No ciclo 2026–2027, a ANPD indicou como temas prioritários, entre outros:

- direitos dos titulares;
- proteção de crianças e adolescentes no ambiente digital;
- tratamento pelo Poder Público;
- inteligência artificial e tecnologias emergentes no tratamento de dados pessoais.

A Agenda Regulatória 2025–2026 inclui direitos dos titulares, RIPD, biometria, segurança mínima, IA, tratamento de alto risco, anonimização/pseudonimização, governança, agregadores, consentimento e outros temas.

Em agosto de 2026, o plano ECA Digital prevê fase de adaptação/monitoramento de mecanismos de aferição de idade entre agosto e novembro de 2026 e ações de fiscalização mais adiante segundo o cronograma regulatório.

Portanto:

```text
NORMATIVE_STATE_2024 != NORMATIVE_STATE_2026
```

Um framework estático de LGPD já é insuficiente para representar o estado regulatório atual.

## 6. Transferência internacional — não reduzir a “dados fora do Brasil”

A Resolução 19/2024 regulamenta mecanismos dos arts. 33–36 da LGPD e diferencia hipóteses, mecanismos e requisitos.

Em 2026, a Resolução 32 reconhece adequação da União Europeia.

O registry Robotics deve registrar:

```text
exporter
importer
destination jurisdiction/organization
transfer characterization
applicable mechanism
adequacy status
contractual mechanism if any
purpose
categories of data
onward transfers
rights/contact
observed source/date
```

Não se deve inferir mecanismo apenas porque há infraestrutura estrangeira ou acesso remoto.

## 7. União Europeia — AI Act em 26/08/2026

O Regulamento (UE) 2024/1689 entrou em vigor em 2024 e tem aplicação escalonada.

Em 2026, a regra geral passou a ser aplicável em **2 de agosto de 2026**, mas o regime de determinadas obrigações de sistemas de alto risco foi ajustado pelo Regulamento (UE) 2026/1744:

- casos de alto risco do Anexo III: aplicação relevante adiada para **2 de dezembro de 2027**;
- sistemas de alto risco ligados aos produtos do Anexo I: **2 de agosto de 2028**.

Obrigações já aplicáveis em fases anteriores ou na aplicação geral não devem ser confundidas com as datas desses subconjuntos.

Invariante:

```text
AI_ACT_EXISTS
!= ALL_HIGH_RISK_OBLIGATIONS_HAVE_SAME_EFFECTIVE_DATE
```

O framework deve guardar `article + system_class + applicability_date + jurisdiction + role(provider/deployer/etc.)`.

## 8. Standards — versão e estado importam

### 8.1 ISO/IEC 27701

A edição publicada atual é **ISO/IEC 27701:2025, edição 2**, para Privacy Information Management Systems.

### 8.2 ISO 14001

A edição publicada atual é **ISO 14001:2026, edição 4**. A edição 2015 foi substituída e organizações certificadas possuem período de transição conforme seu ciclo/certificadora.

### 8.3 ISO/IEC 42001

**ISO/IEC 42001:2023** permanece publicada como standard de sistema de gestão de IA.

### 8.4 ISO 8000

**ISO 8000-1:2022** fornece visão geral e princípios da família de qualidade de dados. Usar a família apenas pelo número “8000” é insuficiente: a parte aplicável deve ser identificada.

### 8.5 IEEE 7000 series

Referências relevantes observadas como standards ativos incluem:

- IEEE 7000-2021 — ética no design;
- IEEE 7002-2022 — processo de privacidade de dados;
- IEEE 7003-2024 — viés algorítmico;
- IEEE 7007-2021 — ontologia para Robotics/automation orientados eticamente;
- IEEE 7009-2024 — fail-safe para sistemas autônomos/semi-autônomos.

### 8.6 RFC

- RFC 6973 é **Informational**, não Internet Standard Track; fornece considerações de privacidade para protocolos;
- RFC 3552 é **BCP 72**, com atualizações posteriores; fornece disciplina para Security Considerations.

Isso demonstra por que `RFC` também precisa de classe/status, não apenas número.

## 9. Contrato de evolução normativa

Cada fonte `s` mantém:

```text
source_id
issuer
authority_type
jurisdiction
version/number
publication_date
effective_date
status
supersedes
superseded_by
scope
source_url
checked_at
impacted_controls
```

### 9.1 Eventos que obrigam revalidação

- nova lei ou emenda;
- nova resolução/regulamento;
- decisão de adequação;
- decisão judicial material ao claim;
- nova edição/retirada de standard;
- vencimento/alteração de certificado;
- alteração de finalidade;
- novo tipo de dado, inferência ou compartilhamento;
- nova jurisdição;
- mudança relevante no modelo/algoritmo;
- nova categoria de usuário vulnerável;
- incidente de segurança;
- resultado de auditoria independente contrário ao baseline.

## 10. Não regressão

Uma atualização `Δ` é rejeitada quando:

1. remove campo obrigatório de direitos sem fundamento jurídico;
2. transforma `TOKEN_VAZIO` em `PASS` sem evidência;
3. converte guidance em lei;
4. mantém standard retirado como current;
5. usa certificado fora de escopo;
6. aumenta coleta/inferência sem novo propósito/base/necessidade;
7. amplia compartilhamento sem atualizar destinatário/transferência;
8. perde proveniência;
9. apaga recibos históricos;
10. diminui contestabilidade sem autoridade e justificativa;
11. reduz proteção de criança/adolescente por default de conveniência;
12. promove claim econômico/criminal sem contraditório e fonte competente.

## 11. Proveniência e cadeia de custódia

Para cada regra ou claim:

```text
SOURCE
→ SNAPSHOT
→ EXCERPT/ANCHOR
→ INTERPRETATION
→ CONTROL_MAPPING
→ IMPLEMENTATION_REFERENCE
→ EXECUTION_RECEIPT
→ INDEPENDENT_ASSURANCE (quando houver)
→ CLAIM_STATE
```

Não armazenar apenas URL. URL sem data, escopo e versão não sustenta reprodutibilidade suficiente.

## 12. Contratos

### 12.1 Contrato normativo

Define a autoridade e o alcance do requisito.

### 12.2 Contrato técnico

Define o controle ou implementação que pretende satisfazê-lo.

### 12.3 Contrato de evidência

Define qual teste/artefato pode demonstrar o controle — e o que **não** demonstra.

### 12.4 Contrato de usuário

Expõe em linguagem acessível propósito, dados, automação, compartilhamento, retenção, direitos e contato.

### 12.5 Contrato de auditoria

Define independência, amostragem, critério, período, escopo, exceções e limitações.

## 13. Falsificadores jurídicos e de compliance

Um claim de conformidade deve cair ou ser reduzido se:

- fonte primária contradiz o crosswalk;
- versão normativa mudou;
- operação real excede finalidade declarada;
- base legal não cobre o propósito;
- direito existe no documento mas rota é inexistente/inoperante;
- retenção prática excede a regra sem justificativa;
- certificado não cobre o produto/site/processo alegado;
- transferências não correspondem ao mecanismo declarado;
- decisão automatizada material não aparece no inventário;
- incidente relevante não possui cadeia de resposta exigível;
- a interface produz interpretação sistematicamente errada nos usuários.

## 14. Ciência de fronteira: Direito como requisito testável sem reduzir Direito a código

O objetivo não é “compilar a lei” como se interpretação jurídica fosse puramente mecânica. O objetivo é decompor afirmações operacionais em elementos auditáveis:

```text
regra aplicável
+ fato observado
+ interpretação declarada
+ controle
+ evidência
+ incerteza
+ contraditório
```

O resultado é uma ponte entre exatas e humanas: a lógica formal ajuda a detectar inconsistências; a hermenêutica delimita significado e competência; a evidência empírica testa implementação; a ética estabelece fronteiras de não instrumentalização da pessoa.

## 15. Hipóteses sistêmicas e econômicas

Podem ser investigadas, mas não promovidas por narrativa:

- concentração e lock-in;
- assimetria de informação;
- assimetria regulatória;
- custo desproporcional de assurance/certificação;
- dependência tecnológica;
- efeitos distributivos entre economias desenvolvidas e emergentes;
- influência de plataformas sobre mercados de informação;
- risco sistêmico financeiro por infraestrutura informacional.

Cada uma exige definição operacional, dados, causalidade, alternativas e falsificador.

```text
CONCENTRATION != CARTEL
DEPENDENCY != LEGAL_SLAVERY_CLASSIFICATION
FOREIGN_CERTIFICATION != SOVEREIGNTY_VIOLATION
FINANCIAL_HARM != INTENTIONAL_ATTACK
```

## 16. Estado das lacunas

### Fechadas documentalmente nesta linha de trabalho

- artigos LGPD mapeados;
- classes de authority/source;
- crosswalk com standards;
- distinção informação/consentimento;
- First Question / Pre-Processing Governance Gate;
- ligação proposta ao Mapa;
- evolução normativa 2026 identificada;
- contrato de não regressão definido.

### Permanecem `TOKEN_VAZIO`

- parecer jurídico vinculante para implantação concreta;
- cláusulas integrais de standards não publicamente acessíveis em sua totalidade;
- runtime Robotics;
- prova de compreensão dos usuários;
- auditoria independente do runtime;
- matrícula formal do LGPD como autoridade/produtor no Mapa;
- claims fortes concorrenciais, financeiros ou de soberania sem caso e evidência específicos.

## 17. Fontes oficiais de controle do snapshot

- Planalto — Lei 13.709/2018;
- Planalto — Lei 15.211/2025;
- Planalto — Lei 15.352/2026;
- ANPD — Regulamentações;
- ANPD — Transferência Internacional de Dados;
- ANPD — ECA Digital;
- ANPD — Agenda Regulatória 2025–2026;
- ANPD — Mapa de Temas Prioritários 2026–2027;
- EUR-Lex — Regulamentos 2024/1689 e 2026/1744;
- ISO — metadata oficial de 27701:2025, 14001:2026, 42001:2023 e 8000-1:2022;
- IEEE Standards Association — metadata da série 7000;
- RFC Editor — RFC 6973 e RFC 3552.

## 18. Invariante final

```text
LEGALIDADE SEM PROVENIÊNCIA = CLAIM FRÁGIL
TRANSPARÊNCIA SEM COMPREENSÃO = PARADOXO
CONTROLE SEM ROTA OPERACIONAL = CONTROLE NOMINAL
AUDITORIA SEM ESCOPO = ASSERTIVA AMBÍGUA
NORMA SEM VERSÃO = RISCO DE OBSOLESCÊNCIA
AUTOMAÇÃO SEM CONTESTAÇÃO/EXPLICAÇÃO QUANDO EXIGÍVEL = GAP
MUDANÇA SEM REVALIDAÇÃO = REGRESSÃO POTENCIAL
```

**F_ok:** baseline V3 inclui mudanças jurídicas/regulatórias materiais até 26/08/2026 e contrato de evolução/não regressão.

**F_gap:** execução, assurance independente e interpretação jurisdicional de casos concretos continuam fora do alcance documental.

**F_next:** materializar snapshot JSON V3, testes de integridade e incorporá-los ao workflow do PR.
