def detect_variable_type(user_input):
    try:
        # Try to evaluate the input
        evaluated_input = eval(user_input)
        
        # Check for different types
        if isinstance(evaluated_input, int):
            return "Integer"
        elif isinstance(evaluated_input, float):
            return "Float"
        elif isinstance(evaluated_input, bool):
            return "Boolean"
        elif isinstance(evaluated_input, str):
            return "String"
        elif isinstance(evaluated_input, list):
            return "List"
        elif isinstance(evaluated_input, dict):
            return "Dictionary"
        elif isinstance(evaluated_input, tuple):
            return "Tuple"
        elif isinstance(evaluated_input, set):
            return "Set"
        else:
            return "Unknown type"
    except:
        # If eval fails, it's a string
        return "String"

# Taking input from user
user_input = input("Enter a variable: ")

# Detecting the type
variable_type = detect_variable_type(user_input)

# Printing the detected type
print(f"The type of the entered variable is: {variable_type}")
