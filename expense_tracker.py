import json
import os
def save_expenses(expenses):
	with open("expenses.json", "w") as f:
		json.dump(expenses, f)
def load_expenses():
	if os.path.exists("expenses.json"):
		with open("expenses.json", "r") as f:
			return json.load(f)
	return[]
expenses = load_expenses()
while True:
	print("\n1. Add expense")
	print("2. View all expenses")
	print("3. View total")
	print("4. Quit")
	choice = input("\nChoose an option (1-4): ")
	if choice == "1":
		category = input("Category (food/transport/shopping/other): ")
		amount = float(input("Amount spent: Rs."))
		description = input("Description: ")
		expenses.append({"category": category, "amount": amount, "description": description})
		print("Expense added!")
		save_expenses(expenses)
	elif choice == "2":
		if len(expenses) == 0:
			print("No expenses yet.")
		else:
			print("\n--- Your Expenses ---")
			for expense in expenses:
				print(expense["category"].upper() + " | Rs." + str(expense["amount"]) + " | " + expense["description"])
	elif choice == "3":
		total = sum(expense["amount"] for expense in expenses)
		print("\nTotal spent: Rs." + str(round(total,2)))
	elif choice == "4":
		print("Goodbye!")
		break
	else:
		print("Invalid option. PLease choose 1-4.")
```
