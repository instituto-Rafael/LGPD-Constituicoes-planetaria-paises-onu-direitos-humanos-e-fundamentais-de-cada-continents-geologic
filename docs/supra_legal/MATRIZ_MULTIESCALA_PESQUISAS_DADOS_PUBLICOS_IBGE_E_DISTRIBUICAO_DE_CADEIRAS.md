# Matriz multiescala — pesquisas, dados públicos, IBGE, cadastro eleitoral e distribuição de cadeiras

> **Documento técnico-jurídico, estatístico e operacional sobre infraestrutura informacional do processo eleitoral.**  
> Versão: 1.0 — 12 de julho de 2026.  
> Este texto não atribui culpa automática ao IBGE, à Justiça Eleitoral, a instituto de pesquisa, partido, servidor, plataforma ou eleitor. Responsabilidade exige competência, conduta, finalidade, controle, nexo, dano ou risco juridicamente relevante e prova.

## 1. A pergunta correta

A pesquisa eleitoral “dá” cadeira a um partido?

**Diretamente, não.** As cadeiras de vereador são juridicamente distribuídas a partir dos votos válidos, do número de lugares da Câmara, do quociente eleitoral, do quociente partidário, das votações nominais e das regras de preenchimento das sobras.

**Indiretamente, pode influenciar o caminho até esses votos.** Pesquisa, estatística territorial e dados de campanha podem orientar:

- escolha de candidaturas;
- desistências e alianças;
- concentração territorial de recursos;
- agenda de visitas e eventos;
- mensagens por bairro ou grupo social;
- distribuição de propaganda;
- mobilização e comparecimento;
- captação de doadores e apoiadores;
- percepção pública de viabilidade;
- voto útil e abandono de opções percebidas como inviáveis.

Portanto:

```text
pesquisa ≠ cadeira

pesquisa
→ decisão estratégica
→ distribuição de recursos
→ comunicação e mobilização
→ votos nominais e de legenda
→ quocientes e médias
→ cadeiras
```

A cadeia pode produzir êxito eleitoral sem que a pesquisa participe formalmente da apuração.

## 2. Quatro bases que não podem ser confundidas

| Base | Gestor principal | Unidade | Função eleitoral possível | Limite essencial |
|---|---|---|---|---|
| Estatística demográfica e territorial | IBGE | população, domicílios, território, agregados | dimensionamento institucional, contexto social e políticas públicas | não é cadastro nominal de preferência eleitoral |
| Cadastro eleitoral | Justiça Eleitoral | eleitor inscrito, domicílio, zona e seção | habilitação para votar e organização da votação | sigilo do voto e finalidade eleitoral pública |
| Pesquisa eleitoral | instituto ou entidade responsável | amostra de respondentes | estimar opinião em período e método determinados | não equivale a censo nem a resultado eleitoral |
| Dados partidários e digitais | partidos, campanhas, plataformas e fornecedores | contatos, interações, apoiadores, audiência | organização, comunicação e mobilização | LGPD, finalidade, transparência e proibição de abuso |

Misturar as quatro bases cria conclusões falsas, como:

```text
população_do_IBGE = número_de_eleitores              [FALSO]
amostra_de_pesquisa = resultado_da_urna               [FALSO]
cadastro_eleitoral = preferência_política             [FALSO]
dado_agregado = sempre_anônimo_e_sem_risco             [FALSO]
dado_público = uso_irrestrito_para_qualquer_finalidade [FALSO]
```

## 3. Onde o IBGE realmente entra

### 3.1 Número máximo de vereadores

A Constituição fixa faixas populacionais para a composição das Câmaras Municipais, com limites que começam em nove vereadores nos municípios de até quinze mil habitantes e avançam conforme a população.

Logo, a informação populacional oficial pode influenciar o **limite constitucional de lugares** disponível no município.

```text
população_oficial
→ faixa_do_art_29_IV
→ limite_máximo_de_cadeiras
→ lei_orgânica_e_composição_da_Câmara
```

Esse é um vínculo institucional real entre estatística demográfica e estrutura de representação.

### 3.2 O que o IBGE não faz

O IBGE não:

- registra o título eleitoral;
- decide quem está apto a votar;
- registra votos;
- calcula votos de legenda;
- entrega cadeiras a partidos;
- apura o quociente partidário;
- conhece, por função estatística, o voto secreto de cada pessoa;
- transforma recenseado em eleitor de determinado partido.

