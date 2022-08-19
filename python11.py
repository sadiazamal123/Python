# python code to find product and sum of numbers from 1 to n.
from itertools import product
n = int(input("Enter number: "))
sum = 0
product= 1
# loop from 1 to n
for num in range(1, n + 1, 1):
    sum = sum + num
    product = product * num
print("Sum of first ",n, "numbers is: ", sum)
print("Product of first ",n, "numbers is: ", product)