class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
    
    def __str__(self):
        return f"{self.street}, {self.zip_code} {self.city} Phone: {self.phone} Open hours: {self.open_hours}"
        
class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"{self.first_name} {self.last_name} Hired: {self.hire_date} Born: {self.birth_date} Location: {self.street}, {self.zip_code} {self.city} Phone: {self.phone}"

class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"{self.author_name} {self.author_surname} Published on: {self.publication_date} Pages: {self.number_of_pages} Library: {self.library}"

class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        list_books = "".join(f"{item}" for item in self.books)
        return f"{self.employee} Order student: {self.student} Date: {self.order_date} Books: {list_books}"


if __name__ == '__main__':
    library1 = Library("City1", "Street1", "11-111", "8:00 - 16:00", "111-111-111")
    library2 = Library("City2", "Street2", "22-222", "9:00 - 7:00", "222-222-222")

    employee1 = Employee("En1", "Es1", "2011-01-01", "1991-01-01", "City1", "Street1", "11-111", "111-000-111")
    employee2 = Employee("En2", "Es2", "2012-02-02", "1982-02-02", "City2", "Street2", "22-222", "222-000-222")
    employee3 = Employee("En3", "Es3", "2013-03-03", "1993-03-03", "City3", "Street3", "33-333", "333-000-333")

    book1 = Book(library1, "2011-01-01", "Author1", "Surname1", 100)
    book2 = Book(library2, "2012-02-02", "Author2", "Surname2", 200)
    book3 = Book(library1, "2013-03-03", "Author3", "Surname3", 300)
    book4 = Book(library2, "2014-04-04", "Author4", "Surname4", 400)
    book5 = Book(library1, "2015-05-05", "Author5", "Surname5", 500)

    order1 = Order(employee1, "Student1", [book1, book2, book3], "2023-04-04")
    order2 = Order(employee2, "Student2", [book4, book5], "2023-05-05")

    print(order1)
    print(order2)