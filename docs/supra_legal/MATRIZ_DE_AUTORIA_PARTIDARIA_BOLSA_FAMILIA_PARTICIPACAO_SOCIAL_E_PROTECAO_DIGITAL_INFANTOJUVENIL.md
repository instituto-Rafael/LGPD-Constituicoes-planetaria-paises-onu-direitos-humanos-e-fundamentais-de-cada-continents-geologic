# Matriz de autoria partidária — Bolsa Família, participação social e proteção infantojuvenil

> **Documento técnico-jurídico e probatório.**  
> Versão 1.0 — 12 de julho de 2026.  
> Este texto distingue autoria da proposta, apoio legislativo, execução administrativa, continuidade federativa e propaganda partidária. Não atribui propriedade exclusiva de política pública a partido, governo ou autoridade sem documentação correspondente.

## 1. Problema central

A expressão política:

```text
"Bolsa Família do partido X"
```

comprime uma cadeia institucional extensa:

```text
programas_preexistentes
+ iniciativa_do_Executivo
+ medida_provisória_ou_projeto
+ relatoria
+ emendas
+ comissões
+ votação_da_Câmara
+ votação_do_Senado
+ sanção
+ orçamento_anual
+ regulamentação
+ gestão_federal
+ gestão_estadual
+ gestão_municipal
+ CadÚnico
+ saúde
+ educação
+ assistência_social
+ controle_social
+ alterações_posteriores
```

Essa cadeia não possui um único “dono”.

## 2. O que a Lei nº 10.836/2004 demonstra

A lei que criou a primeira versão do Programa Bolsa Família declarou expressamente que o programa unificava procedimentos de gestão e execução de políticas anteriores, especialmente:

- Bolsa Escola;
- Programa Nacional de Acesso à Alimentação;
- Bolsa Alimentação;
- Auxílio-Gás;
- Cadastro Único.

Logo:

```text
Bolsa_Família_2004
≠ criação_material_a_partir_do_zero
```

O programa foi criado por iniciativa presidencial e convertido em lei pelo Congresso, mas incorporou estruturas anteriores e foi executado por uma rede federativa.

## 3. Gestão pública e federativa

A legislação definiu que a execução e a gestão seriam:

- públicas;
- governamentais;
- descentralizadas;
- intersetoriais;
- resultantes da conjugação de esforços entre entes federados;
- submetidas a participação comunitária e controle social.

Estados, Distrito Federal e municípios aderem e executam funções de cadastramento, gestão de benefícios, condicionalidades, articulação intersetorial, acompanhamento e controle.

O próprio portal atual do MDS descreve o Bolsa Família como programa social federal de gestão compartilhada entre Governo Federal, estados e municípios, articulando assistência social, saúde e educação.

```text
PROGRAMA_FEDERAL
≠ PROPRIEDADE_PARTIDÁRIA
```

## 4. Não existe um único percentual de “quanto o PT fez”

A pergunta “quanto por cento o PT representa no Bolsa Família?” não possui resposta única porque mistura grandezas institucionais diferentes.

### 4.1 Presidência

A Presidência pode:

- editar medida provisória;
- enviar projeto;
- coordenar ministérios;
- regulamentar;
- executar orçamento;
- sancionar ou vetar.

Isso é **papel institucional**, não percentual de votos legislativos.

### 4.2 Câmara dos Deputados

A Câmara pode:

- aprovar ou rejeitar;
- emendar;
- alterar valores e critérios;
- votar orçamento;
- fiscalizar execução.

### 4.3 Senado Federal

O Senado revisa o texto, pode emendar e aprovar ou rejeitar, além de exercer suas competências próprias.

### 4.4 Estados e municípios

Executam partes relevantes do cadastro, acompanhamento, saúde, educação, assistência e controle social.

### 4.5 Sociedade e conselhos

A política possui instâncias locais de participação e controle social.

Portanto, a autoria deve ser vetorial:

```text
AUTORIA_PUBLICA =
{
  iniciativa,
  desenho,
  emendas,
  apoio_legislativo,
  orçamento,
  regulamentação,
  execução,
  fiscalização,
  manutenção,
  controle_social
}
```

## 5. Como calcular a participação de cada partido

O cálculo só é possível para atos que deixem rastro individualizável.

### 5.1 Votação nominal

Para cada partido `p`:

```text
favoráveis_p = número de parlamentares do partido que votaram SIM
contrários_p = número de parlamentares do partido que votaram NÃO
abstenções_p = número de abstenções
ausentes_p = número de ausências
```

Percentual de apoio entre votos expressos:

```text
apoio_expresso_p =
favoráveis_p /
(favoráveis_p + contrários_p + abstenções_p)
```

Participação do partido no total de votos favoráveis:

```text
participação_nos_sim_p =
favoráveis_p / total_de_votos_sim
```

Essas duas métricas respondem perguntas diferentes.

