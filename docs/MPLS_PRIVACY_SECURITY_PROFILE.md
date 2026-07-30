# MPLS — perfil jurídico, de privacidade e segurança

```text
status = DOCUMENTARY_BASELINE
real_network_validation = TOKEN_VAZIO
claim_allowed = false
```

## Invariante

```text
MPLS != encryption
VRF != legal authorization
route separation != purpose limitation
carrier private network != absence of personal data risk
```

MPLS e BGP/MPLS IP VPN oferecem mecanismos de encaminhamento por rótulos e separação lógica. Confidencialidade e integridade exigem criptografia adicional quando o risco assim determinar.

## Controles mínimos

1. inventário CE/PE/P;
2. VRFs, RDs e RTs versionados;
3. importação/exportação mínima de rotas;
4. filtros e limites de prefixos;
5. prevenção e detecção de route leak;
6. autenticação e proteção do plano de controle;
7. gestão segregada e control plane policing;
8. IPsec, MACsec, TLS/mTLS ou criptografia de aplicação conforme o risco;
9. gestão de chaves, rotação e revogação;
10. minimização e retenção de telemetria;
11. inventário de metadados e destinatários;
12. exclusão padrão de dados infantis;
13. resposta a incidentes;
14. rollback testado;
15. revisão independente.

## Metadados

Labels, VRFs, rotas, NetFlow/IPFIX, syslog, AAA, inventários e telemetria podem revelar relações, localização, comportamento e topologia. Devem possuir finalidade, base legal, retenção, controle de acesso e registro de exportações.

## Proteção infantil

```text
child_data = DENIED_BY_DEFAULT
behavioral_profiling = false
commercial_exploitation = false
biometric_tracking = false
```

Exceções legítimas exigem melhor interesse, necessidade, segregação, criptografia, retenção mínima e supervisão humana.

## Incidentes

Classes prioritárias:

```text
ROUTE_LEAK
VRF_CROSS_CONNECT
PREFIX_HIJACK
CONTROL_PLANE_COMPROMISE
UNAUTHORIZED_TELEMETRY
PERSONAL_DATA_EXPOSURE
CHILD_DATA_EXPOSURE
```

Fluxo:

```text
DETECT → VERIFY → CONTAIN → PRESERVE → RESTORE → ASSESS → NOTIFY_IF_REQUIRED → REPAIR
```

## Fontes técnicas

- RFC 3031 — MPLS Architecture.
- RFC 4364 — BGP/MPLS IP VPNs.
- RFC 5920 — Security Framework for MPLS and GMPLS Networks.
- RFC 8964 — MPLS data-plane security observations.

## Fronteira

Este perfil não certifica nenhuma rede. Saída do `TOKEN_VAZIO` exige configurações sanitizadas, teste de isolamento, teste de route leak, teste criptográfico, rollback, exercício de incidente e receipt independente.