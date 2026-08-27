# Índice — Robotics Information Governance V1

**Estado:** `PROPOSED_AUDITABLE`

## Rota canônica

```text
fonte oficial
-> papel jurídico
-> tratamento
-> automação/inferência
-> informação ao titular
-> direito/controle
-> evidência
-> anomalia/falsificador
-> ação verificável
```

## Artefatos

| Artefato | Função |
|---|---|
| [`../docs/ROBOTICS_INFORMATION_GOVERNANCE_FIRST_QUESTION.md`](../docs/ROBOTICS_INFORMATION_GOVERNANCE_FIRST_QUESTION.md) | especificação humana, jurídica e semântica |
| [`../data/robotics_information_governance_v1.json`](../data/robotics_information_governance_v1.json) | contrato legível por máquina |
| [`../tests/test_robotics_information_governance.py`](../tests/test_robotics_information_governance.py) | invariantes e não regressão estrutural |
| [`indice_derivadas.md`](indice_derivadas.md) | catálogo histórico de derivadas/antiderivadas do repositório |
| [`../docs/supra_legal/CADEIA_CUSTODIA_BIGTECH_AUDIOVISUAL.md`](../docs/supra_legal/CADEIA_CUSTODIA_BIGTECH_AUDIOVISUAL.md) | precedente interno para responsabilidade algorítmica e fronteiras de claim |

## Índice mínimo de privacidade e governança

### P0 — Primeiro contato

- existe tratamento de dados pessoais?
- existe inferência ou automação relevante?
- a pessoa consegue saber o que ocorre sem ler documentação extensa?
- `ACKNOWLEDGED != CONSENT` está preservado?

### P1 — Quem decide

- controlador;
- operador;
- controladoria conjunta, quando aplicável;
- fornecedor/modelo/plataforma/infraestrutura conforme função real;
- encarregado/canal de contato quando aplicável.

### P2 — O que entra

- coleta direta;
- terceiros;
- inferências;
- dados sensíveis;
- necessidade e minimização.

### P3 — Por que entra

- finalidade;
- base jurídica;
- compatibilidade de reutilização;
- alternativa menos intrusiva.

### P4 — O que a automação faz

- ranking;
- recomendação;
- perfilamento;
- scoring;
- decisão automatizada;
- geração/inferência;
- moderação/priorização.

### P5 — Para onde vai

- compartilhamento;
- suboperadores;
- transferências internacionais;
- proveniência;
- propagação de correção/eliminação/oposição/revogação quando aplicável.

### P6 — O que a pessoa controla

- informação;
- confirmação/acesso;
- correção;
- anonimização/bloqueio/eliminação quando cabível;
- compartilhamento;
- revogação do consentimento quando aplicável;
- oposição/contestação;
- direitos relativos a decisões automatizadas.

### P7 — Como provar

- logs;
- recibos;
- retenção;
- segurança;
- incidentes;
- impacto;
- auditoria e não regressão.

## Matriz de relações

| Código | Relação | Pergunta |
|---|---|---|
| R1 | `DIRECT` | A e B variam na mesma direção observável? |
| R2 | `INVERSE` | A aumenta enquanto B diminui? |
| R3 | `EXCLUSIVE` | dois estados são incompatíveis no mesmo claim/contexto? |
| R4 | `DERIVATIVE` | qual a taxa de mudança? |
| R5 | `ANTIDERIVATIVE` | qual o efeito acumulado? |
| R6 | `LOGARITHMIC` | o volume precisa ser comprimido para evitar falsa dominância? |
| R7 | `ANOMALY_PARADOX` | a observação viola o modelo esperado ou revela exceção? |

## Topologia de rapport

```text
privacidade
├─ proteção de dados
├─ consumidor
├─ segurança da informação
├─ governança de IA
├─ concorrência
├─ direitos humanos
└─ design/interface
```

Pontes adicionais:

```text
proveniência <-> accountability
explicabilidade <-> contestação
minimização <-> segurança
interoperabilidade <-> portabilidade
concentração <-> poder de mercado
personalização <-> perfilamento
retenção <-> risco acumulado
```

## Anomalias prioritárias

1. transparência longa, mas incompreensível;
2. consentimento sem escolha real;
3. anonimização com risco de reidentificação;
4. operador nominal com poder material de controlador;
5. exclusão sem propagação na cadeia;
6. explicação algorítmica sem critérios materiais;
7. minimização declarada com coleta crescente;
8. segurança forte com licitude/governança fracas;
9. personalização útil com opacidade/dependência;
10. concentração tratada como prova automática de cartel.

## Estados epistemológicos

```text
OBSERVACAO
-> HIPOTESE
-> EVIDENCIA_PARCIAL
-> SUSTENTADA | REFUTADA | TOKEN_VAZIO
```

Nenhum atalho sem recibo/fonte.

## Transformações analíticas

As transformações matemáticas são instrumentos de análise, **não conclusões jurídicas automáticas**.

```text
dT/dt                 # mudança de transparência
∫R(t)dt                # risco acumulado
∂²R/(∂A∂D)            # interação automação-dados
log(1+n_evidências)    # compressão de volume documental
PROVED XOR TOKEN_VAZIO # exclusividade epistemológica no mesmo claim/estado
```

## Fontes oficiais de base

- Lei nº 13.709/2018 — LGPD, texto compilado, Planalto;
- ANPD — Titular de Dados;
- ANPD — Direito dos Titulares;
- ANPD — Perguntas Frequentes, inclusive direitos dos arts. 18 e 20.

**Data de verificação deste índice:** 2026-08-26.

---

**F_ok:** navegação semântica compacta criada.  
**F_gap:** validação jurídica independente e teste de usabilidade do First Question Gate.  
**F_next:** rodar testes, revisar fontes por claim e validar a interface em cenário real.
