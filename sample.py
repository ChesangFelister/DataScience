import numpy as np

my_list = [1, 2, 3]
my_list1 = [5, 6, 7, 8]

my_array = np.array([my_list, my_list1])
print(my_array)

print(my_array.shape)

print(my_array.dtype)
new_array = np.arange(5,50,3)
print(new_array)
