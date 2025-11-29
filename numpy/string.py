
import numpy  as np
ar1=np.array(['Aditya','Sham','Ram'])
ar2=np.array(['Aditya','Raj','Ram'])
print("First Array:",ar1)
print("Second Array:",ar2)

print("Equal:",np.char.equal(ar1,ar2))


print("Not Equal:",np.char.not_equal(ar1,ar2))

print("Grater than:",np.char.greater(ar1,ar2))

print("Less:",np.char.less(ar1,ar2))

print("Grater Equal:")
print(np.char.greater_equal(ar1,ar2))

print("Less Equal:")
print(np.char.less_equal(ar1,ar2))