# Python Program to Print Odd Numbers from Minimum to Maximum

minimum = int(input(" Please Enter the Minimum Value : "))
maximum = int(input(" Please Enter the Maximum Value : "))

for number in range(minimum, maximum+1):
    if(number % 2 != 0):
        print("{0}".format(number))

# Python Program to Print even Numbers from Minimum to Maximum
# for number in range(minimum, maximum+1):
#     if(number % 2 == 0):
#         print("{0}".format(number))