# Task 1


class Person :
    def __init__(self, first_name, last_name, age,  birth_place, city, hobby ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.birth_place = birth_place
        self.city = city
        self.hobby = hobby
    def intro (self) :
        return f"Hello my name is {self.first_name} {self.last_name}. I'm {self.age}"
    def show_hobby (self) :
        return f"My hobby is {self.hobby}"
    def relocation(self):
        if self.birth_place != self.city :
            return f"I was born in {self.birth_place}, but now I'm living in {self.city}"
        else:
            return f"I've never leave my native {self.birth_place}"


class Student(Person) :
    def __init__(self,first_name, last_name,  age,  birth_place, city, hobby, course, extracurricular_courses  ):
        super().__init__(first_name, last_name, age, birth_place, city, hobby)
        self.course = course
        self.extracurricular_courses = extracurricular_courses
    def next_course (self) :
        intro = super().intro()
        return f"{intro}. Next year I will be on {int(self.course) + 1} course"

class Teacher(Person) :
    def __init__(self, first_name, last_name,  age, birth_place, city, hobby, subject, academic_degree, salary):
        super().__init__(first_name, last_name, age,  birth_place, city, hobby)
        self.subject = subject
        self.academic_degree = academic_degree
        self.salary = salary
    def teach (self) :
        return f"{self.first_name} {self.last_name} subject: {self.subject}"
student_1 = Student("John", "Jonson", 15, "London", "London", "Socker", 2, "Art" )
teacher_1 = Teacher("Peter", "McLoo", 35, "New York", "London", "Horse Ridding", "Math", "Doctor", 7500)
print("*"*20)
print(teacher_1.intro())
print(teacher_1.show_hobby())
print(teacher_1.relocation())
print(teacher_1.teach())
print("*"*20)
print(student_1.intro())
print(student_1.show_hobby())
print(student_1.relocation())
print(student_1.next_course())
