import datetime

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def main():
    pretax_total = 0
    total = 0
    tax = 0
    tip = 0

    num_people = get_int_input("Enter the number of people that dined out: ")
    cost = get_float_input("Enter the pre-tax total (USD): ")
    tax_amount = get_float_input("Enter the total tax amount (USD): ")
    tip_percentage = get_float_input("Enter the tip given in %: ")
    restaurant_name = input("Enter the name of the restaurant: ")

    for i in range(num_people):
        user_name = input(f"Enter the name of person {i + 1}: ")
        num_items = get_int_input(f"Enter the number of items for {user_name}: ")
        pretax = sum([get_float_input(f"Enter cost of item {j + 1}: ") for j in range(num_items)])
        
        user_tax = pretax * (tax_amount/cost)
        user_tip = (tip_percentage/100) * (pretax + user_tax)
        user_total = pretax + user_tax + user_tip

        print(f"Tax for {user_name} is: {round(user_tax, 2)}")
        print(f"Tip for {user_name} is: {round(user_tip, 2)}")
        
        tip += user_tip
        tax += user_tax
        total += user_total
        pretax_total += pretax

        print(f"Tip inclusive total = {round(user_total, 2)}")
        print(25*"-")

    print(f"Total Pretax (USD): {round(pretax_total, 2)}")
    print(f"Total Tax (USD): {round(tax, 2)}")
    print(f"Total Tip (USD): {round(tip, 2)}")
    print(f"Final Bill (USD): {round(total, 2)}")

    date_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{restaurant_name}_{date_str}.txt"
    with open(filename, "w") as f:
        f.write(f"Total Pretax (USD): {round(pretax_total, 2)}\n")
        f.write(f"Total Tax (USD): {round(tax, 2)}\n")
        f.write(f"Total Tip (USD): {round(tip, 2)}\n")
        f.write(f"Final Bill (USD): {round(total, 2)}\n")

if __name__ == "__main__":
    main()
