# NUMPY AND PANDAS ASSIGNMENT


import numpy as np
import pandas as pd



# QUESTION 1
# Create a NumPy array containing numbers from 1 to 10
# and reshape it to a 2x5 matrix.


print("=" * 60)
print("QUESTION 1")
print("=" * 60)

arr1 = np.arange(1, 11)

matrix = arr1.reshape(2, 5)

print("NumPy Array:")
print(arr1)

print("\n2 x 5 Matrix:")
print(matrix)



# QUESTION 2
# Create a NumPy array containing numbers from 1 to 20
# and extract elements between the 5th and 15th index.


print("\n" + "=" * 60)
print("QUESTION 2")
print("=" * 60)

arr2 = np.arange(1, 21)

# Extract elements from index 5 through index 15
result = arr2[5:16]

print("Original Array:")
print(arr2)

print("\nElements from 5th index to 15th index:")
print(result)



# QUESTION 3
# Compute mean, median, and standard deviation
# using the array created in Question 2.


print("\n" + "=" * 60)
print("QUESTION 3")
print("=" * 60)

mean = np.mean(result)
median = np.median(result)
standard_deviation = np.std(result)

print("Array:")
print(result)

print("\nMean:", mean)
print("Median:", median)
print("Standard Deviation:", standard_deviation)



# QUESTION 4
# Create a 2D array x of shape (3,4)
# and a 1D array y of shape (4,).
# Subtract y from each row of x using broadcasting.


print("\n" + "=" * 60)
print("QUESTION 4")
print("=" * 60)

x = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

y = np.array([1, 2, 3, 4])

# Broadcasting
result_broadcasting = x - y

print("Array X:")
print(x)

print("\nArray Y:")
print(y)

print("\nResult after Broadcasting:")
print(result_broadcasting)



# QUESTION 5
# Create a DataFrame with name, age and gender.
# The DataFrame should have 10 rows.


print("\n" + "=" * 60)
print("QUESTION 5")
print("=" * 60)

data = {
    "name": [
        "Anu",
        "Rahul",
        "Meera",
        "Arjun",
        "Sneha",
        "Vishnu",
        "Diya",
        "Akhil",
        "Neha",
        "Ravi"
    ],

    "age": [
        22,
        28,
        35,
        31,
        25,
        40,
        29,
        33,
        24,
        38
    ],

    "gender": [
        "Female",
        "Male",
        "Female",
        "Male",
        "Female",
        "Male",
        "Female",
        "Male",
        "Female",
        "Male"
    ]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)



# QUESTION 5.1
# Add a new column called occupation.
# Values: Programmer, Manager and Analyst.


print("\n" + "=" * 60)
print("QUESTION 5.1")
print("=" * 60)

df["occupation"] = [
    "Programmer",
    "Manager",
    "Analyst",
    "Programmer",
    "Manager",
    "Analyst",
    "Programmer",
    "Manager",
    "Analyst",
    "Programmer"
]

print("DataFrame after adding occupation:")
print(df)



# QUESTION 5.2
# Select rows where age is greater than or equal to 30.


print("\n" + "=" * 60)
print("QUESTION 5.2")
print("=" * 60)

filtered_df = df[df["age"] >= 30]

print("Rows where age >= 30:")
print(filtered_df)



# QUESTION 5.3
# Convert DataFrame to CSV, read the CSV file,
# and display its contents.


print("\n" + "=" * 60)
print("QUESTION 5.3")
print("=" * 60)

# Convert DataFrame to CSV
df.to_csv("employees.csv", index=False)

print("DataFrame successfully saved as employees.csv")

# Read the CSV file
csv_data = pd.read_csv("employees.csv")

print("\nContents of the CSV file:")
print(csv_data)


# COMPLETED


print("\n" + "=" * 60)
print("ASSIGNMENT COMPLETED SUCCESSFULLY")
print("=" * 60)
