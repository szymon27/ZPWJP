class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return sum(self.marks) / len(self.marks) > 50
