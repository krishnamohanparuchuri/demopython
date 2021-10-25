from calc import Calc


print('Enter your first number: ')


x = int(input())


print('Enter your second Number: ')


y = int(input())

print('select operator')
print('1 Addition')
print('2 Subtraction')
print('3 Mutiply')
print('4 Divison')


operator = int(input())


if operator == 1:
    result = Calc.add(x, y)
    print(result)
elif operator == 2:
    result = Calc.sub(x, y)
    print(result)
elif operator == 3:
    result = Calc.mul(x, y)
    print(result)
elif operator == 4:
    result = Calc.div(x, y)
    print(result)
