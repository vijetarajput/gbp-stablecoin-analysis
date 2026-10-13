# GBP Stablecoin Analysis

Onchain analysis of UK sterling (GBP) stablecoins using Dune — supply, adoption and payments, in the context of the Bank of England digital pound debate.

## Why this project

The Bank of England is deciding whether to build a digital pound (a central bank digital currency), while also preparing rules for sterling stablecoins issued by private companies. A key concern is that people may move towards US dollar stablecoins instead of pound-based ones.

Very little public onchain analysis exists on sterling stablecoins. This project aims to fill that gap with open, reproducible data.

## Research questions

1. How large is the sterling stablecoin market compared to US dollar stablecoins?
2. Which GBP stablecoins exist, and on which blockchains?
3. How are they used — trading, transfers or real-world payments?
4. What does this data suggest for the UK digital pound debate?

## Data and method

- Platform: [Dune](https://dune.com) (DuneSQL)
- Data: public onchain token transfer data
- All queries will be published in the `queries/` folder so anyone can check and reuse them.

## Status

🚧 In progress — started October 2026.

🚧 In progress — started October 2026.

- **Phase 1 (done):** manual verification of six GBP stablecoins across five blockchains. See [Key Findings](FINDINGS.md), the [research logbook](LOGBOOK.md) and the [token register](data/gbp_stablecoin_register.csv).
- **Phase 2 (next):** on-chain analysis and a public dashboard on Dune.

## Author

**Vijetasingh Rajput** — London, UK
- Dune: [@vijetasinghrajput](https://dune.com/vijetasinghrajput)
- GitHub: [@vijetarajput](https://github.com/vijetarajput)
