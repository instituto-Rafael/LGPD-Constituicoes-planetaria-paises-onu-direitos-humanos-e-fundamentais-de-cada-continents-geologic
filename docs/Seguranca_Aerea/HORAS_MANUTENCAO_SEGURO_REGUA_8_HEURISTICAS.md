# Horas, Manutenção, Seguro e Régua de Oito Heurísticas

**Status documental:** estrutura técnico-jurídica de triagem e pesquisa exploratória  
**Data de corte:** 2026-07-16  
**Aplicação:** aviação civil brasileira, com foco em operadores RBAC 91, 121 e 135  
**Claim boundary:** este documento não determina culpa, fraude, cobertura securitária ou causa de acidente. Ele define obrigações, fluxos financeiros, dados e gates para auditoria.

## 1. Questão-raiz

A ocorrência visível pode ser um trem de pouso danificado, um toque assimétrico, uma excursão de pista ou uma aeronave retirada de serviço. A responsabilidade não pode ser inferida diretamente do dano:

```text
peça quebrada
≠ erro do piloto automaticamente
≠ falha de manutenção automaticamente
≠ cobertura de seguro automaticamente
≠ fraude automaticamente
```

A cadeia correta é:

\[
\text{evento}
\rightarrow
\text{dados de voo}
\rightarrow
\text{condição meteorológica e de pista}
\rightarrow
\text{técnica aplicada}
\rightarrow
\text{histórico de manutenção}
\rightarrow
\text{limites de tripulação}
\rightarrow
\text{nexo causal}
\rightarrow
\text{responsabilidade}
\rightarrow
\text{cobertura e fluxo financeiro}
\]

## 2. “O piloto é responsável pelas próprias horas” precisa ser dividido

A palavra **horas** mistura pelo menos quatro objetos jurídicos e operacionais diferentes.

### 2.1 Horas de experiência — CIV Digital

A CIV registra experiência de voo para licença, habilitação, experiência recente e comprovação profissional.

- o piloto pode registrar e deve manter veracidade e atualização;
- instrutor ou preposto do operador RBAC 121/135 também pode registrar;
- o Diário de Bordo da aeronave é o registro primário;
- operadores RBAC 121/135 podem declarar horas de seus tripulantes.

Portanto:

\[
R_{\mathrm{CIV}}
=
R_{\mathrm{piloto}}
\cup
R_{\mathrm{instrutor}}
\cup
R_{\mathrm{preposto\ do\ operador}}
\]

conforme quem realizou o lançamento.

### 2.2 Horas de voo e número de pousos na jornada

A Lei nº 13.475/2017 estabelece limites de voo, pousos, jornada, repouso, folga, horas mensais e anuais. Esses limites não são um caderno privado que a empresa pode ignorar.

A empresa:

- cria e administra a escala;
- conhece os voos por ela atribuídos;
- deve impedir planejamento incompatível com os limites;
- deve manter processos de gerenciamento de fadiga;
- deve registrar e responder a reportes.

O tripulante:

- deve informar condições que afetem sua aptidão;
- não deve aceitar operação que saiba incompatível com limites ou segurança;
- deve preservar a veracidade dos próprios registros;
- exerce autoridade e dever operacional conforme sua função.

A responsabilidade é compartilhada, mas não simétrica:

\[
\boxed{
\text{dever do piloto de informar}
\neq
\text{licença para a companhia escalar ilegalmente}
}
\]

### 2.3 Jornada, repouso e fadiga

O gerenciamento da fadiga é expressamente compartilhado entre operador e tripulante. Entretanto, a companhia controla recursos, escala, ambiente de trabalho, treinamento e resposta aos reportes; logo, possui capacidade estrutural maior de prevenção.

### 2.4 Horas e ciclos da aeronave e dos componentes

Horas do piloto não são horas do componente.

Uma peça pode ser controlada por:

- horas de voo;
- ciclos;
- pousos;
- partidas;
- pressurizações;
- tempo calendário;
- condição;
- evento;
- Diretriz de Aeronavegabilidade;
- limitação obrigatória de aeronavegabilidade.

Cada contador deve possuir fonte, unidade, limite e registro próprios.

## 3. Exemplo: toque assimétrico e dano ao trem de pouso

Encostar uma roda antes da outra pode ser normal em correção de vento cruzado, dependendo da técnica aprovada, do tipo de aeronave e das condições. O simples fato de uma roda tocar primeiro não demonstra erro.

Para atribuir dano do trem à técnica do piloto, seriam necessários, entre outros:

