# Create a file for writing and write initial smart meter readings
file_name = "smart_meter_readings.txt"
initial_readings = [
    "MeterID:1234, Reading: 450.50, Date: 2025-04-01\n",
    "MeterID:5678, Reading: 320.75, Date: 2025-04-02\n",
    "MeterID:9101, Reading: 280.10, Date: 2025-04-03\n"
]

# Open file in write mode and write initial data
with open(file_name, 'w') as fh:
    fh.writelines(initial_readings)
print(f"File '{file_name}' created and initial readings added.")

# Open file in read mode
with open(file_name, 'r') as fh:
    # Read the entire content
    content = fh.read()
print("File contents:")
print(content)

# New readings to append
new_readings = [
    "MeterID:1122, Reading: 500.20, Date: 2025-04-04\n",
    "MeterID:3344, Reading: 390.45, Date: 2025-04-05\n"
]

# Open file in append mode and add new data
with open(file_name, 'a') as fh:
    fh.writelines(new_readings)
print(f"New readings appended to '{file_name}'.")

# Open file in read mode
with open(file_name, 'r') as fh:
    print("Reading file line-by-line:")
    for line in fh:
        print(line.strip())  # Strip removes extra whitespace or newline characters

# Open file in read mode
with open(file_name, 'r') as fh:
    lines = fh.readlines()

# Print each line from the list
print("Processing lines as a list:")
for line in lines:
    print(line.strip())

# Open file in append mode
with open(file_name, 'a') as fh:
    single_reading = "MeterID:5566, Reading: 620.80, Date: 2025-04-06\n"
    fh.write(single_reading)
print(f"Single reading added to '{file_name}'.")

# Explicitly closing a file
fh = open(file_name, 'r')
print("Closing file explicitly.")
fh.close()



MeterID:1234, Reading: 450.50, Date: 2025-04-01
MeterID:5678, Reading: 320.75, Date: 2025-04-02
MeterID:9101, Reading: 280.10, Date: 2025-04-03
MeterID:1122, Reading: 500.20, Date: 2025-04-04
MeterID:3344, Reading: 390.45, Date: 2025-04-05
MeterID:5566, Reading: 620.80, Date: 2025-04-06