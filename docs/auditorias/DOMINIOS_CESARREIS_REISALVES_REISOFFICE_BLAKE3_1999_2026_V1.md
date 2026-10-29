# Historical domain/DNS/IIS and BLAKE3 correlation — evidence intake V1
Status: DRAFT / HOLD / PUBLIC_SANITIZED / CLAIM_ALLOWED=false
Recorded: 2026-10-29 (date only); parent: RAFAELIA Ω START HERE V2.2 / LGPD main at branch-creation time.
Authority: institute-Rafael LGPD repository for a public *audit methodology and sanitized index*, not authority over historical web infrastructure or BLAKE3 source code.

## Intent / exact scope
Reconstruct what can be proven for **1999–2017 inclusive**, for these root domains:
- cesarreis.com.br — historical target;
- reisalves.com.br — new target specified by user, **not** silently replaced by reisoffice.com.br;
- reisoffice.com.br — distinct contextual control for the documented César Reis → Reis Office company-name transition.

Each root must be enumerated as HTTP and HTTPS across bare apex, www, ww, wwww, mobile, portal (6 host variants × 2 schemes × 19 years = 228 candidate cells per root; **684 total**). Candidate cells are a plan, NOT actual preserved captures.

Investigate original anchor hrefs, email domains, links to third-party sites, full HTTP 3xx Location chains, HTML bytes and embedded asset paths, original server headers, TLS certificate evidence where period-applicable, historical DNS (A/AAAA/CNAME/MX/NS/SOA), and path fingerprints such as ASP pages.
Potential IIS/vhost/common server hypotheses should be tested using timestamped IPs, ASN, server headers, ASP session/cookie semantics, redirects, raw HTML asset digests; indistinguishable content alone is not proof of common Windows/IIS instance.
WARC bytes or reliably dated independent evidence are needed before confirming past server identity. Current DNS/IP or current IIS headers are NOT retroactive evidence.

