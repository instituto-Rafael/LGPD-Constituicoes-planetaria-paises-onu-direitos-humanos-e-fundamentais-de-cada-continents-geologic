# Manifesto — Impressão, Materiais, Risco e Custódia

**Status:** `MANIFESTO / RESEARCH / PUBLIC-INTEREST / CLAIM-GATED`

Este diretório é o **seed integral de README** para um repositório independente dedicado à relação entre materiais de impressão, segurança química, trabalho especializado, privacidade e cadeia de custódia digital.

> Tintas, toners e processos de impressão podem envolver perigos químicos e particulados, mas risco e gravidade são específicos de formulação, dose, via e contexto. Não há claim genérico de que todo toner ou toda tinta seja tóxico ou letal.

## Fronteiras

- **Toxicologia/SST:** SDS/FDS, NR-26, higiene ocupacional, toxicologia e evidência de exposição.
- **LGPD:** somente quando existirem dados pessoais; saúde é dado pessoal sensível.
- **BLAKE3/RMR:** integridade, proveniência e reprodutibilidade do artefato; nunca substituem análise química, médica ou jurídica.
- **Publicação:** evidência pública mínima; bruto sensível protegido; hashes e manifests quando apropriado.

Documento canônico: `MANIFESTO_IMPRESSAO_MATERIAIS_RISCO_CUSTODIA_V1.md`.

## Estrutura sugerida do repositório independente

```text
README.md
LICENSE
MANIFESTO.md
docs/
  SOURCES.md
  CLAIM_GATES.md
  LGPD_BOUNDARY.md
schemas/
  custody-manifest.schema.json
evidence/
  README.md
```

## Estado

`legal_compliance_claim=false`  
`toxicology_case_claim=false`  
`claim_allowed=false` até fonte específica + contexto + evidência.
