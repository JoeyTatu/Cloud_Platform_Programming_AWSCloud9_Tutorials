basic_pay_rate = float(input("Your basic pay rate: "))
regular_hours = int(input("Your regular hours: "))
overtime_hours = int(input("Your OVERTIME hours: "))

basic_pay = basic_pay_rate * regular_hours
overtime_pay = (basic_pay_rate * 1.5) * overtime_hours

total_pay = basic_pay + overtime_pay

print()
print(f'Regular hours pay: {regular_hours} hours x €{basic_pay_rate} = €{basic_pay}')
print(f'Overtime hours: {overtime_hours} hours x €{basic_pay_rate * 1.5} = €{overtime_pay}')
print()
print(f'Net pay: €{basic_pay} + €{overtime_pay}')
print(f'Net pay: €{total_pay} ')
