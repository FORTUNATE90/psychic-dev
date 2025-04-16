Recursion is a programming technique where a function calls itself within its own definition. This creates a chain of calls that can be used to solve problems that can be broken down into smaller, similar subproblems. 


Problem:  Finding the sum of all the digits in a number.

Recursive Approach:

1. Base Case: If the number is less than 10, the sum is just the number itself.
2. Recursive Case: Otherwise, the sum is the last digit of the number plus the sum of the remaining digits (obtained by recursively calling the function with the number divided by 10).

Python Code:

```python
def sum_of_digits(n):
    #Base case
    if n < 10:
        return n
    #Recursive case
    else:
        return n % 10 + sum_of_digits(n // 10)

# Example usage
number = 12345
result = sum_of_digits(number)
print(f"The sum of the digits in {number} is {result}.")
```

This code will output:

The sum of the digits in 12345 is 15.


This example shows how recursion can be used to elegantly solve problems that involve repetitive operations on data, such as breaking down a number into its individual digits