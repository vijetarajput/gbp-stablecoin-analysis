# GBP Stablecoin Analysis

On-chain analysis of UK sterling (GBP) stablecoins — supply, adoption and payments — in the context of the Bank of England digital pound debate.

## Why this project

The Bank of England is deciding whether to build a digital pound (a central bank digital currency), while also preparing rules for sterling stablecoins issued by private companies. A key concern is that people may move towards US dollar stablecoins instead of pound-based ones.

Public on-chain analysis of sterling stablecoins is limited. An existing community dashboard on Dune covers some tokens and DEX activity; this project adds newer tokens, issuer and regulatory verification, holder concentration, bot-versus-genuine usage, and a reproducible token register.

## Research questions

1. How large is the sterling stablecoin market compared to US dollar stablecoins?
2. Which GBP stablecoins exist, and on which blockchains?
3. How are they used — trading, transfers or real-world payments?
4. What does this data suggest for the UK digital pound debate?

## Data and method

- **Verification:** each token checked against blockchain explorers (Etherscan, Gnosisscan, Solscan, Basescan, Celoscan) and official issuer pages, with screenshots in [`evidence/`](evidence/).
- **Market data:** daily CoinGecko data, saved in [`data/`](data/).
- **On-chain analysis:** [Dune](https://dune.com) (DuneSQL). Queries will be published in a `queries/` folder so anyone can check and reuse them.

## Status

🚧 In progress — started October 2026.

- **Phase 1 (done):** verification of six GBP stablecoins across five blockchains, plus one year of tGBP market data. See [Key Findings](FINDINGS.md), the [research logbook](LOGBOOK.md) and the [token register](data/gbp_stablecoin_register.csv).
- **Phase 2 (next):** on-chain analysis and a public dashboard on Dune.

## Author

**Vijetasingh Rajput** — India

- Dune: [@vijetasinghrajput](https://dune.com/vijetasinghrajput)
- GitHub: [@vijetarajput](https://github.com/vijetarajput)
