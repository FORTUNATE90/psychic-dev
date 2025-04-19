# Example: Coordinate points
point = (10, 20)
print("Tuple:", point)
# Accessing elements
print("X-coordinate:", point[0])

# Example: Looping over a range
for i in range(1, 6):
    print(f"Range value: {i}")

# Example: Modifying a list
fruits = ["apple", "banana"]
fruits.append("cherry")
fruits[0] = "orange"
print("List:", fruits)

# List is mutable
mutable_list = [1, 2, 3]
mutable_list[0] = 10
print("Mutable List:", mutable_list)

# Tuple is immutable
immutable_tuple = (1, 2, 3)
try:
    immutable_tuple[0] = 10  # Error
except TypeError as e:
    print("Error:", e)