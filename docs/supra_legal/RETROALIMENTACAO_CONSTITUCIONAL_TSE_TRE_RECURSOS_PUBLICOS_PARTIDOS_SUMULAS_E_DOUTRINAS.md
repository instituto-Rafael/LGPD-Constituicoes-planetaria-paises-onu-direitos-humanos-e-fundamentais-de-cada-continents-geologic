# Retroalimentação constitucional — TSE, TRE, recursos públicos, partidos, súmulas e doutrinas

> **Matriz jurídico-constitucional, eleitoral, administrativa, financeira e probatória.**  
> Versão 1.0 — 12 de julho de 2026.  
> Este documento consolida os temas desenvolvidos na sessão. É um mapa abrangente das normas diretamente relacionadas, mas não pretende substituir pesquisa processual específica nem afirmar que literalmente toda norma brasileira foi catalogada. Leis, resoluções e precedentes podem ser alterados; antes de protocolo ou ação judicial, deve-se confirmar a redação vigente e a jurisprudência aplicável ao fato, ao ano eleitoral e à circunscrição.

## 1. Correção terminológica indispensável

Somente o **Supremo Tribunal Federal** pode aprovar súmula com efeito vinculante nos termos do art. 103-A da Constituição.

```text
SÚMULA_VINCULANTE = STF
```

O Tribunal Superior Eleitoral:

- organiza e divulga a súmula de sua jurisprudência;
- edita resoluções dentro da autorização legal;
- uniformiza a interpretação eleitoral;
- julga recursos oriundos dos TREs.

Os Tribunais Regionais Eleitorais:

- aplicam a Constituição, as leis, as resoluções e os precedentes do TSE;
- podem organizar jurisprudência e enunciados locais;
- não criam súmula vinculante constitucional;
- não podem contrariar decisão ou instrução do TSE.

```text
súmula_TSE ≠ súmula_vinculante_do_art_103_A
súmula_TRE ≠ norma_nacional_vinculante
resolução_TSE ≠ lei
```

## 2. Hierarquia normativa

```text
CONSTITUIÇÃO
↓
emendas_constitucionais
↓
leis_complementares
↓
leis_ordinárias
↓
resoluções_do_TSE_autorizadas_em_lei
↓
atos_operacionais_dos_TREs
↓
decisões_e_atos_dos_juízos_eleitorais
```

A resolução do TSE não pode:

- alterar a Constituição;
- criar restrição sem suporte legal;
- substituir o Congresso;
- tratar livremente da organização interna dos partidos;
- inovar além da autorização legislativa.

O art. 23-A do Código Eleitoral restringe o poder regulamentar do TSE às matérias especificamente autorizadas em lei.

## 3. Núcleo constitucional da sessão

### 3.1 Estado Democrático de Direito

A República fundamenta-se em:

- soberania;
- cidadania;
- dignidade da pessoa humana;
- pluralismo político;
- poder emanado do povo.

```text
ESTADO_DEMOCRÁTICO =
liberdade_do_voto
+ pluralismo
+ igualdade
+ controle_do_poder
+ direitos_fundamentais
+ responsabilidade
```

### 3.2 Direitos fundamentais

São diretamente relevantes:

- igualdade;
- liberdade de expressão;
- direito de resposta;
- proteção da honra, imagem, intimidade e vida privada;
- acesso à informação;
- devido processo legal;
- contraditório e ampla defesa;
- inadmissibilidade de prova ilícita;
- presunção de inocência;
- proteção de dados pessoais;
- direito de petição;
- acesso ao Judiciário.

### 3.3 Voto

O art. 14 estrutura:

```text
soberania_popular
+ sufrágio_universal
+ voto_direto
+ voto_secreto
+ valor_igual
```

O resultado por seção é público e agregado; o voto individual permanece secreto.

### 3.4 Anualidade eleitoral

A lei que altera o processo eleitoral entra em vigor na publicação, mas não se aplica à eleição realizada até um ano de sua vigência.

```text
mudança_normativa ≠ aplicação_imediata_ao_pleito
```

### 3.5 Partidos políticos

A Constituição garante autonomia partidária, mas exige:

- caráter nacional;
- respeito ao regime democrático;
- prestação de contas à Justiça Eleitoral;
- proibição de recursos de governos ou entidades estrangeiras;
- cumprimento das regras de acesso a fundos públicos e rádio/TV;
- aplicação mínima em promoção da participação feminina;
- distribuição mínima de recursos e tempo para candidaturas femininas;
- aplicação constitucionalmente determinada em candidaturas pretas e pardas.

Partido é pessoa jurídica de direito privado e não se equipara a entidade paraestatal.

