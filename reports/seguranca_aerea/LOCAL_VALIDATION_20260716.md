# Validação Local — Régua de Oito Heurísticas

**Data:** 2026-07-16  
**Escopo:** cópia byte a byte dos arquivos criados na branch do PR #27  
**Limite:** validação local não substitui GitHub Actions, revisão jurídica, perícia ou validação científica externa.

## Hashes SHA-256

```text
scripts/seguranca_aerea/audit_ruler_8h.py
2ddd531904ed85bff67e2e231ed9b6119a67b41422e6616ed53ad9ab35a77446

data/seguranca_aerea/audit_case_template.json
5153c72f5cf5a35f90e3f4bfc8f62750d9f78514985847dea511ef121bbf4131

tests/seguranca_aerea/test_audit_ruler_8h.py
719d4611387b00368d42637bbad04f9097f2f4cce325327d66de09089a739183
```

## Testes executados

```bash
python3 tests/seguranca_aerea/test_audit_ruler_8h.py
```

Resultado:

```text
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

Casos cobertos:

1. oito dimensões desconhecidas preservam intervalo `0..100` e retornam `INSUFFICIENT_EVIDENCE`;
2. oito dimensões com score 2 e evidência completa retornam 50 e `TARGETED_AUDIT`;
3. hard gate de vida limite excedida prevalece e retorna `BLOCKED_REVIEW_REQUIRED`;
4. score desconhecido não aceita evidência diferente de zero.

## Execução do template

```bash
python3 scripts/seguranca_aerea/audit_ruler_8h.py \
  data/seguranca_aerea/audit_case_template.json
```

Estado esperado e observado:

```json
{
  "decision": "INSUFFICIENT_EVIDENCE",
  "causal_claim_allowed": false,
  "risk": {
    "lower_bound_0_100": 0.0,
    "upper_bound_0_100": 100.0,
    "evidence_coverage_0_100": 0.0
  }
}
```

A saída demonstra a invariante:

```text
TOKEN_VAZIO não é convertido em zero nem em culpa.
```
