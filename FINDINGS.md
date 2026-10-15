# Key Findings

A summary of what the verification phase found. Full details, sources and evidence are in the [LOGBOOK](LOGBOOK.md) and the [register](data/gbp_stablecoin_register.csv).

*Status: preliminary, based on manual verification (13–15 October 2026). On-chain analysis with Dune is the next phase.*

---

## 1. The sterling stablecoin market is very small

Total GBP stablecoin market capitalisation was roughly $31.8M on CoinGecko's category page (13 Oct 2026). Summing coin-level figures for the six tokens reviewed gives about $30.2M, consistent with that estimate. All stablecoins together exceed $300B, so sterling stablecoins represent well under 0.1% of the market.

## 2. Six tokens reviewed, four distinct models

| Model | Example | Issuer |
|---|---|---|
| UK-registered (MLR only), fiat-backed | GBPA, tGBP | Agant Finance Ltd; BCP Technologies Ltd |
| E-money token | GBPe | Monerium |
| Offshore-licensed, fiat-backed | VGBP | VNX Global Ltd (Bermuda) |
| Decentralised, crypto-backed (CDP) | GBPm (formerly cGBP) | None (Mento Protocol) |
| Unclear / dormant | poundtoken (1GBP), likely the original GBPT | Unconfirmed (originally Blackfridge) |

## 3. Size and usage do not match

The largest token (tGBP, ~20M supply) trades about $67K per day, around 0.25% of supply. The smallest active token (GBPe, ~505K supply) shows the most holders (1,302) and transfers (203,735) on its main chain.

## 4. Supply is highly concentrated

On Ethereum, GBPA has 2 holders and one address holds ~99.99% of supply. tGBP has 309 holders, but the top 10 hold ~96% (Gini ~0.98). VGBP on Base shows a similar pattern (Gini ~0.995).

## 5. Some tokens stall or shrink

poundtoken (1GBP) has had only a handful of transfers in five months, and its listed website no longer belongs to an issuer. A public Dune query labels this contract as GBPT. GBPm supply roughly halved between April and October 2026. VGBP's Celo deployment has 20 holders and very few recent transfers.

## 6. Transfer counts are not a reliable measure of use

VGBP shows 265K transfers on Solana, but recent activity is dominated by tiny, repeated DEX loops consistent with arbitrage bots. Any usage claim must separate bot activity from genuine transfers and payments.

## 7. Consumer protection gap

Both UK-based issuers reviewed operate under anti-money-laundering registration only. Neither GBPA nor tGBP is covered by the FSCS, and GBPA's issuer states it is also outside the Financial Ombudsman Service.

## 8. Multi-chain tokens need per-chain verification

VGBP is deployed on Solana (9 decimals), Base and Celo (18 decimals each). Summing on-chain supply across the three chains (126,595.21) exactly matches CoinGecko's reported total, confirming its full deployment. The same token can use different decimals on different chains, so supply calculations must be set per chain.

## 9. Public data sources and dashboards contain errors

Market caps, volumes, issuer names and supply figures differed across CoinGecko pages, third-party sites and search snippets. An existing public Dune dashboard on GBP stablecoins (@duneuk) appears to use a mistyped tGBP contract address and incorrect decimals in its supply query (to be confirmed by running the query), and does not cover GBPA, GBPe or VGBP on Solana. Blockchain explorers and official issuer pages were used as the reference throughout.

---

## Open questions for the Dune phase

- Are GBPe's transfers driven by real payments (e.g., card spending) or by bots?
- Who operates the address (0x90830ed5...) that submits many GBPe transactions? Is it a payment relayer?
- How has each token's supply changed over time, across all chains, including GBPe's migration from its v1 to v2 contract?
- How much activity is DEX trading versus wallet-to-wallet transfers?
- How does GBPe compare with Monerium's euro token (EURe), issued with the same technology?

## Implications for the digital pound debate (to be developed)

Private sterling stablecoins exist but remain small, concentrated and lightly used, and the UK-based ones currently offer limited consumer protection. This supports the case for clear regulation of sterling stablecoins, and raises the question of whether private stablecoins alone can provide the public-money role that a digital pound would serve.
