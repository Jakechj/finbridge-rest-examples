# FinBridge REST API examples

Short, runnable examples for the [FinBridge](https://finbridge.gronox.kr) REST API: Korean (DART), US (SEC EDGAR), Taiwan, Japan and Europe company filings and financial statements. Every response states when its data is from (`data_as_of`) and links the source filing.

## Setup

1. Get a free API key at https://finbridge.gronox.kr/login (Google sign-in).
2. `export FINBRIDGE_API_KEY=smcp_...`

Requests use `Authorization: Bearer <key>`. The full API description is at https://mcp.gronox.kr/api/v1/openapi.json.

## Run

```sh
bash examples/curl.sh
python examples/python_example.py
node examples/node_example.mjs
```

No third-party packages are needed (Python standard library, Node 18+ fetch).

## Endpoints used

| Endpoint | What it returns |
|---|---|
| `GET /api/v1/companies/{market}/{symbol}` | Company profile, key figures, latest filings |
| `GET /api/v1/companies/{market}/{symbol}/financials?limit=` | Normalised financial statement rows |
| `GET /api/v1/companies/kr/{symbol}/revision-history?year=&report=&as_of=` | Every filed version of a Korean periodic report (original and each amendment), and the version that was public on `as_of` |

`market` is `kr`, `us`, `tw`, `jp` or `eu`. Company codes work as you would type them: `005930`, `AAPL`, `2330.TW`, `7203.T`.

## Point-in-time example

Korea Zinc amended its FY2024 annual report twice. Asking for the figures as known on 2025-06-30 returns the 2025-03-31 amendment, not the later 2026 restatement:

```sh
curl -H "Authorization: Bearer $FINBRIDGE_API_KEY" \
  "https://mcp.gronox.kr/api/v1/companies/kr/010130/revision-history?year=2024&report=annual&as_of=2025-06-30"
```

Free-plan limits (calls per day, years of history) apply. Data is for information only and is not investment advice.

## License

MIT — see [LICENSE](LICENSE).
