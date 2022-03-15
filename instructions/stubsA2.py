# Author: Opeyemi Adesina
# Institution: University of the Fraser Valley
# Academic Session: Fall, 2020

# -------------------------------------------# Problem Analysis #-------------------------------------------#


# -------------------------------------------# End of Problem Analysis #-------------------------------------------#

from math import sqrt  # imports only the square root operation from the math module

# receiving number of employees as an input from the user
numberOfEmployees = int(input("Enter the number of employees: "))


# operation builds gross income list from user input
def buildGrossIncomeList(numberOfEmployees):  # Step 1

    # creating and initializing income list as empty
    grossIncomeList = []
    i = 0

    print(
        "\n\n------------------------- Enter Employees' Salaries (i.e., Gross Incomes) Below -------------------------")
    while (i < numberOfEmployees):
        grossIncome = input("Enter an employee's gross income: ")

        # checking if the value entered is an empty string or not
        if (grossIncome.strip() == ""):
            print("Gross income can't be an empty string...")
            grossIncome = input("Re-enter the employee's gross income: ")

        # type conversioning from string to floating point number - monies should be in float
        grossIncome = float(grossIncome)
        if (grossIncome < 0.0):
            print("Gross income can't be negative...")
            grossIncome = float(input("Re-enter non-negative value for the employee's gross income: "))

        grossIncomeList.append(grossIncome)
        i += 1
    return grossIncomeList


#Function to compute provincial taxes for the input gross income
def computeProvTaxes(grossIncome):  # Step 2.1.1

    ##-----------------------------------------##
    ## Insert your code here!!!
    ##-----------------------------------------##

    if grossIncome <= 39147.00:
        tax = grossIncome * 0.087
    elif 39147.01 <= grossIncome <= 78294.00:
        tax = (grossIncome - 39147.01) * 0.145 + 3405.789
    elif 78294.01 <= grossIncome <= 139780.00:
        tax = (grossIncome - 78294.01) * 0.158 + 5676.31355 + 3405.789
    elif 139780.01 <= grossIncome <= 195693.00:
        tax = (grossIncome - 139780.01) * 0.178 + 9714.78642 + 5676.31355 + 3405.789
    elif 195693.00 <= grossIncome <= 250000.00:
        tax = (grossIncome - 195693.00) * 0.198 + 9952.51222 + 9714.78642 + 5676.31355 + 3405.789
    elif 250000.01 <= grossIncome <= 500000.00:
        tax = (grossIncome - 250000.01) * 0.20 + 10752.786 + 9952.51222 + 9714.78642 + 5676.31355 + 3405.789
    elif 500000.01 <= grossIncome <= 1000000.00:
        tax = (grossIncome - 250000.01) * 0.213 + 49999.998 + 10752.786 + 9952.51222 + 9714.78642 + 5676.31355 + \
              3405.789
    else:
        tax = (grossIncome - 1000000.01) * 0.218 + 106499.99787 + 49999.998 + 10752.786 + 9952.51222 + 9714.78642 + \
              5676.31355 + 3405.789
    return round(tax, 2)


#Function to compute federal taxes for the input gross income
def computeFedTaxes(grossIncome):  # Step 2.1.2

    ##-----------------------------------------##
    ## Insert your code here!!!
    ##-----------------------------------------##
    if grossIncome <= 50197.00:
        tax = grossIncome * 0.15
    elif 50197.01 <= grossIncome <= 100392.00:
        tax = (grossIncome - 50197.01) * 0.205 + 7529.55
    elif 100392.01 <= grossIncome <= 155625.00:
        tax = (grossIncome - 100392.01) * 0.26 + 10289.97295 + 7529.55
    elif 155625.01 <= grossIncome <= 221708.00:
        tax = (grossIncome - 155625.01) * 0.29 + 14360.5774 + 10289.97295 + 7529.55
    else:
        tax = (grossIncome - 221708.01) * 0.33 + 19164.0671 + 14360.5774 + 10289.97295 + 7529.55
    return round(tax, 2)


