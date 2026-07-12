# Sete heurísticas — mapas termais, CadÚnico, pesquisas, obras públicas, Big Tech e responsabilidade institucional

> **Documento técnico-jurídico, estatístico e probatório.**  
> Versão: 1.0 — 12 de julho de 2026.  
> Este texto não afirma que todo mapa territorial, pesquisa eleitoral, programa social, obra pública, veículo de mídia, plataforma digital ou órgão estatal integra prática criminosa. A qualificação como crime exige tipo legal, conduta, autoria, elemento subjetivo quando exigido, nexo e prova. Ausência de acusação formal não prova licitude, mas também não prova pacto institucional.

## 1. Premissa consolidada da sessão

A cadeia material investigável é:

```text
CadÚnico e políticas sociais registram pessoas, famílias, endereços e vulnerabilidades
+ IBGE registra população, território e condições agregadas
+ Justiça Eleitoral publica eleitorado, seções e resultados agregados
+ pesquisas estimam intenção de voto e competitividade
+ partidos organizam estratégia territorial
+ mídia e plataformas ampliam determinados enquadramentos
+ agentes públicos executam políticas e obras
→ forma-se infraestrutura informacional capaz de orientar campanha
```

Essa capacidade estratégica é real. O erro está em saltar diretamente de “capacidade” para “crime”.

```text
capacidade_de_influência ≠ ilícito_demonstrado
correlação_territorial ≠ voto_individual
silêncio_institucional ≠ legalidade
silêncio_institucional ≠ conspiração_provada
```

# HEURÍSTICA 1 — MAPA TERMAL, GRANULARIDADE E FALÁCIA ECOLÓGICA

## 1.1 O que é mapa termal

“Mapa termal” ou *heatmap* é uma visualização em que intensidade, cor ou densidade representam uma variável territorial, como:

- famílias cadastradas;
- beneficiários;
- renda;
- população;
- eleitorado;
- comparecimento;
- abstenção;
- votos por partido ou candidatura;
- resultado de pesquisa;
- alcance de propaganda;
- gasto de campanha;
- entrega de obras e serviços.

## 1.2 O que ele permite afirmar

Com fonte, método e escala adequados, pode-se afirmar:

- que determinada área possui maior concentração agregada de beneficiários;
- que um partido obteve maior proporção de votos em determinada seção ou território;
- que uma pesquisa registrou preferência agregada em determinado estrato;
- que campanha ou mídia concentrou recursos em determinada região;
- que existe correlação espacial entre variáveis.

## 1.3 O que ele não permite afirmar sozinho

```text
área_com_muitos_beneficiários
≠ cada_beneficiário_votou_no_partido_mais_votado

seção_com_70_por_cento_de_votos_em_X
≠ identificação_de_quem_votou_em_X
```

Inferir comportamento individual a partir de média territorial é **falácia ecológica**.

## 1.4 Regra de segurança

```text
AFIRMAÇÃO_TERRITORIAL_VÁLIDA =
fonte
+ data
+ unidade_geográfica
+ denominador
+ método
+ incerteza
+ proteção_contra_reidentificação
```

## 1.5 Gatilhos de risco

- mapa por domicílio individual;
- células com pouquíssimas famílias;
- combinação de CadÚnico, saúde, escola e voto por seção;
- identificação de liderança familiar;
- inferência de opinião política;
- lista de pessoas expostas em campanha;
- uso de vulnerabilidade para pressão ou recompensa.

# HEURÍSTICA 2 — CADÚNICO, BOLSA FAMÍLIA E FINALIDADE DO DADO

## 2.1 O que o CadÚnico registra

O Cadastro Único identifica e caracteriza famílias de baixa renda, registrando endereço, características do domicílio, composição familiar, identificação das pessoas, escolaridade, trabalho, renda, deficiência e outras informações necessárias às políticas sociais.

Logo, ele possui capacidade territorial e familiar muito superior a um simples total municipal.

## 2.2 A finalidade originária

```text
FINALIDADE_ORIGINÁRIA =
seleção_de_beneficiários
+ execução_de_políticas
+ organização_de_serviços
+ avaliação_social
+ controle_e_averiguação
```

Não inclui automaticamente:

```text
microdirecionamento_partidário
perfilamento_eleitoral
pressão_sobre_beneficiário
inferência_de_opinião_política
```

## 2.3 LGPD

A LGPD considera **opinião política** e filiação a organização política dados pessoais sensíveis. Dados de acesso público também continuam submetidos a finalidade, boa-fé e interesse público que justificaram sua divulgação.