```text
personalidade_privada
+ dinheiro_público
= autonomia_com_accountability
```

### 3.6 Administração pública

A administração direta e indireta obedece:

```text
LIMPE =
legalidade
+ impessoalidade
+ moralidade
+ publicidade
+ eficiência
```

A publicidade de atos, programas, obras, serviços e campanhas públicas deve ser educativa, informativa ou de orientação social e não pode conter promoção pessoal.

### 3.7 Prestação de contas

O art. 70 da Constituição exige prestação de contas de qualquer pessoa física ou jurídica, pública ou privada, que utilize, arrecade, guarde, gerencie ou administre dinheiro, bens ou valores públicos.

```text
RECURSO_PÚBLICO_SEGUE_O_CONTROLE
mesmo_quando_recebido_por_pessoa_jurídica_privada
```

### 3.8 Justiça Eleitoral

São órgãos:

- TSE;
- TREs;
- juízes eleitorais;
- juntas eleitorais.

Sua competência deriva da Constituição e das leis, não de uma competência geral ilimitada.

### 3.9 Ministério Público

O Ministério Público defende:

- ordem jurídica;
- regime democrático;
- interesses sociais e individuais indisponíveis.

No sistema eleitoral, o Ministério Público Eleitoral utiliza membros do MPF e dos MPs estaduais conforme a instância.

### 3.10 Segurança pública

A Polícia Federal exerce polícia judiciária da União e apura infrações dentro de sua competência. Polícias militares realizam policiamento ostensivo e preservação da ordem pública. Nenhuma polícia substitui TSE, TRE, juiz ou Ministério Público na decisão eleitoral.

## 4. Competências do TSE

O TSE atua, entre outros campos, em:

- registro e cancelamento de diretórios nacionais;
- candidaturas presidenciais;
- recursos contra decisões dos TREs;
- contabilidade e origem de recursos dos órgãos nacionais;
- expedição de instruções autorizadas em lei;
- consultas em tese de autoridades federais e órgãos nacionais de partidos;
- organização e divulgação de sua jurisprudência;
- supervisão nacional dos sistemas eleitorais;
- prestação de contas nacionais e de campanhas presidenciais;
- distribuição do FEFC aos diretórios nacionais;
- regulamentação de pesquisas, propaganda, contas, cadastro e atos eleitorais.

```text
TSE = tribunal + administração_eleitoral + regulamentação_limitada
```

O TSE não pode usar resolução para criar matéria reservada à lei.

## 5. Competências dos TREs

Os TREs atuam em:

- registro de diretórios estaduais e municipais;
- candidaturas a governador, senador e deputados;
- recursos contra juízes e juntas eleitorais;
- contabilidade e origem de recursos regionais;
- consultas em tese de autoridades públicas e partidos;
- organização regional, zonas e seções;
- propaganda partidária estadual;
- prestação de contas estaduais;
- corregedoria regional;
- apuração e diplomação dos cargos de sua competência;
- cumprimento das instruções e decisões do TSE;
- providências urgentes para executar a lei.

```text
TRE ≠ filial_partidária
TRE ≠ legislador_estadual_eleitoral
TRE = tribunal_regional_da_Justiça_Eleitoral
```

## 6. Juízo eleitoral, poder de polícia e limite

O juiz eleitoral pode adotar providências para inibir propaganda ilegal. Entretanto:

- não pode realizar censura prévia geral;
- não pode instaurar de ofício procedimento para impor multa de propaganda;
- deve respeitar competência, provocação, contraditório e prova;
- pode registrar ocorrências e encaminhar fatos ao MPE;
- responde aos mecanismos recursais e correicionais.

A Lei nº 9.504/1997 permite representação ao TRE contra juiz eleitoral que descumpra a lei ou dê causa ao descumprimento. Membros dos tribunais e do Ministério Público têm dever de fiscalizar as instâncias inferiores dentro de suas atribuições.

## 7. Regime jurídico dos recursos públicos dos partidos

### 7.1 As quatro vias centrais

```text
RECURSOS_OU_BENEFÍCIOS_PÚBLICOS_A_PARTIDOS =
1. Fundo_Partidário
2. FEFC
3. rádio_e_televisão_gratuitos_com_compensação_fiscal
4. uso_gratuito_de_escolas_e_Casas_Legislativas_para_reuniões
```

Há ainda serviços públicos eleitorais neutros — segurança, organização da eleição, transporte público de eleitoras e eleitores e estrutura de votação — que não constituem patrimônio de partido.

### 7.2 Fundo Partidário

O Fundo Partidário é formado por:

- multas e penalidades eleitorais;
- recursos destinados por lei;
- doações admitidas;
- dotações orçamentárias da União.

