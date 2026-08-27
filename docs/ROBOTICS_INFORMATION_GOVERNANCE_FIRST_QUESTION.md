# Robotics Information Governance — First Question Gate V1

**Estado:** `PROPOSED_AUDITABLE`
**Escopo:** LGPD + sistemas automatizados + responsabilidade informacional + conscientização do titular
**Regra epistemológica:** `fonte -> claim -> estado -> evidência -> ação`

## 1. Definição operacional de Robotics

Neste repositório, **Robotics** não é usado como categoria jurídica positivada. É um rótulo operacional para **sistemas robóticos ou automatizados que coletam, inferem, classificam, recomendam, ranqueiam, decidem, executam ou compartilham informação sobre pessoas**.

Inclui, quando houver tratamento de dados pessoais ou efeito relevante sobre pessoas:

- IA generativa e preditiva;
- sistemas de recomendação e ranking;
- perfilamento e scoring;
- agentes, bots e RPA;
- motores de decisão automatizada;
- sensores, biometria e dispositivos robóticos conectados;
- publicidade comportamental e inferências;
- sistemas de moderação, priorização, busca e autocomplete;
- integrações entre plataformas, data brokers e provedores de infraestrutura.

> `Robotics` = categoria de governança deste projeto; não substituir os conceitos legais de controlador, operador, encarregado, titular, tratamento ou decisão automatizada.

## 2. Primeira Pergunta — proposta de governança

A primeira interação material de um serviço que trate dados pessoais por automação deve tornar inteligível, antes de exigir escolhas complexas, a pergunta fundamental:

> **“Este serviço usa dados pessoais e/ou sistemas automatizados para coletar, inferir, classificar, recomendar, decidir ou compartilhar informações sobre você? Veja o que acontece, por quê, com quem, por quanto tempo e quais controles você possui.”**

Essa abertura é chamada de **First Question Gate (FQG)**.

O FQG é uma **proposta de governança e design auditável**. Não é apresentado como obrigação textual geral já existente na LGPD.

### 2.1 O que o FQG não pode fazer

- não transformar informação em consentimento forçado;
- não presumir que consentimento é a única base legal possível;
- não esconder finalidade, compartilhamento ou retenção atrás de múltiplas telas;
- não usar “aceitar tudo” como condição visual dominante;
- não confundir simples ciência do titular com concordância jurídica;
- não impedir o exercício de direitos quando o usuário rejeita tratamento opcional.

## 3. Responsabilidade das empresas que trabalham com informação

A responsabilidade deve seguir **função real + poder decisório + evidência**, e não apenas o tamanho ou a marca da empresa.

```text
Responsabilidade_informacional
  = papel_no_tratamento
  + poder_de_decisão
  + finalidade
  + capacidade_de_prevenir
  + impacto
  + dever_de_transparência
  + resposta_a_incidentes_e_direitos
```

### 3.1 Agentes

| Papel | Pergunta de auditoria |
|---|---|
| Controlador | Quem decide finalidades e elementos essenciais do tratamento? |
| Operador | Quem trata dados em nome de outro agente e sob instruções? |
| Controladoria conjunta | Há decisões convergentes sobre finalidade/meios que exigem análise conjunta? |
| Fornecedor de modelo/IA | O fornecedor apenas oferece tecnologia ou também determina uso, finalidade, retenção, logging ou inferência? |
| Plataforma | Que decisões próprias toma sobre ranking, recomendação, publicidade, segurança, moderação e dados derivados? |
| Data broker/intermediário | Qual a origem, base jurídica, finalidade, compartilhamento e possibilidade de oposição/correção? |
| Infraestrutura | Há mera hospedagem/processamento ou decisões adicionais sobre dados? |

O papel deve ser determinado caso a caso. Nome comercial, contrato ou autoqualificação não encerram a análise.

## 4. Matriz 7 × 7 de conscientização e governança

Cada camada possui sete perguntas mínimas. `TOKEN_VAZIO` é resposta válida quando a evidência ainda não existe.

### L1 — Identidade e autoridade

1. Quem é o controlador?
2. Quem é o operador?
3. Há controladoria conjunta?
4. Quem é o encarregado/canal de contato quando aplicável?
5. Quem pode alterar finalidade ou meios essenciais?
6. Quem responde aos direitos do titular?
7. Qual entidade jurídica recebe receita ou benefício do tratamento?

### L2 — Coleta, origem e minimização

1. Quais dados são coletados diretamente?
2. Quais dados vêm de terceiros?
3. Quais dados são inferidos?
4. Quais são sensíveis?
5. O que é estritamente necessário?
6. O que é opcional?
7. Qual dado pode ser eliminado sem romper a finalidade legítima?

### L3 — Finalidade, necessidade e base jurídica

1. Para que cada dado é tratado?
2. Qual base jurídica sustenta cada finalidade?
3. A finalidade é específica e informada?
4. Existe reutilização incompatível?
5. A necessidade foi demonstrada?
6. Existe alternativa menos intrusiva?
7. Mudança de finalidade dispara nova análise e nova informação ao titular?

