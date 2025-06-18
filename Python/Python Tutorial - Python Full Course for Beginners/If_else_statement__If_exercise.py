price_house = 1000000
good_credit = True

if good_credit:
    down_payment = price_house * 0.10
else:
    down_payment = price_house * 0.20
print(f"Down payment: ${down_payment}")