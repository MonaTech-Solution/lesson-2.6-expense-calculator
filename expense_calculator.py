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

print("Expense Calculator")
name = input("Enter your name: ")

print("FIRST ITEM DETAILS")
# Get First Item Purchase details
first_item = input("Enter first item name: ")
first_item_price = input("Amount paid: ")
first_item_quantity = input("Enter quantity: ")

# Convert price and quantity to numeric value
first_item_price = float(first_item_price)
first_item_quantity = float(first_item_quantity)

# Estimated first item price
first_item_total = first_item_price * first_item_quantity