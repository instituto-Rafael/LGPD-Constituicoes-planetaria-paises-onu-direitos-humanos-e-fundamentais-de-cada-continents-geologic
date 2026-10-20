# Core físico puro × multicore × buffers físicos — Prerregistro técnico-jurídico V3

**Data:** 2026-10-20 · **Parent:** CPU_SMT_LICENSING_ANTITRUST_EVIDENCE_V2_20261020.md · **Autor da hipótese:** ΔRafaelVerboΩ · **Estado:** DRAFT_NO_MERGE/CLAIM_ALLOWED_FALSE.
**Objeto:** propor uma política auditável de licenciamento por capacidade física material, sem duplicação por thread lógica e sem confundir o recurso físico com a métrica escolhida em um contrato.

## 1. Três contratos distintos — não intercambiáveis
- **POR_PACKAGE/PROCESSADOR_FÍSICO:** uma unidade por package/socket físico; processador multicore continua sendo um package. Esta é a versão mais próxima da frase do autor: “uma máquina com processador físico e lógico, esse é um licenciamento”.
- **POR_CORE_FÍSICO:** uma unidade por núcleo físico, independentemente do número de threads SMT. Quatro cores no mesmo package podem representar quatro unidades.
- **POR_CAPACIDADE_BUFFER:** métrica experimental que compara capacidades físicas observadas de uma **categoria tipada** de buffers, agrupadas por identidade física e núcleo proprietário, com um limiar de capacidade definido pela proposta contratual. Não é contagem universal e nunca deve substituir uma cláusula diferente em contrato em vigor.

Esta bifurcação é obrigatória para impedir que “processador”, “núcleo”, “buffer” e “licença” sejam tratados como sinônimos legais ou elétricos.

## 2. Matriz de casos sintéticos, referência arbitrária L1D 32 KiB
| Modelo sintético | Package | Cores | Threads | L1D privada por core | L2 compartilhada | Por package | Por core | Por buffer V1 |
|---|---:|---:|---:|---|---|---:|---:|---:|
| 1 core puro, SMT off | 1 | 1 | 1 | 32 KiB | não medido | 1 | 1 | 1 |
| 1 core, SMT x2 | 1 | 1 | 2 | 32 KiB | não medido | 1 | 1 | 1 |
| 4 cores, SMT off | 1 | 4 | 4 | 32 KiB por core | 512 KiB | 1 | 4 | 4 |
| 4 cores, SMT x2 | 1 | 4 | 8 | 32 KiB por core | 512 KiB | 1 | 4 | 4 |
| 4 cores, buffers menores | 1 | 4 | 8 | 16 KiB por core | não medido | 1 | 4 | 2 |
| 1 core sem cache interno, ausência confirmada | 1 | 1 | 1 | zero **verificado** | não medido | 1 | 1 | 1 |
| Cache/buffer sem observação confiável | 1 | 1 | 2 | TOKEN_VAZIO | TOKEN_VAZIO | 1 se package verificado | 1 se core verificado | TOKEN_VAZIO |

Os números não são faturas, preços, benchmarks ou provas de capacidade incremental real. L1D é uma cache, escolhida **apenas como proxy** mensurável para este ensaio; não define todos os buffers possíveis. Referência de 32 KiB é arbitrária/experimental e não provém de lei, CADE, tratado, norma NIST, fabricante ou contrato.

### Fórmula de proposta auditável
Sejam `P` o número de cores físicos validados, `B_t` a soma da capacidade de buffers físicos **privados, únicos** de uma mesma classe `t` (e mesma unidade) e `R_t` a referência declarada pela política hipotética:

`U_buffer = min(P, max(1, ceil(B_t / R_t)))`.

A soma exclui buffers compartilhados (reportados separadamente uma vez), não confunde L1 e store buffer, não aumenta sob SMT apenas e trata ausência de evidência como TOKEN_VAZIO. Valor de buffer ausente, sob hardware confirmado sem esse tipo de cache, não elimina a existência de núcleo.

Como `U_buffer` não é universalmente correlacionado com throughput, latência ou energia, precisa de benchmark independente para qualquer alegação de justiça econômica. Em arquiteturas com cache compartilhada e núcleos legítimos, usar somente bytes privados pode **subestimar** trabalho físico; por isso a contagem por core e por package permanece paralela e o modelo deve poder ser rejeitado.

