from cgitb import text
from os import environ


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017



##A grocery store name of your choice
store_name = "Welcome to Kroger OTR"

#A grocery store phone number and/or website URL and/or address of choice

store_phone_number = "(513) 263-5900"
store_url = "https://www.kroger.com/stores/details/014/00513"

#The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2020-02-07 03:54 PM)
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%Y/%m/%d %H:%M %p")

#The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $3.50, etc.)
def to_usd(my_price):
   
    return f"${my_price:,.2f}" #> $12,000.71
#The total cost of all shopping cart items (i.e. the "subtotal"), formatted as US dollars and cents (e.g. $19.47), calculated as the sum of their prices
subtotal = 0

selected_ids = []

# Input variable for product id and fails if input is invalis
while True:

    selected_id = input("Please input a product identifier: ")
    
    if selected_id == "DONE" or selected_id == "done":
        
        break
    elif int(selected_id) > len(products) or int(selected_id) <= 0:
        print("Invalid product id, please try again.")
    else:
          
        selected_ids.append(selected_id)
# Info Output
print("--------------------------------")
print(store_name)
print(store_phone_number)
print(store_url)
print("Today's checkout date and time: ", dt_string)
print("--------------------------------")
#Prints out which products you selected and calculates price
for selected_id in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    subtotal = int(subtotal + matching_product["price"])
    print("Selected product: " + matching_product["name"] + " " + str(matching_product["price"])) 
    print("--------------------------------")
print(f"Subtotal: {to_usd(subtotal)}")
print("--------------------------------")

# Calculated Sales tax bases on Ohio 5.75% sales tax
tax_owed = int(subtotal) * 0.0575
print(f"Tax Owed: {to_usd(tax_owed)}")
print("--------------------------------")


total_price = int(tax_owed + subtotal)
print(f"Total Price: {to_usd(total_price)}")
print("--------------------------------")
print("Thank you for vistiting Kroger OTR, Please come again!")
print("--------------------------------")


