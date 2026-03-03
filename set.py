# cities = {"Tokyo", "Madrid", "Berlin", "delhi"}
# cities2 = {"Tokyo", "seoul","kabul", "Madrid"}
# cities3 = cities.difference(cities2)
# print(cities3) 

# info= {'name':'karan', 'age':'19', 'eligible':'true'}
# print(info)
# print(info.get('name'))

# a = int(input("enter the number:"))
# for i in range(1,11):
    # print ( a*i )


# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# try:
    # result = a / b
    # print("Result is:", result)

# except:
    # print("You cannot divide by zero!")

# num = int(input("Enter a number: "))
# try:
    # print(10 / num)

# except ZeroDivisionError:
    # print("Error: Cannot divide by zero!")

# except ValueError:
    # print("Error: Please enter a valid number!")

class InsufficientBalanceError(Exception):
    pass

balance = 5000
withdraw = int(input("Enter withdrawal amount: "))

if withdraw > balance:
    raise InsufficientBalanceError("Not enough balance!")


