# Restaurant-Bill-Splitter-for-Splitwise

This is an enhanced Python script designed to calculate individual shares of a restaurant bill for a group of people. The bill includes not just the pre-tax total, but also tax, tip, and an optional restaurant surcharge. The calculated shares can be conveniently added to Splitwise.

The script gathers inputs like the number of diners, pre-tax total, tax amount, tip percentage, surcharge percentage, and the restaurant's name. For each individual, it asks for their name and the cost of the items they ordered. The script then computes the tax, tip, surcharge, and total amount for each person, displaying the results.

Additionally, the script saves a text file with the complete bill details. The file is named using the format RestaurantName_YYYY-MM-DD_HH-MM-SS.txt.
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
    Enter the restaurant surcharge in %: 2  # New feature
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

## Features
- Calculates tax, tip, and surcharge individually for each person.
- Generates a text file with complete bill details for record-keeping.
- Error handling for invalid inputs.

## Contributing

Contributions to this project are welcomed! Feel free to submit pull requests or open issues for any bugs, enhancements, or feature requests. Your feedback helps make this tool even better!
