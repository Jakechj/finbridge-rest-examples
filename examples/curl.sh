#!/usr/bin/env bash
# FinBridge REST API — curl examples.
# Get a free API key at https://finbridge.gronox.kr/login, then:
#   export FINBRIDGE_API_KEY=smcp_...
#   bash examples/curl.sh
set -euo pipefail
: "${FINBRIDGE_API_KEY:?set FINBRIDGE_API_KEY first}"
BASE="${FINBRIDGE_BASE:-https://mcp.gronox.kr}"
H=(-sS -H "Authorization: Bearer $FINBRIDGE_API_KEY")

echo "== Company profile: Samsung Electronics (KRX 005930)"
curl "${H[@]}" "$BASE/api/v1/companies/kr/005930"; echo

echo "== Annual financial statements, last 3 years: Apple (AAPL)"
curl "${H[@]}" "$BASE/api/v1/companies/us/AAPL/financials?limit=3"; echo

echo "== Every filed version of Korea Zinc's FY2024 annual report, as known on 2025-06-30"
curl "${H[@]}" "$BASE/api/v1/companies/kr/010130/revision-history?year=2024&report=annual&as_of=2025-06-30"; echo
