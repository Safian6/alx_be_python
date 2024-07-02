num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = str(input("Choose the operation (+, -, *, /): "))

match operation:
    case ('+'):
        result = num1 + num2
        print("The result is: ", result)
    case ('-'):
        result = num1 - num2
        print("The reult is : ", result)
    case ('*'):
        result = num1 * num2
        print(f'The result is ', result)
    case ('/'):
        if num2 == 0:
            print(f'Can not divide be zero.')
        else:
            result = num1 / num2
            print(f'The result is ', result)
    case _:
        print("Invalid operation. Please choose one of the following: +, -, *, /")