Distribuição legal básica:

```text
5% = partes_iguais_aos_partidos_habilitados
95% = proporção_dos_votos_na_última_eleição_para_Câmara
```

A cláusula constitucional de desempenho condiciona o acesso.

### 7.3 Destinações permitidas do Fundo Partidário

A lei permite aplicação em:

- sedes e serviços partidários;
- pessoal, dentro dos limites legais;
- propaganda doutrinária e política;
- alistamento e campanhas;
- fundações e institutos de pesquisa, doutrinação e educação política;
- programas de participação política das mulheres;
- organismos partidários internacionais admitidos;
- alimentação;
- consultoria contábil e advocatícia;
- bens, sedes e reformas;
- impulsionamento político digital nas condições e períodos legais.

```text
DIREITO_VIGENTE:
Fundo_Partidário_pode_financiar_propaganda_doutrinária_e_política
```

Isso é diferente da proposta desenvolvida na sessão para ampliar educação cívica neutra e reduzir propaganda proprietária sobre obras e políticas públicas.

### 7.4 FEFC

O Fundo Especial de Financiamento de Campanha:

- é constituído por dotações orçamentárias da União no ano eleitoral;
- é disponibilizado pelo Tesouro Nacional ao TSE;
- é distribuído aos diretórios nacionais;
- exige critérios partidários aprovados e divulgados publicamente;
- deve financiar campanha dentro das regras;
- não utilizado, deve ser devolvido integralmente ao Tesouro;
- deve respeitar os pisos constitucionais e regulamentares para candidaturas femininas, negras e indígenas conforme a norma vigente.

A Resolução TSE nº 23.752/2026 atualizou pontos da Resolução nº 23.607/2019 para as Eleições 2026.

### 7.5 Horário partidário e eleitoral

O tempo em rádio e televisão é gratuito para o partido, mas não é economicamente sem custo público: emissoras recebem compensação fiscal.

A propaganda partidária pode difundir:

- programas partidários;
- mensagens a filiados;
- atividades congressuais;
- posição sobre temas políticos;
- filiação e papel dos partidos;
- participação política de mulheres, jovens e pessoas negras.

A propaganda paga em rádio e televisão é proibida; a veiculação gratuita ocorre nas formas legais.

### 7.6 Uso gratuito de prédios públicos

Partido com estatuto registrado no TSE pode utilizar gratuitamente escolas públicas e Casas Legislativas para reuniões ou convenções, respondendo pelos danos causados.

```text
uso_gratuito_autorizado
≠ apropriação_do_prédio
≠ uso_livre_de_servidores_e_recursos
```

## 8. Contas, segregação e rastreabilidade

Partidos e candidaturas devem:

- abrir contas específicas;
- separar recursos por natureza;
- manter escrituração contábil;
- identificar origem e destino;
- guardar documentos;
- prestar contas à Justiça Eleitoral;
- devolver recursos públicos não usados ou indevidamente aplicados.

A Resolução TSE nº 23.604/2019 submete partidos e dirigentes, em matéria financeira e contábil, à Constituição, leis eleitorais, LAI, normas contábeis e resoluções do TSE.

A Resolução TSE nº 23.607/2019 exige conta bancária eleitoral específica e proíbe transferência entre contas de naturezas distintas, salvo exceção regulamentar.

### 8.1 Fonte vedada

Em regra, partidos não podem receber recursos de:

- origem estrangeira;
- entes públicos fora das exceções legais;
- pessoas jurídicas;
- autoridades públicas nas hipóteses regulamentadas.

São excepcionados o Fundo Partidário e o FEFC.

### 8.2 Sanções e devolução

Podem ocorrer:

- devolução do valor irregular;
- multa;
- suspensão ou perda de cotas;
- recolhimento ao Tesouro;
- impedimento de quitação eleitoral;
- efeitos sobre registro ou anotação do órgão, mediante devido processo;
- representação por captação ou gastos ilícitos;
- cassação, se presentes os requisitos da lei específica;
- inelegibilidade em hipóteses legais.

A ausência de comprovação ou uso indevido de Fundo Partidário ou FEFC determina devolução, com atualização e juros quando cabíveis.

## 9. Improbidade administrativa: duas vias diferentes

### 9.1 Agente público usando o Estado para promoção

A Lei nº 8.429/1992 tipifica, no art. 11, XII, a publicidade feita no âmbito da administração, com recursos do erário, contrária ao art. 37, § 1º, da Constituição, quando promove inequivocamente o agente e personaliza atos, programas, obras, serviços ou campanhas.

Exige-se:

```text
ato_doloso
+ tipo_legal
+ finalidade_ilícita
+ benefício_indevido
+ individualização
+ prova
```