- trajetória, atitude e razão de descida;
- velocidade e energia;
- vento cruzado, rajada e cisalhamento;
- posição na pista;
- cargas verticais e laterais;
- ângulo de deriva e alinhamento;
- comandos e atuação dos sistemas;
- limites do fabricante;
- dados FDM/DFDR;
- inspeção do trem, pneus, freios, fixações e estrutura;
- histórico de pousos, manutenção, corrosão, trincas e eventos anteriores.

A hipótese “o piloto tentou tocar macio para seguir métrica” exige ainda:

- existência verificável da métrica;
- ciência do piloto;
- pressão ou incentivo;
- alteração comprovada da técnica;
- relação causal entre essa alteração e o dano.

Sem esses gates:

```text
claim_allowed: false
```

## 4. Responsabilidade da companhia pela manutenção e pelas trocas

Para operadores RBAC 121 e 135, a empresa aérea é a principal responsável pela aeronavegabilidade e pela conclusão adequada da manutenção.

Isso permanece verdadeiro quando a manutenção é contratada:

```text
operador contrata oficina
→ oficina executa e libera o trabalho
→ operador supervisiona o provedor
→ operador continua principal responsável pela aeronavegabilidade
```

A empresa deve manter um Programa de Manutenção de Aeronavegabilidade Continuada — PMAC, com:

1. responsabilidade pela aeronavegabilidade;
2. Manual Geral de Manutenção;
3. organização de manutenção;
4. execução e aprovação;
5. programação;
6. itens de inspeção obrigatória;
7. registros;
8. manutenção contratada;
9. treinamento;
10. sistema de análise e supervisão continuada.

A companhia não pode transferir integralmente sua obrigação à oficina por contrato privado.

## 5. Responsabilidade da organização de manutenção

A organização certificada sob o RBAC 145 responde tecnicamente pelo trabalho que executa.

Ela deve:

- possuir escopo autorizado;
- utilizar dados técnicos aplicáveis;
- dispor de pessoal, ferramentas e instalações adequados;
- inspecionar o artigo trabalhado;
- manter controle de qualidade;
- registrar o serviço;
- aprovar o retorno ao serviço somente quando o artigo estiver aeronavegável em relação ao trabalho realizado.

A liberação de manutenção não significa:

```text
aeronave perfeita em todos os aspectos
```

Ela significa, dentro do escopo e dos dados aplicáveis:

```text
trabalho executado e inspecionado
→ artigo aeronavegável quanto ao trabalho realizado
```

Se uma oficina executa serviço incorreto, podem coexistir:

- responsabilidade regulatória da organização;
- responsabilidade técnica de profissionais;
- responsabilidade contratual perante o operador;
- responsabilidade civil por dano;
- eventual atuação do seguro de responsabilidade da oficina;
- sub-rogação da seguradora do operador contra responsáveis.

## 6. Semântica financeira do seguro

### 6.1 Prêmio

O prêmio é o valor pago para contratar a garantia. Em operação comercial, o segurado ou estipulante normalmente é o explorador, proprietário, arrendatário ou pessoa definida na apólice — não o piloto empregado apenas por pilotar.

### 6.2 Franquia

A franquia é a parte do prejuízo que permanece com o segurado conforme contrato.

### 6.3 Indenização de casco

Pode financiar reparo, reposição ou perda total dentro do interesse segurado, valor de garantia, condições e exclusões.

### 6.4 Responsabilidade civil

Garante efeitos patrimoniais da imputação de responsabilidade e protege também o interesse de terceiros prejudicados nos termos legais e contratuais.

### 6.5 Manutenção programada

Desgaste normal, revisão, troca por vida limite ou obsolescência não se convertem automaticamente em dano acidental coberto.

### 6.6 Agravamento do risco

O segurado não deve agravar intencionalmente e de forma relevante o risco. Agravamentos relevantes devem ser comunicados. A recusa de indenização exige a análise jurídica e o nexo previsto na lei e na apólice.

### 6.7 Dolo e fraude

Provocação dolosa de sinistro e fraude na reclamação podem levar à perda da indenização, além de outras consequências.

### 6.8 Sub-rogação

Após pagar seguro de dano, a seguradora pode assumir direitos contra terceiro responsável.

A Lei nº 15.040/2024 impede, em regra, sub-rogação contra empregado quando o sinistro decorre de culpa não grave. Dolo, culpa grave, apólices específicas e outras relações exigem análise própria.

## 7. Fluxos financeiros possíveis

