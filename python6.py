
# Python Program to find the area of triangle
a = float(input('Enter first side '))
b = float(input('Enter second side '))
c = float(input('Enter third side '))
s = (a + b + c) / 2         # calculating the semi-perimeter
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of Triangle is %0.2f' %area)