```text
dado_público ≠ dado_sem_finalidade
beneficiário_identificado ≠ alvo_eleitoral_livre
```

## 2.4 Mapa social legítimo

Pode ser legítimo produzir mapas agregados para:

- planejar CRAS;
- distribuir equipes;
- estimar demanda;
- avaliar cobertura;
- identificar deserto de serviço;
- acompanhar execução financeira;
- avaliar desigualdade regional.

## 2.5 Mapa social eleitoralmente problemático

O risco cresce se houver:

```text
acesso_individual_ou_microterritorial
+ partido_ou_campanha
+ intenção_de_voto
+ contato_direto
+ benefício_ou_ameaça
```

## 2.6 Qualificação jurídica

Nem toda violação de dados constitui crime. Conforme o fato, pode haver:

- infração administrativa de proteção de dados;
- responsabilidade civil;
- improbidade ou infração funcional, conforme a lei e os elementos;
- conduta eleitoral vedada;
- abuso de poder;
- captação ilícita de sufrágio;
- falsidade;
- crime de violação de sigilo ou acesso indevido, quando presentes seus tipos específicos.

# HEURÍSTICA 3 — PESQUISA ELEITORAL COMO MEDIÇÃO E COMO INTERVENÇÃO

## 3.1 Dupla natureza

```text
PESQUISA_COMO_MEDIÇÃO = estima_preferências
PESQUISA_COMO_INTERVENÇÃO = altera_percepção_de_viabilidade
```

A divulgação pode estimular:

- voto útil;
- migração de doadores;
- concentração de cobertura;
- alianças;
- desistências;
- mobilização de agentes;
- escolha dos municípios prioritários;
- impulsionamento digital territorial.

## 3.2 A pesquisa não é neutra por simples definição

Mesmo metodologicamente correta, sua apresentação pode influenciar. Isso não a torna ilícita.

A pergunta jurídica é:

```text
influência_legítima_ou_manipulação?
```

## 3.3 Obrigações de 2026

A pesquisa pública deve registrar no PesqEle, entre outros elementos:

- contratante;
- pagador;
- custo e origem dos recursos;
- metodologia;
- plano amostral;
- ponderações;
- área física;
- margem de erro;
- nível de confiança;
- questionário;
- profissional de estatística;
- documentação auditável.

Nas pesquisas municipais envolvendo mais de um município, há registro separado para cada município abrangido.

## 3.4 Fiscalização

Ministério Público, candidaturas, partidos, federações e coligações, conforme legitimidade, podem requerer acesso ao sistema interno de controle, verificar coleta e confrontar planilhas ou mapas escolhidos aleatoriamente, preservada a identidade das pessoas entrevistadas.

## 3.5 O que já é crime específico

```text
DIVULGAÇÃO_DE_PESQUISA_FRAUDULENTA = crime_eleitoral
```

Também existem sanções para pesquisa sem registro e para obstaculização da fiscalização prevista em lei.

## 3.6 O que não basta para acusar

- a pesquisa ter errado;
- outro instituto apresentar resultado distinto;
- a pesquisa influenciar voto útil;
- o partido investir onde aparece competitivo;
- a mídia destacar primeiro e segundo lugares.

É necessário demonstrar fraude, deficiência relevante, manipulação ou outro ilícito específico.

# HEURÍSTICA 4 — OBRAS PÚBLICAS, PROGRAMAS E CADEIA DE AUTORIA

## 4.1 Obra entregue não pertence juridicamente ao partido

Uma obra pública resulta de cadeia que pode incluir:

```text
necessidade_social
→ estudo_e_projeto
→ plano_plurianual
→ lei_orçamentária
→ emenda_parlamentar
→ convênio_ou_transferência
→ licitação
→ contrato
→ licença
→ fiscalização
→ execução
→ aditivos
→ entrega
→ manutenção
→ controle
```

## 4.2 Créditos políticos permitidos

Pode ser verdadeiro dizer que determinado governo:

- propôs;
- priorizou;
- financiou;
- destravou;
- executou;
- concluiu;
- ampliou.

A afirmação precisa indicar **qual verbo e qual documento**.

## 4.3 Publicidade institucional

A Constituição determina caráter educativo, informativo ou de orientação social e proíbe nomes, símbolos ou imagens que caracterizem promoção pessoal de autoridades ou servidores.

## 4.4 Uso eleitoral

A campanha pode debater realizações públicas com recursos e identificação próprios. O que não pode é fundir:

```text
obra_do_Estado = patrimônio_do_partido
beneficiário = devedor_eleitoral
inauguração_oficial = comício_custeado_pelo_erário
```

