# Registro curado de fontes primárias e jurisprudência de alto impacto

```text
status = PRIMARY_SOURCE_RESEARCH_REGISTER
legal_advice = false
complete_global_coverage = false
universal_precedent_claim = false
claim_allowed = false
```

Este registro organiza decisões e instrumentos por jurisdição e tema. Ele não transforma uma decisão estrangeira em regra universal e não substitui análise dos fatos, competência, pedidos, vigência e direito aplicável.

## 1. Propriedade intelectual, APIs e software

### US-SCOTUS-GOOGLE-ORACLE-2021

- **Caso:** Google LLC v. Oracle America, Inc.
- **Tribunal:** Supreme Court of the United States.
- **Tema:** declarações de API Java e fair use.
- **Fonte oficial:** https://www.supremecourt.gov/opinions/20pdf/18-956_d18f.pdf
- **Sustenta:** análise contextual de finalidade, natureza funcional, quantidade e efeito de mercado.
- **Não sustenta:** “toda API é livre”, “copiar qualquer código é fair use” ou licença automática para derivados.

## 2. Metadados, localização e retenção

### US-SCOTUS-CARPENTER-2018

- **Caso:** Carpenter v. United States.
- **Tema:** histórico de localização por torres celulares.
- **Fonte oficial:** https://www.supremecourt.gov/opinions/17pdf/16-402_h315.pdf
- **Sustenta:** metadados extensivos podem revelar profundamente a vida privada.
- **Não sustenta:** expectativa idêntica para qualquer log ou qualquer contexto privado.

### EU-CJEU-DIGITAL-RIGHTS-2014

- **Casos:** C-293/12 e C-594/12.
- **Tema:** retenção generalizada e indiscriminada de dados de comunicações.
- **Fonte oficial:** https://curia.europa.eu/juris/liste.jsf?num=C-293/12
- **Sustenta:** necessidade, proporcionalidade e salvaguardas contra retenção ampla.

### BR-STF-ADI-6387

- **Tema:** compartilhamento de dados de telecomunicações com o IBGE.
- **Fonte oficial:** https://portal.stf.jus.br/processos/detalhe.asp?incidente=5895165
- **Sustenta:** finalidade pública não elimina necessidade, segurança, proporcionalidade e proteção de dados.

## 3. Transferência internacional e Big Tech

### EU-CJEU-SCHREMS-II-2020

- **Caso:** C-311/18.
- **Tema:** transferências internacionais, cláusulas contratuais e Privacy Shield.
- **Fonte oficial:** https://curia.europa.eu/juris/liste.jsf?num=C-311/18
- **Sustenta:** análise de proteção efetiva no destino e medidas suplementares.
- **Não sustenta:** proibição absoluta de toda transferência internacional.

### EU-CJEU-META-BUNDESKARTELLAMT-2023

- **Caso:** C-252/21.
- **Tema:** posição dominante, consentimento, combinação de dados e GDPR.
- **Fonte oficial:** https://curia.europa.eu/juris/liste.jsf?num=C-252/21
- **Sustenta:** proteção de dados, escolha real e poder de mercado podem interagir.

### EU-CJEU-GOOGLE-SPAIN-2014

- **Caso:** C-131/12.
- **Tema:** mecanismo de busca, tratamento de dados e desindexação.
- **Fonte oficial:** https://curia.europa.eu/juris/liste.jsf?num=C-131/12
- **Sustenta:** responsabilidade do operador e possibilidade de desindexação em condições delimitadas.
- **Não sustenta:** apagar automaticamente a fonte original ou remover informação de toda jurisdição.

## 4. Não discriminação, orientação sexual, identidade de gênero e crença

### BR-STF-ADO-26-MI-4733

- **Tema:** homotransfobia e proteção penal enquanto persistir omissão legislativa.
- **Fonte oficial:** https://portal.stf.jus.br/processos/detalhe.asp?incidente=4515053
- **Sustenta:** proteção contra discriminação por orientação sexual e identidade de gênero; preservação de expressão religiosa pacífica.
- **Não sustenta:** incitação de hostilidade ou tratamento inferior sob pretexto religioso.

## 5. Fontes normativas centrais

| ID | Instrumento | Fonte oficial |
|---|---|---|
| BR-CF88 | Constituição Federal do Brasil | https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm |
| BR-LGPD | Lei 13.709/2018 | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm |
| BR-ECA | Lei 8.069/1990 | https://www.planalto.gov.br/ccivil_03/leis/l8069.htm |
| EU-GDPR | Regulation (EU) 2016/679 | https://eur-lex.europa.eu/eli/reg/2016/679/oj |
| US-CONSTITUTION | Constituição e emendas dos EUA | https://constitution.congress.gov/constitution/ |
| UN-UDHR | Declaração Universal | https://www.ohchr.org/en/human-rights/universal-declaration/translations/english |
| UN-ICCPR | Pacto de Direitos Civis e Políticos | https://www.ohchr.org/en/instruments-mechanisms/instruments/international-covenant-civil-and-political-rights |
| UN-CRC | Convenção dos Direitos da Criança | https://www.ohchr.org/en/instruments-mechanisms/instruments/convention-rights-child |

## 6. Governança de incidentes

O registro deve ser cruzado com a regulamentação vigente da ANPD, autoridade europeia competente e obrigações setoriais. A existência de um incidente não produz automaticamente culpa, multa ou indenização.

```text
alert != incident confirmed
incident confirmed != relevant risk threshold met
notification duty != admission of liability
regulator contact != criminal accusation
```

## 7. Jurisprudência não é licença

```text
case law != software license
privacy ruling != permission to copy code
fair use ruling != blanket commercialization right
antitrust authority != data protection authority in every jurisdiction
```

## 8. Campos obrigatórios para novos casos

```yaml
case_id: ...
jurisdiction: ...
court_or_authority: ...
date: ...
official_source: ...
facts: ...
question_presented: ...
holding: ...
supports: []
does_not_support: []
current_status: ...
verified_at: ...
```

## 9. Lacunas

```text
Brazilian case-by-case factual analysis = TOKEN_VAZIO
complete US state privacy survey = TOKEN_VAZIO
complete EU member-state implementation survey = TOKEN_VAZIO
independent counsel review = TOKEN_VAZIO
```