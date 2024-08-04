

import sys
import json
from datetime import datetime, timedelta

class VibratoRechargePlugin:
    def __init__(self, user_id):
        self.user_id = user_id
        self.shaking_currency = 0
        self.purchase_attempts = 0
        self.purchase_limit = 99
        self.balance_history = []

    def recharge_shaking_currency(self, amount):
        if amount > 0:
            self.shaking_currency += amount
            self.update_balance_history(amount)
            return f"Recharged {amount} shaking currency. Current balance: {self.shaking_currency}"
        else:
            return "Invalid amount"

    def purchase_item(self, item_cost):
        if self.purchase_attempts < self.purchase_limit:
            if self.shaking_currency >= item_cost:
                self.shaking_currency -= item_cost
                self.purchase_attempts += 1
                self.update_balance_history(-item_cost)
                return f"Purchased item for {item_cost}. Remaining balance: {self.shaking_currency}"
            else:
                return "Insufficient balance"
        else:
            return "Purchase limit reached"

    def update_balance_history(self, amount):
        today = datetime.now().date()
        self.balance_history.append((today, amount))
        # Keep only the last 9 days
        self.balance_history = [(date, amt) for date, amt in self.balance_history if date >= today - timedelta(days=9)]

    def get_balance_history(self):
        return self.balance_history

def main():
    if len(sys.argv) < 2:
        print("Usage: myplugin1.py <user_id>")
        return

    user_id = sys.argv[1]
    plugin = VibratoRechargePlugin(user_id)

    while True:
        print("\nOptions:")
        print("1. Recharge Shaking Currency")
        print("2. Purchase Item")
        print("3. View Balance History")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            amount = float(input("Enter amount to recharge: "))
            print(plugin.recharge_shaking_currency(amount))

        elif choice == "2":
            item_cost = float(input("Enter item cost: "))
            print(plugin.purchase_item(item_cost))

        elif choice == "3":
            history = plugin.get_balance_history()
            for date, amt in history:
                print(f"Date: {date}, Amount: {amt}")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
