# Key Findings

A summary of what the verification phase found. Full details, sources and evidence are in the [LOGBOOK](LOGBOOK.md) and the [register](data/gbp_stablecoin_register.csv).

*Status: preliminary, based on manual verification and public market data (13–17 October 2026). Transaction-level analysis with Dune is the next phase.*

---

## 1. The sterling stablecoin market is very small

Total GBP stablecoin market capitalization was roughly $31.8M on CoinGecko's category page (13 Oct 2026). Summing coin-level figures for the six tokens reviewed gives about $30.2M, consistent with that estimate. Dollar-denominated stablecoins total around $300B, so sterling stablecoins are equivalent to about 0.01% of that market. Even euro stablecoins (~EUR 450M in January 2026) are more than ten times larger.

## 2. Six tokens reviewed, four distinct models

| Model | Example | Issuer |
|---|---|---|
| UK-registered (MLR only), fiat-backed | GBPA, tGBP | Agant Finance Ltd; BCP Technologies Ltd |
| E-money token | GBPe | Monerium |
| Offshore-licensed, fiat-backed | VGBP | VNX Global Ltd (Bermuda) |
| Decentralized, crypto-backed (CDP) | GBPm (formerly cGBP) | None (Mento Protocol) |
| Unclear / dormant | poundtoken (1GBP), likely the original GBPT | Unconfirmed (originally Blackfridge) |

## 3. Size and usage do not match

The largest token (tGBP, ~20M supply) traded on average ~$82K per day over the past year (~0.42% of market cap per day; ~0.76% over the last 30 days). GBPe, with a supply of only ~505K, shows the largest holder count of the tokens reviewed (1,302 on Gnosis) and 203,735 transfers. A single-day snapshot (~$67K) used earlier understated this variation; averages are used instead.

## 4. Supply is highly concentrated

On Ethereum, GBPA has 2 holders and one address holds ~99.99% of supply. tGBP has 309 holders, but the top 10 hold ~96% (Gini ~0.98). VGBP on Base shows a similar pattern (Gini ~0.995).

## 5. Some tokens stall or shrink

poundtoken (1GBP) has had only a handful of transfers in five months, and its listed website no longer belongs to an issuer. A public Dune query labels this contract as GBPT. GBPm supply roughly halved between April and October 2026. VGBP's Celo deployment has 20 holders and very few recent transfers.

## 6. Transfer counts are not a reliable measure of use

VGBP shows 265K transfers on Solana, but the ten most recent transfers inspected were tiny, repeated DEX loops consistent with arbitrage bots. GBPe shows a different pattern: many of its transactions are submitted by a single automated address (over 3.9 million transactions), and a sampled transaction was tagged "Gnosis Pay" and executed through a "Spender Module", moving 6.34 GBPe from a user wallet. In a sample of the 100 most recent GBPe transfers (17 Oct 2026, about 17 hours), 65% of distinct transactions used the same Gnosis Pay "Spender Module" method, with a median amount of 11 GBPe, typical of everyday card spending; 24 transfers were dust-sized, similar to bot activity. This is consistent with card payments being the main use of GBPe, although the sample covers less than one day. Transfer counts alone are therefore not a reliable measure of use. Sample data: [data/gnosisscan_gbpe_recent_100_transfers_2026-10-17.csv](data/gnosisscan_gbpe_recent_100_transfers_2026-10-17.csv)

## 7. Consumer protection gap

Both UK-based issuers reviewed operate under anti-money-laundering registration only. Neither GBPA nor tGBP is covered by the FSCS, and GBPA's issuer states it is also outside the Financial Ombudsman Service.

## 8. Multi-chain tokens need per-chain verification

VGBP is deployed on Solana (9 decimals), Base and Celo (18 decimals each). Summing on-chain supply across the three chains (126,595.21) is consistent with CoinGecko's reported total of 126,595, confirming its full deployment. The same token can use different decimals on different chains, so supply calculations must be set per chain.

## 9. Public data sources and dashboards contain errors

Market caps, volumes, issuer names and supply figures differed across CoinGecko pages, third-party sites and search snippets. In an existing public Dune dashboard on GBP stablecoins (@duneuk), the supply query's tGBP contract address differs from the verified address by two transposed characters and divides tGBP amounts by 1e6 although the contract uses 18 decimals; it also omits GBPA, GBPe and VGBP on Solana. The effect on the dashboard's outputs has not been tested by running the query. Blockchain explorers and official issuer pages were used as the reference throughout.

## 10. tGBP grew in a few large steps, not gradually

CoinGecko daily data (Nov 2025 – Oct 2026) shows tGBP supply rising from ~1.1M to a peak of ~25.5M in mid-2026, then falling to ~20M. Almost all change happened on six days, including a ~19% drop (~£5M redeemed) on 8 August 2026. This step pattern points to a few large institutional mints and redemptions, consistent with the high holder concentration in Finding 4. USD market cap also moves with the GBP/USD exchange rate, so supply is measured in tokens (≈ GBP). Daily data: [data/coingecko_tgbp_daily_2025-11-12_to_2026-10-15.csv](data/coingecko_tgbp_daily_2025-11-12_to_2026-10-15.csv)

---

## Open questions for the Dune phase

- Does the Gnosis Pay share of GBPe transactions (65% in a 17-hour sample) hold over the full transaction history?
- What share of VGBP transfers on Solana is bot-like, measured over a full period rather than a small sample?
- How has each token's supply changed over time, across all chains, including GBPe's migration from its v1 to v2 contract?
- How much activity is DEX trading versus wallet-to-wallet transfers?
- How does GBPe compare with Monerium's euro token (EURe), issued with the same technology?

## Implications for the digital pound debate

Private sterling stablecoins exist but remain small, concentrated and lightly used, and the UK-based ones currently offer limited consumer protection. Their uses also differ sharply: one token's activity looks bot-driven, another's looks like card payments. This supports the case for clear regulation of sterling stablecoins, and raises the question of whether private stablecoins alone can provide the public-money role that a digital pound would serve.
