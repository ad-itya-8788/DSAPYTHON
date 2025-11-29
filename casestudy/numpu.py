import numpy as np

# -----------------------------
# 1) ARRAY CREATION
# -----------------------------
arr1 = np.array([1,2,3,4,5])
print("Normal Array:", arr1)

print("Add two in Each Element:",arr1+2)
print("Multiplay Each Element By 2",arr1*2)
print("Cos Value:",np.cos(arr1))
zeros_arr = np.zeros((2,3))
print("Zeros Array:\n", zeros_arr)

ones_arr = np.ones((3,3))
print("Ones Array:\n", ones_arr)

range_arr = np.arange(1, 11, 2)
print("Arange Array:", range_arr)

lin_arr = np.linspace(1, 5, 5)
print("Linspace Array:", lin_arr)

eye_mat = np.eye(4)
print("Identity Matrix:\n", eye_mat)

rand_arr = np.random.rand(3,3)
print("Random Decimal Array:\n", rand_arr)

rand_int = np.random.randint(10, 90, size=5)
print("Random Integers:", rand_int)

# -----------------------------
# 2) ARRAY PROPERTIES
# -----------------------------
print("Shape:", arr1.shape)
print("Size:", arr1.size)
print("Dimension:", arr1.ndim)
print("Datatype:", arr1.dtype)

# -----------------------------
# 3) MATHEMATICAL OPERATIONS (UFUNCS)
# -----------------------------
print("Square root:", np.sqrt(arr1))
print("Power (arr^2):", np.power(arr1,2))
print("Absolute:", np.abs(arr1))
print("Exponential:", np.exp(arr1))
print("Log:", np.log(arr1))
print("Sine:", np.sin(arr1))
print("Cosine:", np.cos(arr1))
print("Round:", np.round([1.2,3.6,4.5]))

# -----------------------------
# 4) STATISTICAL FUNCTIONS
# -----------------------------
arr2 = np.array([5,1,9,4,7,2])
print("Array:", arr2)
print("Mean:", np.mean(arr2))
print("Median:", np.median(arr2))
print("Standard Deviation:", np.std(arr2))
print("Variance:", np.var(arr2))
print("Sum:", np.sum(arr2))
print("Min:", np.min(arr2))
print("Max:", np.max(arr2))
print("Argmin (index):", np.argmin(arr2))
print("Argmax (index):", np.argmax(arr2))

# -----------------------------
# 5) INDEXING & SLICING
# -----------------------------
print("First Element:", arr2[0])
print("Slice [1:4]:", arr2[1:4])
print("Every 2nd Element:", arr2[::2])

twod = np.array([[1,2,3],[4,5,6]])
print("2D Array:\n", twod)
print("Element [1,2]:", twod[1,2])
print("First row:", twod[0,:])
print("Second column:", twod[:,1])

# -----------------------------
# 6) LOOP THROUGH 2D ARRAY
# -----------------------------
print("Looping:")
for i in range(twod.shape[0]):
    for j in range(twod.shape[1]):
        print(twod[i][j], end=" ")
    print()

# -----------------------------
# 7) SORTING
# -----------------------------
print("Sorted:", np.sort(arr2))
print("Argsort:", np.argsort(arr2))

# -----------------------------
# 8) LOGICAL & COMPARISON
# -----------------------------
print("arr2 > 5:", arr2 > 5)
print("Any True:", np.any(arr2 > 5))
print("All True:", np.all(arr2 > 0))
print("Where > 5:", np.where(arr2 > 5))

# -----------------------------
# 9) ARRAY RESHAPE & FLATTEN
# -----------------------------
reshaped = np.reshape(twod, (3,2))
print("Reshaped Array (3x2):\n", reshaped)

flattened = twod.flatten()
print("Flattened Array:", flattened)

# -----------------------------
# 10) MATRIX OPERATIONS
# -----------------------------
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

print("A + B:\n", A + B)
print("A - B:\n", A - B)
print("A * B (element-wise):\n", A * B)
print("Matrix Dot Product:\n", A.dot(B))
