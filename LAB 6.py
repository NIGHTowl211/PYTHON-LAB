# Create a python class called bank account which repetresent a bank account having attribute account number, name, balaance.
# Create a constructer with parameter account number, name, balance. 
# Create a deposit method which manages a depot actions
# create a withdrawal method which manages withdrawal actions
# create a bank fees method to apply the bank fees with a percentage of 5 percent of the balace account. 
# create a display menthod to display account details.

class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance


    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance+amount
            print(f"Deposited: ₹{amount:.2f}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance = self.balance- amount
            print(f"Withdrawn: ₹{amount:.2f}")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

    def bank_fees(self):
        fee = self.balance * 0.05
        self.balance= self.balance- fee
        print(f"Bank fees applied: ₹{fee:.2f}")

    
    def display(self):

        print(f"Account Number: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Balance: ₹{self.balance:.2f}")

account = BankAccount(123456, "Alisha", 1000)
account.display()
account.deposit(2000)
account.withdraw(1200)
account.bank_fees()
account.display()

#Create 2 employees and print their salary slips.Methods:
#calculate_salary() → Returns total salary after adding DA (20%) and HRA (15%).
#display() → Prints employee details with total salary.

class Employee:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        da = self.salary * 0.20           
        hra = self.salary * 0.15          
        total_salary = self.salary + da + hra
        return total_salary

    def display(self):
        total = self.calculate_salary()
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Basic Salary: ₹{self.salary:.2f}")
        print(f"Total Salary: ₹{total:.2f}")


emp1 = Employee(1, "Aman", 10000)
emp2 = Employee(2, "Alisha", 20000)

emp1.display()
emp2.display()

# You are designing a program for a school.
# Create a Student class with the following attributes:

# name, roll_no, marks (out of 100)

# Scenario:

# Create 3 student objects.
# Display their details.
# Add a method grade() that prints "Pass" if marks ≥ 40, otherwise "Fail".

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):

        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")

    def grade(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")
        print()


student1 = Student("Priya", 1, 55)
student2 = Student("Aman", 2, 37)
student3 = Student("Alisha Raj", 3, 86)

student1.display()
student1.grade()
student2.display()
student2.grade()
student3.display()
student3.grade()


