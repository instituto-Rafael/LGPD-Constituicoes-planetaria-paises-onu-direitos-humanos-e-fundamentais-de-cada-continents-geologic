# ROBOTICS × MAPA — NORMATIVE CROSSWALK V2

**State:** `PROPOSED_AUDITABLE`
**Checked:** `2026-08-26`
**Federation target:** `rafaelmeloreisnovo/Mapa`

## 1. Thesis

Robotics governance is not a substitute for law, regulation, standards, certification or independent audit. It is a control plane that makes the relationship among them visible to the person affected by automated information processing.

The design target is:

```text
PERSON
 -> CLEAR INFORMATION
 -> AUTHORITY + PURPOSE + LEGAL BASIS
 -> DATA + AUTOMATION + SHARING + RETENTION
 -> RIGHTS + CONTROLS
 -> RISK + STANDARDS + ASSURANCE
 -> EVIDENCE + RECEIPT
 -> REVIEW / CONTEST / REVOKE / CORRECT where applicable
```

The user is not treated as a passive input object. However, `user control` does not mean that consent is the only lawful basis or that a preference can override a statutory duty.

## 2. Mapa inheritance

Robotics follows Mapa's federated discipline:

```text
identity -> authority -> boundary -> purpose -> evidence -> gate -> transition -> receipt
```

and inherits:

- `TOKEN_VAZIO != false`;
- `implementation != execution != evidence != release`;
- unknown critical sensitivity fails closed;
- source and producer authority remain explicit;
- material transitions preserve rollback/revocation state and append-only receipts;
- standards and external references do not automatically become operational authority.

Current Mapa references used by this crosswalk:

- `docs/governance/SHARED_DATA_GOVERNANCE_V2.md`;
- `AGENTS.md`;
- proposed `docs/governance/ROBOTICS_USER_SOVEREIGNTY_FEDERATION_V1.md`.

## 3. Brazil — constitutional and statutory legal anchors

### 3.1 Constitution

| Source | Anchor | Robotics mapping |
|---|---|---|
| Constituição Federal | art. 5º, X | intimacy, private life, honor and image boundary |
| Constituição Federal | art. 5º, XII | confidentiality of communications/data within constitutional/legal scope |
| Constituição Federal | art. 5º, LXXIX | fundamental right to personal-data protection, including digital means |

The constitutional layer is not reducible to a checkbox. It constrains interpretation of lower-level processing rules.

### 3.2 LGPD — core article map

| LGPD | Operational meaning for Robotics | Required evidence/control |
|---|---|---|
| art. 6º | purpose, adequacy, necessity, free access, data quality, transparency, security, prevention, non-discrimination, accountability | per-purpose processing map + evidence |
| art. 7º | legal bases for ordinary personal-data processing | basis must be declared per purpose; consent is not universal |
| art. 8º | consent quality, proof, specific purposes and revocation | separate consent state + receipt when consent is used |
| art. 9º | facilitated, clear, adequate and conspicuous information about processing | First Question/Pre-Processing Governance Gate |
| art. 10 | legitimate-interest constraints, necessity and transparency | legitimate-interest assessment + minimization + transparency |
| art. 11 | sensitive-data legal bases and safeguards | elevated criticality + legal-basis gate |
| art. 14 | best interests and special conditions for children/adolescents | child-data profile + guardian/best-interest controls where applicable |
| art. 17 | titularity and fundamental rights of the data subject | user governance capsule identity/rights layer |
| art. 18 | confirmation, access, correction, anonymization/block/deletion, portability, sharing information, consent information/revocation and other rights | rights API/route + receipt |
| art. 20 | review of decisions based solely on automated processing affecting interests; clear information on criteria/procedures on request | automated-decision registry + review/contest route |
| art. 37 | records of processing operations | processing ledger |
| art. 38 | data-protection impact report may be required by ANPD | RIPD/DPIA gate and evidence |
| art. 40 | interoperability standards may be set for portability, free access, security and retention | interoperable export/control layer |
| art. 41 | data-protection officer/contact rules, subject to applicable regulation/exceptions | public contact/authority route |
| art. 44 | irregular treatment includes failure to provide security reasonably expected | safety/security expectation test |
| art. 46 | technical and administrative security measures; from design through execution | security-by-design + runtime controls |
| art. 48 | relevant security incident communication to authority and data subject | incident receipt + notification route |
| art. 49 | systems must meet security, good-practice/governance principles and regulations | system architecture compliance gate |
| art. 50 | privacy governance programs, education, internal/external supervision, risk mitigation, incident response, continuous monitoring and participation of the titular | Robotics governance program |
| art. 51 | ANPD encouragement of technical standards facilitating data-subject control | standards crosswalk/user control interfaces |
| art. 52 | administrative sanctions and criteria, including governance/corrective measures | enforcement/risk consequence mapping |

