#The follwing code is a basic calculator
 #Defines a function calculate that takes an operator and two numbers as inputs.

def calculate(operator, num1, num2):  
    if operator == "+":
        return num1 + num2  #If the operator is '+', it adds the two numbers and returns the result.
    elif operator == "-":
        return num1 - num2  #If the operator is '-', it subtracts the second number from the first and returns the result.
    elif operator == "*":
        return num1 * num2  #If the operator is '*', it multiplies the two numbers and returns the result.

    elif operator == "/":   #If the operator is '/', it handles division with additional checks.
        if num2 == 0:  #f the second number (num2) is zero, it returns an error message indicating that division by zero is not allowed.
            return "Error: Division by zero is not allowed."
        
        # the following section Checks if both numbers are even, both are odd,
        #  or if one is even and one is odd, and prints the corresponding message.
        if num1 % 2 == 0 and num2 % 2 == 0:
            print(num1, "and", num2, "are both even numbers.")
        elif num1 % 2 != 0 and num2 % 2 != 0:
            print(num1, "and", num2, "are both odd numbers.")
        else:
            if num1 % 2 != 0:
                print("The odd number is:", num1)
            else:
                print("The odd number is:", num2)

        #the following section checks If the first number is greater than or equal to the second, 
        # it performs the division, prints a validity message, and returns the result. 
        # If not, it prints a message indicating the calculation is invalid and returns 'None'.

        if num1 >= num2:
            print("The calculation is valid.")
            return num1 / num2
        else:
            print("The calculation is not valid because the first number is less than the second number.")
            return None
    else:
        # checks If the operator is not one of the recognized ones ('+',' -', '*', '/'), 
        # it returns an error message.
        return "Error: Invalid operator." 

# Prompts the user to input two numbers and an operator.
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
operator = input("Enter your operator (+, -, *, /): ")


result = calculate(operator, num1, num2) #Calls the calculate function with the user-provided inputs and stores the result.

#If the calculation is valid and a result is returned, it prints the final result. 
# If the calculation is invalid (e.g., division by zero, invalid operator), 
# it prints a message indicating no result.

if result is not None:
    print("The final result is:", result)
else:
    print("No result due to an invalid calculation.")
