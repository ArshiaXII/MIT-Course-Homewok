def bisection_search_for_smallest_payment(balance, annualInterestRate):
    monthly_interest_rate = annualInterestRate / 12.0
    lower_bound = balance / 12
    upper_bound = (balance * (1 + monthly_interest_rate)**12) / 12.0
    new_balance = balance
    payment = (lower_bound + upper_bound) / 2

    while abs(new_balance) > 0.01:
        new_balance = balance
        payment = (lower_bound + upper_bound) / 2
        for i in range(12):
            new_balance = new_balance - payment + ((new_balance - payment) * monthly_interest_rate)
        if new_balance > 0:
            lower_bound = payment
        else:
            upper_bound = payment

    return "Lowest Payment: {:.2f}".format(payment)

print(bisection_search_for_smallest_payment(balance, annualInterestRate))
