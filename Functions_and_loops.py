# FEDERAL TAX
def federal_tax(grossIncome):
    if grossIncome <= 50197.00:
        tax = grossIncome * 0.15
    elif 50197.01 <= grossIncome <= 100392.00:
        tax = (grossIncome - 50197.01) * 0.205 + 7529.55

    elif 100392.01 <= grossIncome <= 155625.00:
        tax = (grossIncome - 100392.01) * 0.26 + 10289.97295 + 7529.55
    elif 155625.01 <= grossIncome <= 221708.00:
        tax = (grossIncome - 221708.00) * 0.29 + 14360.5774 + 10289.97295 + 7529.55
    else:
        tax = (grossIncome - 155625.01) * 0.33 + 19164.0671 + 14360.5774 + 10289.97295 + 7529.55
    return tax


# PROVISIONAL TAX
def provisional_tax(grossIncome):
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
    return tax


# Canada_Pension_PLan = 5.7% of gross income up to maximum of $3,499.80
def canada_pension_plan(grossIncome):
    tax = grossIncome * 0.057
    if tax > 3499.80:
        tax = 3499.80
    return tax


# Employment_Insurance = 1.58% of the gross income (but to a maximum amount of $952.74).
def employment_insurance(grossIncome):
    tax = grossIncome * 0.0158
    if tax > 952.74:
        tax = 952.74
    return tax


def health_premium(grossIncome):
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

    return premium_tax


def main():
    count = int(input("Enter the number of employees: "))
    employees_income = []
    for i in range(count):
        gross_income = float(input("Please enter the gross income of the employees: "))
        employees_income.append(gross_income)
    net_incomes = []
    for income in employees_income:
        fed_tax = federal_tax(income)
        prov_tax = provisional_tax(income)
        health_prem = health_premium(income)
        cpp = canada_pension_plan(income)
        ei = employment_insurance(income)
        net_incomes.append(round(income - (fed_tax + prov_tax + health_prem + cpp + ei), 2))
    print(net_incomes)


if __name__ == "__main__":
    main()
