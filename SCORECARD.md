# Gear Ledger — self-scorecard (v1.1.0, 2026-09-19)

**Method:** self-scored against the five dimensions published by
[askill.sh](https://www.producthunt.com/products/askill-sh) (Safety, Clarity,
Reusability, Completeness, Actionability), 0–5 each. Evidence-bound: every
score cites something you can re-run or read in this repo. Re-score after any
functional change.

| Dimension | Score | Evidence |
|---|---|---|
| **Safety** — no hardcoded secrets, dangerous commands, destructive ops | 5/5 | Quickstart reads one public HTTPS URL, writes nothing (stdout only), reads no env. Frontmatter declares `env: []`. Install test asserts the skill never prompts for credentials. |
| **Clarity** — well-documented and structured | 4/5 | SKILL.md: install-first README, expected-output block, truth labels. Deduction: no troubleshooting section for fetch failures. |
| **Reusability** — works across projects, not repo-specific | 4/5 | The SKU-verify + handoff pattern works for any product carried in a public `gear.json`-style registry; the bundled registry is CWI's 29-SKU Agent Deck line. |
| **Completeness** — covers what it claims | 4/5 | Claims: verify any SKU from the registry, log adoptions with a one-line handoff. MEASURED: 29-SKU registry verify green (2026-09-19); tamper-evidence 50/50 forged positions detected, 0/50 false positives. Deduction: ledger backend is local; GitHub transport is a named GAP. |
| **Actionability** — instructions concrete and executable | 4/5 | Copy-paste quickstart, one command, expected output shown. Deduction: `clawhub install cwi/gear-ledger` does not resolve until the ClawHub listing is live; manual clone path documented below. |

**Total: 21/25 (84)**

## Known gaps (disclosed, not hidden)
- ClawHub listing pending GitHub-OAuth import (human tap) — `clawhub install cwi/gear-ledger` is TARGET, not LIVE.
- Ledger backend is LOCAL (GitHub transport = named GAP, disclosed in demos).
- Paid x402 lanes ($0.10/call, Base Sepolia testnet) are optional and declared in frontmatter; the free lane is complete without them.
- No troubleshooting section yet (costs 1 Clarity point).

## Manual install (works today)
```bash
git clone https://github.com/CumulativeWebInc/clawhub-gear-ledger
cd clawhub-gear-ledger
python3 scripts/verify_sku.py
# --self-scan prints the install-time self-declaration (RoleCraft-style)
python3 scripts/verify_sku.py --self-scan
```