### 3.3 Marco Civil da Internet

Key anchors for internet services include:

- art. 7º VI — clear and complete contractual information;
- art. 7º VII–IX — rules on third-party disclosure, clear information on collection/use/storage/treatment/protection, and highlighted consent where applicable;
- art. 7º X — deletion request subject to legally required retention;
- art. 7º XI — clarity/publicity of use policies;
- art. 8º — privacy and freedom of expression as conditions for full exercise of internet access;
- art. 10 — protection of records, personal data and private communications.

### 3.4 Consumer-information layer

Where there is a consumer relationship, clear, adequate and accessible information must also be analyzed under consumer-protection law. Robotics must not use complexity, interface design or automation to degrade legally required information.

## 4. International rights and data-protection references

These references do not have identical legal force in every jurisdiction. Their role must be tagged as `BINDING | APPLICABLE_BY_JURISDICTION | GUIDANCE | REFERENCE | TOKEN_VAZIO`.

| Instrument | Relevant axis |
|---|---|
| Universal Declaration of Human Rights, art. 12 | arbitrary interference with privacy |
| International Covenant on Civil and Political Rights, art. 17 | privacy protection |
| American Convention on Human Rights, art. 11 | dignity/privacy protection |
| OECD Privacy Guidelines | collection limitation, data quality, purpose specification, use limitation, security, openness, individual participation, accountability |
| GDPR, art. 5 | lawfulness/fairness/transparency, purpose limitation, minimization, accuracy, storage limitation, integrity/confidentiality, accountability |
| GDPR, arts. 12–15 | transparent information and access |
| GDPR, arts. 20–22 | portability, objection and automated decisions within their legal scope |
| GDPR, arts. 24–25 | controller responsibility and data protection by design/default |
| GDPR, art. 30 | records of processing |
| GDPR, art. 32 | security of processing |
| GDPR, art. 35 | DPIA |
| GDPR, art. 42 | certification mechanisms |
| EU AI Act (Reg. 2024/1689) | risk-based AI governance, human agency/oversight, privacy/data governance, transparency, robustness and accountability, subject to its phased applicability |

## 5. Standards and technical assurance crosswalk

Standards are not statutes and certification scope matters.

| Reference | Scope | Robotics use |
|---|---|---|
| ISO/IEC 27001:2022 | information security management system | security governance/evidence |
| ISO/IEC 27701:2025 | privacy information management system | privacy governance/accountability |
| ISO 8000-1:2022 + ISO 8000 family | data quality principles/structure | quality/provenance/integrity of governed data |
| ISO 8000-8:2015 | information/data quality concepts and measurement | measurable data-quality layer |
| ISO 8000-210:2024 | sensor-data quality characteristics/anomalies | physical/IoT robotics sensor data when applicable |
| ISO/IEC 42001 | AI management system | organizational AI governance when applicable |
| ISO 14001:2026 | environmental management system | environmental claims/operations only; not privacy evidence |
| NIST CSF 2.0 | cybersecurity-risk governance | GOVERN/IDENTIFY/PROTECT/DETECT/RESPOND/RECOVER mapping |
| NIST Privacy Framework | privacy risk management | privacy outcomes and enterprise-risk mapping |
| NIST AI RMF 1.0 | AI risk management | GOVERN/MAP/MEASURE/MANAGE; version currently under revision |
| IEEE 7000-2021 | ethical concerns in system design | trace values into requirements/design |
| IEEE 7002-2022 | data privacy process | privacy engineering + assessment process |
| IEEE 7003-2024 | algorithmic bias considerations | bias profile, validation boundaries and user expectations |
| IEEE 7007-2021 | ethically driven robotics/automation ontology | Robotics semantic ontology alignment |
| IEEE 7009-2024 | fail-safe autonomous/semi-autonomous systems | fail-safe/safety layer when applicable |
| RFC 6973 | privacy considerations for Internet protocols | protocol privacy analysis |
| RFC 3552 | security considerations for Internet protocols | protocol threat/security analysis |

