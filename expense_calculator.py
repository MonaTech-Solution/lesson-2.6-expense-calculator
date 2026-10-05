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

print("SECOND ITEM DETAILS")
# Get Second Item Purchase details
second_item = input("Enter second item name: ")
second_item_price = input("Amount paid: ")
second_item_quantity = input("Enter quantity: ")

# Convert price and quantity to numeric value
second_item_price = float(second_item_price)
second_item_quantity = float(second_item_quantity)

# Estimated second item price
second_item_total = second_item_price * second_item_quantity

# Combined total
estimated_total = first_item_total + second_item_total

# Receipt
print(
    f'''
Receipt.
********************
Personal Detail:
********************
Name: {name}
*******************
Purchase Details
*******************
First Item: {first_item}
Quantity: {first_item_quantity}
At: {first_item_price}
Total: {first_item_total}
--------------------
Second Item:{second_item}
Quantity: {second_item_quantity}
At: {second_item_price}
Total: {second_item_total}
---------------------
Sub Total: {estimated_total}
    '''
)