# Python code to check prime number using if-else statement
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if (num % i == 0):
            print(num, 'is not a prime number.')
            break
    else:
        print(num, 'is a prime number.')
            
# If entered number is less than 1, then it is not a prime number
else:
    print(num, "is not a prime number.")