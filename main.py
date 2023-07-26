# Add your functions here!
<<<<<<< HEAD
def add (num1,num2) :
    result = num1 + num2
    print("The result is ", result)

=======
def subtract(num1,num2):
    result = num1 - num2
    print("the result of subtract is: ", result)
>>>>>>> e21777bb947e38407424dd8963314eccf148179c


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
