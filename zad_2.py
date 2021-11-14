from datetime import date
from zad_1 import Student


class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: int):
        self.city = city
        self.street = street,
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return f'Księgarnia: ul. {self.street} {self.zip_code} {self.city}' \
                f'otwarta w godzinach: {self.open_hours}, tel. {self.phone}'


class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: date, birth_date: date,
                 city: str, street: str, zip_code: str, phone: int):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self) -> str:
        return f'Pracownik: {self.first_name}, {self.last_name},' \
               f'zatrudniony {self.hire_date}, ' \
               f'urodzony: {self.birth_date}, ' \
               f'nr {self.phone}, ' \
               f'adres ul. {self.street} {self.zip_code} {self.city}'


class Book:
    def __init__(self, library: Library, publication_date: date, author_name: str,
                 author_surname: str, number_of_pages: int):
        self.library = library,
        self. publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self) -> str:
        return f'Książka, zbiór biblioteki: {self.library} ' \
               f'data publikacji {self.publication_date} ' \
               f'autor: {self.author_name} {self.author_surname} ' \
               f'liczba stron: {self.number_of_pages}'


class Order:
    def __init__(self, employee: Employee, student: Student, book: Book, order_date: date):
        self.employee = employee
        self.student = student
        self.book = book
        self.order_date = order_date

    def __str__(self):
        return f'Zamówienie - ' \
              f'Pracownik biblioteki: {self.employee}' \
              f'studencie: {self.student},' \
              f'książce: {self.book}, ' \
              f'data zamówienia: {self.order_date}'


if __name__ == '__main__':
    lib1 = Library('Katowice', '1 Maja 49', '40-300', '8-17', 725314999)
    lib2 = Library('Kraków', 'Dobra 42', '11-100', '10-20', 554236789)
    ks1 = Book(lib1, 1972-11-22, 'Adam', 'Mickiewicz', 256)
    ks2 = Book(lib2, 1999-8-1, 'Tom', 'Min', 450)
    ks3 = Book(lib2, 2021-5-4, 'Remigiusz', 'Mróz', 321)
    ks4 = Book(lib2, 2005-10-6, 'Harlan', 'Coben', 211)
    ks5 = Book(lib1, 2013-8-17, 'Marry', 'Mea', 100)
    em1 = Employee('Ada', 'Nak', 2020-9-1, 1997-6-14, 'Klast', 'ul. Miodowa 4', '14-574', 742159369)
    em2 = Employee('Krzysztof', 'Kada', 2017-5-23, 1986-2-14, 'Opoczno', 'ul. Leśna 14/1', '23-109', 856147269)
    em3 = Employee('Magda', 'Rekla', 2021-4-24, 2000-9-26, 'Namysłów', 'ul. Prosta 33', '43-000', 824526123)
    st1 = Student('Maja K', 85)
    st2 = Student('Lu', 62)
    st3 = Student('Kim', 42)
    ord = Order(em2, st2, ks3, 2021-11-5)
    ord2 = Order(em1, st3, ks4, 2021-10-29)
    print(ord)
    print(ord2)


    print(ks1)
