# Segurança do Passageiro, Pouso, Informação e Responsabilidade Aeronáutica

**Status documental:** análise técnico-jurídica e proposta regulatória  
**Data de corte:** 2026-07-16  
**Claim boundary:** este documento não atribui culpa individual, não substitui investigação aeronáutica, perícia, parecer jurídico ou decisão judicial.

## 1. Questão central

A percepção pública costuma associar um toque quase imperceptível à perícia do piloto:

```text
pouso macio -> piloto melhor -> operação mais segura
```

Essa equivalência não é tecnicamente válida. Um pouso seguro depende do conjunto formado por aproximação estabilizada, energia correta, toque dentro da zona prevista, alinhamento, condição da pista, frenagem, margem remanescente e decisão de arremeter quando os critérios não forem atendidos.

A hipótese social relevante é outra:

> Se aplausos, avaliações de passageiros ou indicadores de conforto forem usados direta ou indiretamente para pressionar tripulações a buscar o toque mais suave possível, pode surgir um incentivo incompatível com a gestão de risco.

Não foi localizada evidência de que companhias aéreas utilizem formalmente “número de aplausos” como meta de piloto. Portanto, essa afirmação permanece **HIPÓTESE / TOKEN_VAZIO**, enquanto o risco de confundir conforto com segurança é tecnicamente defensável.

## 2. Invariante de segurança do pouso

A invariante operacional proposta é lógica, não uma média de satisfação:

\[
I_{pouso}=
A_{estabilizada}\land
V_{envelope}\land
T_{zona}\land
C_{pista}\land
D_{margem}\land
B_{desaceleração}\land
G_{arremetida}
\]

Onde:

- `A_estabilizada`: aproximação controlada em trajetória, configuração e energia;
- `V_envelope`: velocidade compatível com o procedimento e as condições;
- `T_zona`: toque no local operacionalmente previsto;
- `C_pista`: condição da superfície e ação de frenagem conhecidas ou avaliadas;
- `D_margem`: distância necessária menor ou igual à distância segura disponível;
- `B_desaceleração`: spoilers, freios e reverso aplicados conforme procedimento;
- `G_arremetida`: go-around executado quando a continuação deixa de satisfazer os gates.

Se um elemento obrigatório falha, a suavidade percebida não corrige a violação:

\[
I_{pouso}=0
\quad\text{mesmo quando}\quad
Q_{conforto}\approx 1.
\]

## 3. Pouso macio, pouso firme e excursão de pista

Um toque suave pode ser perfeitamente seguro. O problema surge quando a busca de suavidade prolonga o arredondamento e faz a aeronave flutuar além da zona de toque.

```text
flare prolongado
-> toque tardio
-> menos pista remanescente
-> menor margem para desaceleração
-> maior exposição a excursão de pista
```

A ANAC identifica pouso longo e aplicação ineficaz ou demorada dos freios como fatores relevantes no risco de excursão de pista e destaca a arremetida como oportunidade primária de prevenção. A FAA também trata aproximação instável, excesso de energia, toque longo, condição da pista e frenagem como precursores a serem controlados.

Um toque positivo e controlado pode ser adequado em determinadas condições, especialmente quando é necessário estabelecer contato efetivo com a pista. Isso não significa defender pouso duro: cargas verticais excessivas podem causar dano estrutural, inspeção obrigatória e risco aos ocupantes.

O objetivo não é “o toque mais leve” nem “o toque mais forte”. É:

\[
\boxed{
\text{toque controlado no lugar correto, dentro do envelope e com margem preservada}
}
\]

## 4. Separação obrigatória entre qualidade de serviço e segurança

### 4.1 Qualidade percebida pelo passageiro

Pode incluir:

- conforto;
- atendimento;
- comunicação;
- pontualidade;
- limpeza;
- sensação de suavidade;
- confiança percebida.

### 4.2 Segurança operacional

Deve utilizar dados objetivos, como:

