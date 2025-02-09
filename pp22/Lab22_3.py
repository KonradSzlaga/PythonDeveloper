class Book():
    def __init__(self, author, publisher, genre, title):
        self.__author = author
        self.__publisher = publisher
        self.__genre = genre
        self.__title = title


    def give_short_info(self):
        print(f"Title: {self.__title}, by {self.__author}.")


    def give_full_info(self):
        print(f"Title: {self.__title}, written by {self.__author}, published by: {self.__publisher}. Genre: {self.__genre}.")


books = []

# Tworzenie obiektów klasy Book
books.append(Book("J.K. Rowling", "Bloomsbury", "Fantasy", "Harry Potter and the Sorcerer's Stone"))
books.append(Book("George Orwell", "Secker & Warburg", "Dystopian", "1984"))
books.append(Book("J.R.R. Tolkien", "Allen & Unwin", "Fantasy", "The Lord of the Rings"))
books.append(Book("Agatha Christie", "Collins Crime Club", "Mystery", "Murder on the Orient Express"))
books.append(Book("Stephen King", "Viking Press", "Horror", "The Shining"))
books.append(Book("Harper Lee", "J.B. Lippincott & Co.", "Fiction", "To Kill a Mockingbird"))
books.append(Book("Dan Brown", "Doubleday", "Thriller", "The Da Vinci Code"))
books.append(Book("F. Scott Fitzgerald", "Charles Scribner's Sons", "Classic", "The Great Gatsby"))

for book in books:
    book.give_short_info()
    book.give_full_info()