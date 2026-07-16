# Segurança Aérea — Índice Canônico

Esta pasta reúne a camada técnico-jurídica sobre segurança do passageiro, pouso, horas de tripulação, aeronavegabilidade, manutenção, seguro e responsabilidade.

## Ordem de leitura

1. [Segurança do passageiro, pouso e responsabilidade](SEGURANCA_PASSAGEIRO_POUSO_RESPONSABILIDADE.md)
2. [Horas, manutenção, seguro e régua de oito heurísticas](HORAS_MANUTENCAO_SEGURO_REGUA_8_HEURISTICAS.md)
3. [Claims ledger](CLAIMS_LEDGER_POUSO_SEGURO.md)
4. [Template de caso](../../data/seguranca_aerea/audit_case_template.json)
5. [Régua executável](../../scripts/seguranca_aerea/audit_ruler_8h.py)
6. [Testes](../../tests/seguranca_aerea/test_audit_ruler_8h.py)

## Invariantes

```text
registro do piloto ≠ gestão integral da escala
manutenção contratada ≠ transferência integral da aeronavegabilidade
peça próxima do limite ≠ peça automaticamente insegura
peça substituída após sinistro ≠ fraude automaticamente
seguro pago ≠ culpa transferida
score alto ≠ causalidade provada
TOKEN_VAZIO ≠ zero
```

## Fluxo de pesquisa

```text
fonte
→ claim atômico
→ estado epistemológico
→ dado operacional
→ heurística
→ intervalo de risco
→ hard gate
→ próxima obrigação de prova
```

## Execução

```bash
python3 scripts/seguranca_aerea/audit_ruler_8h.py \
  data/seguranca_aerea/audit_case_template.json \
  -o reports/seguranca_aerea/audit_result.json
```

## Teste

```bash
python3 tests/seguranca_aerea/test_audit_ruler_8h.py
```

A ferramenta é somente de triagem. Ela mantém `causal_claim_allowed=false` e não substitui investigação SIPAER, perícia, ANAC, seguradora, manutenção certificada ou decisão judicial.