### 5.2 Votação simbólica

Na votação simbólica não existe lista completa de votos individuais.

Podem existir:

- orientação de bancada;
- manifestação de liderança;
- declaração posterior;
- requerimento de verificação;
- registro de voto contrário;
- ata e notas taquigráficas.

Mas:

```text
orientação_de_bancada
≠ voto_individual_de_cada_parlamentar
```

Logo:

```text
PERCENTUAL_PARTIDÁRIO_EXATO = TOKEN_VAZIO
```

### 5.3 Votação secreta

Quando o voto é juridicamente secreto:

```text
partido_do_parlamentar
≠ prova_do_voto
```

Não se pode imputar posição individual nem calcular percentual partidário real sem violar a própria natureza do sigilo.

```text
VOTO_INDIVIDUAL_SECRETO = TOKEN_VAZIO
```

### 5.4 Sanção presidencial

A sanção demonstra concordância institucional do Presidente com o texto final, mas não transforma todo o processo em ato exclusivo do partido presidencial.

## 6. Índice de contribuição documentada

Não deve existir um número único sem pesos explícitos. Um índice experimental pode ser:

```text
ICD_p =
  w1 × iniciativa_documentada
+ w2 × emendas_incorporadas
+ w3 × votos_nominais_favoráveis
+ w4 × orçamento_aprovado
+ w5 × execução_comprovada
+ w6 × manutenção
+ w7 × fiscalização
```

Regras:

1. pesos públicos;
2. fontes verificáveis;
3. nenhuma imputação onde o voto não for nominal;
4. separação entre governo e partido;
5. possibilidade de contraprova;
6. atualização histórica;
7. resultado não significa propriedade da política.

## 7. Propaganda eleitoral e nome partidário

Uma comunicação honesta pode afirmar:

- “o governo presidido por X editou a medida”;
- “a bancada do partido apresentou determinada emenda”;
- “foram registrados N votos favoráveis do partido”;
- “o governo executou determinado orçamento”;
- “o município implementou determinado serviço”.

Não deve afirmar como fato exclusivo:

```text
"o benefício pertence ao partido"
"o partido sozinho criou toda a política"
"a família deve o benefício ao partido"
```

Quando não houver votação nominal ou cadeia documental completa, a propaganda deve declarar a limitação:

```text
"não há registro nominal suficiente para atribuir percentual exato por partido"
```

## 8. Participação social vinculada à educação

A proposta apresentada busca transformar transferência de renda em instrumento de inclusão social, aproximação familiar e participação comunitária.

A política pode fortalecer:

- conselho escolar;
- associação de mães, pais e responsáveis;
- grêmio estudantil;
- representação de turma;
- conselho de classe, conforme o sistema educacional;
- busca ativa escolar;
- acompanhamento de frequência;
- mediação de conflitos;
- integração entre escola, assistência, saúde e Conselho Tutelar;
- alfabetização de responsáveis;
- educação cidadã e digital.

### 8.1 Salvaguarda

Participação política, partidária ou voto em conselho não deve ser exigido como condição coercitiva para a sobrevivência material da família.

Uma família vulnerável não deve perder renda por:

- não possuir tempo;
- trabalhar em horários incompatíveis;
- deficiência;
- distância;
- analfabetismo;
- não participação em reunião política;
- discordância com direção escolar ou governo.

O desenho mais seguro é:

```text
RENDA_BÁSICA_PROTEGIDA
+ oferta_de_participação
+ apoio_para_participar
+ reconhecimento_não_coercitivo
+ serviços_de_alfabetização_e_mediação
```

## 9. Rede integrada de proteção e participação

```text
família
↔ escola
↔ representação_de_turma
↔ conselho_escolar
↔ assistência_social
↔ saúde
↔ Conselho_Tutelar
↔ conselhos_de_políticas_públicas
↔ controle_social_municipal
```

Cada elo deve possuir:

- competência definida;
- proteção de dados;
- registro de encaminhamento;
- proibição de uso partidário;
- contraditório;
- indicadores de resultado;
- canal de denúncia.

## 10. Custo do programa e PIB

Não se deve utilizar “1% do PIB” como constante universal.

```text
percentual_do_PIB_ano =
despesa_anual_do_programa /
PIB_nominal_do_mesmo_ano
```

O valor muda conforme:

- número de famílias;
- valor médio do benefício;
- adicionais;
- inflação;
- revisão cadastral;
- orçamento;
- PIB nominal.

A avaliação adequada deve comparar o custo com resultados em:

- pobreza;
- segurança alimentar;
- frequência escolar;
- vacinação e saúde;
- mortalidade;
- violência;
- trabalho infantil;
- desenvolvimento local;
- custo evitado para outras políticas.

## 11. Crianças, jogos digitais e contratos

### 11.1 Capacidade civil

No Brasil, a regra geral atual é:

