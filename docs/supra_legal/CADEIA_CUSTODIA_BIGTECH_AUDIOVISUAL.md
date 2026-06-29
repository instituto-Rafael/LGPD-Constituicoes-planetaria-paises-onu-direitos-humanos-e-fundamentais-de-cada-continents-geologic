# Cadeia de custódia — Big Tech, audiovisual, dados e algoritmos

> Protocolo de evidência segura para obras audiovisuais sensíveis em plataformas digitais.  
> Regra absoluta: não baixar, não armazenar, não circular e não anexar material sensível. Preservar apenas metadados lícitos e rotas formais.

## 1. Escopo

Este documento define como coletar, organizar e encaminhar dados sobre obras sensíveis em catálogos digitais, sem criar risco jurídico pela circulação de conteúdo potencialmente ilícito.

Abrange:

- Google Play/Google TV;
- Apple TV;
- Prime Video;
- Sony/Columbia ou páginas oficiais de titulares;
- Movies Anywhere/Fandango e lojas digitais;
- buscadores;
- redes sociais e clipes;
- CDN/cache;
- anúncios, remarketing, recomendação e rankings.

## 2. Princípio de mínima evidência segura

Coletar somente:

```text
título + URL + plataforma + país + data/hora + classificação + descritores + preço + modalidade + copyright + titular + protocolo
```

Não coletar:

```text
cena sensível + imagem sensível + trecho de vídeo + frame + download + repost + anexo de nudez/conteúdo sexual envolvendo menor
```

## 3. Matriz por plataforma

| Campo | Descrição | Exemplo de preenchimento |
|---|---|---|
| Plataforma | Serviço/loja/catálogo | Google Play, Apple TV, Prime Video |
| País/região | Localização regulatória | Brasil, EUA, UE |
| URL | Link público | URL da página, sem conteúdo sensível |
| Data/hora | Momento da captura | ISO-8601, fuso local |
| Título | Nome local e original | A Lagoa Azul / The Blue Lagoon |
| Versão | Digital, DVD, remaster, trailer, clipe | TOKEN_VAZIO se não confirmado |
| Classificação | Faixa etária exibida | 16, 16+, R, PG-13 |
| Descritores | Nudez, conteúdo sexual, violência etc. | Copiar texto da plataforma |
| Preço | Aluguel/compra/assinatura | R$, USD, EUR etc. |
| Monetização | Compra, aluguel, ads, assinatura | TOKEN_VAZIO se não visível |
| Titular/copyright | Entidade exibida | Columbia/Sony/outro |
| Recomendação | Títulos relacionados/autoplay | Sem inferir dolo |
| Anúncio | Promovido/patrocinado/remarketing | Registrar só se houver evidência |
| Denúncia | Link/canal da plataforma | URL/protocolo |
| Resposta | Remoção, negativa, silêncio | Data + protocolo |

## 4. Risco algorítmico

O risco algorítmico não é apenas a presença do título no catálogo. Ele pode surgir da combinação de:

- busca;
- autocomplete;
- ranking;
- thumbnail;
- trailer;
- títulos relacionados;
- autoplay;
- recomendação personalizada;
- públicos semelhantes;
- remarketing;
- push/e-mail/SMS;
- anúncios;
- dados derivados;
- classificação etária;
- inferência de idade/interesse.

Modelo:

```text
R_algorítmico = conteúdo_sensível × metadados × recomendação × anúncio × perfilamento × menoridade × retenção
```

## 5. O que pode ser afirmado sem logs internos

Pode-se afirmar:

- a plataforma exibiu página de catálogo;
- a plataforma exibiu classificação e descritores;
- a plataforma exibiu preço/modalidade de acesso, se visível;
- a plataforma ofereceu busca, trailer, wishlist ou relação com outros títulos, se visível;
- a plataforma é agente profissional com capacidade técnica de auditar catálogo;
- há risco de amplificação algorítmica quando houver recomendação/ads/ranqueamento.

Não afirmar sem logs internos:

- que o algoritmo quis explorar crianças;
- que houve direcionamento deliberado a menores;
- que houve campanha publicitária específica;
- que houve venda literal de dados;
- que houve dolo de executivo, servidor ou técnico;
- que houve lavagem/fraude/conluio.

## 6. Trilha financeira mínima

Quando houver monetização visível, registrar:

| Eixo | Dado seguro |
|---|---|
| Modalidade | aluguel, compra, assinatura, anúncio |
| Preço | valor, moeda, data/hora |
| Plataforma | marketplace, loja, streamer |
| Entidade | vendedor, distribuidor, titular, quando visível |
| Recibo | apenas se usuário comprar legitimamente; não comprar para obter prova sensível sem orientação jurídica |
| Fiscal | CNPJ/entidade, nota, tributo, remessa: TOKEN_VAZIO até prova documental |

## 7. Cadeia de notificação

Sequência recomendada:

1. Registrar metadados públicos.
2. Não circular conteúdo sensível.
3. Notificar a plataforma pelo canal oficial.
4. Guardar protocolo.
5. Notificar titular/distribuidor, se identificado.
6. Encaminhar a órgão competente, se houver suspeita de violação de proteção infantil.
7. Pedir preservação de logs por via competente.
8. Solicitar revisão de classificação/versão, quando aplicável.
9. Acompanhar resposta e prazo.
10. Escalonar se houver silêncio ou resposta inadequada.

## 8. Arquitetura de responsabilidade

```text
Responsabilidade_plataforma = controle_de_catálogo + ciência + capacidade_de_remover + monetização + dever_de_diligência
```

```text
Responsabilidade_algorítmica = sistema_de_recomendação + risco_previsível + audiência_menor + ausência_de_mitigação + benefício
```

```text
Responsabilidade_financeira = receita + ilicitude_base + ciência + nexo + beneficiário + ocultação/dissimulação
```

A última fórmula só deve ser usada como hipótese investigável enquanto não houver prova de ilicitude-base e fluxo financeiro específico.

## 9. Protocolo de evidência em formato JSON

```json
{
  "case_id": "TOKEN_VAZIO",
  "title_local": "TOKEN_VAZIO",
  "title_original": "TOKEN_VAZIO",
  "platform": "TOKEN_VAZIO",
  "country_region": "TOKEN_VAZIO",
  "url": "TOKEN_VAZIO",
  "captured_at": "TOKEN_VAZIO",
  "age_rating": "TOKEN_VAZIO",
  "content_descriptors": [],
  "access_mode": "rent|buy|subscription|ad_supported|free|TOKEN_VAZIO",
  "price": "TOKEN_VAZIO",
  "currency": "TOKEN_VAZIO",
  "copyright_notice": "TOKEN_VAZIO",
  "rights_holder_displayed": "TOKEN_VAZIO",
  "recommendation_evidence": "TOKEN_VAZIO",
  "ad_evidence": "TOKEN_VAZIO",
  "notification_protocol": "TOKEN_VAZIO",
  "response_status": "TOKEN_VAZIO",
  "risk_notes": "sem acusação; hipótese investigável"
}
```

## 10. Links operacionais

- DSA — EUR-Lex: https://eur-lex.europa.eu/eli/reg/2022/2065/oj/eng
- GDPR — EUR-Lex: https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng
- LGPD — Planalto: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm
- ECA — Planalto: https://www.planalto.gov.br/ccivil_03/leis/l8069.htm
- Classificação Indicativa — gov.br: https://www.gov.br/pt-br/servicos/obter-classificacao-indicativa
- ANCINE — ROE: https://www.gov.br/ancine/pt-br/assuntos/atribuicoes-ancine/registro/registro-de-obras-nao-publicitarias/registro-de-obra-estrangeira

---

**F_ok:** cadeia de custódia segura estruturada.  
**F_gap:** logs internos, critérios de recomendação e dados de monetização exigem canal formal.  
**F_next:** preencher matriz por plataforma e anexar apenas metadados verificáveis.
