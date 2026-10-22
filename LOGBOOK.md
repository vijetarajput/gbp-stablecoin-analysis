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

*(Five-coin summary superseded by the six-coin table below.)*

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

**Verification: VGBP on Base and Celo**
- Base: 0xaeb4bb7debd1e5e82266f7c3b5cff56b3a7bf411, VNX British Pound (VGBP), 18 decimals, ~25,299 supply, 287 holders, website vnx.io (Basescan).
- Celo: 0x7ae4265ecfc1f31bc0e112dfcfe3d78e01f4bb7f, VNX British Pound (VGBP), 18 decimals, ~28,606 supply, 20 holders, 1,123 transfers; most recent transfers 14 and 86 days ago (Celoscan).
- Decimals differ by chain for the same token (9 on Solana, 18 on Base and Celo). Queries must take decimals per chain, not per token.
- Reconciliation: Solana 72,689.71 + Base 25,299.32 + Celo 28,606.18 = 126,595.21, matching CoinGecko's total supply of 126,595. This confirms VGBP is deployed on exactly these three chains.
- Evidence: [Basescan screenshot](evidence/2026-10-15_vgbp_base_basescan.png) · [Celoscan screenshot](evidence/2026-10-15_vgbp_celo_celoscan.png)

**Dune tables: GBPe (migration confirmed)**
- Search "monerium" returned two GBPe transfer tables on Gnosis, both maintained by @dune.
- monerium_gbpe_v2_gnosis.gbpe_evt_transfer: table preview shows contract_address 0x8e34bfec4f6eb781f9743d9b4af99cd23f9b7053, the current contract verified on 13 Oct.
- monerium_gbpe_gnosis.gbp_evt_transfer: table preview shows contract_address 0x5cb9073902f2035222b9749f8fb0c9bfe5527108, the older address previously seen only on a third-party site. This confirms it as the pre-migration contract.
- Full GBPe supply history will need both tables (v1 before migration, v2 after).
- Clue for the payments hypothesis: in both tables, many transactions are submitted by the same sender, 0x90830ed5... (evt_tx_from). This pattern is consistent with a relayer service submitting transactions on users' behalf, as card-payment products often do. To identify on Gnosisscan.
- Idea: Monerium also issues EURe on several chains. Comparing GBPe and EURe (same issuer and technology, different currency) may isolate currency-specific demand.
- Evidence: [v2 table](evidence/2026-10-15_gbpe_v2_dune_table.png) · [v1 table](evidence/2026-10-15_gbpe_v1_dune_table.png)

---

## 16 October 2026

**GBPe relayer investigation**
- Opened a sampled GBPe v2 transaction on Gnosisscan: 0x56f98cd1d3a473655fd25ae55c64f6e56e2f4ca55a80cfe10af07067cb23df2d (block 45736440, 18 April 2026).
- The explorer tags the transaction "Gnosis Pay". The sender, 0x90830Ed558f12D826370DC52E9D87947A7F18De9, called a contract labelled "Spender Module".
- Transfer: 6.34 GBPe (about $8.43) from a user Safe wallet to a GnosisSafeL2 address. The explorer labels the user wallet "Gnosis Pay Compromised Safe 16775"; the meaning of this label was not investigated and it is not used in the analysis.
- The sender is an externally owned account (EOA) with 3,914,470 transactions and about 193 xDAI held for gas fees. No explorer label.
- Interpretation: consistent with a Gnosis Pay relayer submitting card payments on users' behalf. Based on one sampled transaction; the share of payments among all GBPe transfers was not measured.
- Contrast with VGBP: the ten most recent VGBP transfers on Solana (13 Oct) were tiny DEX loops consistent with bots, whereas the sampled GBPe activity is payment-like.
- Evidence: [transaction](evidence/2026-10-16_gbpe_relayer_tx.png) · [relayer address](evidence/2026-10-16_gbpe_relayer_address.png)

