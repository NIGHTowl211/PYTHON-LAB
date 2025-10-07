#1
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

#2
for i in range(1, 6):
    for j in range(5, i - 1, -1):
        print(j, end="")
    print()

#3
n = int(input("Enter a number: "))
flag = 0
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            flag = 1
            break
    print("Not Prime" if flag else "Prime")
else:
    print("Not Prime")

#4
n = int(input("Enter a number: "))
sum_digits = 0
while n > 0:
    sum_digits += n % 10
    n //= 10
print(sum_digits)

#5
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
