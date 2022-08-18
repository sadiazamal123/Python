# Python code to create and print an array
import array as arr
# creating an array with integer type
a = arr.array('i', [1, 2, 3])            # i for integer numbers in array
print("The first array is : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()

# print any element of an array
print("First element:", a[0])
print("Second element:", a[1])
print("Last element:", a[-1])

# creating an array with float type
b = arr.array('d', [2.5, 3.2, 3.3])      # d for float numbers in array
print("The second array is : ", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")
