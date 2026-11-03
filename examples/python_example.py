"""FinBridge REST API — Python example (standard library only).

    export FINBRIDGE_API_KEY=smcp_...
    python examples/python_example.py
"""
import json
import os
import urllib.parse
import urllib.request

BASE = os.environ.get("FINBRIDGE_BASE", "https://mcp.gronox.kr")
KEY = os.environ["FINBRIDGE_API_KEY"]


def get(path: str, **params) -> dict:
    url = f"{BASE}{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    # Some edge proxies reject the default "Python-urllib" user agent, so send our own.
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {KEY}", "User-Agent": "finbridge-rest-examples/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


# Korea Zinc FY2024 annual report: what was public on 2025-06-30?
hist = get("/api/v1/companies/kr/010130/revision-history", year=2024, report="annual", as_of="2025-06-30")
pit = hist.get("point_in_time") or {}
print("status:", pit.get("status"))
print("filing used:", pit.get("receipt_id"), pit.get("publication_date"))
print("net income:", (pit.get("metrics") or {}).get("net_income"))
for v in hist.get("versions", []):
    print(" version", v.get("receipt_id"), v.get("publication_date"), (v.get("metrics") or {}).get("net_income"))

# Annual statements for a US company
fin = get("/api/v1/companies/us/AAPL/financials", limit=3)
print(json.dumps(fin, ensure_ascii=False)[:400])
