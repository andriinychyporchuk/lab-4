class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def calculate_average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0
    
class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, name):
        self.students = [student for student in self.students if student.name != name]

    def list_students_with_average_grades(self):
        for student in self.students:
            average_grade = student.calculate_average_grade()
            print(f"Name: {student.name}, Average Grade: {average_grade}")

classroom = Classroom()

while True:
    print("1. Додати студента")
    print("2. Видалити студента")
    print("3. Показати список студентів")
    print("4. Вийти")

    choice = input("Виберіть опцію: ")

    if choice == "1":
        name = input("Введіть ім'я студента: ")
        grades = input("Введіть оцінки студента (через пробіл): ").split()
        grades = [int(grade) for grade in grades]
        student = Student(name, grades)
        classroom.add_student(student)
    elif choice == "2":
        name = input("Видалити студента: ")
        classroom.remove_student(name)
    elif choice == "3":
        classroom.list_students_with_average_grades()
    elif choice == "4":
        break
    else:
        print("Невірна команда.")