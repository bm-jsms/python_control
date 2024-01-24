class Students:
    students = []

    def __init__(self, name, age):
        self.name = name
        self.age = age

        Students.students.append(self)

    @staticmethod
    def is_adult(age):
        return age >= 18

    @classmethod
    def create_student(cls, name, age):
        if cls.is_adult(age):
            return cls(name, age)
        else:
            print(f"\n[!] The student {name} is not an adult")

    @classmethod
    def show_students(cls):
        for i, student in enumerate(cls.students):
            print(f"\n[{i + 1}] {student.name} - {student.age}")


Students.create_student("Hackermate", 23)
Students.create_student("Hackerman", 24)
Students.create_student("Nero", 28)
Students.create_student("Diana", 27)
Students.create_student("Xerosec", 15)

print(Students.show_students())