- menores de 16 anos: absolutamente incapazes de exercer pessoalmente atos da vida civil;
- maiores de 16 e menores de 18: relativamente incapazes para certos atos ou para a maneira de exercê-los;
- aos 18 anos completos: cessa a menoridade civil, salvo regras especiais e hipóteses de emancipação.

Portanto:

```text
IDADE_GERAL_DE_CAPACIDADE_CIVIL = 18
```

Não existe regra geral atual de que todo contrato somente possa ser celebrado aos 21 anos.

### 11.2 Compra dentro de jogo

A compra digital é relação contratual e de consumo, mas sua validade e responsabilidade dependem de:

- idade;
- representação ou assistência dos responsáveis;
- transparência;
- consentimento;
- desenho persuasivo;
- classificação indicativa;
- publicidade;
- proteção de dados;
- possibilidade de arrependimento e contestação;
- vantagem manifestamente excessiva;
- proteção integral da criança e do adolescente.

### 11.3 Regra protetiva proposta

```text
PRODUTO_DIGITAL_INFANTOJUVENIL =
sem_pressão_de_compra
+ sem_design_manipulativo
+ gasto_limitado
+ confirmação_do_responsável
+ preço_claro
+ sem_publicidade_comportamental_sensível
+ histórico_acessível
+ cancelamento_simples
```

## 12. ECA e prioridade absoluta

O Estatuto da Criança e do Adolescente impõe à família, comunidade, sociedade e Poder Público a obrigação de assegurar, com prioridade absoluta, direitos à vida, saúde, alimentação, educação, esporte, lazer, profissionalização, cultura, dignidade, liberdade e convivência familiar e comunitária.

A proteção digital não depende apenas de uma lei com a palavra “digital”. Os princípios gerais de proteção integral, prioridade absoluta, dignidade e defesa contra exploração já estruturam a análise jurídica, complementados por legislação civil, consumerista, de dados e normas específicas vigentes.

## 13. Fórmula de neutralidade da política social

```text
POLÍTICA_SOCIAL_DEMOCRÁTICA =
continuidade_estatal
+ gestão_federativa
+ participação_social
+ controle
+ avaliação
+ proteção_de_dados
+ proibição_de_coerção
+ neutralidade_partidária_do_benefício
```

```text
ATRIBUIÇÃO_PARTIDÁRIA_VÁLIDA =
ato_específico
+ documento
+ voto_nominal_quando_existente
+ orçamento
+ execução
+ limitação_expressa
```

```text
APROPRIAÇÃO_PARTIDÁRIA_INDEVIDA =
benefício_público
+ narrativa_de_propriedade
+ apagamento_da_cadeia_institucional
+ pressão_ou_gratidão_eleitoral
+ vantagem_partidária
+ prova
```

## 14. Protocolo de auditoria

```json
{
  "policy": "TOKEN_VAZIO",
  "predecessor_programs": [],
  "executive_initiative": "TOKEN_VAZIO",
  "rapporteurs": [],
  "incorporated_amendments": [],
  "chamber_vote_type": "nominal|symbolic|secret|TOKEN_VAZIO",
  "chamber_party_votes": {},
  "senate_vote_type": "nominal|symbolic|secret|TOKEN_VAZIO",
  "senate_party_votes": {},
  "presidential_sanction_or_veto": "TOKEN_VAZIO",
  "annual_budgets": [],
  "federal_execution": [],
  "state_execution": [],
  "municipal_execution": [],
  "social_control": [],
  "publicity_claim": "TOKEN_VAZIO",
  "verified_attribution": [],
  "unknown_attribution": [],
  "counterevidence": []
}
```

## 15. Fontes oficiais

- Lei nº 10.836/2004 — primeira versão do Bolsa Família: https://www2.camara.leg.br/legin/fed/lei/2004/lei-10836-9-janeiro-2004-490604-normaatualizada-pl.html
- Portal atual do Bolsa Família — MDS: https://www.gov.br/mds/pt-br/acoes-e-programas/bolsa-familia
- Código Civil — Lei nº 10.406/2002: https://www2.camara.leg.br/legin/fed/lei/2002/lei-10406-10-janeiro-2002-432893-normaatualizada-pl.html
- Estatuto da Criança e do Adolescente: https://www2.camara.leg.br/legin/fed/lei/1990/lei-8069-13-julho-1990-372211-normaatualizada-pl.html

---

**F_ok:** a propriedade partidária foi substituída por matriz de atos, votos, execução federativa e controle social.  
**F_gap:** os percentuais partidários das votações específicas de 2003/2004 e 2023 permanecem `TOKEN_VAZIO` até a auditoria das sessões, votações nominais, simbólicas, orientações e registros de cada Casa.  
**F_next:** extrair a tramitação integral, classificar cada deliberação e produzir tabela por partido somente onde houver voto individual ou orientação formal verificável.
