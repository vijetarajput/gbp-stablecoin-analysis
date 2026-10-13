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
