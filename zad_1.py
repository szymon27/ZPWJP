class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return sum(self.marks) / len(self.marks) > 50

        

if __name__ == '__main__':
    student1 = Student("Szymon", [50, 60, 40])
    student2 = Student("Jan", [41, 50, 60, 50])
    print(student1.is_passed())
    print(student2.is_passed())