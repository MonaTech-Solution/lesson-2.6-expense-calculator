# Name: Expense calculator using f-strings
"""
Requirements
• Ask for the person’s name.
• Ask for the item name.
• Ask for the price.
• Ask for the quantity.
• Convert price and quantity to appropriate numeric types.
• Calculate the total.
• Display a readable receipt-style message using an f-string.
• Store important information in variables.
• Test at least three different inputs.
• Commit the completed logical stage to Git
"""

# Get Purchase details
print("Expense Calculator")
name = input("Enter your name: ")
item = input("Enter item name: ")
price = input("Amount paid: ")
quantity = input("Enter quantity: ")

# Convert price and quantity to numeric value
price = float(price)
quantity = float(quantity)