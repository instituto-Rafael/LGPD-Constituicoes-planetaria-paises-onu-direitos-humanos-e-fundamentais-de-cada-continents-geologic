# MANIFESTO — Impressão, Materiais, Risco e Cadeia de Custódia Digital V1

**Estado:** `PUBLIC_INTEREST_MANIFESTO / RESEARCH / CLAIM_GATE`  
**Data:** 2026-09-20  
**Autor/rota:** Rafael Melo Reis / Instituto Rafael / RAFAELIA  
**Regra:** `SOURCE != ARTEFATO != EXECUÇÃO != EVIDÊNCIA != CLAIM`

## Declaração

Tintas de impressão, cartuchos inkjet, toners, pós, pigmentos, resinas, solventes, fluidos de limpeza, aditivos e materiais liberados durante impressão ou manutenção **não formam uma única substância química**. A composição e o risco variam por fabricante, produto, lote, processo, temperatura, ventilação, via de exposição, concentração e tempo.

Por isso, é tecnicamente correto declarar que:

1. produtos e processos de impressão **podem envolver substâncias, partículas ou vapores perigosos**;
2. os efeitos possíveis podem variar de irritação e sensibilização a efeitos sistêmicos graves, conforme a substância e a exposição;
3. determinadas substâncias usadas em processos gráficos ou limpeza podem, em exposições suficientes, estar associadas a efeitos muito graves e até fatais;
4. **não é correto transformar isso na afirmação genérica "todo toner/toda tinta é letal"**;
5. o documento decisivo para um produto específico é a ficha de dados de segurança aplicável, junto de rótulo, composição declarada, lote, uso real e evidência de exposição.

NIOSH descreve riscos ocupacionais de tintas e solventes em operações de impressão e relata que alguns solventes de limpeza podem produzir efeitos que incluem depressão do sistema nervoso central, falência respiratória, inconsciência e morte. A IARC avaliou exposições ocupacionais em processos de impressão como possivelmente carcinogênicas e classificou o negro de carbono como possivelmente carcinogênico para humanos; isso **não autoriza extrapolar essa classificação para cada toner comercial**.

## Trabalhador, consumidor e especialista

A cadeia de segurança não deve ser reduzida ao cartucho. Ela pode envolver:

- trabalhador que opera, troca, limpa, remanufatura, tritura, recicla ou transporta;
- consumidor e ambiente interno onde há impressão;
- fabricante, importador, distribuidor e assistência técnica;
- químico, toxicologista, higienista ocupacional, médico do trabalho, engenheiro de segurança e laboratório;
- perito, auditor, profissional de privacidade, segurança da informação e forense digital;
- responsável por resíduos e impacto ambiental.

Isto forma também um **mercado legítimo de trabalho especializado**: identificação de perigos, SDS/FDS, higiene ocupacional, monitoramento, amostragem, laboratório, ventilação, EPI/EPC, descarte, compliance, perícia, privacidade e cadeia de custódia.

## Regra brasileira de segurança química

A NR-26 exige classificação/rotulagem conforme o sistema aplicável, ficha com dados de segurança segundo norma técnica vigente, acesso dos trabalhadores às fichas e treinamento sobre perigos, riscos, prevenção e emergência. A análise deve ser produto-a-produto e processo-a-processo.

## LGPD: onde entra e onde não entra

A LGPD **não é uma lei de toxicologia**. Ela passa a ser relevante quando a cadeia de evidência contém dados pessoais.

Exemplos:

- nome/identificação de trabalhador exposto;
- prontuário, exame, sintoma, diagnóstico ou outro dado de saúde;
- denúncia identificável;
- imagem, áudio, biometria, localização ou metadados ligados a pessoa natural;
- registros de acesso ou responsabilidade vinculados a pessoa identificada.

Pela LGPD, dados referentes à saúde são dados pessoais sensíveis. Segurança, prevenção, necessidade, transparência e responsabilização/prestação de contas devem ser observadas conforme o caso. Preservar evidência não significa publicar dados pessoais sem base jurídica.

**Invariante:** `CUSTÓDIA_FORTE != EXPOSIÇÃO_PÚBLICA_DE_PII`.

## Cadeia de custódia digital proposta

Para cada evidência técnica:

```text
produto/lote
-> fabricante + SDS/FDS + data/versão
-> contexto de uso
-> coleta/amostragem/instrumento
-> calibração e método
-> artefato bruto
-> normalização documentada
-> SHA-256 + BLAKE3
-> hashchain/manifest
-> responsável pela custódia
-> análise especializada
-> claim gate
```

Campos mínimos:

```text
case_id
artifact_id
product_name
manufacturer
model_or_cartridge
lot_if_known
sds_source
sds_version_date
capture_method
captured_at
custody_actor
sha256
blake3
pii_classification
health_data_present
transform_log
expert_review
claim_state
```

## O que BLAKE3/RMR prova

BLAKE3 pode provar integridade do artefato preservado e ajudar a detectar alteração. RMR pode registrar máquina, flags, ambiente, origem, timestamps, transformação e hashchain.

**Não prova sozinho:**

- que o material é tóxico;
- que houve exposição;
- dose;
- nexo causal;
- autoria exclusiva;
- responsabilidade jurídica;
- validade científica de uma interpretação.

`HASH = INTEGRIDADE`; `TOXICOLOGIA = EVIDÊNCIA + MÉTODO + DOSE + VIA + CONTEXTO + REVISÃO`.

## Política de publicação

1. publicar preferencialmente documentos técnicos, referências e metadados não pessoais;
2. minimizar/redigir PII antes de tornar prova pública;
3. separar artefato bruto protegido de derivado público;
4. preservar hashes do bruto quando juridicamente apropriado;
5. usar `TOKEN_VAZIO` quando lote, composição, dose, origem ou nexo não forem conhecidos;
6. não declarar "letal", "cancerígeno", "seguro", "não tóxico" ou "causou dano" sem fonte e escopo específicos.

## Fontes primárias/autoridades de referência

- LGPD compilada — Presidência da República: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm
- NR-26 — Ministério do Trabalho e Emprego: https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-partitaria-permanente/normas-regulamentadora/normas-regulamentadoras-vigentes/norma-regulamentadora-no-26-nr-26
- NIOSH — Local Exhaust Ventilation Systems in Printing Operations: https://www.cdc.gov/niosh/engcontrols/ecd/detail37.html
- NIOSH — Controlling Cleaning-Solvent Vapors at Small Printers: https://www.cdc.gov/niosh/docs/hazardcontrol/hc24.html
- IARC Monographs Vol. 65 — Printing Processes and Printing Inks, Carbon Black and Some Nitro Compounds: https://publications.iarc.who.int/Book-And-Report-Series/Iarc-Monographs-On-The-Identification-Of-Carcinogenic-Hazards-To-Humans/Printing-Processes-And-Printing-Inks-Carbon-Black-And-Some-Nitro-Compounds-1996
- IARC Monographs Vol. 93 — Carbon Black, Titanium Dioxide, and Talc: https://publications.iarc.who.int/Book-And-Report-Series/Iarc-Monographs-On-The-Identification-Of-Carcinogenic-Hazards-To-Humans/Carbon-Black-Titanium-Dioxide-And-Talc-2010

## R3

**F_ok:** risco químico é declarado sem generalização; LGPD, SST e custódia foram separados por autoridade.  
**F_gap:** composição, lote, dose e exposição de qualquer caso concreto permanecem `TOKEN_VAZIO` até prova.  
**F_next:** vincular SDS/FDS e artefatos reais somente quando houver produto/caso identificável e cadeia de custódia autorizada.
