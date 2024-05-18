import json
from pathlib import Path
import csv


def get_layerzero_wallets():
    wallets = []
    print(f"Start checking ineligible wallets...")
    with open("app/layerzero_wallets/wallets.csv", newline='') as csvfile:
        data = csv.DictReader(csvfile)
        for i, row in enumerate(data):
            if "ADDRESS" in row:
                address = row["ADDRESS"].lower()
                wallets.append(address)
    print(f"Found {len(wallets)} ineligible wallets")
    return wallets


class Checker:
    def __init__(self) -> None:
        self.layerzero_wallets = get_layerzero_wallets()

    def check_wallets(self, wallets: list[str]):
        eligible_wallets = []
        ineligible_wallets = []
        for wallet in wallets:
            if wallet in self.layerzero_wallets:
                ineligible_wallets.append(wallet)
            else:
                eligible_wallets.append(wallet)
        return eligible_wallets, ineligible_wallets
