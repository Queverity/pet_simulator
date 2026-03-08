class Student:
    def __init__(self,name,grade,age):
        self.name = name
        self.grade = grade
        self.age = age

    def grade_up(self):
        self.grade += 1
        self.age += 1

student_one = Student("Dave",5,11)

print(f"Grade: {student_one.grade}th | Age: {student_one.age}")

student_one.grade_up()

print(f"Grade: {student_one.grade}th | Age: {student_one.age}")