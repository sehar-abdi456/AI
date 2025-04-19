# Q1: Create a 1D NumPy array of integers from 10 to 50 and print the array
import numpy as np
arr = np.arange(10, 51)  # Create array from 10 to 50 (inclusive)
print("Array:", arr)

# Q2: Reshape the array into a 3x4 matrix and print
arr = np.arange(12).reshape(3, 4)  # Reshape 1D array of 12 elements to 3x4 matrix
print("Reshaped 3x4 matrix:\n", arr)

# Q3: Flatten a 2D array into a 1D array
arr = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array
flattened_arr = arr.flatten()  # Flatten the 2D array to 1D
print("Flattened array:", flattened_arr)

# Q4: Element-wise operations between two arrays (Sum, Difference, Product, Quotient)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("Sum:", arr1 + arr2)
print("Difference:", arr1 - arr2)
print("Product:", arr1 * arr2)
print("Quotient:", arr1 / arr2)

# Q5: Dot product of two 2D arrays
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
dot_product = np.dot(a, b)  # Dot product of a and b
print("Dot product:\n", dot_product)

# Q6: Compute Mean, Median, and Standard Deviation of an array
arr = np.array([10, 20, 30, 40, 50])
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))

# Q7: Sum of all elements, Sum of rows, Sum of columns
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Sum of all elements:", np.sum(arr))
print("Sum of rows:", np.sum(arr, axis=1))  # Sum along each row
print("Sum of columns:", np.sum(arr, axis=0))  # Sum along each column

# Q8: Filter elements greater than 25 from the array
arr = np.array([10, 20, 30, 40, 50])
filtered_arr = arr[arr > 25]  # Filter elements where values are greater than 25
print("Filtered elements:", filtered_arr)

# Q9: Find indices of non-zero elements in an array
arr = np.array([0, 3, 0, 5, 6, 0, 7])
non_zero_indices = np.nonzero(arr)  # Indices of non-zero elements
print("Indices of non-zero elements:", non_zero_indices)

# Q10: Generate random numbers
# a) 1D array of 10 random integers between 0 and 100
rand_integers = np.random.randint(0, 101, 10)
# b) 2D array of random floats (4x4)
rand_floats = np.random.random((4, 4))
print("Random integers:", rand_integers)
print("Random floats:\n", rand_floats)

# Q11: Generate random array with fixed seed and reproduce the result
np.random.seed(42)
rand_array = np.random.randint(1, 11, 5)  # Random integers between 1 and 10
print("Random array with seed 42:", rand_array)
np.random.seed(42)  # Reset seed
print("Reproduced array with seed 42:", np.random.randint(1, 11, 5))

# Q12: Stack arrays vertically and horizontally
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
# a) Stack vertically
vertical_stack = np.vstack((arr1, arr2))
# b) Stack horizontally
horizontal_stack = np.hstack((arr1, arr2))
print("Vertical stack:\n", vertical_stack)
print("Horizontal stack:", horizontal_stack)

# Q13: Create a histogram from random data
import matplotlib.pyplot as plt
data = np.random.randint(1, 101, 50)  # Generate random integers between 1 and 100
plt.hist(data, bins=10, edgecolor="black")
plt.title("Histogram")
plt.show()

# Q14: Generate results of 20 binomial experiments (successes in 10 trials)
results = np.random.binomial(10, 0.5, 20)
print("Number of successes in 20 experiments:", results)

# Q15: Create a stacked array with different constant rows
zeros = np.zeros((1, 4))
ones = np.ones((1, 4)) * -1
twos = np.ones((1, 4)) * 2
result = np.vstack((ones, zeros, twos))
print("Final array:\n", result)

# Q16: Create an array with specific step sizes and update a row
arr = np.arange(10, 50, 2).reshape(4, 5)  # Array from 10 to 48 with step 2
arr[3] = [1, 2, 3, 4, 5]  # Update the 4th row with new values
print("Updated array:\n", arr)

# Q17: Generate a sequence of -1 and 1
sequence = np.random.choice([-1, 1], size=10, p=[0.5, 0.5])
print("Sequence of -1 and 1:", sequence)

# Q18: Extract scores based on specific conditions (less than 130, for "Sta/ra", etc.)
names = np.array(["Roxana", "Sta/ra", "Roxana", "Sta/ra", "Roxana"])
scores = np.array([126, 115, 130, 141, 132])
# a) Extract scores < 130
print("Scores < 130:", scores[scores < 130])
# b) Scores of "Sta/ra"
print("Sta/ra's scores:", scores[names == "Sta/ra"])
# c) Add 10 points to Roxana's scores
scores[names == "Roxana"] += 10
print("Updated scores:", scores)

# Q19: Concatenate rows to form a new array
row1 = np.ones((1, 4)) * -1
row2 = np.zeros((1, 4))
row3 = np.ones((1, 4)) * 2
result = np.concatenate((row1, row2, row3), axis=0)
print("Array:\n", result)

# Q20: Create an array with even numbers from 2 to 40
arr = np.arange(2, 42, 2).reshape(4, 5)
print("Array:\n", arr)

# Q21: Create an array of even numbers and extract columns and rows
arr = np.arange(10, 50, 2).reshape(4, 5)
print("4x5 array of even numbers:\n", arr)
third_column = arr[:, 2]  # Extract third column
print("Third column:", third_column)
arr[3] = [1, 2, 3, 4, 5]  # Update the 4th row
print("Updated array:\n", arr)

# Q22: Convert sequence of 0 and 1 into -1 and 1
sequence = np.random.binomial(1, 0.5, 10)  # Generate 0 and 1
converted_sequence = np.where(sequence == 0, -1, 1)  # Map 0 to -1, 1 to 1
print("Converted sequence:", converted_sequence)
