cap_price = 5
shirt_price = 10
hoodie_price = 20

cap_qty = int(input("Please enter quantity of CAPS: "))
shirt_qty = int(input("Please enter quantity of SHIRTS: "))
hoodie_qty = int(input("Please enter quantity of HOODIES: "))
total_qty = (cap_qty + shirt_qty + hoodie_qty)

cap_total = (cap_price * cap_qty)
shirt_total = (shirt_price * shirt_qty)
hoodie_total = (hoodie_price * hoodie_qty)

total_price = (cap_total + shirt_total + hoodie_total)

print(f'{cap_qty} caps\n{shirt_qty} shirts\n{hoodie_qty} hoodies\n\n{total_qty} items\n\nTotal price: €{total_price}')