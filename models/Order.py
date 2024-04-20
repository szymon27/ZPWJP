class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        list_books = "".join(f"{item}" for item in self.books)
        return f"{self.employee} Order student: {self.student} Date: {self.order_date} Books: {list_books}"
