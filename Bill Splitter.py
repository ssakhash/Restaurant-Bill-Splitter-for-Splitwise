# Import the datetime module for generating timestamped filenames
import datetime

# Function to get float input from the user
# Loops until valid float input is provided
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:  # Handle invalid float input
            print("Please enter a valid number.")

# Function to get integer input from the user
# Loops until valid integer input is provided
def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:  # Handle invalid integer input
            print("Please enter a valid integer.")

# Main function to execute the bill-splitting logic
def main():
    # Initialize variables to store various totals
    pretax_total = 0
    total = 0
    tax = 0
    tip = 0
    surcharge_total = 0  # Initialize surcharge_total variable
    
    # Collect general information about the dining experience
    num_people = get_int_input("Enter the number of people that dined out: ")
    cost = get_float_input("Enter the pre-tax total (USD): ")
    tax_amount = get_float_input("Enter the total tax amount (USD): ")
    tip_percentage = get_float_input("Enter the tip given in %: ")
    surcharge_percentage = get_float_input("Enter the restaurant surcharge in %: ")  # Get surcharge percentage
    restaurant_name = input("Enter the name of the restaurant: ")
    
    # Loop through each person to collect their specific details and calculate their costs
    for i in range(num_people):
        user_name = input(f"Enter the name of person {i + 1}: ")
        num_items = get_int_input(f"Enter the number of items for {user_name}: ")
        
        # Calculate pre-tax total for each individual
        pretax = sum([get_float_input(f"Enter cost of item {j + 1}: ") for j in range(num_items)])
        
        # Calculate tax, tip, and surcharge for each individual based on their pre-tax total
        user_tax = pretax * (tax_amount/cost)
        user_tip = (tip_percentage/100) * pretax
        user_surcharge = (surcharge_percentage / 100) * pretax  # Calculate surcharge for the individual
        
        # Calculate the total amount for each individual
        user_total = pretax + user_tax + user_tip + user_surcharge  # Add surcharge to total

        # Display individual's tax, tip, and surcharge
        print(f"Tax for {user_name} is: {round(user_tax, 2)}")
        print(f"Tip for {user_name} is: {round(user_tip, 2)}")
        print(f"Surcharge for {user_name} is: {round(user_surcharge, 2)}")  # Display surcharge

        # Update the running totals
        tip += user_tip
        tax += user_tax
        total += user_total
        pretax_total += pretax
        surcharge_total += user_surcharge  # Add to surcharge total

        # Display individual's total amount
        print(f"Tip inclusive total = {round(user_total, 2)}")
        print(25*"-")

    # Display overall totals
    print(f"Total Pretax (USD): {round(pretax_total, 2)}")
    print(f"Total Tax (USD): {round(tax, 2)}")
    print(f"Total Tip (USD): {round(tip, 2)}")
    print(f"Total Surcharge (USD): {round(surcharge_total, 2)}")  # Display total surcharge
    print(f"Final Bill (USD): {round(total, 2)}")

    # Generate a timestamped filename and save the bill details to a file
    date_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{restaurant_name}_{date_str}.txt"
    with open(filename, "w") as f:
        f.write(f"Total Pretax (USD): {round(pretax_total, 2)}\n")
        f.write(f"Total Tax (USD): {round(tax, 2)}\n")
        f.write(f"Total Tip (USD): {round(tip, 2)}\n")
        f.write(f"Total Surcharge (USD): {round(surcharge_total, 2)}\n")  # Save total surcharge to file
        f.write(f"Final Bill (USD): {round(total, 2)}\n")

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()