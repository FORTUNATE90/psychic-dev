import random

# Generate 1000 random sensor data inputs
sensor_data = [random.randint(1, 10000) for _ in range(1000)]

def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

# Example usage
target = sensor_data[500]  # Pick a random target from the dataset
index = linear_search(sensor_data, target)
print(f"Linear Search: Found target at index {index}")

def binary_search(data, target):
    left, right = 0, len(data) - 1
    while left <= right:
        mid = ( merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example usage
sorted_data = merge_sort(sensor_data.copy())
print("Merge Sort: Finished sorting")

def quick_sort(data):
    if len(data) <= 1:
        generated sensor data (1000 inputs) and measure the number of steps or time taken. Use Python's `time` library for benchmarking.

```python
import time

# Measure execution time
start = time.time()
sorted_data = quick_sort(sensor_data.copy())
end = time.time()
print(f"Quick Sort Execution Time: {end - start:.6f} seconds")