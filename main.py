# Add your functions here!
<<<<<<< HEAD
<<<<<<< HEAD
def modulo(num1,num2):
    result = num1 % num2
    print("The result is: ", result)
=======
<<<<<<< HEAD
=======
>>>>>>> 45fc61c14f6c5d085774e7a5593de28ce3080519
def add (num1,num2) :
    result = num1 + num2
    print("The result is ", result)
>>>>>>> a925c8391cd13b54ba938d97a003b9f10a22a1df

def subtract(num1,num2):
    result = num1 - num2
    print("the result of subtract is: ", result)

def divide(num1, num2 )
    result = num1 / num2
    print("The result is: ", result)

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