### 3.3 Sigilo estatístico

As informações individualizadas prestadas para fins estatísticos estão submetidas a regime de sigilo e finalidade própria. A divulgação legítima ocorre por resultados agregados, tabelas, indicadores, mapas e produtos estatísticos que devem mitigar identificação indevida.

O fato de uma estatística ser pública não significa que o dado individual subjacente possa ser cedido, cruzado ou reutilizado livremente para propaganda política.

### 3.4 Quando pode haver responsabilidade do IBGE

Não existe culpa apenas porque o instituto produz dados úteis à política. Poderia haver matéria de apuração se fossem demonstrados, por exemplo:

- vazamento de informação individual protegida;
- compartilhamento fora da finalidade estatística e sem base jurídica;
- favorecimento seletivo de partido ou candidatura;
- manipulação metodológica deliberada;
- divulgação assimétrica ou embargo utilizado com finalidade eleitoral;
- falha grave de segurança com nexo demonstrado;
- recusa discriminatória de acesso a produto que deveria ser público e isonômico;
- produção oficial apresentada de modo partidário por agente competente.

```text
produzir_estatística_pública ≠ culpa

responsabilidade_estatística =
conduta_irregular
+ competência
+ violação_de_dever
+ finalidade_ou_culpa_quando_exigida
+ nexo
+ prova
```

## 4. Onde o TSE e a Justiça Eleitoral entram

A Justiça Eleitoral administra o cadastro eleitoral e organiza a circunscrição, as zonas, seções, locais de votação, candidaturas, prestação de contas, votação e totalização.

O cadastro eleitoral responde a uma pergunta diferente da estatística populacional:

```text
IBGE: quantas pessoas e quais características agregadas existem no território?
TSE: quais pessoas estão juridicamente inscritas e aptas na circunscrição eleitoral?
```

A diferença importa porque:

- habitantes incluem pessoas sem alistamento eleitoral;
- eleitores podem possuir domicílio eleitoral sujeito às regras próprias;
- segundo turno municipal depende de número de **eleitores**, não apenas de habitantes;
- o total de vereadores está vinculado a faixas de **habitantes**;
- quocientes eleitorais dependem de **votos válidos efetivamente apurados**.

## 5. Como as cadeiras proporcionais são formadas

### 5.1 Quantidade total de lugares

Primeiro existe o número de cadeiras da Câmara Municipal, dentro dos limites constitucionais populacionais e da disciplina local válida.

### 5.2 Quociente eleitoral

```text
QE = votos_válidos_da_circunscrição / lugares_a_preencher
```

O Código Eleitoral disciplina o arredondamento.

### 5.3 Quociente partidário

```text
QP_partido = votos_válidos_do_partido / QE
```

A parte inteira indica inicialmente quantos lugares a legenda pode preencher, observadas as exigências legais de votação nominal.

### 5.4 Candidatos e sobras

O preenchimento considera a ordem de votação nominal dentro da legenda e as regras legais e jurisprudenciais de distribuição dos lugares remanescentes.

Como os arts. 109 e 111 do Código Eleitoral receberam alterações e decisões do STF nas ADIs 7.228, 7.263 e 7.325, qualquer cálculo operacional deve usar:

```text
lei_atualizada
+ resolução_do_TSE_da_eleição
+ efeitos_temporais_dos_acórdãos_do_STF
```

Não se deve reutilizar fórmula de eleição anterior sem conferir a regra vigente.

## 6. Êxito partidário e inteligência eleitoral

O partido não recebe “um pedaço de cada cadeira”. Ele recebe um número inteiro de lugares conforme as regras proporcionais. Porém, antes da eleição, pode estimar probabilidades e definir metas territoriais.

### 6.1 Cadeia estratégica legítima

```text
dados_públicos_agregados
+ pesquisas_regulares
+ histórico_eleitoral
+ presença_organizacional
→ cenários
→ estratégia
→ campanha
→ votos
```

Isso pode ser legítimo quando respeita transparência, proteção de dados, financiamento, igualdade de oportunidades e ausência de coerção.

### 6.2 Cadeia de risco

```text
dados_públicos
+ dados_pessoais_indevidos
+ perfilamento_opaco
+ vulnerabilidade_social
+ desinformação
+ pressão_microterritorial
→ assimetria_de_poder
→ redução_da_autonomia
→ possível_abuso
```