Mera ilegalidade ou discordância interpretativa não basta.

### 9.2 Recursos públicos recebidos pelos partidos

O art. 23-C da Lei de Improbidade determina que enriquecimento, perda, desvio, apropriação, malbaratamento ou dilapidação de recursos públicos dos partidos ou fundações seja responsabilizado nos termos da Lei nº 9.096/1995.

```text
DESVIO_DE_RECURSO_PARTIDÁRIO_PÚBLICO
→ regime_específico_da_Lei_dos_Partidos_e_Justiça_Eleitoral
```

Isso não significa imunidade. Significa especialidade da via principal.

Quando agente público utiliza orçamento, servidor, cadastro, publicidade ou bem estatal para beneficiar partido, outras responsabilidades administrativas, eleitorais, civis e penais continuam possíveis.

## 10. Condutas vedadas e máquina pública

O art. 73 da Lei nº 9.504/1997 proíbe condutas tendentes a afetar a igualdade entre candidaturas, inclusive:

- cessão ou uso eleitoral de bens públicos;
- uso indevido de materiais ou serviços públicos;
- cessão de servidor durante o expediente;
- uso promocional de bens e serviços sociais;
- determinadas transferências de recursos;
- publicidade institucional no período vedado;
- pronunciamento fora das exceções;
- gastos publicitários acima dos limites;
- distribuição gratuita de benefícios no ano eleitoral fora das exceções.

Programas sociais legalmente autorizados e já executados podem continuar nas condições da lei, com acompanhamento financeiro e administrativo pelo Ministério Público.

```text
continuidade_de_política_social ≠ propaganda_partidária
```

## 11. Abuso de poder

A LC nº 64/1990 protege a normalidade e legitimidade das eleições contra:

- poder econômico;
- poder político ou de autoridade;
- uso indevido de veículos ou meios de comunicação;
- abuso de função, cargo ou emprego público.

A AIJE pode ser proposta por partido, coligação, candidatura ou MPE, com fatos, indícios, circunstâncias e provas.

```text
ABUSO =
conduta_grave
+ poder_qualificado
+ benefício_eleitoral
+ nexo
+ prova
```

Não é necessário que o ato seja formalmente praticado durante a campanha se seus efeitos e finalidade integrarem o processo eleitoral, conforme o caso concreto e a jurisprudência.

## 12. Captação de sufrágio e cargos

É ilícito oferecer, prometer ou entregar vantagem pessoal, inclusive emprego ou função pública, para obter voto.

```text
cargo_como_composição_administrativa_lícita
≠ cargo_prometido_ao_eleitor_em_troca_de_voto
```

A caracterização exige o fim especial de obter o voto; pedido explícito não é indispensável.

## 13. Obras públicas e políticas sociais

### 13.1 Regra constitucional atual

O Estado pode informar obra, programa ou serviço em linguagem impessoal e educativa.

O partido pode, em sua propaganda própria, defender sua atuação, mas não pode:

- usar recursos ou canais estatais irregularmente;
- apresentar informação sabidamente falsa;
- condicionar benefício a voto;
- apagar documentação de forma enganosa quando a falsidade for juridicamente demonstrável;
- atribuir a beneficiário dívida eleitoral.

### 13.2 Proposta desenvolvida na sessão

Foi formulada uma proposta normativa mais rigorosa:

```text
OBRA_PÚBLICA_SEM_DONO_PARTIDÁRIO
```

Ela exigiria:

- ficha de proveniência;
- iniciativa;
- emendas;
- votação nominal, simbólica ou secreta;
- orçamento;
- financiamento;
- licitação;
- execução;
- fiscalização;
- manutenção;
- governos sucessivos;
- limitação expressa quando a autoria não puder ser medida.

Essa proibição absoluta de propaganda partidária sobre obra pública **não existe hoje de forma geral** e dependeria de reforma legal e controle constitucional.

## 14. Bolsa Família e neutralidade partidária

A política resultou de cadeia que incluiu programas anteriores, iniciativa executiva, Congresso, regulamentação, orçamento, União, estados, municípios, CadÚnico, saúde, educação, assistência e controle social.

```text
BOLSA_FAMÍLIA = política_pública_federal_de_gestão_compartilhada
≠ propriedade_do_partido
```

Pode-se afirmar documentalmente que determinado governo:

- propôs uma versão;
- editou medida;
- sancionou lei;
- ampliou orçamento;
- regulamentou;
- executou.

Não se pode inventar percentual de participação partidária quando a deliberação foi simbólica ou secreta.

## 15. Votação nominal, simbólica e secreta

### 15.1 Nominal

Permite calcular:

