import math

# Function definition
def f(x):
    return 4 * x + math.sin(x) - math.exp(x)

# Derivative of the function (for Newton-Raphson)
def f_prime(x):
    return 4 + math.cos(x) - math.exp(x)

# Bisection Method
def bisection_method(a, b, tol):
    steps = 0
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    while (b - a) / 2 > tol:
        steps += 1
        c = (a + b) / 2  # Midpoint
        if f(c) == 0:  # Found exact root
            break
        elif f(a) * f(c) < 0:
            b = c  # Root lies in [a, c]
        else:
            a = c  # Root lies in [c, b]
    return steps

# Newton-Raphson Method
def newton_raphson_method(x0, tol, max_iter=500):
    steps = 0
    x = x0
    for _ in range(max_iter):
        steps += 1
        fx = f(x)
        fpx = f_prime(x)
        if fpx == 0:
            raise ValueError("Derivative is zero. Newton-Raphson method fails.")
        x_new = x - fx / fpx
        if abs(x_new - x) < tol:  # Convergence check
            break
        x = x_new
    return steps

# Comparison Function
def compare_methods(a, b, x0, tol):
    try:
        bisection_steps = bisection_method(a, b, tol)
        newton_steps = newton_raphson_method(x0, tol)
        print(f"Bisection Method Steps: {bisection_steps}")
        print(f"Newton-Raphson Method Steps: {newton_steps}")
    except ValueError as e:
        print(f"Error: {e}")

# Example Usage
a, b = 0, 1  # Interval for bisection method
x0 = 0.5     # Initial guess for Newton-Raphson method
tol = 1e-6   # Tolerance

compare_methods(a, b, x0, tol)