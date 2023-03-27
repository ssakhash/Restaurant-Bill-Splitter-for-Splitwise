# Restaurant-Bill-Splitter-for-Splitwise

This is a simple Python script that helps you calculate the individual shares of a restaurant bill for a group of people, including tax and tip, which can then be added to Splitwise.

The script takes user inputs such as the number of people in the group, pre-tax total, tax amount, tip percentage, and the name of the restaurant. It then asks for the individual's name and the cost of the items they ordered. Finally, it calculates the tax, tip, and the total amount for each individual, and prints the results.

The script also creates a text file containing the final bill details, named with the format RestaurantName_Date.txt.
## Usage

    1. Download or clone the repository.
    2. Open your terminal or command prompt and navigate to the folder containing the script.
    3. Run the script with python 'Bill Splitter.py'.
    4. Follow the prompts to enter the required information.
    5. Once the script has finished running, you can find the generated text file in the same folder as the script.
    
## Example

    Enter the number of people that dined out: 3
    Enter the pre-tax total (USD): 100.00
    Enter the tax amount (USD): 8.00
    Enter the tip given in %: 15
    Enter the name of the restaurant: Tasty Bites

    Enter the name of person 1: Alice
    Enter the number of items for Alice: 2
    Enter cost of item 1: 20.00
    Enter cost of item 2: 30.00

    Enter the name of person 2: Bob
    Enter the number of items for Bob: 1
    Enter cost of item 1: 10.00

## Requirements

    - Python 3.x
    - NumPy

## Contributing

Feel free to contribute to this project by submitting pull requests or opening issues for any bugs or feature requests. Your feedback is appreciated!