```text
apoio_interno_do_partido = SIM_partido / votos_expressos_partido
participação_nos_SIM = SIM_partido / total_SIM
```

### 15.2 Simbólica

É votação válida, mas geralmente não produz lista completa individual.

```text
orientação_da_bancada ≠ voto_individual
PERCENTUAL_EXATO = TOKEN_VAZIO
```

### 15.3 Secreta

Quando constitucional ou legalmente secreta:

```text
partido_do_parlamentar ≠ prova_do_voto
VOTO_INDIVIDUAL = TOKEN_VAZIO
```

## 16. Pesquisas eleitorais

A legislação vigente permite pesquisas, condicionadas a:

- registro;
- metodologia;
- contratante e pagador;
- plano amostral;
- ponderação;
- margem de erro;
- nível de confiança;
- questionário;
- fiscalização.

Pesquisa fraudulenta pode configurar crime; pesquisa não registrada gera sanção.

A tese desenvolvida na sessão de proibir pesquisas ou impedir ranking durante campanha é proposta de reforma, porque a lei atual adota transparência e fiscalização, não proibição geral.

```text
pesquisa_influencia
≠ pesquisa_automaticamente_ilícita
```

## 17. Mapas, urnas e resultados territoriais

O boletim de urna e o resultado por seção permitem:

- total exato da eleição naquele conjunto;
- margem por candidatura ou partido;
- abstenção;
- brancos e nulos;
- heterogeneidade territorial;
- comparação histórica.

Não permitem identificar o voto individual.

```text
resultado_por_seção = dado_público_agregado
mapa_social + resultado_agregado ≠ lista_de_votos_individuais
```

## 18. Transporte eleitoral

Deve-se distinguir:

- transporte público gratuito, universal, impessoal e sem propaganda;
- caravana de campanha anterior ao pleito, contabilizada e sem condicionamento;
- transporte seletivo de eleitoras e eleitores no dia da votação;
- transporte associado a vantagem, pressão ou fraude.

A auditoria deve identificar veículo, proprietário, pagador, motorista, rota, passageiros, propaganda, prestação de contas e eventual uso de servidor ou combustível público.

## 19. Dados, CadÚnico e Big Tech

Opinião política é dado pessoal sensível. Bases sociais não podem ser automaticamente convertidas em ferramentas de perfilamento eleitoral.

```text
dado_público ≠ dado_sem_finalidade
beneficiário_social ≠ alvo_partidário_livre
```

A combinação de vulnerabilidade, endereço, comportamento digital e inferência política exige base legal, necessidade, proporcionalidade, segurança e auditoria.

## 20. Participação social e proteção infantojuvenil

A sessão propôs integrar:

```text
família
↔ escola
↔ turma
↔ conselho_escolar
↔ assistência
↔ saúde
↔ Conselho_Tutelar
↔ controle_social
```

A participação deve ser apoiada, acessível e não coercitiva. Renda mínima não deve ser retirada por ausência em reunião política ou dificuldade material de participação.

O ECA, o Código Civil, o CDC e a LGPD também alcançam relações digitais e compras em jogos; não é correto afirmar que todo contrato depende de 21 anos. A capacidade civil geral plena começa aos 18 anos, ressalvadas regras específicas.

## 21. Súmulas vinculantes do STF diretamente relacionadas

> Conferir sempre o texto e o estado atual no repositório oficial do STF antes de uso processual.

| Súmula vinculante | Relação com a sessão |
|---|---|
| SV 3 | contraditório e ampla defesa em decisões do TCU que possam desfazer ato benéfico, ressalvada a hipótese indicada no próprio enunciado |
| SV 10 | órgão fracionário não pode afastar lei por inconstitucionalidade sem observar reserva de plenário |
| SV 13 | proibição constitucional de nepotismo e designações recíprocas |
| SV 14 | defesa tem acesso aos elementos de prova já documentados em investigação policial e relacionados ao exercício defensivo |
| SV 21 | é inconstitucional exigir depósito ou arrolamento prévio para admitir recurso administrativo |
| SV 43 | é inconstitucional provimento que permita servidor assumir cargo de outra carreira sem concurso |

Estas súmulas vinculam Judiciário e administração direta e indireta nas esferas federal, estadual e municipal.

## 22. Súmulas comuns do STF relevantes

Não são “vinculantes” pelo art. 103-A, mas são referências clássicas:

| Súmula | Conteúdo funcional |
|---|---|
| STF 346 | administração pode declarar nulidade dos próprios atos |
| STF 473 | administração pode anular atos ilegais e revogar atos por conveniência e oportunidade, preservados direitos e controle judicial |

