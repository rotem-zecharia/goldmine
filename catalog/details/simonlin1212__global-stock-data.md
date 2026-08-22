# simonlin1212/global-stock-data

US stock market data for AI coding assistants — zero-auth, official sources. CBOE options with full Greeks + 0DTE flow, FINRA market-wide short volume, SEC EDGAR filing stream, and a free market-wide 

## installation

**3 steps, 2 minutes.**

```bash

## configuration

| Endpoint | Data |
|----------|------|
| **CBOE official** | Full chain + **IV + delta/gamma/vega/theta/rho**, plus **0DTE filtering** and **unusual-flow** detection (vol/OI > 1 = new positioning) |
| Yahoo (fallback) | Options chain, all expiries — **no Greeks** |

## tools

| Endpoint | Data |
|----------|------|
| Sina / Tencent / Eastmoney push2 | US/HK real-time quotes, 25-78 fields |
| Sina / Yahoo chart | K-line, daily→minute, US back to 1984 |
| Eastmoney datacenter / GMAININDICATOR | Statements + key metrics (bilingual) |
| Yahoo quoteSummary | 23 modules: financials / analysts / institutional holdings |
| Eastmoney push2his | Daily main/large/medium/small fund flow |
| Eastmoney search / push2 list / Yahoo search / SEC CIK | Search / full-market list / news / ticker↔CIK |

Every source is free, no API key. Yahoo crumb is auto-managed; SEC EDGAR only needs a declared User-Agent.

</details>

---
