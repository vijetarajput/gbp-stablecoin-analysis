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


**Verification: GBPe (Monerium GBP e-money)**
- Gnosis contract: 0x8e34bfec4f6eb781f9743d9b4af99cd23f9b7053, 18 decimals.
- Triangulated across three sources: CoinGecko, Gnosisscan, and Monerium's official token documentation (docs.monerium.com/tokens).
- Monerium docs also list GBPe on Ethereum, Polygon and Arbitrum. This project currently tracks Gnosis only.
- CoinGecko notes the token recently migrated to a new contract. An older address (0x5Cb9073902F2035222B9749F8fB0c9BFe5527108) appears on a third-party site; not verified as official. Dune tables must be checked against the new contract before use.
- Legal model: issued as an e-money token. This differs from tGBP, whose issuer states it is not e-money.
- Supply: ~505K GBPe (~$670K). Smallest of the three coins reviewed.
- Activity: 1,302 holders and 203,735 transfers on Gnosis, far more than GBPA or tGBP on Ethereum, despite the smallest supply.
- Hypothesis: high transfer count may reflect card payments (e.g., Gnosis Pay). To be tested with Dune data.
- Data quality note: CoinGecko shows an all-time high of $53.28, almost certainly a thin-liquidity glitch; excluded from analysis.
- Evidence: [Gnosisscan screenshot](evidence/2026-10-13_gbpe_gnosisscan_verification.png) · [Monerium docs screenshot](evidence/2026-10-13_gbpe_monerium_docs.png)

**Updated comparison (13 Oct 2026)**

| | GBPA | tGBP | GBPe |
|---|---|---|---|
| Issuer | Agant | BCP Technologies Ltd | Monerium |
| Main chain checked | Ethereum | Ethereum | Gnosis |
| Supply (chain checked) | ~1.0M | ~14.3M | ~505K |
| Holders (chain checked) | 2 | 309 | 1,302 |
| Decimals | 6 | 18 | 18 |
| Legal model | Not yet checked | Not e-money (MLR registration) | E-money |

**Key pattern:** size and usage do not match. The largest coin (tGBP) shows low activity; the smallest (GBPe) shows the most transfers.


**Check: poundtoken (1GBP), possible successor of GBPT**
- Background: GBPT ("poundtoken") was launched in July 2022 by Blackfridge (Isle of Man), per press coverage at the time. No recent news found.
- Not listed on CoinGecko (search for "poundtoken" returned no results).
- Etherscan search found a token named "poundtoken" with symbol 1GBP (not GBPT): 0x86b4dbe5d203e634a12364c0e428fa242a3fba98, 18 decimals.
- Supply ~45.8K on Ethereum, 177 holders, 3,088 total transfers.
- Activity: last transfer ~67 days ago; previous ones ~77 and ~148 days ago. The token is effectively dormant.
- Etherscan token information is unverified ("?" icon), unlike GBPA and tGBP.
- The website linked on Etherscan (poundtoken.io) now hosts a UK crypto information site that explicitly states it is not an issuer. This suggests the original project's domain is no longer controlled by the issuer.
- Status: DORMANT. Link to the original Blackfridge GBPT is unconfirmed.
- Source quality lesson: a 2026 exchange blog post described GBPT as one of the most popular GBP stablecoins. On-chain and CoinGecko evidence does not support this claim.
- Evidence: [Etherscan screenshot](evidence/2026-10-13_1gbp_poundtoken_etherscan.png) · [poundtoken.io homepage](evidence/2026-10-13_poundtoken_io_homepage.png) · [poundtoken.io "not an issuer" section](evidence/2026-10-13_poundtoken_io_not_issuer.png)

**Second pattern:** some GBP stablecoins launch and then go quiet. Launching a sterling stablecoin is not the same as achieving adoption.
