from models.Student import Student


if __name__ == '__main__':
    student1 = Student("Szymon", [50, 60, 40])
    student2 = Student("Jan", [41, 50, 60, 50])
    print(student1.is_passed())
    print(student2.is_passed())
