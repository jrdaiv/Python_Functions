# Task 1 & 2

# user = input("Welcome, to my calculator app! Please pick Add, Subtract, Divide, or Multiply! ")
# num1 = input("Please enter first number. ")
# num2 = input("Please enter second number. ")
# def add_nums(num1, num2):
#     return num1 + num2
# print("the total is: ", int(num1) + int(num2))



user = input("Welcome, to my calculator app! Please pick Add, Subtract, Divide, or Multiply! ")
if user == "Add":
    num1 = input("Please enter first number. ")
    num2 = input("Please enter second number. ")
    def add_nums(num1, num2):
        return num1 + num2
    print("the total is: ", int(num1) + int(num2))
elif user == "Subtract":
    num1 = input("Please enter first number. ")
    num2 = input("Please enter second number. ")
    def sub_nums(num1, num2):
        return num1 - num2
    print("The total is: ", int(num1) - int(num2))
elif user == "Divide":
    num1 = input("Please enter first number. ")
    num2 = input("Please enter second number. ")
    def div_nums(num1, num2):
        return num1 / num2
    print("The total is: ", int(num1) / int(num2))
elif user == "Multiply":
    num1 = input("Please enter first number. ")
    num2 = input("Please enter second number. ")
    def mul_nums(num1, num2):
        return num1 * num2
    print("The total is: ", int(num1) * int(num2))
else:
    print("Invalid input")







