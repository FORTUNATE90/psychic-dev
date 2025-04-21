import matplotlib.pyplot as plt
import numpy as np

# Input size
n = np.linspace(1, 100, 500)

# Complexity functions
o_1 = np.ones_like(n)
o_log_n = np.log2(n)
o_n = n
o_nlogn = n * np.log2(n)
o_n2 = n**2
o_nk = n**3  # Example: k = 3

# Plot
plt.figure(figsize=(10, 6))
plt.plot(n, o_1, label="O(1)", linestyle="--")
plt.plot(n, o_log_n, label="O(log n)")
plt.plot(n, o_n, label="O(n)")
plt.plot(n, o_nlogn, label="O(n log n)")
plt.plot(n, o_n2, label="O(n^2)")
plt.plot(n, o_nk, label="O(n^k)")

# Labels and Legend
plt.title("Complexity Classes")
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time")
plt.ylim(0, 10000)  # Set a reasonable range for y
plt.legend()
plt.grid()
plt.show()


def access_element(arr):
    return arr[0]  # Accessing the first element is always constant time

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Not found

def sum_array(arr):
    total = 0
    for num in arr:
        total += num  # Iterating through the array once
    return total