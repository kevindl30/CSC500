
#Program that allows a user to input their meal price to determine the
#cost of tax, tip and total price

meal_price = float(input('What does your meal cost? '))
tip_percent = .18
tax_percent = .07

tip = meal_price * tip_percent
tax = meal_price * tax_percent
total = meal_price + tip + tax

total_tax = meal_price * tax_percent
total_tip = meal_price * tip_percent

print('\nTax $', '{:.2f}'.format(total_tax), sep='')
print('Tip $', '{:.2f}'.format(total_tip), sep='')

print('\nYour $', '{:.2f}'.format(meal_price), ' meal with an ', int(tip_percent * 100), '% tip and ', int(tax_percent * 100), '% tax, cost $' '{:.2f}'.format(total),'.', sep='')
