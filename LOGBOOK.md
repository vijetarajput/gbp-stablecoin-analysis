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


**Verification: VGBP (VNX British Pound)**
- Solana token: 5H4voZhzySsVvwVYDAKku8MZGuYBC7cXaBKDPW4YHWW1, 9 decimals (different again from GBPA's 6 and tGBP/GBPe's 18).
- Issuer: VNX Global Ltd, licensed by the Bermuda Monetary Authority (Class M digital asset business licence), per CoinGecko. First offshore issuer found in this project.
- First mint: 20 December 2024 (Solscan).
- Supply: ~72.7K on Solana out of ~126.6K total (CoinGecko). Remaining ~54K appears to be on other chains, not yet identified.
- Holders on Solana: 572. Total transfers: 265,177.
- Activity check: recent transfers are tiny ($0.12–$0.26), repeat the same wallets, and loop between DEX pools (Raydium, Meteora) via an aggregator. This pattern is consistent with arbitrage bots rather than real payments.
- 24h trading volume: ~$5.65 (CoinGecko coin page).
- Source conflict: CoinGecko's GBP category summary described VGBP at $1.43 with $509K daily volume. The coin page shows $1.34 and $5.65. The coin page and on-chain data were used.
- Evidence: [Solscan overview](evidence/2026-10-13_vgbp_solscan_1.png) · [Solscan transfers](evidence/2026-10-13_vgbp_solscan_2.png) · [CoinGecko overview](evidence/2026-10-13_vgbp_coingecko_issuer_1.png) · [CoinGecko issuer description](evidence/2026-10-13_vgbp_coingecko_issuer_2.png)

**Methodology lesson:** raw transfer counts can be inflated by bots. High transfer numbers do not prove real usage. The GBPe "payments" hypothesis must be tested with this in mind (e.g., by separating DEX/bot activity from wallet-to-wallet or card-related flows).

**Coins reviewed so far (13 Oct 2026)**

| | GBPA | tGBP | GBPe | poundtoken (1GBP) | VGBP |
|---|---|---|---|---|---|
| Issuer | Agant | BCP Technologies Ltd | Monerium | Unconfirmed | VNX Global Ltd |
| Jurisdiction / model | Not yet checked | UK, MLR registration, not e-money | E-money | Unknown | Bermuda licence |
| Chain checked | Ethereum |


**Verification: GBPm (Mento British Pound, formerly cGBP)**
- Search for "Celo British Pound" on CoinGecko returned nothing. Further search showed the token was renamed.
- Celo contract: 0xccf663b1ff11028f0b19058d0f7b674004a40746, 18 decimals. Address matched across GeckoTerminal, a third-party listing, and Celoscan.
- Rename confirmed on Celoscan: banner states Celo stablecoins have rebranded into Mento (cGBP → GBPm). Website: mento.org.
- Model: no company issuer. DefiLlama describes GBPm as a GBP-pegged synthetic stablecoin minted through CDPs, with USDm deposited as collateral. Category: crypto-backed.
- Supply: ~234.6K on Celo (Celoscan and DefiLlama live page agree). DefiLlama's chart shows supply fell from roughly 450K–500K in April 2026 to ~234K now.
- Holders: 307. Total transfers: 61,971.
- Activity: the main GeckoTerminal pool (cGBP/USDT, Uniswap V3 on Celo) showed $0 trading volume in the last 24 hours; most recent trades were on 8 October.
- Source quality lesson: a search snippet suggested ~88.5K on Celo and ~173K on Monad. The live DefiLlama page and Celoscan both show ~234.6K on Celo. The snippet was outdated. Always open the live page.
- Search lesson: GeckoTerminal results for "cGBP" also returned unrelated Solana pools whose addresses happen to start with "CGBP". Matching letters is not evidence.
- Evidence: [Celoscan screenshot](evidence/2026-10-13_gbpm_celoscan_verification.png) · [DefiLlama model screenshot](evidence/2026-10-13_gbpm_defillama_model.png)

**Coins reviewed (13 Oct 2026)**

| | GBPA | tGBP | GBPe | poundtoken (1GBP) | VGBP | GBPm |
|---|---|---|---|---|---|---|
| Issuer | Agant | BCP Technologies Ltd | Monerium | Unconfirmed | VNX Global Ltd | None (Mento Protocol) |
| Model | Not yet checked | UK MLR registration, not e-money | E-money | Unknown | Bermuda licence | Crypto-backed CDP |
| Chain checked | Ethereum | Ethereum | Gnosis | Ethereum | Solana | Celo |
| Supply (chain checked) | ~1.0M | ~14.3M | ~505K | ~45.8K | ~72.7K | ~234.6K |
| Holders (chain checked) | 2 | 309 | 1,302 | 177 | 572 | 307 |
| Decimals | 6 | 18 | 18 | 18 | 9 | 18 |
| Status | Active, concentrated | Active, low usage | Active, many transfers | Dormant | Active, bot-dominated | Shrinking, low trading |

