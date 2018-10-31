annual_salary = float(input("What is your annual salary? "))
percentage_of_salary = float(input("How much of your salary can you save? Please enter the percentage as a decimal. "))
total_cost = float(input("How much is your dream home? "))

current_savings = 0
months_to_down_payment = 0
downpayment = total_cost * .25
r = .04

while current_savings < downpayment:
   monthly_savings = ((annual_salary * percentage_of_salary) / 12) + ((current_savings * r) / 12)
   current_savings += monthly_savings
   months_to_down_payment += 1

   print(months_to_down_payment)