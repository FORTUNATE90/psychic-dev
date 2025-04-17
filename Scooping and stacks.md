Here's an example to demonstrate scoping and how the call stack works in Python

# Global variable
x = 10

def outer_function():
    # Enclosing variable
    x = 5

    def inner_function():
        # Local variable
        x = 2
        print(f"Inner Function: x = {x}")  # Local scope

    inner_function()
    print(f"Outer Function: x = {x}")      # Enclosing scope

# Accessing Global variable
print(f"Global Scope: x = {x}")
outer_function()
print(f"Global Scope after function calls: x = {x}")


OUTPUT

Global Scope: x = 10
Inner Function: x = 2
Outer Function: x = 5
Global Scope after function calls: x = 10