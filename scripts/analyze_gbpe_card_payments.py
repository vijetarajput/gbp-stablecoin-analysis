"""Classify GBPe transfers and compute the Gnosis Pay card-payment share.

Input:  data/gbpe_v2_transfers_12m.csv (from fetch_gbpe_transfers.py)
Output: monthly summary CSV and headline statistics printed to the console.

Classification: method 0x8a320255 = Gnosis Pay Spender Module call (card payment),
identified from a transaction tagged "Gnosis Pay" on Gnosisscan; CoW Protocol
settlement methods = trades; mints/burns via the zero address; dust < 0.001 GBPe.
"""
import pandas as pd

ZERO = "0x0000000000000000000000000000000000000000"
df = pd.read_csv("data/gbpe_v2_transfers_12m.csv")
df["time"] = pd.to_datetime(df["time"], utc=True)
df = df.drop_duplicates()
w = df[(df.time >= "2025-10-17") & (df.time < "2026-10-17")].copy()

def classify(r):
    m = str(r["method"])
    if r["from"] == ZERO:
        return "mint"
    if r["to"] == ZERO:
        return "burn"
    if m == "0x8a320255":
        return "card_payment"
    if m in ("settle", "0x13d79a0b", "0x9008d19f"):
        return "cow_trade"
    if m in ("0xa9059cbb", "transfer", "transferFrom", "0x23b872dd"):
        return "simple_transfer"
    return "dex_aggregator_other"

w["cat"] = w.apply(classify, axis=1)
cp = w[w.cat == "card_payment"]
tx = w.groupby("tx").agg(
    cat=("cat", lambda s: "card_payment" if (s == "card_payment").any() else s.mode()[0]),
    time=("time", "min")).reset_index()

print("Transfers:", len(w), "| distinct transactions:", len(tx))
print("Card-payment transactions:", (tx.cat == "card_payment").sum(),
      f"({(tx.cat == 'card_payment').mean():.1%})")
print("Distinct paying wallets:", cp["from"].nunique())
print("Median card payment (GBPe):", cp.value_gbpe.median())
print("Dust transfers (<0.001 GBPe):", (w.value_gbpe < 0.001).sum())

tx["month"] = tx.time.dt.strftime("%Y-%m")
cp = cp.assign(month=cp.time.dt.strftime("%Y-%m"))
monthly = tx.groupby("month").agg(tx=("tx", "count"),
                                  card=("cat", lambda s: (s == "card_payment").sum()))
monthly["share"] = (monthly.card / monthly.tx * 100).round(1)
monthly["payers"] = cp.groupby("month")["from"].nunique()
monthly["card_value"] = cp.groupby("month").value_gbpe.sum().round(0)
monthly.to_csv("data/gbpe_monthly_card_payments_2025-10_to_2026-10.csv")
print(monthly)
