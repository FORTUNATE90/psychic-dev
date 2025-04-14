# psychic-dev

FUNCTIONS, DATA TYPES AND RECURSION

Functions are reusable blocks of code that perform specific tasks. They make programs more organized and efficient. Data types define the kind of data a variable can hold, like numbers, text, or booleans (true/false). Recursion is a technique where a function calls itself to solve a problem, breaking it down into smaller, similar subproblems.


*CODE ON FUNCTION,DATA TYPES AND RECURSION*



# Example of Functions, Data Types, and Recursion

# Function to calculate the factorial of a number using recursion
def factorial(n):
    # Check for valid input
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1

    # Recursive case
    return n * factorial(n - 1)

# Function to demonstrate data type usage
def data_type_examples():
    # Integer
    integer_example = 42
    
    # Float
    float_example = 3.14
    
 "Hello, World!"
    
    # List
    list_example = [1, 2, 3, 4, 5]
    
    # Dictionary
    dict_example = {"name": "Alice", "age": 25}
    
    # Boolean
    bool_example = True
    
    # Print examples
    print("Integer:", integer_example)
    print("Float:", float_example)
    print("String:", string_example)
    print("List:", list_example)
    print("Dictionary:", dict_example)
    print("Boolean:", bool_example)

# Main function to execute the examples
if __name__ == "__main__":
    # Demonstrate data types
    print("Data Type Examples:")
    data_type_examples()
    
    # Demonstrate recursion with factorial
    print("\nFactorial Example:")
    try:
        number = 5
        print(f"Factorial of {number}:", factorial(number))
    except ValueError as e:
        print(e)


RESULT


Data Type Examples:
Integer: 42
Float: 3.14
String: Hello, World!
List: [1, 2, 3, 4, 5]
Dictionary: {'name': 'Alice', 'age': 25}
Boolean: True

Factorial Example:
Factorial of 5: 120






