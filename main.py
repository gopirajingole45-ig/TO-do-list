a = int(input("Insert first number: "))
b = int(input("Insert second number: "))

op = input("Enter operation ( Addition, Subtraction, Multiplication, Division, Remainder, Exponential): ")

op = op.lower()

if op == "addition":
    print("Addition of a and b is:", a + b)

elif op == "subtraction":
    print("Subtraction of b from a is:", a - b)

elif op ==  "multiplication":
    print("Multiplication of a and b is:", a * b)

elif  op == "division":
    if b != 0:
        print("Division of a with b is:", a / b)
    else:
        print("Error: Division by zero is not allowed")

elif  op == "remainder":
    print("Remainder of a with b is:", a % b)

elif  op == "exponential":
    print("Exponential of a and b is:", a ** b)

else:
    print("Invalid operation ❌")