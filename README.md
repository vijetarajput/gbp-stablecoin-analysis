# GBP Stablecoin Analysis

On-chain analysis of UK sterling (GBP) stablecoins — supply, adoption and payments — in the context of the Bank of England digital pound debate.

Preprint: https://ssrn.com/abstract=7627799 (DOI: 10.2139/ssrn.7627799)

## Why this project

The Bank of England is deciding whether to build a digital pound (a central bank digital currency), while also preparing rules for sterling stablecoins issued by private companies. Dollar-denominated stablecoins dominate the global stablecoin market, which raises the question of what role, if any, sterling stablecoins currently play.

Public on-chain analysis of sterling stablecoins is limited. An existing community dashboard on Dune covers some tokens and DEX activity; this project adds newer tokens, issuer and regulatory verification, holder concentration, bot-versus-payment usage, and a reproducible token register.

## Research questions

1. How large is the sterling stablecoin market compared to US dollar stablecoins?
2. Which GBP stablecoins exist, and on which blockchains?
3. How are they used — trading, transfers or real-world payments?
4. What does this data suggest for the UK digital pound debate?

## Data and method

- **Verification:** each token checked against blockchain explorers (Etherscan, Gnosisscan, Solscan, Basescan, Celoscan) and official issuer pages, with screenshots in [`evidence/`](evidence/).
- **Market data:** daily CoinGecko data for tGBP, saved in [`data/`](data/).
- **Transfer data:** 12 months of GBPe transfers on Gnosis (84,000+ transfers), collected from the public Blockscout API and classified by transaction type (card payment, DEX trade, mint/burn, dust), saved in [`data/`](data/).
- **Reproducibility:** Python scripts to collect and classify the transfer data are in [`scripts/`](scripts/) and can be run in Google Colab at no cost.

## Status

🚧 In progress — started October 2026.

- **Phase 1 (done):** verification of six GBP stablecoins across five blockchains, one year of tGBP market data, and usage analysis: bot-like activity in VGBP, and card payments via Gnosis Pay in GBPe (78% of transactions over 12 months). See [Key Findings](FINDINGS.md), the [research logbook](LOGBOOK.md) and the [token register](data/gbp_stablecoin_register.csv).
- **Phase 2 (next):** extend the transfer analysis to other tokens and chains, and investigate why GBPe card payments declined during 2026.

## Author

**Vijetasingh Rajput** — India

- Dune: [@vijetasinghrajput](https://dune.com/vijetasinghrajput)
- GitHub: [@vijetarajput](https://github.com/vijetarajput)
