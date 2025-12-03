import matplotlib.pyplot as plt

marks = [
    45, 67, 89, 56, 45, 23, 90, 77, 56, 43,
    34, 67, 22, 10, 88, 76, 54, 33, 21, 19,
    90, 92, 55, 60, 72, 84, 38, 46, 51, 63,
    70, 73, 66, 28, 39, 40, 58, 46, 47, 65,
    75, 85, 95, 99, 12, 18, 27, 37, 49, 57
]

plt.hist(marks,bins=30,color='green')
plt.title("Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of students")
plt.grid(True)
plt.show()