**Patterns (updated)**
1. Size and usage do not match.
2. Some GBP stablecoins launch and go quiet; others shrink.
3. Supply is concentrated in a few wallets.
4. Four distinct models exist: UK-registered fiat-backed, e-money, offshore-licensed, and decentralised crypto-backed.
5. Transfer counts alone are misleading because of bot activity.
6. Data sources often disagree or go stale; on-chain explorers and live pages are the reference.


**Update: GBPA regulatory status**
- Issuer footer on agant.io names Agant Finance Limited, registered with the FCA as a cryptoasset firm under the Money Laundering Regulations 2017 (FRN 1037671).
- The issuer states that GBPA services are not covered by the Financial Services Compensation Scheme (FSCS) or the Financial Ombudsman Service (FOS).
- The footer does not state whether GBPA is e-money, so no claim is made either way.
- This resolves the "Not yet checked" entry for GBPA in earlier tables. Model: UK MLR registration (same category as tGBP).
- Evidence: [Agant footer screenshot](evidence/2026-10-13_gbpa_agant_issuer_footer.png)

**Regulatory observation:** both UK-based issuers reviewed (Agant and BCP Technologies) operate under anti-money-laundering registration only, and neither product is covered by the FSCS. This is the protection gap that the Bank of England's proposed regime for systemic sterling stablecoins aims to address.


---

## 15 October 2026

**Correction: existing GBP stablecoin dashboard found**
- A Dune search for "tgbp" surfaced "Stablecoin Analysis: British Sterling Pound" by @duneuk (dune.com/duneuk/stablecoin-analysis-british-sterling-pound), last updated about two months earlier. It did not appear in the earlier "GBP" search.
- It covers GBPT, VGBP, TGBP and a token labelled "CCBP" (likely cGBP), with weekly supply, DEX volume, active addresses, comparison with USD/EUR stablecoins, and lending/borrowing. Its lending section concludes GBP stablecoins are largely absent from DeFi lending.
- This corrects the 13 October note that no comprehensive GBP dashboard existed.
- Remaining gaps this project addresses: newer tokens (GBPA, GBPe, GBPm), issuer and legal-model verification, holder concentration, separation of bot activity from genuine use, dormant tokens (GBPT appears dormant), and links to the digital pound debate.
- The @duneuk work will be cited as related work.
- Evidence: [@duneuk dashboard screenshot](evidence/2026-10-15_duneuk_gbp_dashboard.png)

**Dune tables: tGBP**
- Search "tgbp" returned decoded tables under tgbp_ethereum.stabletokenv1oft_*. "OFT" indicates a LayerZero Omnichain Fungible Token, consistent with tGBP's presence on 8 chains. evt_oftreceived records cross-chain arrivals.


**Review of @duneuk "GBP Supply Tracking" query (dune.com/queries/6276583)**
- Forked from @0nchainlabs. Covers GBPT and VGBP (Base) via a balances template, GBPT via tokens_ethereum.balances, tGBP via mint/burn in tokens.transfers, and VGBP + GBPm on Celo via raw celo.logs.
- Correction to earlier note: GBPm (Celo) is included in this query. Not included: GBPA, GBPe (Gnosis), and VGBP on Solana.
- New address found: VGBP on Celo, 0x7ae4265ecfc1f31bc0e112dfcfe3d78e01f4bb7f (to verify). VGBP on Base: 0xaeb4bb7debd1e5e82266f7c3b5cff56b3a7bf411 (to verify).
- The query labels 0x86b4...fba98 as GBPT, supporting (but not proving) that the "poundtoken (1GBP)" contract is the original Blackfridge GBPT.
- Potential data-quality issues (to confirm by running the query):
  - tGBP contract address appears mistyped: "...bedf1519966..." instead of the verified "...bed1f519966...".
  - tGBP amounts are divided by 1e6, but the verified contract uses 18 decimals.
  - Weekly SUM of balance snapshots may overstate supply if the source tables are daily.
- Methods to reuse: mint/burn supply from tokens.transfers; raw logs with the ERC-20 Transfer topic for chains without decoded tables (applicable to Gnosis/GBPe).