#Function to compute the CPP of employee given gross income.
Beginning of Step 3 - Computing employee's CPP
def computeCPP(grossIncome):
    ##-----------------------------------------##
    ## Insert your code here!!!
    ##-----------------------------------------##
    tax = grossIncome * 0.057
    if tax > 3499.80:
        tax = 3499.80
    return round(tax, 2)
#function to compute the Employment Insurance of employee given gross income.
def computeEI(grossIncome):
    ##-----------------------------------------##
    ## Insert your code here!!!
    ##-----------------------------------------##
    tax = grossIncome * 0.0158
    if tax > 952.74:
        tax = 952.74
    return round(tax, 2)

#Function to compute Health Premium
def computeHealthPremium(grossIncome):
    ##-----------------------------------------##
    ## Insert your code here!!!
    ##-----------------------------------------##

    if grossIncome <= 22000.00:
        premium_tax = 0
    elif 22000 < grossIncome <= 38000.00:
        premium_tax = (grossIncome - 22000.00) * 0.06
        if premium_tax > 300:
            premium_tax = 300
    elif 38000 < grossIncome <= 50000.00:
        premium_tax = (grossIncome - 38000.00) * 0.06 + 300
        if premium_tax > 450:
            premium_tax = 450
    elif 50000 < grossIncome <= 74000.00:
        premium_tax = (grossIncome - 50000.00) * 0.25 + 450
        if premium_tax > 600:
            premium_tax = 600
    elif 74000 < grossIncome <= 202000.00:
        premium_tax = (grossIncome - 74000.00) * 0.25 + 600
        if premium_tax > 750:
            premium_tax = 750
    else:
        premium_tax = (grossIncome - 202000.00) * 0.25 + 750
        if premium_tax > 900:
            premium_tax = 900

    return round(premium_tax, 2)


# Function to compute net incomes by invoking gross income list less the total deductions
def computeNetIncomes(grossIncomeList):  # Step 2

    netIncomeList = []  # creating and initializing the net income list

    ##-----------------------------------------##
    ## Insert your code here!!!
    ##-----------------------------------------##
    deductions = computeDeductions(grossIncomeList)
    for i in range(len(grossIncomeList)):
        netIncomeList.append(round((grossIncomeList[i] - deductions[i]), 2))
    return netIncomeList


# Function computes net incomes by invoking deductions
def computeDeductions(grossIncomeList):  # Step 2

    totalDeductionsList = []  # creating and initializing the net income list

    ##-----------------------------------------##
    ## Insert your code here!!!
    ##-----------------------------------------##
    for income in grossIncomeList:
        fed_tax = computeFedTaxes(income)
        prov_tax = computeProvTaxes(income)
        health_prem = computeHealthPremium(income)
        cpp = computeCPP(income)
        ei = computeEI(income)
        totalDeductionsList.append(fed_tax + prov_tax + health_prem + cpp + ei)
    return totalDeductionsList


# function computes mean or average of a set of numbers
def mean(inputList):  # Step 3

    ##-----------------------------------------##
    ## Insert your code here!!!
    ##-----------------------------------------##

    return sum(inputList) / len(inputList)

#Function to compute the standard deviation of the input list
def standardDeviation(inputList):  # Step 4

    ##-----------------------------------------##
    ## Insert your code here!!!
    ##-----------------------------------------##

    average = mean(inputList)
    std_dev = (sum((x - average) ** 2 for x in inputList) / len(inputList)) ** 0.5
    return std_dev

#Function to normalize the values in the Input List
def normalize(inputList):
    ##-----------------------------------------##
    ## Insert your code here!!!

    ##-----------------------------------------##
    normalizedList = []
    average = mean(inputList)
    stdev = standardDeviation(inputList)
    for val in inputList:
        if stdev == 0:
            normalizedList.append(1)
        else:
            normalizedList.append((val - average) / stdev)
    return normalizedList
