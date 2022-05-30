salary = float(input())


def calculateTax(value):
    discount = value - 2000
    tax = 0

    if discount <= 0:
        return 0

    if value <= 3000:
        tax += discount * 0.08
        return tax
    else:
        tax += 1000 * 0.08
        discount = value - 3000

    if value <= 4500:
        tax += discount * 0.18
        return tax
    else:
        tax += 1500 * 0.18
        discount = value - 4500

    if value > 4500:
        tax += discount * 0.28
        return tax


result = calculateTax(salary)
if result == 0:
    print('Isento')
else:
    print('R$', format(result, '.2f'))
