"""Fetch GBPe (v2) token transfers on Gnosis from the public Blockscout API.

Run in Google Colab or any Python 3 environment with `requests` and `pandas`.
Transfers are returned newest-first; stop the loop once the desired start date
is reached, then save `rows` to CSV (as done for the 12-month window used here).
"""
import time
import requests
import pandas as pd

URL = ("https://gnosis.blockscout.com/api/v2/tokens/"
       "0x8e34bfec4f6eb781f9743d9b4af99cd23f9b7053/transfers")
rows, params, page = [], {}, 0
session = requests.Session()

while True:
    data = None
    for attempt in range(6):
        try:
            r = session.get(URL, params=params, timeout=60)
            if r.status_code == 200:
                data = r.json()
                break
        except Exception:
            pass
        time.sleep(5 * (attempt + 1))
    if data is None:
        print("STOPPED at page", page, "| resume params:", params)
        break
    for it in data.get("items", []):
        total = it.get("total") or {}
        value = int(total.get("value", 0)) / 10 ** int(total.get("decimals") or 18)
        rows.append({
            "tx": it.get("transaction_hash"),
            "time": it.get("timestamp"),
            "method": it.get("method"),
            "from": (it.get("from") or {}).get("hash"),
            "to": (it.get("to") or {}).get("hash"),
            "value_gbpe": value,
        })
    page += 1
    if page % 100 == 0:
        pd.DataFrame(rows).to_csv("gbpe_v2_transfers_partial.csv", index=False)
        print(f"Page {page} | transfers so far: {len(rows)} | reached: {rows[-1]['time']}")
    params = data.get("next_page_params")
    if not params:
        break
    time.sleep(0.5)

pd.DataFrame(rows).to_csv("gbpe_v2_transfers_12m.csv", index=False)
