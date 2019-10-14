# Write a class structure that implements a library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []

# Library class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance of
# Book class and adds the book to books list for current library.
# - group_by_author(author: Author) - returns a list of all books grouped by
# the specified author
# - group_by_year(year: int) - returns a list of all books grouped by the
# specified year

# All 3 classes must have a readable __repr__ method!

# Also, book class should have a class variable which holds the amount of
# all existing books


class Author:
    def __init__(self, name: str, country: str, birthday: int, books: list):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __repr__(self):
        return f'{self.name} (born in {self.birthday} in {self.country})'


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.authors = set()
        self.books_amount = 0

    def new_book(self, name: str, year: int, author: Author, b_type: str):
        book = Book(name, year, author, b_type)
        if book not in self.books:
            self.books.append(book)
            self.authors.add(author)
            self.books_amount += 1

    def group_by_author(self, author: Author):
        return [book.name for book in self.books if book.author.name == author.name]

    def group_by_year(self, year: int):
        return [book.name for book in self.books if book.year == year]

    def fetch_by_type(self, fetch_type: str):
        return [book.name for book in self.books if book.type == fetch_type]

    def __repr__(self):
        return f'The library is called {self.name} and has' \
               f'{self.books_amount} books in total.'


class Book:
    def __init__(self, name: str, year: int, author: Author, b_type: str):
        self.name = name
        self.year = year
        self.author = author
        self.type = b_type

    def __repr__(self):
        return f'The book "{self.name}" is written by {self.author} in {self.year}.'


A = Author('Haruki Murakami', 'Japan', 1949, ['Norwegian Wood', '1Q84'])

B = Library('№ 1')
B.new_book('1Q84', 2009, A, 'novel')
B.new_book('Men without Women', 2014, A, 'novel')
B.new_book('Tokyo legends', 2006, A, 'storybook')

for book in B.books:
    print(book)

print(B.group_by_author(A))
print(B.group_by_year(2009))
print(B.fetch_by_type('novel'))
