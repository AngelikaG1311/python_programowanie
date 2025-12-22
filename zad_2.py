from datetime import date


class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f" Library:\n"
            f" Address: {self.street},{self.zip_code},{self.city}\n"
            f" Open hours: {self.open_hours}\n"
            f" Phone: {self.phone}\n"
        )


class Employee:
    def __init__(self, first_name, last_name, hire_date,
                 birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f" {self.first_name} {self.last_name}\n"
            f" Hire date:{self.hire_date}\n"
            f" Birth date:{self.birth_date}\n"
            f" Address:{self.street}, {self.zip_code} {self.city}\n"
            f" Phone:{self.phone}\n"
        )


class Book:
    def __init__(self, library, publication_date, author_name,
                 author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f" Author:{self.author_name} {self.author_surname}\n"
            f" Publication date:{self.publication_date}\n"
            f" Pages:{self.number_of_pages}\n"
            f" Available in:{self.library}\n"
        )


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return (
            f" {self.name} {self.surname}"
        )


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return (
            f" Order date: {self.order_date}\n"
            f" Handled by:{self.employee}\n"
            f" Student:{self.student}\n"
            f" Books:{self.books}"
        )


library1 = Library(
    "Krakow",
    "Starowislna 5",
    "30-001",
    "8:00-18:00",
    "111-222-333")
library2 = Library(
    "Krakow",
    "Szkolna 7",
    "30-002",
    "8:00-16:00",
    "444-222-333")

book1 = Book(library1, 2012, "Stephen", "King", 500)
book2 = Book(library1, 2011, "Martin", "Harari", 430)
book3 = Book(library2, 2015, "Jane", "Jacobs", 200)
book4 = Book(library2, 2013, "Thomas", "Martin", 590)
book5 = Book(library1, 2018, "Frank", "Herbert", 450)

employee1 = Employee(
    "Adam",
    "Nowak",
    date(
        2021,
        8,
        9),
    date(
        1993,
        12,
        11),
    "Krakow",
    "Krolewska 4",
    "30-009",
    "777-333-111")
employee2 = Employee("Bartosz", "Mazurek", date(2022, 7, 5), date(
    1991, 3, 5), "Wieliczka", "Solna 2", "30-002", "555-333-111")
employee3 = Employee("Andrzej", "Lasek", date(2020, 4, 4), date(
    1992, 8, 9), "Olkusz", "Krakowska 7", "30-003", "777-333-888")

student1 = Student("Anna", "Wisniewska")
student2 = Student("Piotr", "Lewandowski")

order1 = Order(employee1, student2, book5, date(2025, 12, 21))
order2 = Order(employee2, student1, book3, date(2025, 12, 20))

print(order1)
print(order2)
