#create a base class person with atrribute name and age.
#create a derived class employee that inherits from person ands adds atrribute adds attribute employee id and salary.
#implement multilebvel inheritance with a class manager derived from employee with dept atrribute.
#implement multiple inheritance with a class "trainer" that inherits from employee and certification.
#create object for each class and display their info.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, employeeId, salary):
        super().__init__(name, age)
        self.employeeId = employeeId
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, age, employeeId, salary, dept):
        super().__init__(name, age, employeeId, salary)
        self.dept = dept


class Certification:
    def __init__(self, certification):
        self.certification = certification


class Trainer(Employee, Certification):
    def __init__(self, name, age, employeeId, salary, certification):
        Employee.__init__(self, name, age, employeeId, salary)
        Certification.__init__(self, certification)

    
if __name__ == "__main__":
    m = Manager("Aman", 35, "M123", 75000, "HR")
    print(f"Manager: {m.name}, Age: {m.age}, ID: {m.employeeId}, Salary: {m.salary}, Dept: {m.dept}")

    t = Trainer("Alisha", 40, "T456", 65000, "AWS Certified")
    print(f"Trainer: {t.name}, Age: {t.age}, ID: {t.employeeId}, Salary: {t.salary}, Certification: {t.certification}")


#an online store has a base class product and two derived class, electronics and clothing. electronics attribute- brand and warranty and clothin attribute- size and fabric type.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Electronics(Product):
    def __init__(self, name, price, brand, warranty):
        super().__init__(name, price)
        self.brand = brand
        self.warranty = warranty

class Clothing(Product):
    def __init__(self, name, price, size, fabricType):
        super().__init__(name, price)
        self.size = size
        self.fabricType = fabricType

if __name__ == "__main__":
    e = Electronics("Smartphone", 30000, "Samsung", "2 years")
    print(f"Electronics: {e.name}, Price: {e.price}, Brand: {e.brand}, Warranty: {e.warranty}")

    c = Clothing("T-shirt", 500, "L", "Cotton")
    print(f"Clothing: {c.name}, Price: {c.price}, Size: {c.size}, Fabric: {c.fabricType}")


#a school has a person teacher and class teacher, each level adds its own property and method.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def teach(self):
        print(f"{self.name} is teaching {self.subject}")


class ClassTeacher(Teacher):
    def __init__(self, name, age, subject, classSection):
        super().__init__(name, age, subject)
        self.class_section = class_section
    
    def manage_class(self):
        print(f"{self.name} manages class section {self.class_section}")


if __name__ == "__main__":
    p = Person("Ajay", 30)
    p.display_info()
    
    t = Teacher("Priya", 35, "Mathematics")
    t.display_info()
    t.teach()
    
    ct = ClassTeacher("Rahul", 40, "Science", "8A")
    ct.display_info()
    ct.teach()
    ct.manage_class()
