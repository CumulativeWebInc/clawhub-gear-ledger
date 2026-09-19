# Gear Ledger — `clawhub install cwi/gear-ledger`

Verify any Agent Deck SKU from the public registry and log adoptions — one
fetch, one handoff line, permanent hash-chained provenance.

**Free. No login, no API key, no credentials asked — ever.** License: MIT-0.

## Install

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
