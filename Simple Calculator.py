while True:
    num1 = float(input('Enter your first number: '))
    num2 = float(input('Enter your second number: '))

    operator = (input('Enter the operator (+ - * /)'))

    result = 0

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    print(result)