**tGBP market data (CoinGecko, 12 Nov 2025 – 15 Oct 2026)**
- Downloaded daily market capitalization, volume, and closing price from CoinGecko's historical data page. Saved as [data/coingecko_tgbp_daily_2025-11-12_to_2026-10-15.csv](data/coingecko_tgbp_daily_2025-11-12_to_2026-10-15.csv).
- Implied supply (market cap ÷ closing price) rose from ~1.1M tokens (Nov 2025) to a peak of ~25.5M (mid-2026), then fell to ~20M.
- Almost all change occurred on six days: 3 Dec 2025, 1 Mar, 24 Mar, 21 Apr, 14 Jul, and 8 Aug 2026. On 8 Aug, supply fell ~19% (~£5M redeemed). This step pattern suggests a few large institutional mints and redemptions.
- USD market cap also moves with the GBP/USD exchange rate, so supply is measured in tokens (≈ GBP), not USD.
- First two days (market cap not tracked) and the final partial day were excluded.

**Corrections and additions**
- tGBP trading volume: the 13 Oct figure (~$67K/day, ~0.25% of supply) was a single-day snapshot. Averages from the daily data are ~0.42% of market cap per day over the year and ~0.76% over the last 30 days. Averages are used from now on.
- GBPA total supply: about 1.9M tokens across all chains, per the @rchen8 community dashboard (dune.com/rchen8/gbpa); ~1.0M of this is on Ethereum. Used for the market-size total of ~$30.2M.
- @duneuk query: the tGBP address mismatch (two transposed characters) and the 1e6 divisor are visible directly in the query text, so they are confirmed as written. Only their effect on the dashboard's outputs remains untested.
- VGBP bot assessment: based on the ten most recent transfers shown on Solscan on 13 Oct, not a full-period analysis.

---

## 17 October 2026

**GBPe payment share (sample of 100 transfers)**
- Copied the 100 most recent GBPe transfers from Gnosisscan's token transfer list on 17 Oct 2026 (about 17 hours of activity). Saved as [data/gnosisscan_gbpe_recent_100_transfers_2026-10-17.csv](data/gnosisscan_gbpe_recent_100_transfers_2026-10-17.csv).
- 47 transfers (47 of 72 distinct transactions, 65%) used method 0x8a320255, the same Spender Module call as the transaction tagged "Gnosis Pay". All moved GBPe from a user Safe to a settlement Safe. Median amount 11 GBPe; total ~2,459 GBPe.
- In three cases, a CoW Protocol settlement of the same amount (10.7, 34.99, 66.75 GBPe) shortly preceded the payment, suggesting users converted other assets into GBPe just before spending.
- Other transfers were DEX and aggregator trades (CoW, LiFi, Uniswap, RelayRouter); 24 were dust transfers below 0.001 GBPe, similar to bot activity seen for VGBP.
- Limitation: classification relies on the method identifier matching the sampled Gnosis Pay transaction; covers 17 hours only.

**GBPe card payments over 12 months (full-period analysis)**
- Collected all GBPe v2 transfers on Gnosis from the public Blockscout API using Google Colab (Dune query creation is not available on the free plan). Window: 17 Oct 2025 – 16 Oct 2026. 501 duplicate rows from API pagination were removed, leaving 84,382 transfers in 67,494 distinct transactions.
- Data: [data/gbpe_v2_transfers_12m.csv](data/gbpe_v2_transfers_12m.csv) · Monthly summary: [data/gbpe_monthly_card_payments_2025-10_to_2026-10.csv](data/gbpe_monthly_card_payments_2025-10_to_2026-10.csv) · Scripts: [scripts/](scripts/)
- Card payments (method 0x8a320255, Gnosis Pay Spender Module): 52,662 transactions, 78% of all GBPe transactions (79% excluding dust). All were sent to a single settlement address.
- 488 distinct wallets made card payments; 347 made 10 or more. The top 10 wallets accounted for only 14% of payments, in contrast to the high concentration of token holdings.
- Median card payment 11 GBPe; total ~3.0M GBPe over the year. By value, card payments were only 13% of non-mint/burn transfer volume, because trades are larger.
- Trend: monthly card payments fell 59% between Nov 2025 and Sep 2026; active paying wallets fell 39% from their Dec 2025 peak (206) to Sep 2026 (125).
- Monerium minted ~3.1M and burned ~3.1M GBPe over the year, about six times the outstanding supply, indicating active on/off-ramping.
- Correction: the "swap immediately before payment" pattern seen in three cases of the 100-transfer sample occurred in only 29 of 52,662 payments (0.1%) over the full year. It is not a meaningful pattern and is no longer claimed.
- Evidence: [figure](evidence/fig_gbpe_card_payments.png)

