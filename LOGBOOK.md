# Research Logbook

A dated record of what was found, how it was verified, and decisions taken.

---

## 13 October 2026

**Data access**
- Dune's curated stablecoin tables (stablecoins_evm.*) are Enterprise-only. Decision: build the analysis from general and project-specific tables instead.

**Existing work reviewed**
- Searched Dune for "GBP". Found a small community dashboard for GBPA by @rchen8 (dune.com/rchen8/gbpa) and decoded transfer data for Monerium GBPe on Gnosis.
- No comprehensive GBP stablecoin dashboard found. This is the gap this project addresses.

**Method learned**
- Supply can be calculated as cumulative mints minus burns (approach used in @rchen8's GBPA query).

**Market size (CoinGecko, 13 Oct 2026)**
- Total GBP stablecoin market cap: ~$31.8M, compared with $300B+ for all stablecoins.

**Verification: GBPA (Agant GBP)**
- Ethereum contract: 0xbbe6aab0ed76e90aea0d1cd978ec231c8adcdf8b
- Confirmed on Etherscan: name "Agant GBP", symbol GBPA, 6 decimals, linked to agant.io/gbpa.
- Observation: ~1.0M GBPA on Ethereum held by only 2 addresses. Etherscan reports whale concentration of 99.99%, meaning a single address holds almost the entire Ethereum supply. Broad adoption is not yet visible on Ethereum.
- Evidence: [Etherscan screenshot](evidence/2026-10-13_gbpa_etherscan_verification.png) · [Live Etherscan page](https://etherscan.io/token/0xbbe6aab0ed76e90aea0d1cd978ec231c8adcdf8b)
  
  
**Verification: tGBP (Tokenised GBP)**
- Ethereum contract: 0x27f6c8289550fce67f6b50bed1f519966afe5287 (found via CoinGecko, confirmed on Etherscan).
- Name tGBP, 18 decimals (GBPA uses 6, so supply queries must divide by 1e18, not 1e6).
- Issuer conflict resolved: one secondary source named Transfero, but the official site (tokenisedgbp.com) names BCP Technologies Ltd, FCA reference 928840.
- Regulatory note: FCA registration is under the Money Laundering Regulations 2017 only. The site states tGBP is not e-money and is not protected by the FSCS.
- Official contract register lists 8 chains: Ethereum, Base, Solana, Arbitrum, Polygon, BNB Chain, Gnosis, Avalanche (CoinGecko description says six).
- Supply: ~14.3M on Ethereum out of ~20M total (CoinGecko). Price ~$1.32, consistent with the £1 peg.
- Holders on Ethereum: 309. Top 5 hold 85%, top 10 hold 96%, Gini 0.98. Holder base is wider than GBPA but still highly concentrated.
- Activity: ~$67K daily trading volume against ~$26M supply (~0.25% per day), suggesting low usage.
- Evidence: [Etherscan screenshot](evidence/2026-10-13_tgbp_etherscan_verification.png) · [Issuer footer screenshot](evidence/2026-10-13_tgbp_issuer_footer.png)

**Early comparison (13 Oct 2026)**

| | GBPA | tGBP |
|---|---|---|
| Issuer | Agant | BCP Technologies Ltd |
| Ethereum supply | ~1.0M | ~14.3M |
| Ethereum holders | 2 | 309 |
| Top-10 share | 100% | 96% |
| Decimals | 6 | 18 |
