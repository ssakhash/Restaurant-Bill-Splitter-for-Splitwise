import numpy as np
import datetime

pretax_total = 0
total = 0
tax = 0
tip = 0

num_people = int(input("Enter the number of people that dined out: "))
cost = float(input("Enter the pre-tax total (USD): "))
tax_amount = float(input("Enter the tax amount (USD): "))
tip_percentage = float(input("Enter the tip given in %: "))
restaurant_name = input("Enter the name of the restaurant: ")

for i in range(num_people):
    # Input Data
    user_name = input(f"Enter the name of person {i + 1}: ")
    num_items = int(input(f"Enter the number of items for {user_name}: "))
    pretax = 0
    
    for j in range(num_items):
        item_cost = float(input(f"Enter cost of item {j + 1}: "))
        pretax += item_cost

    # Calculation
    user_tax = float(pretax) * (tax_amount/cost)
    user_tip = (tip_percentage/100) * (float(pretax) + user_tax)
    user_total = float(pretax) + user_tax + user_tip

    # Printing
    print("Tax for " + user_name + " is: " + str(np.round(user_tax, 2)))
    print("Tip for " + user_name + " is: " + str(np.round(user_tip, 2)))

    tip = tip + user_tip
    tax = tax + user_tax
    total = total + user_total
    pretax_total = pretax_total + float(pretax)

    print("Tip inclusive total = ", np.round(user_total, 2))
    print(25*"-")

print("Total Pretax (USD): ", np.round(pretax_total, 2))
print("Total Tax (USD): ", np.round(tax, 2))
print("Total Tip (USD): ", np.round(tip, 2))
print("Final Bill (USD): ", np.round(total, 2))

# Save file with name of restaurant and current date
date_str = datetime.datetime.now().strftime("%Y-%m-%d")
filename = f"{restaurant_name}_{date_str}.txt"
with open(filename, "w") as f:
    f.write(f"Total Pretax (USD): {np.round(pretax_total, 2)}\n")
    f.write(f"Total Tax (USD): {np.round(tax, 2)}\n")
    f.write(f"Total Tip (USD): {np.round(tip, 2)}\n")
    f.write(f"Final Bill (USD): {np.round(total, 2)}\n")