## 3. Evidência de contradição à definição universal de núcleo por buffer
- **Arm Cortex-M0, documento técnico Arm DAI0321A:** núcleos Cortex-M0, M0+, M1, M3 e M4 não têm cache interna (com ressalvas específicas de pré-busca); Cortex-M0 r0p0 e M0+ r0p0 não incluem write buffer na interface de barramento. Núcleo existe sem cache ou write buffer. URL: https://documentation-service.arm.com/static/5efefb97dbdee951c1cd5aaf
- **Arm Cortex-A53:** implementação de 1–4 cores, cada core com L1 e L2 compartilhada, demonstrando classes e níveis de propriedade distintos. URL: https://www.arm.com/products/silicon-ip-cpu/cortex-a/cortex-a53
- **Intel Hyper-Threading:** duas threads lógicas podem compartilhar caches e recursos de execução. URL: https://www.intel.com/content/www/us/en/developer/articles/guide/hyper-thread-tuning-guide-for-video-ai-workload.html
- **Microsoft SQL Server físico:** Hyper-Threading não muda contagem de licenças por core neste modo; há mínimos comerciais, então contagem física ≠ automaticamente preço de 1 licença. URL: https://www.microsoft.com/licensing/guidance/Core-based-licensing-models
- **IBM PVU:** um “processor” na métrica contratual pode significar cada núcleo do chip; contratos não têm semântica universal. URL: https://www.ibm.com/software/passportadvantage/pvu-licensing-for-customers
- **Linux x86 topology:** enumera package/core/thread por mecanismos específicos; o ID de cache precisa de escopo por nível, tipo e sharing set; não reutilizar número bruto de `id` em níveis distintos como identidade física única global. https://www.kernel.org/doc/html/latest/arch/x86/topology.html e https://github.com/torvalds/linux/blob/master/Documentation/ABI/testing/sysfs-devices-system-cpu

## 4. Falsificadores prioritários
1. **F1:** CPU monocore sem cache L1 e sem write buffer ainda executa instruções (Arm Cortex-M0) → refuta cache ou write buffer obrigatório para existência de CPU.
2. **F2:** ativar SMT num core não cria novo núcleo nem segunda L1 física → em regra física por core, licenças não mudam. Falsificador da tese oposta “cada thread cria um core”.
3. **F3:** dois cores físicos com L2/L3 compartilhada mantêm dois cores → uma cache compartilhada não reduz número de núcleos reais.
4. **F4:** duas CPUs heterogêneas de mesmo número de cores podem ter diferentes tamanhos de L1 e diferentes desempenhos → `bytes L1=performance` não é monotonicamente universal.
5. **F5:** contratos lícitos podem cobrar por socket, core, vCPU, instância ou usuário, e a contagem acordada não muda por definição técnica nova; questionar em cada caso transparência, conformidade, abuso e concorrência.
6. **F6:** VM sem visão confiável da topologia host não fornece prova de identidade física; reportar TOKEN_VAZIO.
7. **F7:** duplicar observação do mesmo buffer em duas threads não duplica seu `physical_id`; contradizer metadados `capacity`/owner de mesmo ID provoca CONFLICT, não soma silenciosa.
8. **F8:** cores sem buffer de classe selecionada mas com recursos de execução reais tornam métrica estritamente por buffer inadequada, salvo referência contratual específica.

## 5. Arquitetura executável proposta e fronteiras
Produtor jurídico: este dossiê; Mapa branch `docs/core-license-fairness-20261020`: `tools/cpu_buffer_license_v1.h` — algoritmo de comparação freestanding C11, sem libc/heap/syscall/I/O; `tests/test_cpu_buffer_license_v1.c` — 14+ invariantes/negações sintéticas; `data/governance/physical-core-buffer-license-policy.v1.json` — contrato de tipos/ausências; `domains/legal-licensing/` — roteamento e evidência.

**Atenção:** a fonte C não lê sozinha CPUID, sysfs, cache nem registradores do aparelho: exige entrada de topologia produzida por coletor separado, confiável e juridicamente autorizado. Um teste local de fixtures não mede um aparelho nem confirma a fatura. O programa compara **políticas**, não calcula legalmente o valor devido.

Implementar o coletor Linux/Android e bare-metal em domínios separados e sob autoridade do repo produtor do dispositivo; não presumir OS por ter um core freestanding. Uma CPU sem cache é caso válido, não *erro*.

## 6. Gates e segurança jurídica
G0 hipótese identificada → OK; G1 fontes primárias técnicas → amostra documentada; G2 compilação e fixtures locais espelhadas → PASS_LOCAL_HOSTED_FIXTURE, **não** CI exact-head GitHub; G3 topologia física real → TOKEN_VAZIO; G4 contrato e fatura específicos → TOKEN_VAZIO; G5 parecer jurídico/antitruste → TOKEN_VAZIO; G6 CI independente/execução ARM real → TOKEN_VAZIO; Claim jurídico de enriquecimento ilícito → **não demonstrado**.

Cadeia de custódia: recurso tipado → snapshot/modelo/SKU/firmware/OS → hash da captura → cálculo reprodutível → cláusula e preço → cálculo de diferença → análise jurídica independente. Dados comerciais privados não vão para repo público. Mapa não altera juridicamente termos de terceiros.

## R3
F_ok: modelo comparativo falsificável por socket/core/buffer; sem duplicação de recursos compartilhados ou SMT; casos cacheless e desconhecidos preservados.
F_gap: identificação de buffers reais/benchmarks multi-ISA, hardware independente, contratos reais e parecer jurídico.
F_next: capturar topologia de um monocore conhecido e multicore em equipamento controlado; usar mesma métrica tipada/benchmark; confrontar cobranças e revisar juridicamente sem alegação automática.
