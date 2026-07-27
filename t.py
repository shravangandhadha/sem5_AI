num1 = int(input("enter first number:  "))
num2 = int(input("enter second number:  "))
op = input("select an operator: +, -, *, /, %")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Cannot divide by zero")
elif op == "%":
    print(num1 % num2)
else:
    print("Invalid operator")