## 4.5 Sequência obrigatória de evidência

Cada obra divulgada deveria permitir reconstrução pública de:

```json
{
  "project": "TOKEN_VAZIO",
  "initial_study": "TOKEN_VAZIO",
  "legislative_authorization": "TOKEN_VAZIO",
  "budget_program": "TOKEN_VAZIO",
  "parliamentary_amendment": "TOKEN_VAZIO",
  "funding_entities": [],
  "agreement_or_transfer": "TOKEN_VAZIO",
  "procurement": "TOKEN_VAZIO",
  "contractors": [],
  "supervising_body": "TOKEN_VAZIO",
  "execution_governments": [],
  "delivery_act": "TOKEN_VAZIO",
  "maintenance_responsibility": "TOKEN_VAZIO"
}
```

## 4.6 Votos públicos e voto secreto

Separar:

```text
VOTO_DO_ELEITOR = secreto
VOTAÇÃO_LEGISLATIVA = em_regra_pública, salvo hipóteses constitucionais ou regimentais
ATO_ADMINISTRATIVO = motivado, documentado e controlável
```

A narrativa partidária não pode apagar votos legislativos, emendas, controles e governos anteriores ou posteriores que integrem a obra.

# HEURÍSTICA 5 — MÍDIA, BIG TECH E ARQUITETURA DE APRESENTAÇÃO

## 5.1 Influência pelo enquadramento

Plataformas e mídia podem alterar:

- alcance;
- ordem de exibição;
- repetição;
- recomendação;
- segmentação;
- preço da atenção;
- visibilidade de pesquisas;
- visibilidade de obras e programas;
- formação da percepção de viabilidade.

```text
não_criar_o_conteúdo ≠ não_influenciar_a_distribuição
```

## 5.2 Responsabilidade por papel real

Distinguir:

- veículo jornalístico;
- provedor de aplicação;
- rede de anúncios;
- contratante de impulsionamento;
- criador do conteúdo;
- influenciador remunerado;
- processador de dados;
- partido ou candidatura beneficiária.

## 5.3 Regras eleitorais digitais

As normas de 2026 exigem, conforme o caso:

- identificação inequívoca do conteúdo impulsionado;
- repositório público de impulsionamento;
- transparência de gastos;
- dever de verificação razoável da fidedignidade;
- rotulagem de conteúdo sintético gerado ou manipulado por IA;
- observância das ordens e competências da Justiça Eleitoral.

## 5.4 Inferência política e microdirecionamento

O risco aumenta quando uma plataforma ou campanha combina:

```text
vulnerabilidade_social
+ geolocalização
+ histórico_de_navegação
+ opinião_política_inferida
+ propaganda_personalizada
```

Opinião política inferida, quando vinculada a pessoa identificada ou identificável, pode integrar tratamento de dado sensível.

## 5.5 Limite da afirmação

Big Tech influenciar não equivale automaticamente a cometer crime. A responsabilidade depende do ato, conhecimento, controle, benefício, norma, resposta a notificações e prova.

# HEURÍSTICA 6 — MATRIZ DE COMPETÊNCIAS E RESPONSABILIDADES

## 6.1 TSE

- regulamenta nacionalmente eleições e pesquisas;
- administra PesqEle e sistemas nacionais;
- julga matérias de sua competência;
- estabelece normas de propaganda e internet;
- organiza dados e transparência eleitoral.

## 6.2 TRE

- supervisiona e julga regionalmente;
- designa juízos para poder de polícia;
- atua em registros, recursos, pesquisas e propaganda conforme competência;
- mantém corregedoria e controle cadastral regional.

## 6.3 Juízo eleitoral

- exerce poder de polícia dentro dos limites legais;
- processa representações e medidas eleitorais de primeiro grau;
- recebe questões de alistamento, propaganda e fiscalização municipal.

## 6.4 Ministério Público Eleitoral

O ramo funcional adequado é o **Ministério Público Eleitoral**, composto por membros do MPF e dos MPs estaduais conforme o grau de jurisdição.

Pode:

- fiscalizar a ordem eleitoral;
- impugnar pesquisas nas hipóteses legais;
- requisitar diligências;
- promover ações eleitorais e ação penal pública;
- exercer controle externo da atividade policial.

```text
MPF_isoladamente ≠ toda_a_estrutura_eleitoral
```

## 6.5 Polícia Federal

- exerce polícia judiciária da União;
- investiga crimes eleitorais conforme atribuição, requisição e direção jurídica do caso;
- preserva cadeia de custódia e realiza diligências autorizadas.