## 6. Certification and independent-audit invariant

Independent certification and audit are confidence mechanisms because self-assertion is not equivalent to third-party assurance.

```text
self_declaration != independent_assurance
standard_reference != certificate
certificate != certification_of_every_process
financial_audit != privacy_audit
privacy_audit != cybersecurity_penetration_test
inspection != legal_adjudication
```

Every assertion such as `ISO certified`, `audited`, `verified`, `compliant` or `accredited` must expose at least:

```text
standard/version
issuer
accreditation/status where relevant
scope
sites/products/processes covered
issue/expiry/transition dates
exceptions/nonconformities where publishable
source/evidence
```

### 6.1 Capital markets analogy

Brazilian securities-market rules require independent auditing in regulated contexts, and CVM describes external auditing as fundamental to the credibility of financial information and protection of users/investors. This supports the general assurance principle, but the claim `every listed company requires exactly two independent external audits` is **not established here** and remains `TOKEN_VAZIO` unless a specific rule/context is identified.

### 6.2 Environmental-management analogy

ISO 14001 demonstrates why organizations maintain auditable management systems for environmental responsibilities. In 2026, the current ISO edition is ISO 14001:2026. A Petrobras refinery page also reports ISO 14001 certification for that specific refinery. This is evidence for a bounded certified scope, not proof that every Petrobras operation has the same certificate or scope.

### 6.3 Commodity assurance analogy

Bureau Veritas Brazil states that it classifies roughly 45% of the volume of grains leaving Brazil and describes independent certification/inspection as increasing reliability in commodity transactions. This is an example of cross-border assurance infrastructure, not evidence of loss of national sovereignty.

Fundação Vanzolini describes certification/audit as independent conformity assessment and is accredited for multiple management-system certification activities. A foreign buyer or certifier requesting additional verification may reflect contractual, accreditation, risk or destination-market requirements; calling that request an `invasion of sovereignty` requires a separate legal and factual test.

## 7. Sovereignty and cross-border assurance

Robotics must distinguish:

```text
foreign/private assurance request
!= exercise of public sovereignty
!= unlawful extraterritorial coercion
!= trade barrier
!= discrimination
```

A cross-border requirement can be legitimate, contractual, voluntary, regulatory, duplicative, discriminatory or unlawful depending on facts and applicable law. The system must classify the source of authority and preserve `TOKEN_VAZIO` instead of collapsing all cases into one narrative.

## 8. Economic/systemic claims ledger

The following are valid research hypotheses but cannot be promoted automatically:

- excessive platform concentration;
- dependency/lock-in;
- interoperability suppression;
- discriminatory certification costs;
- asymmetric standards-setting power;
- manipulation of information markets;
- manipulation of financial markets;
- systemic financial risk;
- structural disadvantages for developing economies;
- digital/algorithmic forms of dependency or extractive development.

Required minimum evidence before strong legal/economic claims:

```text
relevant market
market power/share
entry barriers/network effects
substitutability
observed conduct
causal mechanism
affected parties
financial/economic data
jurisdiction
applicable competition/securities/trade rule
independent source or regulator finding
falsifier
```

`market concentration != cartel proof`.
`dependency != slavery as a legal classification`.
`cross-border certification != sovereignty violation by itself`.
`harmful financial effect != intentional attack on the financial system`.

## 9. Robotics User Governance Capsule

Robotics SHOULD produce a user-visible and machine-readable capsule for every material service context:

