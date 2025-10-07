#1
lst = []
for i in range(10):
    num = int(input("Enter the number: "))
    lst.append(num)
print("Largest:", max(lst))
print("Smallest:", min(lst))

#2
names = []
for i in range(5):
    name = input("Enter the name: ")
    names.append(name)
print("Sorted Names:", sorted(names))

#3
lst = [1, 3, 5, 7, 9]
reverse = lst[::-1]
print("Reversed list:", reverse)

#4
marks = []
n = int(input("Number of students: "))
for i in range(n):
    mark = int(input("Enter the marks of the student: "))
    marks.append(mark)
average = sum(marks) / len(marks)
print("Average of marks:", average)

#5
lst = [1, 3, 5, 7, 9]
i = 0

while i < len(lst):
    print(lst[i])
    i = i + 1