#factorial of a number

factorial = 1
number = int(input('Pls enter a number: '))
for i in range(1,number+1):
    factorial*=i
print(f"The factorial of number {number} is {factorial}")