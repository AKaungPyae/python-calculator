# Add your functions here!
def add (num1,num2) :
    result = num1 + num2
    print("The result is ", result)

def subtract(num1,num2):
    result = num1 - num2
    print("the result of subtract is: ", result)

def modulo(num1,num2):
    result = num1 % num2
    print("The result is: ", result)
    
def main():
    print("Enter the operation you want to perform: ")
=======
>>>>>>> a925c8391cd13b54ba938d97a003b9f10a22a1df

    user_operation = input()
    user_input1 = int(input("Enter the first number: "))
    user_input2 = int(input("Enter the second number: "))

    if user_operation == "add":
        add(user_input1, user_input2)
    elif user_operation == "subtract":
        subtract(user_input1, user_input2)
    elif user_operation == "multiply":
        multiply(user_input1, user_input2)
    elif user_operation == "divide":
        divide(user_input1, user_input2)
    elif user_operation == "modulo":
        modulo(user_input1, user_input2)


main()
