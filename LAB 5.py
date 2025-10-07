#1
def averageMarks(sub1=0, sub2=0, sub3=0):
    return (sub1 + sub2 + sub3) / 3

print("Average Marks:", averageMarks(80, 90))


#2
def totalBill(items):
    total = 0
    for name, price in items:
        total += price
    return total

bill = totalBill([("coffee", 25), ("Sandwich", 5), ("cake", 3)])
print("Total Bill:", bill)


#3
def applyDiscount(price, discount):
    return price * (1 - discount)

print("Price after discount:", applyDiscount(100, 0.15))


#4
def calculateArea(length, breadth=None):
    if breadth is None:
        return length * length
    else:
        return length * breadth

print("Square Area:", calculateArea(5))
print("Rectangle Area:", calculateArea(5, 10))


#5
def bonus(salary, rate=0.10):
    return salary * (1 + rate)

print("Bonus with positional:", bonus(50000, 0.10))
print("Bonus with keyword:", bonus(salary=50000, rate=0.20))
print("Bonus with default rate:", bonus(50000))


#6
def studentRecord(course, *subjects, **details):
    print("Course:", course)
    print("Subjects:", subjects)
    print("Details:", details)

studentRecord("B.Tech", "Maths", "Physics", "Chem", age=20, grade='A')