Elas sustentam autotutela, mas não autorizam destruição arbitrária de política ou obra válida nem dispensam motivação, direitos adquiridos, continuidade e devido processo.

## 23. Súmulas do TSE relacionadas

| Súmula TSE | Aplicação |
|---|---|
| 18 | juiz com poder de polícia não pode instaurar de ofício procedimento para aplicar multa de propaganda |
| 19 | prazo de inelegibilidade por abuso econômico ou político |
| 20 | documento unilateral sem fé pública não basta, isoladamente, para comprovar filiação ausente da lista oficial |
| 41 | registro de candidatura não permite reexaminar mérito de decisão de outro Judiciário ou Tribunal de Contas causadora de inelegibilidade |
| 42 | contas julgadas não prestadas impedem quitação durante o mandato e até a apresentação |
| 45 | juiz pode conhecer inelegibilidade de ofício no registro, preservando contraditório e ampla defesa |
| 46 | quebra de sigilo fiscal exige ordem judicial fundamentada, com acesso direto do MPE limitado ao enunciado |
| 48 | retirada posterior de propaganda irregular em bem particular não afasta automaticamente a multa |
| 51 | registro de candidatura não é via para afastar vícios decididos em processo de contas |
| 57 | apresentação das contas é suficiente para quitação na regra descrita no enunciado; não se confunde com contas não prestadas |
| 62 | os fatos imputados delimitam o pedido, não a qualificação jurídica escolhida pelo autor |
| 63 | multa eleitoral só alcança sócios com requisitos de desconsideração, contraditório e ampla defesa |

Súmulas canceladas devem ser marcadas como históricas e não usadas como direito vigente.

## 24. Precedentes estruturantes do STF e TSE

| Precedente | Efeito central |
|---|---|
| STF ADI 4.650 | declarou inconstitucional o financiamento eleitoral por pessoas jurídicas |
| STF ADI 5.394 | reforçou identificação do doador originário e rastreabilidade |
| STF ADI 5.617 | estabeleceu proteção mínima de recursos para candidaturas femininas, depois constitucionalizada e ampliada pela EC 117 |
| STF ADPF 738 | tratou da distribuição proporcional de recursos e tempo para candidaturas negras |
| STF ADI 6.032 | exigiu processo regular e ampla defesa para efeitos graves sobre órgão partidário por contas não prestadas |
| TSE consultas sobre mulheres, pessoas negras e indígenas | integradas às Resoluções nº 23.607 e nº 23.752/2026 |

Decisões concretas precisam ser lidas integralmente; ementa isolada não substitui contexto, modulação e dispositivo.

## 25. Doutrinas jurídicas vinculadas

### 25.1 Princípio republicano

O poder e o patrimônio público não pertencem ao governante nem ao partido.

### 25.2 Separação entre Estado e partido

```text
ESTADO ≠ PARTIDO
GOVERNO ≠ PATRIMÔNIO_PRIVADO_DA_LEGENDA
```

### 25.3 Impessoalidade

Obra, serviço, programa e benefício devem ser apresentados institucionalmente, sem culto à personalidade.

### 25.4 Igualdade de oportunidades eleitorais

A máquina pública não pode alterar artificialmente a disputa em favor de candidatura.

### 25.5 Autenticidade e liberdade do voto

O voto deve resultar de escolha livre, sem coação, compra, abuso ou fraude.

### 25.6 Accountability

Quem recebe recurso público deve registrar, justificar, prestar contas, permitir auditoria e responder.

### 25.7 Finalidade e vinculação

Recurso público deve ser aplicado na finalidade autorizada.

### 25.8 Segregação contábil

Fontes diferentes exigem contas, registros e destinações distinguíveis.

### 25.9 Continuidade do serviço público

Mudança de governo não autoriza abandonar serviço útil sem avaliação, motivação e transição.

### 25.10 Ciclo de vida do ativo

Construção, manutenção, depreciação, reinvestimento e substituição devem ser auditados como uma cadeia.

### 25.11 Proporcionalidade

Sanção deve considerar gravidade, dano, benefício, participação e capacidade de correção.

### 25.12 Tipicidade sancionatória

Não há crime, improbidade ou cassação por analogia livre. É necessário tipo, elementos e prova.

### 25.13 Devido processo

Nenhuma responsabilização séria dispensa competência, ciência, defesa, motivação e prova lícita.

### 25.14 Responsabilidade individualizada

```text
RESPONSABILIDADE =
competência
+ dever
+ ciência
+ possibilidade_de_agir
+ ato_ou_omissão
+ elemento_subjetivo_quando_exigido
+ nexo
+ prova
```

### 25.15 Proveniência informacional

Afirmações sobre autoria pública devem conservar origem, tramitação, votação, orçamento, execução e limitações.

