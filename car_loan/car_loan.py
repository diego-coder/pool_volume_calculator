annual_interest_in_percentage = float(input("Enter, in terms of percentage, the amount of interest paid per month: "))
annual_interest_in_decimal = annual_interest_in_percentage/100
interest_rate_per_month = annual_interest_in_decimal/12

car_payment = int(input("Enter the amount you pay per month: "))
starting_number_of_monthly_payments = int(input("Enter total number of monthly payments over the life of the loan: "))

principal_total = (car_payment * starting_number_of_monthly_payments)
equated_monthly_installment = (principal_total) * (((interest_rate_per_month) * (1 + interest_rate_per_month)**starting_number_of_monthly_payments)/(((1 + interest_rate_per_month)**starting_number_of_monthly_payments) - 1))

#starting_number_of_monthly_payments)/(12 * ((1 + interest_rate_per_month) * starting_number_of_monthly_payments) - 1))
total_interest_to_be_paid = (principal_total * starting_number_of_monthly_payments * annual_interest_in_decimal * 12)/100

print("You pay " + str(annual_interest_in_percentage) + "% interest per month.")
print("Your monthly car payment is $" + str(car_payment) + " per month.")
print("The length of your loan is " + str(starting_number_of_monthly_payments) + " months, and the principal cost of your car is $" + str(principal_total) + ". The amount of interest you will pay over the life of the loan is $" + str(total_interest_to_be_paid) + ".")

total_cost = equated_monthly_installment * starting_number_of_monthly_payments
number_of_payments_already_made = int(input("Enter the total number of payments you have already made on the car, if any: "))

if number_of_payments_already_made == 0:
    payoff_months = starting_number_of_monthly_payments
    print("You have not made any payments yet, so you have " + str(payoff_months) + f" months left at {round(equated_monthly_installment, 2)} each, and have {round(total_cost, 2)} total left in both principal and interest to pay.")

else:
    payoff_months = starting_number_of_monthly_payments - number_of_payments_already_made
    total_dollar_payments_so_far = number_of_payments_already_made * equated_monthly_installment
    print("You have already made " + str(number_of_payments_already_made) + f" payments totalling {round(total_dollar_payments_so_far, 2)} and have " + str(payoff_months) + f" months to pay the remaining balance of ${round((total_cost - (number_of_payments_already_made * equated_monthly_installment)), 2)}.")