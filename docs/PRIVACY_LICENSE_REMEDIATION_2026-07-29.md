# Remediação de licença e dados pessoais — 2026-07-29

## Constatação

O arquivo raiz anteriormente denominado `LICENSE` não funcionava como instrumento de licença. Ele misturava:

- pseudocódigo;
- manifesto espiritual e jurídico;
- proposições de sanção;
- pedidos conversacionais;
- dados pessoais diretamente identificáveis;
- ausência de separação entre software, documentação, dados e terceiros.

## Risco observado

O conteúdo anterior incluía identificadores pessoais e data de nascimento completa em arquivo público. Isso contrariava minimização, limitação de finalidade e a própria intenção protetiva do repositório.

## Ações executadas nesta branch

1. substituição integral do `LICENSE` na revisão corrente;
2. adoção de licenciamento em camadas;
3. remoção de identificadores pessoais da versão atual do arquivo;
4. bloqueio de redistribuição e treinamento quando direitos de dataset forem desconhecidos;
5. criação de registro de fontes e jurisprudência;
6. criação de perfil MPLS de privacidade e segurança;
7. preservação de `claim_allowed=false`.

## Limite da remediação

A substituição remove a exposição do `HEAD` desta branch após eventual merge, mas não apaga automaticamente o conteúdo de commits antigos, forks, clones, caches ou indexadores.

```text
head_remediation = IMPLEMENTED
full_git_history_purge = TOKEN_VAZIO
fork_and_cache_remediation = TOKEN_VAZIO
search_index_removal = TOKEN_VAZIO
independent_privacy_review = TOKEN_VAZIO
```

Uma remoção histórica completa exige procedimento separado, com avaliação de impacto e coordenação:

```text
preservar backup jurídico restrito
→ identificar todos os blobs e commits
→ reescrever histórico com ferramenta apropriada
→ invalidar referências antigas
→ solicitar limpeza de caches quando possível
→ orientar colaboradores a reclonar
→ verificar forks e releases
→ registrar receipt
```

## Por que o histórico não foi reescrito automaticamente

Reescrever histórico público é uma operação destrutiva para referências, clones, PRs, tags e hashes. Ela não deve ser executada silenciosamente nem confundida com simples edição de arquivo.

## Estado da licença

```text
documentation = CC-BY-NC-SA-4.0 by default when original and identified
software = PolyForm-Noncommercial-1.0.0 by default when original and identified
datasets = PER_DATASET_MANIFEST
third_party = UPSTREAM_TERMS_PREVAIL
commercial_use = SEPARATE_AGREEMENT
```

## Próximos gates

- revisar outros arquivos por CPF, RG, endereços, telefones, emails e datas completas;
- verificar imagens e metadados EXIF;
- verificar arquivos compactados e releases;
- classificar cada dataset;
- revisão jurídica independente;
- decidir, com autorização explícita, se haverá reescrita do histórico.

## Fronteira

Esta remediação reduz exposição e corrige governança documental. Não constitui declaração de conformidade integral com LGPD, GDPR ou outra lei.