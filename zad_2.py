from models.Library import Library
from models.Book import Book
from models.Employee import Employee
from models.Order import Order


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
