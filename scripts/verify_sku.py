#!/usr/bin/env python3
"""Gear Ledger quickstart: verify an Agent Deck SKU from the registry.

Free lane, no credentials. Stdlib only.
Usage: python3 verify_sku.py [sku-gear-id]   (default: gear-ledger)
Exit 0 on verified SKU; exit 1 if the SKU is not in the registry.
"""
import json
import sys
import urllib.request

GEAR_URL = "https://cumulativewebinc.github.io/cwi-learn/gear.json"


def fetch(url, retries=2):
    """Fetch JSON. curl-first: this VM's Fastly path truncates Python-urllib
    bodies (IncompleteRead) while curl receives full bodies with
    Accept-Encoding: identity. urllib is the fallback."""
    import subprocess, shutil
    if shutil.which("curl"):
        last = None
        for _ in range(retries + 1):
            try:
                p = subprocess.run(
                    ["curl", "-sS", "--fail", "--max-time", "30",
                     "-H", "Accept-Encoding: identity",
                     "-A", "clawhub-skill/1.0.0", url],
                    capture_output=True, text=True, timeout=40)
                if p.returncode == 0:
                    return json.loads(p.stdout)
                last = RuntimeError(p.stderr.strip() or f"curl rc={p.returncode}")
            except Exception as e:
                last = e
        raise last
    last = None
    for _ in range(retries + 1):
        try:
            req = urllib.request.Request(
                url,
                headers={"Accept-Encoding": "identity",
                         "User-Agent": "clawhub-skill/1.0.0"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except Exception as e:
            last = e
    raise last

def main():
    want = sys.argv[1] if len(sys.argv) > 1 else "gear-ledger"
    try:
        reg = fetch(GEAR_URL)
    except Exception as e:
        print(f"REGISTRY FAIL: could not fetch gear.json ({e})", file=sys.stderr)
        return 1
    items = reg.get("items", [])
    match = next((i for i in items if i.get("gear") == want), None)
    if match is None:
        print(f"SKU FAIL: '{want}' is not in the Agent Deck registry. Do not log it.", file=sys.stderr)
        return 1
    eq = match.get("equipped_by", [])
    print(f"SKU OK: {match.get('name')} ({match.get('gear')}) v{match.get('version')}")
    print(f"Department: {match.get('department')} · slot: {match.get('slot')}")
    print(f"Product: {match.get('product_url')}")
    print(f"equipped_by: {len(eq)} — {', '.join(eq) if eq else '(none yet)'}")
    print(f"Registry holds {len(items)} SKUs (updated {reg.get('updated')}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
