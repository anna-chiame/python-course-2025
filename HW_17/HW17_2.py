# Task 2
#  клас Автор
class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []  # список об'єктів Book, написаних цим автором

    def __str__(self):
        return f"{self.name} ({self.country}, {self.birthday})"

    def __repr__(self):
        return f"Author(name='{self.name}', country='{self.country}', birthday='{self.birthday}')"

#  клас Книга
class Book:
    total_books = 0  # класова змінна

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author  # посилання на об'єкт Author
        Book.total_books += 1  # кожного разу, коли створюється книга

    def __str__(self):
        return f"'{self.name}' ({self.year}) by {self.author.name}"

    def __repr__(self):
        return f"Book(name='{self.name}', year={self.year}, author='{self.author.name}')"

# клас Бібліотека
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        """
        Створює нову книгу, додає її в бібліотеку і в список книг автора.
        """
        book = Book(name, year, author)
        self.books.append(book)

        if author not in self.authors:
            self.authors.append(author)

        author.books.append(book)
        return book

    def group_by_author(self, author):
        """
        Повертає список книг, написаних цим автором.
        """
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        """
        Повертає список книг, виданих у вказаний рік.
        """
        return [book for book in self.books if book.year == year]

    def __str__(self):
        return f"Library '{self.name}' with {len(self.books)} books"

    def __repr__(self):
        return f"Library(name='{self.name}', books={len(self.books)}, authors={len(self.authors)})"

# Приклади
franko = Author("Іван Франко", "Україна", "1856-08-27")
lesya = Author("Леся Українка", "Україна", "1871-02-25")
shevchenko = Author("Тарас Шевченко", "Україна", "1814-03-09")
kostomarov = Author("Микола Костомаров", "Україна", "1817-05-16")
skovoroda = Author("Григорій Сковорода", "Україна", "1722-12-03")
orwell = Author("George Orwell", "UK", "1903-06-25")
austen = Author("Jane Austen", "UK", "1775-12-16")
rowling = Author("J.K. Rowling", "UK", "1965-07-31")
hemingway = Author("Ernest Hemingway", "USA", "1899-07-21")

lib = Library("UkrLit & World Classics")

lib.new_book("Кобзар", 1840, shevchenko)
lib.new_book("Лісова пісня", 1911, lesya)
lib.new_book("Перехресні стежки", 1900, franko)
lib.new_book("1984", 1949, orwell)
lib.new_book("Pride and Prejudice", 1813, austen)
lib.new_book("The Old Man and the Sea", 1952, hemingway)

print("\n=== Книги Івана Франка ===")
print(lib.group_by_author(franko))

print("\n=== Книги за 1949 рік ===")
print(lib.group_by_year(1949))

print("\n=== Уся бібліотека ===")
for b in lib.books:
    print(b)

print("\nЗагальна кількість створених книг:", Book.total_books)