### Cenário A — erro não intencional do piloto empregado

```text
dano
→ operador aciona seguro
→ seguradora regula e paga dentro da cobertura
→ operador suporta franquia, parada e efeitos não cobertos
→ piloto pode sofrer medidas técnicas/trabalhistas proporcionais
→ regresso pessoal não é automático
```

### Cenário B — falha de manutenção contratada

```text
dano
→ operador continua responsável pela aeronavegabilidade
→ seguradora de casco pode pagar conforme apólice
→ seguradora pode buscar terceiro responsável
→ oficina e seu seguro de responsabilidade podem entrar no fluxo
→ contratos e nexo definem a distribuição final
```

### Cenário C — defeito de projeto ou fabricação

```text
dano
→ investigação identifica possível condição de projeto/produção
→ operador e seguradora preservam direitos
→ fabricante/projetista pode responder se o defeito e o nexo forem provados
```

### Cenário D — fraude ou agravamento intencional

```text
risco deliberadamente agravado ou sinistro provocado
→ possível perda de garantia
→ restituições e regresso
→ sanções regulatórias, civis e penais
```

### Cenário E — componente próximo da troca

```text
vida remanescente baixa
≠ peça sem valor
≠ direito automático a substituir pelo seguro
```

Para investigar conversão indevida de manutenção prevista em sinistro, é necessário separar:

\[
C_{\mathrm{dano\ novo}}
\quad\text{de}\quad
C_{\mathrm{desgaste\ preexistente}}
\quad\text{de}\quad
C_{\mathrm{manutenção\ já\ devida}}
\]

## 8. Régua finita de oito heurísticas

A régua é uma ferramenta autoral de **triagem auditável**, não um modelo validado para prever acidentes ou condenar pessoas.

Cada heurística recebe:

```yaml
score: 0 | 1 | 2 | 3 | 4 | null
evidence: 0.0 .. 1.0
weight: positivo
state: VERIFIED | PARTIAL | TOKEN_VAZIO | CONTRADICTION
source_refs: []
```

Escala comum:

| Pontuação | Interpretação |
|---:|---|
| 0 | conformidade documentada ou ausência de anomalia relevante |
| 1 | desvio pequeno ou lacuna documental limitada |
| 2 | combinação relevante que exige revisão |
| 3 | não conformidade séria ou padrão anômalo |
| 4 | gate crítico confirmado ou evidência direta de alto risco |
| `null` | não calculável sem inventar; `TOKEN_VAZIO` |

### H1 — Derivada direta de conformidade

Pergunta:

> Qual é o desvio atual em relação a cada limite aplicável?

Entradas:

- licença, habilitação e experiência recente;
- horas e pousos;
- jornada, repouso e fadiga;
- mínimos meteorológicos;
- vida limite;
- retorno ao serviço;
- SOP e MEL.

Forma genérica:

\[
D^+(x)=
\begin{cases}
\max(0,\frac{x-L}{s}), & \text{limite máximo}\\
\max(0,\frac{L-x}{s}), & \text{limite mínimo}
\end{cases}
\]

A fórmula somente pode ser usada quando \(L\), unidade, tolerância \(s\) e fonte normativa forem definidos.

### H2 — Inversa causal do dano

Parte do efeito e procura causas concorrentes:

\[
\text{dano no trem}
\leftarrow
\{
\text{carga lateral},
\text{razão de descida},
\text{vento},
\text{pista},
\text{falha material},
\text{manutenção},
\text{projeto}
\}
\]

Aplicar árvore de falhas, análise de barreiras e atualização Bayesiana quando houver dados.

A heurística deve preservar múltiplas causas até que evidências excluam alternativas.

### H3 — Antiderivada temporal de exposição

Acumula exposição ao longo do tempo:

\[
A(t)=
\sum_k r_k\Delta t_k
+
\sum_j q_j\Delta c_j
\]

onde \(r_k\) representa riscos por tempo e \(q_j\) riscos por ciclos/eventos.

Entradas:

- fadiga acumulada;
- sequência de jornadas;
- ciclos e pousos;
- defeitos diferidos;
- vida remanescente;
- repetição de hard landing;
- histórico de componentes;
- manutenção adiada.

A antiderivada impede analisar apenas o último pouso e ignorar a história.

### H4 — Reversa cronológica direta

Reconstrói a cadeia do dano para trás:

```text
dano
← toque
← aproximação
← despacho
← escala
← liberação de manutenção
← histórico do componente
← planejamento
```