### L4 — Automação, inferência e Robotics

1. Há decisão, ranking, recomendação ou classificação automatizada?
2. Quais entradas influenciam o resultado?
3. Há dados derivados ou inferidos?
4. O resultado afeta interesse relevante da pessoa?
5. Existe revisão, contestação ou intervenção adequada?
6. Critérios e procedimentos podem ser explicados de modo claro e adequado?
7. Há teste de vieses, erro, segurança e impacto diferencial?

### L5 — Compartilhamento, cadeia e transferências

1. Com quem os dados são compartilhados?
2. Para qual finalidade?
3. Há suboperadores?
4. Há transferência internacional?
5. Existe cadeia de proveniência dos dados?
6. Revogação, oposição, correção ou eliminação propagam-se quando juridicamente aplicáveis?
7. Existe recibo/auditoria de cada transmissão material?

### L6 — Direitos e controle do titular

1. Como obter confirmação e acesso?
2. Como corrigir dados?
3. Como pedir anonimização, bloqueio ou eliminação quando cabível?
4. Como obter informação sobre compartilhamento?
5. Como revogar consentimento quando esta for a base?
6. Como se opor ou contestar tratamento nos casos previstos em lei?
7. Como solicitar revisão/informações sobre decisão automatizada nos termos aplicáveis?

### L7 — Evidência, segurança e accountability

1. Há registro de operações e decisões relevantes?
2. Há política de retenção e descarte?
3. Há controles de segurança compatíveis com o risco?
4. Há registro e resposta a incidentes?
5. Há avaliação de impacto quando necessária ou recomendável?
6. Há trilha de auditoria que diferencia claim, hipótese e prova?
7. Há mecanismo de correção e não repetição após falha?

## 5. Dinâmica semântica e correlações

O framework trata relações em camadas, sem confundir correlação com causalidade.

### 5.1 Tipos de relação

| Relação | Função |
|---|---|
| `DIRECT` | aumento em A acompanha aumento/efeito em B |
| `INVERSE` | aumento em A acompanha redução/efeito oposto em B |
| `EXCLUSIVE` | estados não podem coexistir sob o mesmo contrato |
| `DERIVATIVE` | mede variação local/temporal de uma propriedade |
| `ANTIDERIVATIVE` | mede acumulação ao longo do tempo/ciclo |
| `LOGARITHMIC` | comprime escala para comparação sem tratar volume como prova |
| `ANOMALY_PARADOX` | marca conflito, exceção ou resultado incompatível com o modelo esperado |

### 5.2 Variáveis auditáveis

```text
T(t) = transparência observável
U(t) = controle efetivo do titular
A(t) = intensidade de automação
D(t) = volume/variedade de dados pessoais
S(t) = compartilhamento
R(t) = risco residual
E(t) = evidência verificável
O(t) = opacidade observável
```

As expressões abaixo são **transformações analíticas**, não provas jurídicas automáticas:

```text
Derivada direta:        dT/dt, dR/dt, dU/dA
Derivada inversa:       dU/dO ou análise efeito -> causa com cadeia de evidência
Antiderivada:           ∫ R(t) dt  ≈ soma ponderada de exposição ao risco no ciclo
Correlação cruzada:     ∂²R/(∂A∂D)
Exclusividade:          claim_provado XOR TOKEN_VAZIO  (para o mesmo claim no mesmo estado)
Compressão logarítmica: L(E) = log(1 + n_evidências_independentes)
```

`log(1+n)` serve apenas para evitar que quantidade bruta de documentos domine o índice. Evidências repetidas ou dependentes devem receber peso menor.

## 6. Rapport entre áreas

O Robotics Information Governance conecta pelo menos estas áreas:

```text
LGPD
↕
Direito do consumidor ↔ segurança da informação ↔ governança de IA
↕                         ↕                         ↕
concorrência          interoperabilidade        direitos humanos
↕                         ↕                         ↕
auditabilidade       proveniência              design de interface
```

### 6.1 Regra de conexão

Uma ponte entre áreas só pode ser promovida de `HIPOTESE` para `SUSTENTADA` quando possuir:

- fonte competente;
- definição comum dos termos;
- nexo explícito;
- evidência verificável;
- hipótese alternativa considerada;
- limite de aplicação documentado.

## 7. Anomalias e paradoxos que devem ser testados

| ID | Anomalia/paradoxo | Teste mínimo |
|---|---|---|
| AP-01 | “transparência” extensa porém incompreensível | leitura em camadas + linguagem clara + localização do dado essencial |
| AP-02 | consentimento abundante mas sem escolha real | verificar granularidade, consequência da recusa e dark patterns |
| AP-03 | dado “anônimo” recombinável com identidade | testar risco razoável de reidentificação/contextualização |
| AP-04 | operador nominal com poder decisório de controlador | mapear decisões efetivas, não apenas contrato |
| AP-05 | exclusão local sem propagação a terceiros | verificar cadeia de destinatários e obrigações aplicáveis |
| AP-06 | explicação de IA sem critérios materiais | comparar explicação exibida com variáveis/procedimentos realmente utilizados quando acessíveis |
| AP-07 | minimização declarada com coleta/inferência crescente | inventário temporal + finalidade + necessidade por campo |
| AP-08 | segurança técnica forte com governança fraca | testar licitude, finalidade, direitos e accountability separadamente |
| AP-09 | personalização benéfica que cria dependência/opacidade | medir controle, opção real, reversibilidade e impacto |
| AP-10 | concentração de mercado tratada como prova de cartel | separar estrutura de mercado, poder, conduta coordenada e evidência jurídica |

