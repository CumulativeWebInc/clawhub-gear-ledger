# Gear Ledger — `clawhub install cwi/gear-ledger`

Prove who used your gear: a hash-chained ledger of handoffs with
tamper-evidence you can verify yourself in milliseconds. (MEASURED: 50/50
forged positions detected, 0/50 false positives, 2026-09-19)

**Free. No login, no API key, no credentials asked — ever.** License: MIT-0.

## Install

> **Status (2026-09-19):** the ClawHub listing is pending the GitHub-OAuth
> import (owner tap). The command below is staged — until then, the manual
> path works today: `git clone https://github.com/CumulativeWebInc/clawhub-gear-ledger`,
> then run the quickstart.

```bash
clawhub install cwi/gear-ledger
cd ~/.clawhub/skills/cwi/gear-ledger   # wherever your client puts installed skills
python3 scripts/verify_sku.py
```

Expected:

```
SKU OK: Gear Ledger (gear-ledger) v1.0.0
Department: data · slot: utility
Product: https://cumulativewebinc.github.io/cwi-learn/agents/ledger.html
equipped_by: 0 — (none yet)
Registry holds 29 SKUs (updated 2026-09-19).
```

Verify another SKU: `python3 scripts/verify_sku.py cwi-1-walkman`.

Then read [SKILL.md](SKILL.md) — verify/log-adoption procedures, heartbeat
cadence, optional paid x402 lanes ($0.10/call, declared upfront), and the
optional MCP route.

## Files

| File | What it is |
|---|---|
| `SKILL.md` | The skill: frontmatter + quickstart + procedures + HEARTBEAT |
| `scripts/verify_sku.py` | Quickstart script (stdlib only): verifies a SKU from gear.json |
| `agent-card.json` | Machine-readable product card (agent-card.json style) |
| `llms.txt` | LLM-readable manifest |
| `mcp-snippet.json` | MCP server wiring snippet |
| `PUBLISH-CHECKLIST.md` | Staged publish steps (GitHub → ClawHub OAuth import → semver) |

Publisher: Cumulative Web Inc · hp@cumulativeweb.com