Quanto mais quebrada, contraditória ou adulterada a cadeia, maior a prioridade de auditoria.

### H5 — Reversa indireta organizacional

Procura fatores que não aparecem no comando final:

- pressão por pontualidade;
- incentivo de conforto;
- política de go-around;
- treinamento;
- alocação de pilotos;
- aeroportos especiais;
- fadiga;
- metas financeiras;
- comunicação gerencial.

A heurística pergunta:

\[
\text{quem definiu o ambiente em que a decisão foi tomada?}
\]

### H6 — Inclusiva de responsabilidade em rede

Para cada ator \(a\):

\[
\rho_a =
C_a \times K_a \times D_a \times N_a
\]

onde:

- \(C_a\): controle efetivo;
- \(K_a\): conhecimento ou dever de conhecer;
- \(D_a\): dever jurídico/técnico;
- \(N_a\): nexo com o resultado.

A função não distribui culpa automaticamente. Ela prioriza solicitações de prova para:

- piloto;
- comandante;
- operador;
- despacho;
- manutenção;
- fabricante;
- aeroporto;
- controle;
- seguradora;
- certificadora.

### H7 — Logarítmica econômico-securitária

Valores financeiros possuem caudas longas. A transformação logarítmica reduz domínio sem apagar ordens de grandeza:

\[
L_E = \log(1+I)
-\log(1+F+D+U)
\]

onde:

- \(I\): indenização;
- \(F\): franquia;
- \(D\): custo de indisponibilidade;
- \(U\): custo não coberto.

Uma segunda variável pode observar manutenção potencialmente transferida:

\[
L_M =
\log(1+C_{\mathrm{manutenção\ prevista}})
-
\log(1+C_{\mathrm{operador\ após\ sinistro}})
\]

Nenhuma delas prova fraude. O resultado deve ser comparado com uma linha de base de aeronaves, checks e eventos equivalentes, preferencialmente por mediana e MAD robusto.

### H8 — Fractal/Ômega de recorrência multiescala

Procura o mesmo padrão em diferentes escalas:

1. componente;
2. aeronave;
3. frota;
4. piloto/tripulação;
5. aeroporto;
6. oficina;
7. gestor;
8. seguradora.

Um evento isolado pode ser ruído. Repetição entre níveis pode indicar estrutura:

\[
\Omega_F =
\sum_{\ell=1}^{8}
w_\ell\,P_\ell
\]

onde cada \(P_\ell\) precisa de denominador de exposição.

“Fractal” significa recorrência mensurável entre escalas; não constitui afirmação física ou causal por metáfora.

## 9. Cálculo da régua

Com oito pontuações \(h_i\in[0,4]\) e pesos \(w_i>0\):

\[
R =
100\frac{\sum_i w_i h_i}
{4\sum_i w_i}
\]

Cobertura de evidência:

\[
C =
100\frac{\sum_i w_i e_i}
{\sum_i w_i}
\]

onde \(e_i\in[0,1]\).

Para `TOKEN_VAZIO`, a ferramenta calcula intervalo:

\[
R_{\min}
=
100\frac{\sum_{\mathrm{conhecidos}}w_i h_i}
{4\sum_iw_i}
\]

\[
R_{\max}
=
100\frac{
\sum_{\mathrm{conhecidos}}w_i h_i
+
4\sum_{\mathrm{desconhecidos}}w_i
}
{4\sum_iw_i}
\]

Assim, ausência de dado não vira falso zero.

Faixas de triagem:

| R | Saída |
|---:|---|
| 0–19 | monitoramento |
| 20–39 | revisão |
| 40–59 | auditoria direcionada |
| 60–79 | auditoria urgente |
| 80–100 | crítico |

Cobertura inferior a 60% produz:

```text
INSUFFICIENT_EVIDENCE
```

## 10. Hard gates

Qualquer hard gate prevalece sobre a soma:

- limite de voo/jornada/pousos confirmado como excedido;
- vida limite de componente excedida;
- retorno ao serviço ausente;
- continuidade de aproximação quando gate obrigatório exigia arremetida;
- registro falso ou adulterado;
- evidência de agravamento intencional relevante do risco.

Saída:

```text
BLOCKED_REVIEW_REQUIRED
```

Isso não equivale a culpa. Significa que a operação ou o claim não pode ser promovido sem revisão competente.

## 11. Dados mínimos por caso