- estabilidade da aproximação;
- velocidade e energia na cabeceira;
- ponto de toque;
- distância remanescente;
- vento cruzado, rajadas e cisalhamento;
- condição e contaminação da pista;
- ação de frenagem;
- alertas e excedências;
- go-around quando requerido;
- dados de FDM/FOQA ou programa equivalente;
- relatos de segurança e auditoria LOSA/SGSO;
- manutenção e aeronavegabilidade.

### 4.3 Regra de não contaminação

\[
Q_{serviço}\not\Rightarrow S_{operacional}
\]

Uma avaliação de passageiro pode iniciar triagem, mas não deve classificar individualmente um piloto como seguro ou inseguro sem dados operacionais e revisão técnica.

É inadequado criar remuneração, punição, ranking ou meta de tripulação baseada em “maciez”, aplausos ou impressão isolada da cabine. Caso uma empresa adote tal incentivo, a prática deve passar por avaliação do Sistema de Gerenciamento da Segurança Operacional, porque pode produzir pressão de produção e conflito com a cultura positiva de segurança.

## 5. O papel da comissária e do comissário

A tripulação de cabine não exerce função secundária. No RBAC 121, os comissários possuem atribuições de orientação e controle de passageiros, treinamento de emergência e posições próximas às saídas durante pousos e decolagens. Aeronaves com mais de 44 assentos precisam demonstrar capacidade de evacuação total em 90 segundos ou menos conforme os critérios regulatórios aplicáveis.

O cartão de segurança e a demonstração antes do voo têm função de preparar respostas rápidas para eventos raros e graves. Entretanto, eles normalmente explicam equipamentos e evacuação, não alfabetização sobre risco operacional.

### Proposta complementar de informação ao passageiro

Sem sobrecarregar o briefing, o operador poderia incluir mensagem curta e padronizada:

> “A segurança do pouso não é medida apenas pela suavidade do toque. Dependendo das condições, o contato pode ser mais perceptível. Arremeter é um procedimento normal e seguro quando os critérios de aproximação não são atendidos.”

A mensagem reduz a pressão cultural por “pouso para aplauso” sem expor dados técnicos sensíveis ou interferir na autoridade da tripulação.

## 6. OACI, Estado brasileiro e cadeia de responsabilidade

### 6.1 OACI/ICAO

A Organização da Aviação Civil Internacional estabelece Standards and Recommended Practices (SARPs), planos globais e estruturas de segurança. Ela não opera o voo, não administra normalmente aeroportos brasileiros, não licencia diretamente o piloto brasileiro e não costuma participar de investigações individuais, salvo assistência excepcional solicitada pelos Estados competentes.

A OACI pode ser objeto de proposta normativa, auditoria institucional ou crítica de governança. Contudo, responsabilizá-la civilmente por um acidente individual exige base jurídica própria, competência, violação atribuível e nexo causal. A ausência de uma mensagem específica ao passageiro sobre “pouso macio” não transfere automaticamente a responsabilidade operacional à organização internacional.

### 6.2 ANAC

A Lei nº 11.182/2005 atribui à ANAC a regulação e fiscalização da aviação civil e da infraestrutura aeronáutica e aeroportuária. A Agência implementa normas internacionais em sua esfera, fiscaliza serviços, produtos, processos, treinamento, tripulantes e segurança, e pode adotar medidas cautelares para cessar risco ou ameaça.

Em maio de 2026, a Emenda 25 ao RBAC 121 passou a exigir que o piloto em comando não prossiga além do ponto definido da aproximação sem se assegurar, a partir das informações disponíveis sobre a pista e o desempenho da aeronave, de que um pouso seguro pode ser concluído. Também exige reporte quando a ação de frenagem encontrada for pior que a esperada.

### 6.3 DECEA e Comando da Aeronáutica

O DECEA administra o controle do espaço aéreo e os serviços de navegação aérea. Sua responsabilidade é diferente da regulação econômica/civil, da operação da companhia, da administração da pista e da investigação de segurança.

### 6.4 CENIPA/SIPAER

