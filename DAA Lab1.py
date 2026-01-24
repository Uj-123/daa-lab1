# find even and odd
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("number is even")
else:
   print("number is odd")

# to find square of a number

def square(num):
    return num * num
print (square(num))

# find the largest number
a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))
c = int(input("Enter a third number: "))
if a>b and a>c:
    print("a is largest number")
elif b>c:
    print("b is largest number")
else:
    print("c is largest number")


# sum of all element in the list
number=[2,4,7,8,5]
print("Sum of elements:", sum(number))

#find the reverse of the string
string = "sarita"
reversed_string = string[::-1]

print("Reversed string:", reversed_string)

#find the palindrome
word = input("Enter a word: ")

if word == word[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

#find the factorial number using recursion
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))

# Check for negative numbers
if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    print("Factorial of", num, "is", factorial(num))

# to check if the given number is prime
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a Prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime number")
            break
    else:
        print("Prime number")

#find the sequential search
l=list()
n=int(input("Enter number of elements to be inserted into list: "))
print("enter", n, "values")
for i in range(n):
    l.append(int(input()))
s=int(input("Enter element to be searched: "))
for i in range(len(l-1)):
    if l[i] == s:
        print("Element found at index", i+1)
        break
    else:
        print("Element not found")

