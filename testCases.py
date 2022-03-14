from stubsA2 import *


# Testing the computeProvTaxes(...) operation
def q1():
    test = []

    # testing the first bracket
    income = 29590
    taxes = computeProvTaxes(income)
    result = round(abs(taxes - 2574.33))
    test.append(result <= 0.01)

    # testing the first bracket
    income = 42000
    taxes = computeProvTaxes(income)
    result = round(abs(taxes - 3819.47), 2)
    test.append(result <= 0.01)

    income = 92468.79
    taxes = computeProvTaxes(income)
    result = round(abs(taxes - 11321.72))
    test.append(result <= 0.01)

    income = 120000.79
    taxes = computeProvTaxes(income)
    result = round(abs(taxes - 15671.78))
    test.append(result <= 0.01)

    income = 200000.79
    taxes = computeProvTaxes(income)
    result = round(abs(taxes - 29602.35))
    test.append(result <= 0.01)

    income = 1000000.28
    taxes = computeProvTaxes(income)
    result = round(abs(taxes - 196002.25))
    test.append(result <= 0.01)
    return test


# Testing the computeFedTaxes(...) operation
def q2():
    test = []

    # testing the first bracket
    income = 29590
    taxes = computeFedTaxes(income)
    result = round(abs(taxes - 4438.50))
    test.append(result <= 0.01)

    income = 52000.98
    taxes = computeFedTaxes(income)
    result = round(abs(taxes - 7899.37))
    test.append(result <= 0.01)

    income = 135000.01
    taxes = computeFedTaxes(income)
    result = round(abs(taxes - 26817.61))
    test.append(result <= 0.01)

    income = 92468.79
    taxes = computeFedTaxes(income)
    result = round(abs(taxes - 16195.27))
    test.append(result <= 0.01)

    income = 182456.99
    taxes = computeFedTaxes(income)
    result = round(abs(taxes - 39961.38))
    test.append(result <= 0.01)

    income = 1000000
    taxes = computeFedTaxes(income)
    result = round(abs(taxes - 308180.54))
    test.append(result <= 0.01)

    return test


# Testing the computeCPP(...) operation
def q3():
    test = []

    # testing the first bracket
    income = 35000
    cpp = computeCPP(income)
    result = round(abs(cpp - 1995.00))
    test.append(result <= 0.01)

    income = 92000
    cpp = computeCPP(income)
    result = round(abs(cpp - 3499.80))
    test.append(result <= 0.01)

    return test


# Testing the computeEI(...) operation
def q4():
    test = []

    # testing the first bracket
    income = 35000
    ei = computeEI(income)
    result = round(abs(ei - 553))
    test.append(result <= 0.01)

    income = 92000
    ei = computeEI(income)
    result = round(abs(ei - 952.74))
    test.append(result <= 0.01)

    return test


# Testing the computeHealthPremium(...) operation
def q5():
    test = []

    # testing the first bracket
    income = 10000
    hp = computeHealthPremium(income)
    result = round(abs(hp - 0.0))
    answer = result <= 0.01
    test.append(answer)
    # print(answer)

    income = 23000
    hp = computeHealthPremium(income)
    result = round(abs(hp - 60))
    test.append(result <= 0.01)
    answer = result <= 0.01
    test.append(answer)
    # print(answer)

    income = 35000
    hp = computeHealthPremium(income)
    result = round(abs(hp - 300))
    answer = result <= 0.01
    test.append(answer)
    # print(answer)

    income = 38000
    hp = computeHealthPremium(income)
    result = round(abs(hp - 300))
    answer = result <= 0.01
    test.append(answer)
    # print(answer)

    income = 48500
    hp = computeHealthPremium(income)
    result = round(abs(hp - 450))
    answer = result <= 0.01
    test.append(answer)
    # print(answer)

    income = 70000
    hp = computeHealthPremium(income)
    result = round(abs(hp - 600))
    answer = result <= 0.01
    test.append(answer)
    # print(answer)

    income = 72500
    hp = computeHealthPremium(income)
    result = round(abs(hp - 600))
    answer = result <= 0.01
    test.append(answer)
    # print(answer)

    income = 200000
    hp = computeHealthPremium(income)
    result = round(abs(hp - 750))
    answer = result <= 0.01
    test.append(answer)
    # print(answer)

    income = 200500
    hp = computeHealthPremium(income)
    result = round(abs(hp - 750))
    answer = result <= 0.01
    test.append(answer)
    # print(answer)

    income = 300000
    hp = computeHealthPremium(income)
    result = round(abs(hp - 900))
    answer = result <= 0.01
    test.append(answer)
    # print(answer)

    return test


# Testing the computeNetIncomes(...) and mean(...) operations
def q6():
    test = []

    incomes = [1000000, 150000, 25000, 92468.79]
    nIncomes = computeNetIncomes(incomes)
    x = mean(nIncomes)
    # print( x )
    result = round(abs(x - 165188.20)) <= 0.01
    test.append(result)
    # print(result)

    return test


# Testing the standardDeviation(...) and mean(...) operations
def q7():
    test = []

    incomes = [1000000, 150000, 25000, 92468.79]
    sdev = standardDeviation(incomes)
    result = round(abs(sdev - 396880.40) <= 0.01)
    test.append(result)

    return test


# Testing the normalize(...) and mean(...) operations
def q8():
    test = []

    incomes = [1000000, 150000, 25000, 92468.79]
    nIncomes = computeNetIncomes(incomes)
    normalized = normalize(nIncomes)
    x = sum(normalized)
    result = round(abs(x + 0.01) <= 0.01)
    test.append(result)

    incomes = [92468.79]
    nIncomes = computeNetIncomes(incomes)
    normalized = normalize(nIncomes)
    x = sum(normalized)
    result = round(abs(x - 59749.26) <= 0.01)
    test.append(result)

    return test


# A helper operation
def evaluateQuestion(questions):
    answer = questions[0]
    for question in questions:
        answer = (answer and question)

    return answer
