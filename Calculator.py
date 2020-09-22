# Simple calculator performs one of the following operations
# with two entered numbers:
# addition: +
# subtraction: -
# multiplication: *
# division: /
# modulus: %
# exponentiation: ** or ^
# floor division: //
# The code:
# Enter 2 numbers and an operator
Number1 = float(input('Enter the first number: '))
Operator = input('Enter the operator: ')
Number2 = float(input('Enter the second number: '))

# Perform operation corresponding to the entered
# operator symbol:
if Operator == '*':
    print(Number1 * Number2)
elif Operator == '/':
    print(Number1 / Number2)
elif Operator == '+':
    print(Number1 + Number2)
elif Operator == '-':
    print(Number1 - Number2)
elif Operator == '%':
    print(Number1 % Number2)
elif Operator == '//':
    print(Number1 // Number2)
elif Operator == '**' or Operator == '^':
    print(Number1 ** Number2)
else:
    print('Error: operator "{Operator}" not found. '
          'Only the following operators can be used '
          'in this calculator: '
          '"+" (addition), "-" (subtraction), '
          '"*" (multiplication), "/" (division),'
          '"%" (modulus),"**" or "^" (exponentiation), "//" (floor division).')