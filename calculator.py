def calculator(text_input):
    """
    Calculate the result of a basic arithmetic operation from a string input.

    Supported operations:
        ~   : Division with quotient and remainder
        //  : Integer division
        %   : Modulo (remainder)
        *   : Multiplication
        /   : Division
        +   : Addition
        -   : Subtraction

    Parameters:
        text_input (str): A string representing a single arithmetic operation between
                          two integers. Spaces are ignored (e.g., " 3 + 5 ").

    Returns:
        int, float, or str:
            - For +, -, *, /, //, % → returns numeric result (int or float)
            - For ~ → returns formatted string showing quotient and remainder
            - Returns "Invalid Input" for malformed expressions
            - Returns "ZeroDivisionError: ..." if dividing by zero

    Notes:
        - Input must contain exactly two integer operands and a single operator.
        - Leading/trailing and internal spaces are removed automatically.
        - The function handles integer division, modulo, and division by zero gracefully.
    """
    text_input = text_input.replace(" ", "")
    for operator in ["~", "//", "%", "*", "/", "+", "-"]:  # Scalable list of operators
        if operator in text_input:
            parts = text_input.split(
                operator
            )  # Splitting in two parts based on operator
            # Operands validation!
            if len(parts) != 2:  # Validate input has exactly two parts!
                return "Invalid Input"
            if not (
                    parts[0].isdigit() and parts[1].isdigit()
            ):  # Check if both operands are integers!
                return "Invalid Input"

            operand_one = int(parts[0])
            operand_two = int(parts[1])
            if operator == "~":
                if operand_two == 0:
                    return "ZeroDivisionError: Division by zero"
                quotient, remainder = divmod(operand_one, operand_two)
                return f"{quotient}\nThe remainder is {remainder}"  # Tilde (quotient as answer and remainder)
            elif operator == "//":
                if operand_two == 0:
                    return "ZeroDivisionError: Division by zero"
                return operand_one // operand_two  # Integer division
            elif operator == "%":
                if operand_two == 0:
                    return "ZeroDivisionError: division by zero"
                return operand_one % operand_two  # Modulo (remainder)
            elif operator == "*":
                return operand_one * operand_two  # Multiplication
            elif operator == "/":
                if operand_two == 0:
                    return "ZeroDivisionError: division by zero"
                return operand_one / operand_two  # Division
            elif operator == "+":
                return operand_one + operand_two  # Addition
            elif operator == "-":
                return operand_one - operand_two  # Subtraction
    return "Invalid input"


print("Welcome to the Python calculator!")
user_inputs_number_of_calculations = input("How many calculations do you want to do?")
for number_of_calculations in range(int(user_inputs_number_of_calculations)):
    user_input = input("What do you want to calculate? ").strip()
    result = calculator(
        user_input
    )  # Call the calculate function with the user's chosen operation
    print(f"The answer is {result}")
