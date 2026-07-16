# Claims Ledger — Pouso Seguro, Informação e Responsabilidade

**Documento associado:** `SEGURANCA_PASSAGEIRO_POUSO_RESPONSABILIDADE.md`  
**Regra:** verificação na fonte não equivale a causalidade provada nem a responsabilidade jurídica.  
**Padrão:** `claim_allowed: false` para acusações individuais ou institucionais sem investigação e nexo causal.

## Estados

| Estado | Significado |
|---|---|
| `VERIFICADO_NA_FONTE` | A norma, documento ou dado afirma diretamente o conteúdo. |
| `DERIVADO_TECNICO` | Conclusão lógica limitada, derivada de fontes técnicas. |
| `HIPOTESE_OPERACIONAL` | Relação plausível que exige dados ou experimento. |
| `PROPOSTA_REGULATORIA` | Recomendação, não obrigação jurídica vigente. |
| `TOKEN_VAZIO` | Informação necessária não localizada ou não produzida. |
| `NAO_VERIFICADO` | Alegação pesquisada sem suporte suficiente. |
| `CONTRADITO_PELAS_FONTES_LOCALIZADAS` | Fontes localizadas apontam fato incompatível. |

## Claims atômicos

| ID | Claim | Estado | Evidência/condição | Falsificador ou próximo gate |
|---|---|---|---|---|
| AV-C01 | Um pouso suave não é, isoladamente, prova de pouso seguro. | `DERIVADO_TECNICO` | Segurança depende de estabilidade, energia, zona de toque, pista e desaceleração. | Demonstrar norma que use suavidade isolada como critério suficiente. |
| AV-C02 | Pouso longo e frenagem tardia aumentam risco de excursão de pista. | `VERIFICADO_NA_FONTE` | ANAC e FAA tratam esses fatores como precursores. | Dados que mostrem ausência de relação sob mesmas condições. |
| AV-C03 | Arremeter é uma barreira normal de segurança quando critérios deixam de ser atendidos. | `VERIFICADO_NA_FONTE` | ANAC e doutrina de aproximação estabilizada. | Procedimento específico aplicável que determine continuação segura. |
| AV-C04 | Um toque firme e controlado pode ser adequado em condições específicas. | `DERIVADO_TECNICO` | Necessidade de contato efetivo sem prolongar flutuação; sujeito ao AFM/SOP. | Manual da aeronave/procedimento aplicável proibindo a técnica. |
| AV-C05 | Pouso duro deliberado não é objetivo de segurança. | `DERIVADO_TECNICO` | Carga vertical excessiva pode causar dano e inspeção. | Nenhum; claim limitado ao excesso fora do envelope. |
| AV-C06 | Aplausos ou avaliações de suavidade podem criar pressão social sobre a tripulação. | `HIPOTESE_OPERACIONAL` | Mecanismo de incentivo plausível em cultura organizacional. | Pesquisa/FOQA mostrando ausência de efeito ou inexistência do incentivo. |
| AV-C07 | Companhias aéreas utilizam formalmente quantidade de aplausos como meta de pilotos. | `TOKEN_VAZIO` | Nenhuma política formal localizada. | Política, contrato, KPI ou manual verificável. |
| AV-C08 | Métricas de satisfação e métricas de segurança devem permanecer separadas. | `DERIVADO_TECNICO` | Cultura de segurança e indicadores objetivos de SMS/FDM. | Evidência de sistema seguro em que a fusão não cria conflito. |
| AV-C09 | Reclamação de passageiro pode iniciar triagem, mas não determina culpa do piloto. | `DERIVADO_TECNICO` | Sensação não contém todos os parâmetros operacionais; requer correlação. | Registro completo demonstrando evento e nexo. |
| AV-C10 | O briefing e o cartão de segurança possuem função crítica de evacuação e resposta. | `VERIFICADO_NA_FONTE` | RBAC 121: treinamento, posições e demonstração de evacuação. | Norma superveniente que altere a função. |
| AV-C11 | Briefings atuais podem ser complementados com alfabetização sobre go-around e toque perceptível. | `PROPOSTA_REGULATORIA` | Redução de crença pública inadequada; texto ainda não obrigatório. | Avaliação de fatores humanos indicando efeito adverso superior. |
| AV-C12 | A OACI estabelece SARPs e não opera voos individuais. | `VERIFICADO_NA_FONTE` | Convenção/Anexos e atribuições institucionais. | Mandato específico aplicável ao evento. |
| AV-C13 | A OACI é automaticamente responsável por cada acidente relacionado a informação insuficiente ao passageiro. | `NAO_VERIFICADO` | Responsabilidade requer base jurídica, competência, violação e nexo. | Decisão ou regra aplicável estabelecendo responsabilidade automática. |
| AV-C14 | A ANAC regula e fiscaliza aviação civil e infraestrutura aeroportuária no Brasil. | `VERIFICADO_NA_FONTE` | Lei nº 11.182/2005. | Alteração legislativa. |
| AV-C15 | O CENIPA/SIPAER investiga prioritariamente para prevenção, não para distribuir culpa. | `VERIFICADO_NA_FONTE` | OACI Anexo 13 e CBA/SIPAER. | Alteração normativa. |
| AV-C16 | O piloto automático elimina a responsabilidade humana e organizacional. | `CONTRADITO_PELAS_FONTES_LOCALIZADAS` | Automação é ferramenta; comandante e operador mantêm deveres. | Norma específica atribuindo personalidade/responsabilidade autônoma ao sistema. |
| AV-C17 | Seguro é mecanismo financeiro, não critério de segurança operacional. | `DERIVADO_TECNICO` | CBA exige garantia; apólice não define técnica de pouso. | Contrato/lei que transforme seguradora em autoridade operacional. |
| AV-C18 | Certificação Bureau Veritas equivale a seguro e garante indenização. | `CONTRADITO_PELAS_FONTES_LOCALIZADAS` | Certificação de gestão e seguro têm objetos distintos. | Documento contratual específico, limitado ao caso. |
| AV-C19 | Céu claro pode coexistir com térmicas, cisalhamento e turbulência orográfica. | `DERIVADO_TECNICO` | Fenômenos atmosféricos não dependem de nuvem visível. | Dados locais demonstrando atmosfera estável no intervalo considerado. |
| AV-C20 | O Aeroporto de Lages possui permanentemente o maior fluxo aleatório de vento da região. | `TOKEN_VAZIO` | Não foi produzido estudo comparativo local. | METAR/TAF, rosa dos ventos, topografia e comparação regional. |
| AV-C21 | O caso de 2010 associado à Xuxa envolveu um Learjet 55 que iria buscá-la. | `VERIFICADO_NA_FONTE` | Jornal do Brasil e Folha descrevem aeronave e missão. | Relatório oficial com identificação diferente. |
| AV-C22 | Xuxa estava a bordo na ocorrência de 2010. | `CONTRADITO_PELAS_FONTES_LOCALIZADAS` | Fontes indicam que a aeronave iria buscá-la. | Manifesto de passageiros ou relatório oficial em sentido contrário. |
| AV-C23 | A aeronave do caso era um Embraer Legacy. | `CONTRADITO_PELAS_FONTES_LOCALIZADAS` | Fontes identificam Learjet 55. | Relatório oficial em sentido contrário. |
| AV-C24 | Era o primeiro voo do piloto com Xuxa. | `TOKEN_VAZIO` | Nenhuma fonte localizada. | Registro verificável de escala/contrato. |
| AV-C25 | O piloto tentou impressionar Xuxa com pouso suave e isso causou a excursão. | `NAO_VERIFICADO` | Não há evidência de intenção ou nexo; Xuxa não estava a bordo. | Investigação oficial e evidência direta de motivação/nexo. |
| AV-C26 | Dados de reclamação, FDM/FOQA e tripulação devem ter governança e minimização. | `DERIVADO_TECNICO` | LGPD, proteção de dados de segurança e cultura justa. | Base legal/procedimento específico que exija tratamento mais amplo. |

## Relações epistemológicas essenciais

```text
AV-C06 NOT_EVIDENCE_FOR AV-C07
AV-C21 CONTRADICTS AV-C22
AV-C21 CONTRADICTS AV-C23
AV-C22 NOT_EVIDENCE_FOR AV-C25
AV-C02 SUPPORTS AV-C01
AV-C03 SUPPORTS AV-C11
AV-C08 SUPPORTS AV-C26
```

## Gates antes de promoção

### Para promover AV-C07

Exigir ao menos um dos itens:

- política oficial de companhia;
- contrato de trabalho;
- KPI de treinamento;
- documento de remuneração;
- comunicação interna autenticada;
- estudo independente reproduzível.

### Para promover AV-C20

Exigir:

- série histórica METAR/SPECI/TAF;
- rosa dos ventos por cabeceira;
- topografia e estabilidade;
- dados de rajada/cisalhamento;
- comparação com aeródromos equivalentes;
- método estatístico e incerteza.

### Para promover AV-C25

Exigir:

- relatório oficial;
- declaração verificável;
- gravação admitida legalmente;
- evidência de que a intenção alterou a técnica;
- nexo causal pericial.

Sem esses gates:

```text
claim_allowed: false
```