```json
{
  "controller": "...",
  "processors": [],
  "jurisdiction": [],
  "purposes": [],
  "legal_bases": [],
  "data_collected": [],
  "data_inferred": [],
  "automation": [],
  "sharing": [],
  "retention": {},
  "rights": [],
  "controls": [],
  "certifications": [],
  "external_audits": [],
  "standards_crosswalk": [],
  "risks": [],
  "unknowns": [],
  "evidence": [],
  "receipt": "TOKEN_VAZIO"
}
```

## 10. Normative routing function

For each processing operation `p`:

```text
N(p) = Constitution
     + Applicable_Law
     + Regulator
     + Contract
     + Adopted_Standards
     + Technical_Guidance
     + Internal_Policy
     + User_Rights_And_Preferences
```

The `+` operator means a typed relation, not arithmetic addition.

When two requirements conflict:

```text
CONFLICT -> jurisdiction analysis -> authority precedence -> documented resolution OR TOKEN_VAZIO
```

## 11. Audit transforms

Analytical transforms may assist prioritization but do not create legal proof:

- direct: effect of a processing action on an identified right/control;
- inverse: trace an outcome back to source data/rule/model/authority;
- derivative: rate of change in risk, opacity or collection;
- antiderivative: cumulative exposure across lifecycle;
- exclusive: mutually incompatible states (`PROVED XOR TOKEN_VAZIO` for same scoped claim);
- logarithmic: compress evidence volume so document count does not dominate quality;
- anomaly: declared governance differs from runtime evidence;
- paradox: formally transparent interface remains practically unintelligible.

## 12. Sources checked

Primary/official sources used for this V2 include:

- Constituição Federal compilada — Planalto;
- Lei 13.709/2018 compilada — Planalto;
- Lei 12.965/2014 — Planalto;
- ANPD — Direitos dos Titulares;
- CVM — Resolução CVM 23 and auditor-independent guidance;
- EUR-Lex — GDPR and EU AI Act;
- NIST — CSF 2.0, Privacy Framework, AI RMF;
- ISO — public metadata for ISO/IEC 27001:2022, ISO/IEC 27701:2025, ISO 8000 series and ISO 14001:2026;
- IEEE SA — IEEE 7000, 7002, 7003 and autonomous/intelligent-systems standards;
- RFC Editor — RFC 6973 and RFC 3552;
- OAS/IACHR — American Convention, art. 11;
- OHCHR — international privacy/human-rights references;
- OECD — Privacy Guidelines;
- Petrobras — bounded refinery certification example;
- Bureau Veritas Brazil — agribusiness/commodities assurance examples;
- Fundação Vanzolini — certification/conformity-assessment examples.

## 13. Gates

- `G-NORM-01` Brazilian legal anchors checked against primary/official source — `PASS_DOCUMENTED`
- `G-NORM-02` current ISO edition metadata checked — `PASS_DOCUMENTED`
- `G-NORM-03` NIST current-status metadata checked — `PASS_DOCUMENTED`
- `G-NORM-04` IEEE/RFC references checked — `PASS_DOCUMENTED`
- `G-NORM-05` every referenced standard clause licensed/read in full — `TOKEN_VAZIO`
- `G-NORM-06` jurisdiction-specific legal opinion — `TOKEN_VAZIO`
- `G-NORM-07` Mapa producer enrollment — `TOKEN_VAZIO`
- `G-NORM-08` runtime Robotics implementation — `TOKEN_VAZIO`
- `G-NORM-09` independent assurance of implementation — `TOKEN_VAZIO`

## 14. Final invariant

```text
CLEAR INFORMATION
+ LEGAL AUTHORITY
+ USER RIGHTS
+ TECHNICAL CONTROLS
+ INDEPENDENT ASSURANCE WHERE NEEDED
+ EVIDENCE
+ RECEIPTS
= GOVERNANCE THAT CAN BE CHALLENGED AND VERIFIED
```

**F_ok:** legal articles, standards, audits and Mapa semantics are cross-linked.
**F_gap:** implementation/runtime, full standards clauses, jurisdictional opinions and producer enrollment.
**F_next:** encode this crosswalk as a machine-readable registry and test that no Robotics processing class can be declared `RELEASE_ALLOWED` with missing authority, purpose, rights or evidence.
