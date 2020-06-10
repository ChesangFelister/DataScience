import numpy as np

arr = np.arange(0, 12)
print(arr)

print(arr[0:5])
print(arr[2:6])

arr[0:5] = 20
print(arr)
arr2=arr[0:6]
arr2[:]= 29

print(arr)