## 26. Matriz: direito vigente versus proposta da sessão

| Tema | Direito vigente | Proposta desenvolvida |
|---|---|---|
| propaganda sobre obras | permitida na campanha dentro dos limites; vedada promoção estatal pessoal | proibição geral de apropriação partidária de obra |
| Fundo Partidário | pode financiar propaganda doutrinária e política | reservar maior parte para educação cívica verificável |
| pesquisas | permitidas com registro e fiscalização | proibir ranking ou divulgação durante campanha |
| autoria de política pública | pode ser debatida politicamente | ficha obrigatória de proveniência e percentuais apenas quando mensuráveis |
| tempo eleitoral | distribuído pela representação e regras legais | espaço neutro para ensinar a votar e verificar fontes |
| ativo público | controle orçamentário e administrativo | índice obrigatório de continuidade, manutenção e reinvestimento |
| qualificação de dirigentes | requisitos variam por cargo | formação mínima pública em sete áreas de responsabilidade |
| participação social | conselhos e controles previstos em várias políticas | integração escola-família-assistência-saúde-Conselho Tutelar |

## 27. Cadeia institucional de fiscalização

```text
TSE
↕
TRE
↕
juízo_eleitoral

MPE
↔ PF / polícia_competente

Justiça_Eleitoral
↔ TCU_TCE_TCM
↔ Receita
↔ AGU
↔ CGU_controladorias
↔ ANPD
```

Cada órgão atua dentro de competência própria. Ciência compartilhada não significa responsabilidade indistinta.

## 28. Protocolo integrado de auditoria

```json
{
  "case_id": "TOKEN_VAZIO",
  "election_year": "TOKEN_VAZIO",
  "territory": "TOKEN_VAZIO",
  "public_policy_or_work": "TOKEN_VAZIO",
  "publicity_claim": "TOKEN_VAZIO",
  "state_channel_or_party_channel": "TOKEN_VAZIO",
  "public_resources_used": [],
  "party_fund": [],
  "fefc": [],
  "tax_compensation_airtime": [],
  "public_building_use": [],
  "public_servants_or_assets": [],
  "executive_initiative": "TOKEN_VAZIO",
  "legislative_proceedings": [],
  "vote_type": "nominal|symbolic|secret|TOKEN_VAZIO",
  "party_votes": {},
  "budget_sources": [],
  "contracts": [],
  "execution_governments": [],
  "maintenance_chain": [],
  "social_program_data_access": [],
  "poll_registrations": [],
  "transport_records": [],
  "campaign_accounts": [],
  "party_annual_accounts": [],
  "formal_complaints": [],
  "competent_authorities": [],
  "institutional_responses": [],
  "binding_precedents": [],
  "tse_precedents": [],
  "counterevidence": [],
  "status": "fato_normativo|fato_documental|anomalia|hipótese|indício|prova|decisão|TOKEN_VAZIO"
}
```

## 29. Fórmula de fechamento

```text
USO_LÍCITO_DE_RECURSO_PÚBLICO_PARTIDÁRIO =
autorização_legal
+ finalidade
+ conta_segregada
+ origem_identificada
+ despesa_comprovada
+ transparência
+ prestação_de_contas
+ controle
```

```text
USO_ILÍCITO_OU_IRREGULAR =
recurso_público
+ finalidade_incompatível
+ agente_identificado
+ ato
+ benefício
+ nexo
+ gravidade
+ prova
- justificativas_legítimas
- contraprovas
```

```text
AUTORIA_PARTIDÁRIA_VÁLIDA =
ato_específico
+ documento
+ voto_nominal_quando_existente
+ orçamento
+ execução
+ limitação_expressa
```

## 30. Fontes normativas principais

### Constituição e leis