O risco não está em “usar números”, mas em combinar escala, granularidade, finalidade e poder de intervenção sem salvaguardas.

## 7. O direito e o dever de votar de agentes públicos

Agentes públicos continuam cidadãos. Em regra, possuem direitos políticos e voto direto, secreto e de valor igual ao dos demais eleitores, observadas as restrições constitucionais específicas.

Para maiores de dezoito e menores de setenta anos, o voto é obrigatório, salvo hipóteses constitucionais e legais; é facultativo para analfabetos, maiores de setenta anos e pessoas entre dezesseis e dezoito anos.

O agente público possui duas posições que não podem ser fundidas:

```text
ESFERA_PESSOAL
→ consciência política
→ filiação quando juridicamente permitida
→ voto secreto
→ manifestação nos limites legais

ESFERA_FUNCIONAL
→ legalidade
→ impessoalidade
→ moralidade
→ publicidade
→ eficiência
→ neutralidade do aparato estatal
```

### 7.1 O voto pessoal não vale mais

Cargo, fama, função, autoridade, uniforme ou poder administrativo não ampliam o valor jurídico do voto individual.

```text
1_eleitor = 1_voto_de_valor_igual
```

### 7.2 O dever funcional é maior

Embora o voto tenha valor igual, o dever institucional pode ser superior porque o agente controla:

- bases de dados;
- orçamento;
- canais oficiais;
- pessoal;
- contratos;
- fiscalização;
- comunicação pública;
- programas sociais;
- informações ainda não divulgadas.

Assim:

```text
igualdade_do_voto ≠ igualdade_de_poder_institucional
```

Quanto maior o poder funcional, maior deve ser a separação entre preferência privada e uso do cargo.

## 8. Rapport institucional e sinergia democrática

Neste documento, **rapport** significa relação de confiança verificável entre cidadão e instituição, não técnica de persuasão eleitoral.

Rapport democrático exige:

- linguagem compreensível;
- fonte identificável;
- metodologia reproduzível;
- possibilidade de contestação;
- tratamento igual de partidos e cidadãos;
- proteção de dados;
- resposta a erros;
- registro de decisões;
- controle externo.

**Sinergia institucional** existe quando IBGE, Justiça Eleitoral, órgãos de controle, academia, imprensa e sociedade operam com competências separadas, padrões compatíveis e auditoria cruzada.

```text
sinergia ≠ fusão_de_bases
sinergia = interoperabilidade_governada + separação_de_finalidades + controle
```

## 9. Permutações “andômicas” e análise finita

A expressão “permutações andômicas” não corresponde a categoria jurídica consolidada. Para uso operacional, será tratada como:

```text
permutações_combinatórias
+ testes_aleatorizados
+ cenários_contrafactuais
```

Não é necessário calcular combinações infinitas. Basta testar um conjunto finito de cenários materiais.

### 9.1 Cenários mínimos

1. Sem pesquisa publicada.
2. Com pesquisa publicada integralmente.
3. Com apenas manchete ou ranking.
4. Com microdados pessoais indevidos.
5. Com dados públicos agregados.
6. Com segmentação por bairro.
7. Com propaganda vinculada a programa social.
8. Com comunicação oficial neutra.
9. Com agente público usando canal institucional.
10. Com campanha usando recursos próprios declarados.
11. Com diferença populacional alterando faixa de vereadores.
12. Com mudança no eleitorado sem mudança populacional equivalente.

### 9.2 Contrafactuais

Perguntar:

- O resultado estratégico seria o mesmo sem os dados pessoais?
- A mensagem seria enviada igualmente a todos?
- O partido adversário teria acesso ao mesmo dado público?
- A decisão seria defensável fora do período eleitoral?
- O agente faria a mesma divulgação sem sua preferência política?
- O benefício continuaria sem identificação partidária?
- A cadeira existiria sem a faixa populacional?
- O partido obteria o lugar sem os votos de legenda ou nominais?

## 10. Oito direções multiescala

### Norte — Pessoa e autonomia

**Parábola:** o mapa mostra a rua; não deve escrever o voto do morador.

Régua: liberdade, sigilo, não discriminação e ausência de coerção.

### Nordeste — Dado e granularidade

**Parábola:** quanto mais próximo o mapa chega da porta, maior o dever de não revelar quem mora dentro.