## External sources and observations
| ID | Event date or observation | Node | Observation | State | URL |
|---|---|---|---|---|---|
| SRC-01 | 2003-07-21 | cesarreis.com.br | ACE-Guarulhos report says 2003 event photographs were available at www.cesarreis.com.br. | CORROBORATED_PUBLIC_REFERENCE | [Source](https://www.aceguarulhos.com.br/blog/sucesso-no-evento-dos-40-anos-da-ace-guarulhos-1/) |
| SRC-02 | 2007-07-23 | Cesar Reis -> Reis Office corporate name | Official Gazette issue 140, page 47 (PDF page index 46), contract amendment process 7855.01.1506.1/2006, alteration of corporate name; entry dated 2007-07-11. | CORROBORATED_COMPANY_NAME_ONLY | [Source](https://docs.trt10.jus.br/docs/pub/pub000003126.pdf) |
| SRC-03 | UNKNOWN | cesarreis.com.br | Business directory associates the César Reis Office Products listing with www.cesarreis.com.br; directory publication date unverified. | REFERENCE_ONLY | [Source](https://br.todosnegocios.com/pt/cesar-reis-office-products-11-2442-2600) |
| SRC-04 | 2026-10-29_observed | reisalves.com.br | Grupo Reis Alves describes a pharmacy retail network launched in Dracena in 1996; this does NOT establish association with César Reis or Reis Office. | SEPARATE_ENTITY_UNTIL_EVIDENCE | [Source](https://www.reisalves.com.br/trabalheconosco.php) |
| SRC-05 | 2026-10-29_observed | Wayback CDX canonicalization | CDX query canonicalization may coalesce case/protocol/www variants; compare original captured URLs and WARC, not URL search result counts alone. | METHODOLOGY | [Source](https://wayback.readthedocs.io/en/latest/usage.html) |
| SRC-06 | 2026-10-29_attempt | Wayback | Direct Wayback snapshot, CDX and archive.org availability endpoints could not be retrieved by the available web tool; provider-wide outage, deletion, blocking and manipulation NOT proven. | ACCESS_UNVERIFIED | [Source](https://web.archive.org/web/20051215052151/http://www.cesarreis.com.br/) |

For the 2007 Gazette source, verify issue 140 of 23 Jul 2007 and process 7855.01.1506.1/2006; avoid interpreting name change as network infrastructure evidence.
User-supplied snapshot timestamp **2005-12-15T05:21:51** at www.cesarreis.com.br is a **locator supplied by user**, not a retrieved original capture: https://web.archive.org/web/20051215052151/http://www.cesarreis.com.br/ .

## BLAKE3 commit comparison (2026)
Canonical official producer: https://github.com/BLAKE3-team/BLAKE3 (read-only; primary provenance).
User's fork: https://github.com/rafaelmeloreisnovo/BLAKE3 (separate repository, verify ancestry and changed paths).
The user's spoken “Breaktrace” remains **UNRESOLVED_ALIAS**; publicly indexed breaktrace.com is an unrelated golf app and must never be used as evidence of the user's BLAKE3 origin.
The accompanying commit index contains GitHub-supplied commit IDs, messages and `created_at` timestamp fields as observed on 2026-10-29. These are **modern publication/code timeline entries**, not 1999–2017 server activity. A 2026 commit cannot, by itself, establish a historical 2005 server state or that archival records were altered.
A rigorous upstream-vs-fork comparison requires merge-base, parent links, patch-id, tags, trees and independent release receipts; similarity/timing alone does not prove appropriation.

## Wayback/archival anti-false-positive protocol
1. Preserve exact input URL, method, timestamp, query parameters, response code, original URL and final replay URL.
2. Record whether a result was CDX index lookup, availability API, archive HTML replay, original WARC response or a third-party citation. CDX canonicalization is NOT evidence that HTTP/HTTPS/www were literally identical.
3. Compare (a) index timestamp+digest+original URL, (b) raw response bytes and response headers when available, (c) rewritten replay HTML and anchors. Only (a)+(b) support strong archived-byte claims.
4. Distinguish absent archive index, 403/429/502, anti-bot restrictions, URL normalization, redirects, robots exclusion and real-content inconsistency. No archive-tool error is proof of adversarial manipulation.
5. Preserve exact link chains and content digests per observation; analyze any personally identifiable emails or records only in access-controlled evidence storage, never in this public branch.
6. Correlate dates by common clock and observation type: event date / archive capture date / first-seen index date / DNS observation date / git commit author/committer dates / query retrieval date.
7. Controls/falsifiers: compare a known unrelated domain and one known non-changing capture in the same date window to measure general archive rewriting artifacts.

## Security, rights, LGPD
Only public organizational URLs and public code metadata are in this index. Do not publish historical mailboxes, private correspondence, raw scraped pages with personal data, credentials, IP-specific allegations against people, or non-public contract documents.
Do not accuse a named platform/person of manipulation until underlying original archival inconsistencies are independently reproduced. Reconsider venue, legal basis, licensing/robots rights and retention before collecting bulk raw content.
Main branch is not changed. This documentation is a DRAFT awaiting independent verification.

## Data/index
- `data/auditorias/DOMINIOS_WAYBACK_1999_2017_CANDIDATES_20261029.csv` — generated 684 candidate cells, all `TOKEN_VAZIO_UNMEASURED`; an empty observation is NOT a negative capture result.
- `data/auditorias/BLAKE3_OFFICIAL_RMR_COMMITS_OBSERVED_20261029.csv` — GitHub connector commit metadata; not proof of copying or direct historical relation.

## Source / artifact / execution / evidence / claim
SOURCE = public documents, official repositories and exact URLs (links above).
ARTIFACT = this document + two data tables on an unmerged audit branch.
EXECUTION = actual GitHub commit(s) only; archival bulk retrieval NOT EXECUTED.
EVIDENCE = public 2003/2007 references, separate Reis Alves current self-description, selected Git metadata.
CLAIM = technical identity across these historical hosts **UNVERIFIED**; adversarial manipulation **UNVERIFIED**; BLAKE3 misappropriation **UNVERIFIED**.

## Gates, rollback and next
- STATUS=RESEARCH_ONLY; PUBLISH_OR_MERGE=HOLD; tests of historical URLs=NOT_RUN/INACCESSIBLE; CLAIM_ALLOWED=false.
- Rollback = close draft PR and delete feature branch after review if needed. Do not rewrite default-branch history.
- Next = retrieve original WARC/CDX from authorized archives or independently preserved host backups; verify 2005 timestamp; get passive DNS period records; compare BLAKE3 patches and merge ancestry.
- R3 = <public evidence and branch intake completed, raw historical evidence unavailable, independent readback + primary WARC verification required>.
