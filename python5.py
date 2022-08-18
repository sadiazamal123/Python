# python code to reverse an array (using user define func.)
# def reverseList(A):
#   print( A[::-1])
# A = [10, 20, 30, 40, 50]
# reverseList(A)

# python code to reverse an array (using lib. func)
# from array import *
# array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
# print("Original array: "+str(array_num))
# array_num.reverse()
# print("Reverse the order of the items:")
# print(str(array_num))

# python code to reverse an array (using loop)
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = arr[-1]
if n > len(arr):
   print(f"{n} value is not valid")
else:
   for i in range(n // 2):
      arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
   print(arr)


# python code to reverse an array (using if-else)
# arr = [0, 92, 3, 4, 5, 6, 7, 8, 9]
# n = arr[-1]
# if n > len(arr):
#    print(f"{n} value is not valid")
# else:
#    arr = arr[n-1::-1] + arr[n:]
#    print(arr)