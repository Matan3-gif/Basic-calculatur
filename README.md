# Basic Calculatur
This project is a basic Python calculator that can perform addition, subtraction, multiplication, and division. The calculator takes two numbers and an operator as inputs and returns the result of the operation. It includes additional checks and messages when performing division, particularly when dealing with even and odd numbers.

## Features
### Basic Arithmetic Operations:
* Addition (+)
* Subtraction (-)
* Multiplication (*)
* Division (/)

### Division Checks:

* Handles division by zero with an error message.
* Identifies whether both numbers are even, both are odd, or one is even and one is odd, printing corresponding messages.
* Ensures the first number is greater than or equal to the second number when performing division.

## How It Works

1. User Input:
  * The program prompts the user to input two numbers and an arithmetic operator.

2. Operation Execution:
  * Depending on the operator provided, the program performs the corresponding arithmetic operation:
      * Addition: Adds the two numbers.
      * Subtraction: Subtracts the second number from the first.
      * Multiplication: Multiplies the two numbers.
      * Division:
        * If both numbers are even or odd, it prints a message identifying them.
        * Checks if the first number is greater than or equal to the second number before performing the division.
        * Handles division by zero by returning an error message.
    
3. Result Output:
  * The program outputs the final result of the operation.
  * If the calculation is invalid (e.g., division by zero or an invalid operator), the program will notify the user with an appropriate message.

## Requirements
* Python 3.x

## Running the Program
1. Clone or download the script.

2. Open a terminal or command prompt.

3. Navigate to the directory where the script is located.

4. Run the following command: python simple_calculator.py

5. Follow the on-screen instructions to input numbers and the desired operation.

## Contributing
Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

## License
This project is licensed under the MIT License.