A PF não decide eleição nem substitui o Ministério Público ou a Justiça Eleitoral.

## 6.6 Polícia Militar

- policiamento ostensivo;
- preservação da ordem pública;
- prevenção de violência e coação;
- atendimento de flagrante e comunicação.

Não valida pesquisa, benefício, domicílio ou resultado eleitoral.

## 6.7 AGU

A AGU representa a União e presta consultoria e assessoramento jurídico ao Poder Executivo. Pode atuar na prevenção jurídica de condutas vedadas e na defesa judicial da União.

```text
AGU ≠ órgão_de_acusação_eleitoral
```

## 6.8 ABIN

A grafia correta é **ABIN**, não “ABINC”. A ABIN produz inteligência para subsidiar o processo decisório estatal e avaliar ameaças à ordem constitucional, sob limites de direitos e controle externo.

```text
ABIN ≠ polícia_judiciária
ABIN ≠ Ministério_Público
ABIN ≠ instituto_de_pesquisa_eleitoral
ABIN ≠ ferramenta_partidária
```

## 6.9 ANPD, CGU, TCU e controles

Embora não citados inicialmente, podem ser relevantes:

- **ANPD:** proteção de dados e fiscalização da LGPD;
- **CGU/controladorias:** integridade, auditoria e controle interno;
- **TCU/Tribunais de Contas:** recursos, contratos, obras e execução;
- **corregedorias:** responsabilidade funcional;
- **Câmara e Senado:** fiscalização e controle político;
- **Judiciário:** tutela de direitos e aplicação da lei.

# HEURÍSTICA 7 — DESERTO DE ACUSAÇÃO, TIPICIDADE E FECHAMENTO PROBATÓRIO

## 7.1 “Não houve acusação” pode significar coisas diferentes

```text
A = não_houve_ilícito
B = houve_anomalia_sem_prova
C = ninguém_formalizou_denúncia
D = denúncia_foi_ao_órgão_incompetente
E = faltou_dado_acessível
F = houve_arquivamento_fundamentado
G = houve_omissão
H = prazo_prescreveu_ou_precluiu
I = fato_foi_normalizado_socialmente
```

Sem verificar o rastro, não se pode escolher G automaticamente.

## 7.2 Deserto institucional verificável

```text
DESERTO_DE_CONTROLE =
risco_relevante
+ dever_normativo
+ órgão_competente
+ ciência_formal
+ capacidade_de_agir
+ ausência_de_triagem_ou_resposta
+ prazo
+ nexo
```

## 7.3 Tipicidade

A frase “é crime” só deve ser usada quando houver:

```text
CRIME =
fato
+ tipo_penal_específico
+ autoria
+ elemento_subjetivo_quando_exigido
+ nexo
+ prova
```

Exemplos de núcleos que podem possuir tipificação ou sanção específica, conforme o caso:

- pesquisa eleitoral fraudulenta;
- falsidade documental ou ideológica eleitoral;
- corrupção eleitoral;
- coação;
- violação de sigilo;
- acesso indevido a sistema;
- uso promocional de programa social;
- contratação de rede para ataques ilícitos;
- abuso econômico ou funcional, que pode ter natureza eleitoral sancionatória ainda que não seja crime penal em toda hipótese.

## 7.4 Ausência de tipo penal não significa ausência de responsabilidade

Pode haver:

- nulidade;
- multa;
- cassação;
- inelegibilidade;
- reparação civil;
- sanção administrativa;
- responsabilização disciplinar;
- bloqueio ou eliminação de dados;
- obrigação de transparência;
- correção pública.

## 7.5 Matriz das sete heurísticas

| Heurística | Pergunta central | Erro a evitar | Prova principal |
|---|---|---|---|
| 1. Mapa termal | o mapa é agregado ou identifica pessoas? | falácia ecológica | metodologia e granularidade |
| 2. CadÚnico | o uso respeita a finalidade social? | dado público sem limite | logs, base legal e compartilhamentos |
| 3. Pesquisa | mede, influencia ou foi manipulada? | erro amostral = fraude | PesqEle, questionário e campo |
| 4. Obras | qual foi a cadeia real de autoria? | obra = propriedade partidária | orçamento, contrato e execução |
| 5. Big Tech/mídia | quem controlou alcance e segmentação? | influência = crime automático | anúncios, repositórios e logs |
| 6. Órgãos | quem tinha competência para agir? | atribuir tudo a todos | norma, protocolo e distribuição |
| 7. Deserto de acusação | por que não houve ação formal? | silêncio = pacto | ciência, dever, resposta e prazo |

