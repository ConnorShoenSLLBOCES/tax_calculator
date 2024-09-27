"""
Title: Income Tax Calculator
Author: Connor Shoen

Psudo-Code: Code-like structure in plain english
1.) Input gross income and number of dependants

2.) Compute the taxable income using the formula:
Taxable income = gross income -10000 - (300 / number of dependents)

3.) Compute income tax using the formula:
Tax = taxable income * 0.20

4.) Print the total tax
"""

"""
Better Psudo-Code:

Compute a persons income tax.
1.) Significant constants (Non-changing variables):
    tax_rate
    standard_deduction
    deduction_per_dependant

2.) The Imputs are:
    gross_incoome
    number_of_dependents

3.) Computations:
    Taxable income = standard deduction - a deduction for each dependant
    Income tax = a fixed percentage of your taxable income

4.) The outputs:
    Your income tax
"""

# Initialize Constants
TAX_RATE = 0.20 #Float
STANDARD_DEDUCTION = 10000.00 # Float - any numerical value with a decimal
DEPENDANT_DEDUCTION = 3000.00 # Float


# Request imputs
gross_income = float(input("Enter the gross income: "))
num_dep = int(input("Enter the number of dependents: "))

# Compute income tax
taxable_in = gross_income - STANDARD_DEDUCTION - DEPENDANT_DEDUCTION * num_dep
income_tax = taxable_in * TAX_RATE

# Display income tax
print("Your inncome tax, based on your taxable income of", taxable_in, "is", income_tax, ".")