## 8. Monopólio, oligopólio, cartel e alegações graves

Este repositório não deve promover automaticamente termos como `monopólio`, `cartel`, `conluio`, `máfia` ou equivalentes a fatos provados.

Estados permitidos:

```text
OBSERVACAO -> HIPOTESE -> EVIDENCIA_PARCIAL -> SUSTENTADA | REFUTADA | TOKEN_VAZIO
```

Para concentração econômica, exigir pelo menos:

- definição de mercado relevante;
- participação e poder de mercado;
- barreiras à entrada e efeitos de rede;
- possibilidade de substituição;
- conduta observada;
- fonte econômica/regulatória.

Para cartel/conluio, concentração ou comportamento paralelo isolado não bastam; é necessária evidência adequada do fato alegado conforme o contexto jurídico aplicável.

## 9. First Question Gate — contrato de interface

A interface mínima deve exibir em uma primeira camada curta:

```text
[1] O que é coletado/inferido
[2] Por que é usado
[3] Se há automação relevante
[4] Com quem é compartilhado
[5] Quanto tempo é mantido ou qual critério define retenção
[6] Quais controles/direitos existem
[7] Onde obter detalhes, contestar e falar com o responsável
```

Depois, camadas progressivas podem mostrar detalhes técnicos e jurídicos.

### 9.1 Estados do gate

```text
DISCLOSED
ACKNOWLEDGED
OPTIONAL_CONSENT_GRANTED
OPTIONAL_CONSENT_DENIED
CONSENT_NOT_APPLICABLE
RIGHT_EXERCISE_REQUESTED
TOKEN_VAZIO
```

`ACKNOWLEDGED != CONSENT_GRANTED`.

## 10. Responsabilidade por ciclo de vida

```text
conceber -> coletar -> inferir -> usar -> decidir -> compartilhar -> reter -> eliminar -> auditar
```

Cada transição deve registrar:

```text
ator + papel + finalidade + base + dados + automação + destinatário + risco + evidência + direito aplicável + timestamp
```

## 11. Critério de maturidade

| Nível | Estado |
|---|---|
| M0 | não mapeado |
| M1 | inventário de dados |
| M2 | finalidade/base/papéis mapeados |
| M3 | direitos e FQG operacionais |
| M4 | automação/inferências explicadas e auditáveis |
| M5 | cadeia de compartilhamento/proveniência verificável |
| M6 | métricas, anomalias e correções com evidência |
| M7 | auditoria independente + não regressão + governança contínua |

## 12. Fontes primárias e oficiais verificadas

Consulta de referência em **2026-08-26**:

- Lei nº 13.709/2018 (LGPD), texto compilado — Planalto;
- ANPD — Titular de Dados;
- ANPD — Direito dos Titulares;
- ANPD — Perguntas Frequentes, direitos previstos nos arts. 18 e 20.

A LGPD e a orientação da ANPD sustentam direitos de informação, acesso, correção, eliminação/bloqueio em hipóteses aplicáveis, informação sobre compartilhamento, revogação do consentimento e direitos ligados a decisões automatizadas. O FQG é uma extensão de design/governança proposta para tornar esses deveres e direitos mais visíveis desde o início.

## 13. Gates de evidência

```text
G1 legal_text_verified          = PASS
G2 anpd_guidance_verified       = PASS
G3 FQG_required_by_law          = TOKEN_VAZIO
G4 robotics_legal_term          = TOKEN_VAZIO
G5 implementation_in_product    = TOKEN_VAZIO
G6 independent_usability_test   = TOKEN_VAZIO
G7 market_power_claims          = TOKEN_VAZIO
```

## 14. Falsificadores

O framework deve ser revisto se:

- o FQG reduzir compreensão ou induzir falsa sensação de consentimento;
- a matriz 7×7 não mapear tratamentos materiais;
- métricas não tiverem definição reproduzível;
- “Robotics” causar confusão com conceitos legais;
- testes mostrarem que a interface cria dark patterns;
- nova legislação/regulação tornar parte do contrato incorreta ou insuficiente.

---

**F_ok:** responsabilidade informacional, automação, direitos e conscientização foram unidos em uma camada auditável.  
**F_gap:** obrigação legal textual de “primeira pergunta”, implementação real e alegações de poder de mercado permanecem separados como `TOKEN_VAZIO` até prova.  
**F_next:** validar o registro JSON, executar testes de estrutura e abrir revisão jurídica/técnica por claim.