**Literature and regulatory context reviewed**
- Read and verified 11 sources on stablecoin economics, on-chain measurement, and regulation, including Gorton & Zhang (2023), Lyons & Viswanath-Natraj (2023), Mizrach (2023), the BIS Annual Economic Report 2025 (ch. III), Cong et al. (2023) on wash trading, Daian et al. (2020) on DEX arbitrage bots, and a 2025 systematization of stablecoin designs (arXiv:2506.17622).
- Regulatory update: the FCA published final rules for qualifying stablecoin issuers on 30 June 2026 (following CP25/14), applying to firms authorised under the new regime from 25 October 2027. Until then, UK issuers such as BCP Technologies and Agant remain under MLR registration only.
- EU comparison: under MiCA (Regulation (EU) 2023/1114), e-money tokens must be issued by credit or e-money institutions and be redeemable at par at any time, a protection not stated by the UK MLR-registered issuers reviewed here.
- Benchmark for GBPe: Visa's adjusted stablecoin metrics show retail-sized transactions were under 1% of adjusted stablecoin volume in the 12 months to March 2025. GBPe, where 78% of transactions are card payments, is an unusual case of retail payment use.
- Mizrach (2023) finds that many stablecoins fail over time, consistent with the dormancy of 1GBP and the contraction of GBPm.


---

## 18 October 2026

**DefiLlama coverage gap**
- DefiLlama tracked tGBP and GBPA as stablecoins, but GBPe appeared only as a token page, while Monerium's EURe was tracked as a stablecoin.
- Submitted PR #948 to DefiLlama/peggedassets-server, adding GBPe on six chains with addresses from Monerium's token documentation. Merged 20 Oct 2026. Record and evidence: [vijeta-research/open-source-contributions/defillama](https://github.com/vijetarajput/vijeta-research/tree/main/open-source-contributions/defillama)

---

## 20 October 2026

**DefiLlama cross-checked against this register**
- GBPA: DefiLlama shows ~1.9M in total, confirming the 16 Oct figure from the @rchen8 dashboard. By chain: Ethereum 1.0M, Arc 575,218, Base 250,011, Tempo 50,001, Solana 25,015. The Ethereum figure matches Etherscan (1,000,102; 6 decimals). Arc supply rose 53% over 30 days. The register lists only Ethereum; the other chains are not yet verified on their own explorers.
- VGBP: DefiLlama's total of 126,595.21 matches this register exactly (Solana 72,689.71, Celo 28,606.18, Base 25,299.32).
- Correction: the 15 Oct entry stated that VGBP is deployed on exactly three chains. DefiLlama also lists an Ethereum contract (0x34C9C643Becd939c950bB9F141E35777559817CB), and Etherscan confirms it is VNX British Pound (VGBP), 18 decimals, with zero supply and zero holders. VGBP tokens are held on exactly three chains, but a fourth contract exists. Not added to the register because it holds no tokens.
- GBPe chains: Monerium's token documentation now lists GBPe v2 on six chains (Ethereum, Gnosis, Polygon, Arbitrum, Base, Linea), all with 18 decimals. The 13 Oct entry listed three besides Gnosis.

**GBPe minting route**
- Monerium's help centre states that it does not currently offer GBP IBANs (help.monerium.com/article/12-gbpe-ibans), so GBPe cannot be minted by a customer's GBP bank transfer; users obtain it by swapping, for example on Gnosis. Corrected in DefiLlama via PR #949 (merged 22 Oct 2026).
- Open question: the 17 Oct entry described ~3.1M minted and ~3.1M burned over 12 months as active on/off-ramping. Given that there are no customer GBP IBANs, the source of these mints and burns (for example Monerium or Gnosis Pay settlement) is not yet verified.

---

## 21 October 2026

