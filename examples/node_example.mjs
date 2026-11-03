// FinBridge REST API — Node.js example (Node 18+, built-in fetch).
//   export FINBRIDGE_API_KEY=smcp_...
//   node examples/node_example.mjs
const BASE = process.env.FINBRIDGE_BASE ?? "https://mcp.gronox.kr";
const KEY = process.env.FINBRIDGE_API_KEY;
if (!KEY) throw new Error("set FINBRIDGE_API_KEY first");

async function get(path, params = {}) {
  const url = new URL(path, BASE);
  for (const [k, v] of Object.entries(params)) url.searchParams.set(k, String(v));
  const res = await fetch(url, { headers: { Authorization: `Bearer ${KEY}` } });
  if (!res.ok) throw new Error(`${res.status} ${await res.text()}`);
  return res.json();
}

const profile = await get("/api/v1/companies/kr/005930");
console.log(JSON.stringify(profile).slice(0, 400));

const hist = await get("/api/v1/companies/kr/010130/revision-history", { year: 2024, report: "annual", as_of: "2025-06-30" });
const pit = hist.point_in_time ?? {};
console.log("as of 2025-06-30:", pit.status, pit.receipt_id, pit.metrics?.net_income);