A investigação de segurança busca prevenir novas ocorrências. Conforme o modelo do Anexo 13 da OACI e o sistema brasileiro, sua finalidade não é distribuir culpa ou responsabilidade civil. Relatório técnico, ação indenizatória, processo administrativo e investigação criminal podem coexistir, mas não são a mesma coisa.

### 6.5 Operador aéreo e comandante

O operador deve possuir procedimentos, treinamento, controle operacional, manutenção e SGSO. O comandante detém autoridade final a bordo e deve tomar decisões compatíveis com a segurança, incluindo arremeter.

O piloto automático e o autoland são ferramentas. Eles não absorvem personalidade jurídica nem eliminam o dever de monitoramento e intervenção da tripulação ou as responsabilidades do operador, fabricante, manutenção, aeroporto e controle, conforme o nexo causal de cada caso.

### 6.6 Operador aeroportuário

Deve manter pista, sinalização, áreas de segurança, informações de condição da superfície e demais elementos sob sua responsabilidade. O Código Brasileiro de Aeronáutica reconhece a possibilidade de responsabilidade da administração aeroportuária ou da Administração Pública por culpa de seus operadores em serviços de infraestrutura.

### 6.7 Seguradora

A contratação de seguro é garantia financeira, não substituição da responsabilidade técnica. O pagamento depende de cobertura, apuração, limites e exclusões da apólice. A seguradora não define o que foi um pouso seguro e não deve criar incentivo operacional para aumentar risco.

### 6.8 Certificadoras, inclusive Bureau Veritas

Certificações de sistemas de gestão, como as famílias aeroespaciais 9100/9110/9120, podem apoiar qualidade e auditoria. Elas não são apólice, não garantem indenização e não eliminam responsabilidade por fato concreto.

## 7. Direito do passageiro à informação

O Código de Defesa do Consumidor protege vida, saúde e segurança e assegura informação adequada e clara sobre serviços e seus riscos. Esse dever não significa transmitir ao passageiro cada detalhe instantâneo da operação ou dados protegidos de segurança.

A arquitetura equilibrada é:

```text
informação pública de risco e direitos
+ instrução operacional compreensível
+ canal de reclamação
+ análise técnica protegida
+ prestação de contas agregada
```

A Política Nacional de Aviação Civil também reconhece proteção do consumidor, transparência e respeito à saúde e à segurança como elementos do serviço aéreo.

### Informação que deve ser pública

- direitos e deveres;
- finalidade da demonstração de segurança;
- normalidade da arremetida;
- esclarecimento de que suavidade não é indicador isolado;
- canais de reclamação;
- estatísticas agregadas e recomendações de segurança;
- resultado final de investigações nos limites legais.

### Informação que exige proteção

- gravações de cabine;
- dados identificáveis de tripulantes;
- dados brutos de FDM/FOQA;
- dados pessoais dos passageiros;
- relatos voluntários protegidos;
- informação cuja divulgação comprometa investigação, privacidade ou cultura justa.

## 8. LGPD aplicada aos dados de segurança

A segurança operacional pode utilizar dados extensos sem transformar a tripulação ou o passageiro em alvo de vigilância indiscriminada.

Princípios aplicáveis:

- finalidade específica;
- adequação;
- necessidade/minimização;
- segurança;
- prevenção;
- não discriminação;
- responsabilização e prestação de contas.

### Regra de arquitetura

```text
reclamação do passageiro
-> protocolo e classificação
-> remoção/minimização de dados desnecessários
-> correlação com evento operacional agregado
-> análise por equipe de segurança
-> ação corretiva sistêmica
```

Não deve ocorrer:

```text
aplauso ou nota de maciez
-> ranking público de piloto
-> punição automática
```

FOQA/FDM funciona melhor quando identifica tendências e deficiências sistêmicas, com dados desidentificados, governança e ação corretiva, e não como instrumento de competição estética entre tripulantes.

## 9. Ambiente serrano, Lages e fenômenos atmosféricos

A intuição de que céu claro não significa ar imóvel é correta. Podem existir:

