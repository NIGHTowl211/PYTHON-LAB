#1
import math
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(distance)

#2
import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
print(a + b)

#3
s = "Python"
print(s[::-1])

#4
s = "hello world"
vowels = "aeiouAEIOU"
count = sum(1 for ch in s if ch in vowels)
print(count)

#5
s = "madam"
print("Palindrome" if s == s[::-1] else "Not Palindrome")

#6
s = "python is fun"
print(s.replace(" ", "-"))

#7
s = "hello world from python"
print(s.title())