```yaml
tripulacao:
  licença:
  habilitação:
  experiência_recente:
  horas_no_tipo:
  horas_jornada:
  pousos_jornada:
  repouso:
  reporte_fadiga:

operacao:
  SOP:
  aproximação_estabilizada:
  velocidade:
  razão_descida:
  toque:
  alinhamento:
  vento:
  pista:
  go_around:

aeronave:
  matrícula:
  tipo:
  horas:
  ciclos:
  componentes_vida_limitada:
  defeitos_diferidos:
  liberação_manutenção:

manutencao:
  organização:
  certificado:
  escopo:
  dados_técnicos:
  inspeção:
  retorno_serviço:
  histórico:

seguro:
  segurado:
  coberturas:
  prêmio:
  franquia:
  valor_segurado:
  indenização:
  exclusões:
  sub_rogação:

economia:
  reparo:
  parada:
  manutenção_programada:
  custo_potencialmente_evitado:
  salvado:

proveniencia:
  diário_bordo:
  CIV:
  escala:
  FDM_DFDR:
  METAR_SPECI:
  relatório_manutenção:
  regulação_sinistro:
```

## 12. Ciclos evolutivos de pesquisa

### Ciclo 1 — contexto

Definir operação, norma, aeronave, piloto, aeroporto, evento e período.

### Ciclo 2 — atomização

Separar cada afirmação em claim verificável.

### Ciclo 3 — proveniência

Ligar claim a documento, registro, hash, data e responsável.

### Ciclo 4 — cálculo direto

Aplicar limites, vida remanescente, exposição e custos.

### Ciclo 5 — cálculo inverso

Partir do dano e reconstruir causas alternativas.

### Ciclo 6 — antiderivada

Somar história de fadiga, ciclos, eventos e decisões.

### Ciclo 7 — rede inclusiva

Mapear controle, conhecimento, dever e nexo por ator.

### Ciclo 8 — fechamento Ômega provisório

Emitir:

```text
VERIFIED
PARTIAL
TOKEN_VAZIO
CONTRADICTION
BLOCKED
NEXT_FALSIFIER
```

Nenhum fechamento é definitivo se surgirem novos dados.

## 13. Implementação no repositório

- `scripts/seguranca_aerea/audit_ruler_8h.py`
- `data/seguranca_aerea/audit_case_template.json`
- `tests/seguranca_aerea/test_audit_ruler_8h.py`

Execução:

```bash
python3 scripts/seguranca_aerea/audit_ruler_8h.py \
  data/seguranca_aerea/audit_case_template.json \
  -o reports/seguranca_aerea/audit_result.json
```

Testes:

```bash
python3 tests/seguranca_aerea/test_audit_ruler_8h.py
```

O script:

- não usa dependências externas;
- valida oito heurísticas;
- preserva `TOKEN_VAZIO`;
- calcula intervalo de risco;
- calcula cobertura de evidência;
- aplica hard gates;
- gera hash SHA-256 canônico do input;
- nunca autoriza claim causal.

## 14. Base normativa e técnica consultada

- ANAC — RBAC 61 e IS 61-001: CIV Digital e registros de experiência;
- Lei nº 13.475/2017: limites de voo, pousos, jornada e repouso;
- ANAC — RBAC 117 e IS 117-004: responsabilidade compartilhada na fadiga;
- ANAC — RBAC 121, seções 121.363 e 121.367;
- ANAC — IS 120-016B: PMAC e responsabilidade da empresa;
- ANAC — RBAC 145: organização de manutenção, inspeção e retorno ao serviço;
- ANAC — IS 119-008A: FDM, hard landing e vida útil de componentes;
- Código Brasileiro de Aeronáutica, especialmente arts. 70, 124, 268 e 281;
- Lei nº 15.040/2024: contrato de seguro, agravamento, fraude, regulação e sub-rogação;
- SUSEP — seguro de responsabilidade civil e RETA.

## 15. Síntese

\[
\boxed{
\text{registro do piloto}
\oplus
\text{escala da companhia}
\oplus
\text{aeronavegabilidade}
\oplus
\text{execução da manutenção}
\oplus
\text{seguro}
\oplus
\text{nexo}
}
\]

A responsabilidade não acompanha apenas quem segurava o manche. Ela acompanha:

\[
\boxed{
\text{controle}
+
\text{conhecimento}
+
\text{dever}
+
\text{capacidade de prevenção}
+
\text{nexo causal}
}
\]

A régua de oito heurísticas serve para descobrir **onde calcular, quais dados faltam e qual gate impede uma conclusão**. Ela não serve para fabricar culpa.