**Price data coverage on Dune**
- GBPe is not listed on CoinPaprika (API returns not found), which Dune's curated price tables require. A 2024 attempt to add GBPe to Dune prices (spellbook PR #5898) was closed for this reason. Dune USD valuations of GBPe should therefore not rely on curated prices.
- Dune removed its stablecoin models from the public Spellbook in July 2026 (PR #9865), consistent with the 13 Oct finding that curated stablecoin tables are Enterprise-only.
- Related contribution: spellbook PR #10090 adds Monerium EURe v2 contracts to Dune's price tables on six chains (open, all checks passed). Relevant to the open question comparing GBPe with EURe.

---

## 22 October 2026

**GBPA: other chains verified**
- DefiLlama lists GBPA on five chains (Ethereum, Arc, Base, Solana, Tempo). The addresses in its code (peggedData.ts, checked 22 Oct) match Agant's official documentation (docs.agant.io, "Networks" page), which states that GBPA is deployed on exactly these five chains and uses LayerZero for cross-chain messaging.
- Ethereum, Base and Arc share the same address: 0xbBe6aAB0Ed76e90AeA0d1cd978EC231c8AdCDF8b.
- Each chain was checked on its own explorer. All use 6 decimals, and supply matches DefiLlama:
  - Base (Basescan): Agant GBP, 250,010.8417 supply, 3 holders.
  - Solana (Solscan): DYoCmA91VE8REbWNw3kM736PN7vv97qc2jr5wmUbuNtZ, Token-2022 program, 25,014.724655 supply, 2 holders, 15 transfers.
  - Arc (explorer.arc.io): Agant GBP, 575,218.374 supply, 129 holders, 5,038 transfers.
  - Tempo (explore.tempo.xyz): 0x20C0000000000000000000000a6Da882d075a4C3, TIP-20, currency GBP, 50,001 supply. The ISSUER role is held by 0x5575151bf6076129d0729c0f40d967d41df34a63, which Agant's docs list as the Tempo OFT address.
- Conclusion: DefiLlama's GBPA entry is correct; no change needed.
- Observation: GBPA activity appears concentrated on Arc (129 holders), compared with 2 holders on Ethereum (13 Oct) and 2 on Solana.
- Evidence: [Basescan](https://github.com/vijetarajput/vijeta-research/blob/main/open-source-contributions/defillama/evidence/2026-10-22_basescan_gbpa_verification.png) · [Solscan](https://github.com/vijetarajput/vijeta-research/blob/main/open-source-contributions/defillama/evidence/2026-10-22_solscan_gbpa_verification.png) · [Arc explorer](https://github.com/vijetarajput/vijeta-research/blob/main/open-source-contributions/defillama/evidence/2026-10-22_arcexplorer_gbpa_verification.png) · [Tempo explorer](https://github.com/vijetarajput/vijeta-research/blob/main/open-source-contributions/defillama/evidence/2026-10-22_tempoexplorer_gbpa_verification.png) · [Agant docs](https://github.com/vijetarajput/vijeta-research/blob/main/open-source-contributions/defillama/evidence/2026-10-22_agant_docs_gbpa_networks.png)

**DefiLlama: GBPe live as a stablecoin**
- DefiLlama's site search for "Monerium" now lists "Monerium GBP emoney" as a Stablecoin, following PR #948. The older token page is still listed separately as a Token.
- Evidence: [DefiLlama search screenshot](https://github.com/vijetarajput/vijeta-research/blob/main/open-source-contributions/defillama/evidence/2026-10-22_defillama_search_Monerium_dropdown_after.png)

**DefiLlama: tGBP description corrected**
- DefiLlama's tGBP entry (peggedData.ts, id "317") described tGBP as "the only British Pound backed stablecoin issued by a UK FCA-registered firm".
- The FCA Financial Services Register shows two such firms, both with type "MLD cryptoassets": BCP Technologies Ltd (tGBP issuer, FRN 928840, registered since 3 December 2021) and Agant Finance Limited (GBPA issuer, FRN 1037671, registered since 11 February 2026). The claim has therefore been outdated since 11 February 2026.
- Submitted PR #957 to DefiLlama/peggedassets-server, replacing the claim with the issuer's name and registration type (one line changed). Open as of 22 Oct 2026.
- Also checked: DefiLlama lists tGBP on eight chains (Ethereum, BNB Chain, Base, Polygon, Avalanche, Solana, Arbitrum, Gnosis), the same eight named in the official tGBP contract register (13 Oct entry). The addresses were not checked against the register.
- Evidence: [FCA register: Agant](https://github.com/vijetarajput/vijeta-research/blob/main/open-source-contributions/defillama/evidence/2026-10-22_fca_register_agant_1037671.png) · [FCA register: BCP](https://github.com/vijetarajput/vijeta-research/blob/main/open-source-contributions/defillama/evidence/2026-10-22_fca_register_bcp_928840.png) · [PR #957 screenshot](https://github.com/vijetarajput/vijeta-research/blob/main/open-source-contributions/defillama/evidence/2026-10-22_defillama_pr957_opened.png) · [Live PR](https://github.com/DefiLlama/peggedassets-server/pull/957)
