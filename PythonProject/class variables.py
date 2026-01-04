# class variables = shared among all instances of a class
# defined outside the constructor
# allow you to share data among all objects created from that class

class Student:
    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("amine", 23)
student2 = Student("coco", 40)
student3 = Student("popo", 25)
print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)
print(Student.class_year)
print(Student.num_students)

print(f"my graduating class of {Student.class_year} has {student1.num_students} students")