Régua: anonimização, agregação, finalidade e risco de reidentificação.

### Leste — Pesquisa e percepção

**Parábola:** o termômetro mede a temperatura, mas sua exibição pode mudar o comportamento da sala.

Régua: método, pergunta, ordem, publicação, repetição e enquadramento.

### Sudeste — Partido e estratégia

**Parábola:** a bússola orienta o navio; não substitui o vento real dos votos.

Régua: legalidade da fonte, proporcionalidade da segmentação e transparência financeira.

### Sul — Município e cadeiras

**Parábola:** o tamanho da casa define quantas cadeiras cabem; os votos decidem quem nelas se senta.

Régua: população oficial, lei orgânica, votos válidos, QE, QP e sobras.

### Sudoeste — Agente público

**Parábola:** dentro da cabine ele é eleitor; fora dela continua guardião da chave pública.

Régua: separação entre consciência privada e competência funcional.

### Oeste — Plataforma e alcance

**Parábola:** o alto-falante não escolhe sozinho a mensagem, mas decide quantas pessoas a ouvirão.

Régua: recomendação, publicidade, dados, controle, benefício e resposta a notificação.

### Noroeste — Controle e correção

**Parábola:** a régua mede melhor quando outra régua pode conferir sua marca.

Régua: auditoria independente, trilha de decisão, recurso e reparação.

## 11. Réguas operacionais finitas

Cada operação pode ser avaliada de 0 a 4, sem produzir “nota de culpa”. A escala serve para priorizar auditoria.

| Régua | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| Transparência | inexistente | mínima | parcial | adequada | integral e reproduzível |
| Granularidade | nacional agregada | regional | municipal | bairro/setor | pessoa ou domicílio identificável |
| Assimetria | acesso público igual | pequena diferença | acesso contratual | acesso exclusivo | acesso estatal privilegiado |
| Coerção | nenhuma | linguagem ambígua | pressão simbólica | ameaça ou condicionamento | sanção ou perda concreta |
| Controle do agente | nenhum | indireto | compartilhado | operacional | decisório total |
| Impacto eleitoral | remoto | possível | plausível | provável | demonstrado |
| Reversibilidade | correção imediata | fácil | moderada | difícil | dano permanente |
| Auditabilidade | logs completos | documentação boa | parcial | fragmentária | inexistente |

### 11.1 Regra de interpretação

```text
pontuação_alta ≠ ilicitude_provada
pontuação_alta = prioridade_de_revisão_e_controle
```

### 11.2 Gatilhos de auditoria reforçada

- granularidade 4;
- assimetria 4;
- coerção 3 ou 4;
- uso de base estatal para finalidade eleitoral;
- ausência de logs;
- pesquisa sem documentação essencial;
- alteração de classificação populacional perto do pleito;
- uso de dado sigiloso ou embargo;
- cruzamento capaz de reidentificar beneficiário ou eleitor.

## 12. Responsabilidade por camada

```text
R_total = Σ R_camada
```

Mas as responsabilidades não se transferem automaticamente.

| Camada | Possível responsável | Pergunta de imputação |
|---|---|---|
| Estatística | órgão e agentes competentes | houve violação do sigilo, método ou isonomia? |
| Cadastro eleitoral | Justiça Eleitoral ou operador | houve uso fora da finalidade ou falha de segurança? |
| Pesquisa | instituto, contratante e divulgador | método e divulgação foram regulares e fiéis? |
| Estratégia | partido e campanha | a fonte e o uso dos dados eram lícitos? |
| Plataforma | controlador conforme papel real | houve perfilamento, impulsionamento ou omissão juridicamente relevante? |
| Agente público | autoridade ou servidor | usou competência, canal ou dado oficial para favorecer candidatura? |
| Partido | dirigentes e responsáveis | houve decisão, benefício, financiamento e nexo comprováveis? |
| Eleitor | pessoa natural | exerceu voto livre ou praticou conduta específica prevista em lei? |

## 13. Boas práticas e práticas boas

### Boas práticas técnicas

- documentação de origem e linhagem do dado;
- minimização;
- agregação adequada;
- testes de reidentificação;
- controle de acesso por função;
- logs imutáveis;
- versionamento de metodologia;
- publicação de questionários e ponderações;
- auditoria de algoritmos de recomendação;
- segregação entre dados de governo e campanha.