- térmicas e convecção;
- ascendentes e descendentes;
- cisalhamento;
- rajadas;
- ondas de montanha;
- turbulência orográfica;
- rotor a sotavento;
- variações associadas a frentes e estabilidade atmosférica.

O relevo da Serra Catarinense pode produzir interações entre vento e topografia. Porém não foi localizada, nesta análise, evidência suficiente para afirmar que o Aeroporto de Lages possui “o maior fluxo de conversão” ou um padrão singular permanente de vento aleatório. Essa hipótese exige dados locais.

### Varredura científica recomendada para o aeródromo

\[
R_{aeródromo}=f(
\theta_{vento},
V_{rajada},
\Delta V_{cisalhamento},
N_{estabilidade},
H_{relevo},
R_{pista},
C_{superfície},
T_{touchdown}
)
\]

Dados necessários:

- METAR/SPECI e TAF históricos;
- rosa dos ventos por cabeceira;
- rajadas e vento cruzado;
- topografia e obstáculos;
- relatos PIREP/AIREP quando disponíveis;
- eventos de go-around e aproximação instável;
- ponto de toque e frenagem em dados FDM;
- condição e manutenção da pista;
- horários, sazonalidade e estabilidade atmosférica.

A analogia com o corredor quente/frio de um datacenter é didática para visualizar convecção e recirculação, mas não constitui modelo atmosférico. A atmosfera envolve escala, estratificação, umidade, relevo, turbulência e balanço de energia muito mais complexos.

## 10. Correção documental do caso associado à Xuxa

As fontes jornalísticas localizadas descrevem um **Learjet 55 da OceanAir Táxi Aéreo**, em 12 de agosto de 2010. A aeronave iria ao Aeroporto Tom Jobim buscar Xuxa e sua equipe, mas retornou ao Santos Dumont após problema/pane e sofreu uma excursão, terminando parcialmente na Baía de Guanabara. Xuxa não estava a bordo.

Não foi encontrada sustentação para afirmar que:

- a aeronave era um Embraer Legacy;
- Xuxa estava dentro da aeronave;
- era o primeiro voo daquele piloto com ela;
- o piloto buscava demonstrar perícia;
- a intenção de pousar suavemente causou a ocorrência.

Esses elementos ficam classificados como `NÃO_VERIFICADO` e não podem ser usados para imputação pessoal. O caso pode servir apenas como exemplo da necessidade de aguardar investigação e separar sensação, narrativa e causalidade comprovada.

## 11. Proposta de reforma regulatória e institucional

### P1 — Alfabetização do passageiro

Incluir, no cartão, vídeo ou página de segurança:

- pouso macio não equivale automaticamente a pouso seguro;
- toque perceptível pode ser operacionalmente normal;
- arremetida é decisão legítima de segurança;
- reclamações devem relatar fatos percebidos sem pressionar a tripulação a completar pouso instável.

### P2 — Proibição de indicador estético de pilotagem

Operadores deveriam declarar que aplausos, notas de suavidade ou comentários de celebridades não integram metas de segurança, remuneração ou sanção de pilotos.

### P3 — Canal de reclamação de segurança

Separar no sistema de atendimento:

```text
SERVIÇO
SEGURANÇA PERCEBIDA
ACESSIBILIDADE
DANO
ATRASO/CANCELAMENTO
```

Reclamações de segurança seriam encaminhadas ao SGSO e correlacionadas com dados operacionais, sem conclusões automáticas.

### P4 — Indicadores públicos agregados

Publicar, quando juridicamente possível e sem identificação indevida:

- taxas de aproximação instável;
- arremetidas;
- pousos longos;
- excursões;
- tendências de ação de frenagem;
- ações corretivas;
- auditorias e recomendações.

### P5 — Auditoria independente

Certificadoras ou auditores podem verificar se:

- a companhia separa satisfação e segurança;
- os incentivos não pressionam a continuação de aproximação instável;
- os dados são minimizados e protegidos;
- o SGSO transforma tendências em ações corretivas.

