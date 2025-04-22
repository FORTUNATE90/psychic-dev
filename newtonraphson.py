import math  # Import the math module for mathematical operations

# Maximum number of iterations
N = 500

# Tolerance for convergence
TOL = 0.000001

# Function definition
def fval(x):
    y = 4 * x + math.sin(x) - math.exp(x)  # Function f(x)
    return y

# Derivative of the function
def dfval(x):
    dy = 4 + math.cos(x) - math.exp(x)  # Derivative f'(x)
    return dy

# Input: Initial approximation
x0 = float(input("Enter the initial approximation: "))
print("iter\t xk\t\t\t f(xk)\t\t\t Error")

# Initialize variables
xk = x0
fxk = fval(xk)

# Iterative process
for k in range(1, N + 1):
    xp = xk  # Previous value
    fxp = fxk
    dfxp = dfval(xp)

    # Avoid dividing by zero
    if dfxp == 0:
        print("Derivative is zero. The method fails.")
        break

    # Update xk using the Newton-Raphson formula
    xk = xp - (fxp / dfxp)
    fxk = fval(xk)

    # Calculate the relative error
    err = abs(xk - xp) / abs(xk)

    # Print iteration details
    print(f"{k}\t {xk:.16f}\t{fxk:.16f}\t{err:.12f}")

    # Check for convergence
    if err < TOL:
        print("Required accuracy achieved; Solution is convergent.")
        break
else:
    # If the loop completes without finding a solution
    print("The number of iterations exceeded the maximum limit.")