### Práticas boas institucionais

- não transformar cidadão em alvo invisível;
- não usar pobreza como variável de pressão;
- não confundir informação com destino eleitoral;
- não personalizar política pública;
- permitir correção pública rápida;
- assegurar acesso isonômico a estatísticas públicas;
- proteger o voto secreto inclusive contra inferência abusiva;
- explicar ao eleitor como as cadeiras são formadas;
- preservar independência técnica dos órgãos de Estado.

```text
boa_prática = procedimento correto
prática_boa = procedimento correto + finalidade legítima + resultado compatível com direitos
```

## 14. Cadeia de custódia para auditoria multiescala

```json
{
  "case_id": "TOKEN_VAZIO",
  "municipality": "TOKEN_VAZIO",
  "population_source": "TOKEN_VAZIO",
  "population_reference_date": "TOKEN_VAZIO",
  "council_seat_limit": "TOKEN_VAZIO",
  "local_organic_law_seats": "TOKEN_VAZIO",
  "registered_electors": "TOKEN_VAZIO",
  "valid_votes": "TOKEN_VAZIO",
  "electoral_quotient": "TOKEN_VAZIO",
  "party_votes": "TOKEN_VAZIO",
  "party_quotient": "TOKEN_VAZIO",
  "remainder_rule_version": "TOKEN_VAZIO",
  "poll_registration": "TOKEN_VAZIO",
  "poll_methodology": "TOKEN_VAZIO",
  "public_dataset_used": [],
  "personal_dataset_used": [],
  "data_controller": "TOKEN_VAZIO",
  "campaign_or_official_channel": "TOKEN_VAZIO",
  "microtargeting_present": "TOKEN_VAZIO",
  "public_agent_involvement": "TOKEN_VAZIO",
  "evidence_status": "fact|report|hypothesis|indicator|evidence|TOKEN_VAZIO",
  "official_protocol": "TOKEN_VAZIO"
}
```

## 15. Conclusão operacional

O sistema precisa ser repensado não porque estatística, pesquisa, cadastro ou partidos sejam intrinsecamente culpados, mas porque componentes lícitos podem formar uma arquitetura de influência assimétrica quando integrados sem limites.

A relação correta é:

```text
IBGE define realidade estatística agregada e territorial
TSE define realidade cadastral e eleitoral
pesquisa estima opinião
partido converte informação em estratégia
plataforma amplia alcance
voto válido alimenta o cálculo
lei e jurisprudência distribuem cadeiras
controle verifica abuso
```

A excelência operacional exige que cada elo permaneça identificável, auditável e limitado por finalidade.

```text
coerência_final =
competência_correta
× dado_adequado
× finalidade_legítima
× método_reproduzível
× proteção_da_pessoa
× igualdade_eleitoral
× controle_independente
```

## 16. Fontes normativas e institucionais

- Constituição Federal — arts. 5º, LXXIX; 14; 29, IV; 37; 60, § 4º: https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html
- Código Eleitoral — arts. 106 a 113: https://www2.camara.leg.br/legin/fed/lei/1960-1969/lei-4737-15-julho-1965-356297-normaatualizada-pl.html
- Lei nº 9.504/1997 — pesquisas, propaganda, financiamento e condutas vedadas: https://www2.camara.leg.br/legin/fed/lei/1997/lei-9504-30-setembro-1997-365408-normaatualizada-pl.html
- Lei nº 5.534/1968 — prestação e sigilo das informações estatísticas: https://www.planalto.gov.br/ccivil_03/leis/l5534.htm
- Lei Geral de Proteção de Dados — Lei nº 13.709/2018: https://www2.camara.leg.br/legin/fed/lei/2018/lei-13709-14-agosto-2018-787077-normaatualizada-pl.html
- IBGE — documentos, base jurídica, códigos e princípios: https://www.ibge.gov.br/acesso-informacao/institucional/documentos-ibge.html

---

**F_ok:** pesquisa, IBGE, cadastro eleitoral, estratégia partidária e cadeiras foram separados e reconectados por causalidade verificável.  
**F_gap:** a contribuição causal de pesquisa ou dado específico para uma cadeira concreta exige comparação temporal, financeira, territorial e contrafactual.  
**F_next:** aplicar a matriz a um município e eleição determinados, usando população oficial, lei orgânica, eleitorado, votos, pesquisas registradas e gastos declarados.