A auditoria não substitui ANAC, CENIPA, Judiciário ou seguradora.

## 12. Matriz de responsabilidade

| Evento/obrigação | Responsável primário | Supervisão/apoio | Observação |
|---|---|---|---|
| Normas globais | OACI/Estados | organizações regionais | SARPs dependem de implementação estatal |
| Regulação civil | ANAC | União | fiscalização e medidas cautelares |
| Controle de tráfego | DECEA | Comando da Aeronáutica | navegação e espaço aéreo |
| Operação do voo | operador aéreo | ANAC | SOP, treinamento, manutenção e SGSO |
| Decisão a bordo | comandante | operador | autoridade final, inclusive go-around |
| Pista e infraestrutura | operador aeroportuário | ANAC/ente delegante | condição, sinalização e informação |
| Investigação preventiva | CENIPA/SIPAER | participantes autorizados | prevenção, não culpa |
| Responsabilidade civil/penal | Judiciário e autoridades | perícias | depende de fatos e nexo causal |
| Indenização securitária | seguradora | SUSEP/Judiciário | conforme apólice e obrigação legal |
| Qualidade certificada | organismo certificador | acreditação aplicável | não equivale a seguro ou imunidade |

## 13. Estados epistemológicos

```yaml
VERIFICADO:
  - suavidade não é indicador isolado de segurança
  - pouso longo e frenagem tardia elevam risco de excursão
  - aproximação estabilizada e margem de pouso são gates
  - OACI não costuma investigar individualmente ocorrências
  - ANAC regula e fiscaliza a aviação civil brasileira
  - CENIPA investiga com finalidade preventiva

HIPOTESE:
  - aplausos podem criar pressão social por suavidade
  - avaliações de conforto podem contaminar decisões se usadas como KPI de piloto
  - aeródromos serranos exigem perfil local de risco orográfico

TOKEN_VAZIO:
  - existência de meta empresarial formal de aplausos
  - efeito causal mensurado dessa meta sobre excursões
  - perfil estatístico completo de vento e pouso em Lages

NAO_VERIFICADO:
  - Xuxa estava a bordo no caso de 2010
  - aeronave era Legacy
  - primeiro voo do piloto com Xuxa
  - intenção de impressionar causou o acidente
```

## 14. Fontes normativas e técnicas principais

1. OACI, Anexo 13 — Aircraft Accident and Incident Investigation.
2. OACI, Anexo 19 — Safety Management.
3. OACI, Safety Management Manual, Doc 9859, 4ª edição.
4. Lei nº 11.182/2005 — criação e competências da ANAC.
5. Lei nº 7.565/1986 — Código Brasileiro de Aeronáutica.
6. Lei nº 8.078/1990 — Código de Defesa do Consumidor, arts. 6º, 8º e 9º.
7. Decreto nº 6.780/2009 — Política Nacional de Aviação Civil.
8. RBAC nº 121 e Emenda nº 25, Resolução ANAC nº 801/2026.
9. IS ANAC nº 121-018A — aproximações e definição de aproximação estabilizada.
10. ANAC — Excursão de pista.
11. FAA AC 91-79B — Aircraft Landing Performance and Runway Excursion Mitigation.
12. FAA AC 120-82 — Flight Operational Quality Assurance.
13. Bureau Veritas — IAQG 9100/9110/9120 Quality Management Systems.

## 15. Conclusão

A informação ao passageiro não deve transformar a cabine em centro de decisão técnica, mas deve impedir que uma crença cultural pressione o sistema na direção errada.

\[
\boxed{
\text{segurança demonstrável}
>
\text{suavidade percebida}
>
\text{aplauso}
}
\]

A responsabilidade deve seguir evidência, competência e nexo causal. O seguro financia a reparação; a certificação audita sistemas; o regulador fiscaliza; a investigação previne; o operador e seus agentes executam; o passageiro tem direito à informação adequada e a canais efetivos de reclamação. Nenhuma dessas camadas deve substituir as demais.
