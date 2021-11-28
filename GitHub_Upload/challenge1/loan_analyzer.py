# coding: utf-8
import csv
from os import close
from pathlib import Path

"""Part 1: Automate the Calculations.

"""
loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list

# Create variables
L = len(loan_costs)
# Print the number of loans in the list
print(f"The total number of loans in the list is: {L}")

# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans

# Create variables
S = sum(loan_costs)
#Print total value of the loan
print(f"The total value of the loans is: {S}")

# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount

# Create variables and print the average loan amount
avg = S/L
print(f"The average loan amount is: {avg}")

"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.

# Create variables
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")

#Print each variable
print(f"Future value for this loan is:{future_value}")
print(f"The remaining months for this loan are: {remaining_months}")


# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

# Create variables and formula for Present Value calculation
discount_rate = 0.2
denominator = (1+ (discount_rate/12))**remaining_months
present_value1 = future_value/denominator
print(f"The present value (present_value1) for this loan is:{present_value1:.2f}")

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

# Check if calculated present value of the loan is less or greater than the loan cost
loan_cost= loan.get("loan_price")
if present_value1>=loan_cost:
    print(f"The loan is worth atleast the cost to buy as its present value of ${present_value1:.2f}" + " is greater than loan cost of $",loan_cost)
else:
    print("The loan is too expensive and not worth the price")


"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Create variables
future_value2 = new_loan.get("future_value")
remaining_months2 = new_loan.get("remaining_months")

#Print each variable
print(f"New future value for this loan is:{future_value2}")
print(f"New remaining months for this loan are: {remaining_months2}")


# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.

# Function definition
def calculate_present_value(new_future_value, new_remaining_months, annual_discount_rate):
    # Define formula for Present Value calculation
    new_denominator = (1+ (annual_discount_rate/12)) ** new_remaining_months
    new_present_value = new_future_value/new_denominator
    #print(f"The present value (new_present_value) for this loan is:{new_present_value}")
    return new_present_value

# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.

# Define discount rate
new_discount_rate =0.2

# Call function to calculate the present value of the new loan
present_value_function = calculate_present_value(future_value2, remaining_months2, new_discount_rate)
print(f"The new present value for the new loan is: {present_value_function:.2f}")


"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`
# Create list called inexpensive loans

#Define empty list for inexpensive loans
inexpensive_loans = []

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
# Create for loop to go through the list of loans

for index in range(len(loans)):
    # Create variables that iterate thru each loan in the dictionary
        loan_cost = loans[index].get("loan_price")
    
    # Check if cost of loan is less or equal to $500. If true add the loan to the inexpensive list.
        if loan_cost<=500:
            inexpensive_loans.append(loans[index])

# @TODO: Print the `inexpensive_loans` list

#Print inexpensive loan list
print("The list of inexpensive loans is:", inexpensive_loans)

"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

 Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.

# Open csv file for writing, add header values and insert rows
import csv
header = ['loan_price', 'remaining_months', 'repayment_interval', 'future_value']
with open('inexpensive_loans.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=header)
    # write the header
    writer.writeheader()
    # write a row to the csv file using for loop
    for key in inexpensive_loans:
    # write each row
       writer.writerow(key)
     #print(key)
f.close()





   