## 8. Sete leituras distintas da mesma hipótese

### Leitura 1 — Estatística

```text
benefícios + território + voto_agregado = correlação
```

Não identifica voto individual.

### Leitura 2 — Proteção de dados

```text
vulnerabilidade + pessoa_identificável + inferência_política = risco_elevado
```

### Leitura 3 — Ciência política

Pesquisa pública altera coordenação, viabilidade e voto útil.

### Leitura 4 — Direito eleitoral

A influência é permitida até atravessar fraude, abuso, coação, uso de máquina, falsidade ou conduta vedada.

### Leitura 5 — Administração pública

Programa e obra pertencem à cadeia estatal e orçamentária, não ao patrimônio eleitoral de uma legenda.

### Leitura 6 — Plataforma informacional

Algoritmos e mídia organizam atenção, e por isso exigem transparência, não presunção automática de autoria criminal.

### Leitura 7 — Investigação e prova

A hipótese só fecha quando dados, operadores, decisões, comunicações, benefício e resposta institucional convergem.

## 9. Fórmula de coerência final

```text
INFLUÊNCIA_ELEITORAL_SISTÊMICA =
  dados_sociais_agregados
+ dados_territoriais
+ pesquisas
+ estratégia_partidária
+ publicidade_de_obras_e_programas
+ mídia_e_plataformas
+ capacidade_institucional
```

Isso descreve uma arquitetura de influência.

```text
ILÍCITO_SISTÊMICO_DEMONSTRADO =
  arquitetura_de_influência
+ uso_proibido_ou_abusivo
+ agentes_identificados
+ atos_concretos
+ finalidade
+ benefício
+ nexo
+ gravidade
+ prova
- explicações_legítimas
- contraprovas
```

## 10. Protocolo mínimo de auditoria

```json
{
  "case_id": "TOKEN_VAZIO",
  "territory": "TOKEN_VAZIO",
  "heatmap_variable": "TOKEN_VAZIO",
  "geographic_unit": "municipality|section|census_sector|address|TOKEN_VAZIO",
  "minimum_cell_population": "TOKEN_VAZIO",
  "cadunico_or_social_source": "TOKEN_VAZIO",
  "lawful_purpose": "TOKEN_VAZIO",
  "data_access_logs": [],
  "poll_registrations": [],
  "poll_contractors_and_payers": [],
  "party_strategy_documents": [],
  "public_works_chain": [],
  "institutional_advertising": [],
  "digital_ad_repositories": [],
  "platform_targeting_parameters": [],
  "formal_complaints": [],
  "competent_authorities": [],
  "institutional_responses": [],
  "counterevidence": [],
  "status": "fato|anomalia|hipótese|indício|prova|decisão|TOKEN_VAZIO"
}
```

## 11. Fontes normativas e institucionais

- Constituição Federal — arts. 5º, 14, 37, 127 a 131 e 144: https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html
- Lei Geral de Proteção de Dados: https://www2.camara.leg.br/legin/fed/lei/2018/lei-13709-14-agosto-2018-787077-normaatualizada-pl.html
- Cadastro Único — MDS: https://www.gov.br/mds/pt-br/acoes-e-programas/cadastro-unico
- Lei nº 9.504/1997: https://www2.camara.leg.br/legin/fed/lei/1997/lei-9504-30-setembro-1997-365408-normaatualizada-pl.html
- Resolução TSE nº 23.600/2019, atualizada para 2026 — pesquisas: https://www.tse.jus.br/legislacao/compilada/res/2019/resolucao-no-23-600-de-12-de-dezembro-de-2019
- Resolução TSE nº 23.610/2019, atualizada para 2026 — propaganda e internet: https://www.tse.jus.br/legislacao/compilada/res/2019/resolucao-no-23-610-de-18-de-dezembro-de-2019
- Lei nº 9.883/1999 — SISBIN e ABIN: https://www2.camara.leg.br/legin/fed/lei/1999/lei-9883-7-dezembro-1999-369902-normaatualizada-pl.html
- Competências da AGU: https://www.gov.br/agu/pt-br/acesso-a-informacao/institucional/competencias

---

**F_ok:** mapa termal, CadÚnico, pesquisa, obras, partidos, plataformas e órgãos foram conectados em sete heurísticas distintas.  
**F_gap:** não há, nesta análise geral, município, arquivo de mapa, registro de pesquisa, log de acesso, campanha, obra ou protocolo determinados que permitam acusação concreta.  
**F_next:** preencher o protocolo com um caso delimitado e testar simultaneamente correlação, explicações legítimas, uso indevido, competência e resposta institucional.