- Constituição Federal: https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html
- Código Eleitoral — Lei nº 4.737/1965: https://www2.camara.leg.br/legin/fed/lei/1960-1969/lei-4737-15-julho-1965-356297-normaatualizada-pl.html
- Lei dos Partidos — Lei nº 9.096/1995: https://www2.camara.leg.br/legin/fed/lei/1995/lei-9096-19-setembro-1995-368874-normaatualizada-pl.html
- Lei das Eleições — Lei nº 9.504/1997: https://www2.camara.leg.br/legin/fed/lei/1997/lei-9504-30-setembro-1997-365408-normaatualizada-pl.html
- Lei de Inelegibilidades — LC nº 64/1990: https://www2.camara.leg.br/legin/fed/leicom/1990/leicomplementar-64-18-maio-1990-363991-normaatualizada-pl.html
- Lei de Improbidade — Lei nº 8.429/1992: https://www2.camara.leg.br/legin/fed/lei/1992/lei-8429-2-junho-1992-357452-normaatualizada-pl.html
- Lei de Transporte Eleitoral — Lei nº 6.091/1974: https://www2.camara.leg.br/legin/fed/lei/1970-1979/lei-6091-15-agosto-1974-357590-normaatualizada-pl.html
- Lei de Acesso à Informação — Lei nº 12.527/2011: https://www2.camara.leg.br/legin/fed/lei/2011/lei-12527-18-novembro-2011-611802-normaatualizada-pl.html
- LGPD — Lei nº 13.709/2018: https://www2.camara.leg.br/legin/fed/lei/2018/lei-13709-14-agosto-2018-787077-normaatualizada-pl.html
- Lei atual do Bolsa Família — Lei nº 14.601/2023: https://www2.camara.leg.br/legin/fed/lei/2023/lei-14601-19-junho-2023-794281-normaatualizada-pl.html
- Primeira lei do Bolsa Família — Lei nº 10.836/2004: https://www2.camara.leg.br/legin/fed/lei/2004/lei-10836-9-janeiro-2004-490604-normaatualizada-pl.html
- ECA — Lei nº 8.069/1990: https://www2.camara.leg.br/legin/fed/lei/1990/lei-8069-13-julho-1990-372211-normaatualizada-pl.html
- Código Civil — Lei nº 10.406/2002: https://www2.camara.leg.br/legin/fed/lei/2002/lei-10406-10-janeiro-2002-432893-normaatualizada-pl.html

### Resoluções TSE

- Contas partidárias — Resolução nº 23.604/2019: https://www.tse.jus.br/legislacao/compilada/res/2019/resolucao-no-23-604-de-17-de-dezembro-de-2019
- Contas de campanha — Resolução nº 23.607/2019: https://www.tse.jus.br/legislacao/compilada/res/2019/resolucao-no-23-607-de-17-de-dezembro-de-2019
- Pesquisas — Resolução nº 23.600/2019: https://www.tse.jus.br/legislacao/compilada/res/2019/resolucao-no-23-600-de-12-de-dezembro-de-2019
- Propaganda — Resolução nº 23.610/2019: https://www.tse.jus.br/legislacao/compilada/res/2019/resolucao-no-23-610-de-18-de-dezembro-de-2019
- Cadastro — Resolução nº 23.659/2021: https://www.tse.jus.br/legislacao/compilada/res/2021/resolucao-no-23-659-de-26-de-outubro-de-2021
- Propaganda partidária — Resolução nº 23.679/2022: https://www.tse.jus.br/legislacao/compilada/res/2022/resolucao-no-23-679-de-8-de-fevereiro-de-2022
- Atos gerais de 2026 — Resolução nº 23.751/2026: https://www.tse.jus.br/legislacao/compilada/res/2026/resolucao-no-23-751-de-26-de-fevereiro-de-2026
- Contas para 2026 — Resolução nº 23.752/2026: https://www.tse.jus.br/legislacao/compilada/res/2026/resolucao-no-23-752-de-26-de-fevereiro-de-2026
- Propaganda 2026 — Resolução nº 23.755/2026: https://www.tse.jus.br/legislacao/compilada/res/2026/resolucao-no-23-755-de-26-de-fevereiro-de-2026
- Ilícitos eleitorais 2026 — Resolução nº 23.757/2026: https://www.tse.jus.br/legislacao/compilada/res/2026/resolucao-no-23-757-de-26-de-fevereiro-de-2026
- Votação 2026 — Resolução nº 23.758/2026: https://www.tse.jus.br/legislacao/compilada/res/2026/resolucao-no-23-758-de-26-de-fevereiro-de-2026
- Súmulas do TSE: https://www.tse.jus.br/legislacao/codigo-eleitoral/sumulas/sumulas-do-tse

### STF

- Súmulas vinculantes — repositório oficial: https://portal.stf.jus.br/jurisprudencia/sumariosumulas.asp?base=26

---

**F_ok:** Constituição, TSE, TRE, juízo eleitoral, MPE, recursos públicos partidários, fundos, propaganda, contas, improbidade, abuso, pesquisas, transporte, obras, benefícios, dados, súmulas e doutrinas foram integrados em uma única matriz.  
**F_gap:** “todas as leis e todos os precedentes” é conjunto aberto; continuam pendentes a legislação estadual/municipal, regimentos de cada Casa, súmulas específicas de cada TRE e os acórdãos aplicáveis a um caso concreto.  
**F_next:** converter esta matriz em índice navegável e, para cada caso delimitado, preencher o protocolo com documentos, competência, ato, benefício, nexo, prova e contraprova.
