# Personal library management system using command line
import json

class Book_Collection:
    '''A class created to manage the huge collection of books'''

    def __init__(self):
        '''Constructor to initialize the book collection'''
        self.books_list = []  # List to store books
        self.storage_file = 'books.json'  # File to store book data
        self.read_books_from_file()  # Load books from file on initialization

    def read_books_from_file(self):
        '''Method to read books from the storage file'''
        try:
            with open(self.storage_file, 'r') as file:
                self.books_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.books_list = []

    def save_books_to_file(self):
        '''Method to save the book collection to a file'''
        with open(self.storage_file, 'w') as file:
            json.dump(self.books_list, file, indent=4)

    def create_new_book(self):
        '''Add a new book on the basis of the information provided by the user'''
        book_title = input("Enter the book title: ")
        book_author = input("Enter the author name: ")
        book_year = input("Enter the year of publication: ")
        book_genre = input("Enter the genre: ")
        book_is_read = input("Have you read this book? (yes/no): ").strip().lower() == 'yes'
        book = {
            'title': book_title,
            'author': book_author,
            'year': book_year,
            'genre': book_genre,
            'is_read': book_is_read
        }
        self.books_list.append(book)  # Add the book to the collection
        self.save_books_to_file()  # Save the updated collection to file
        print(f"Book '{book_title}' added to the collection.")

    def delete_book(self):
        '''Delete a book from the collection'''
        book_title = input("Enter the title of the book to delete: ")
        for book in self.books_list:
            if book['title'].lower() == book_title.lower():
                self.books_list.remove(book)
                self.save_books_to_file()
                print(f"Book '{book_title}' deleted from the collection.")
                return
        print(f"Book '{book_title}' not found in the collection.")

    def find_book(self):
        '''Find a book in the collection'''
        search_type = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
        search_text = input("Enter the search term: ").lower()
        found_books = [
            book
            for book in self.books_list
            if (search_text in book['title'].lower() or search_text in book['author'].lower())
        ]

        if found_books:
            print("Found books:")
            for index, book in enumerate(found_books):
                print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']}")
        else:
            print("No books found matching the search term.")

    def update_book(self):
        '''Update book information'''
        book_title = input("Enter the title of the book to update: ")
        for book in self.books_list:
            if book['title'].lower() == book_title.lower():
                print("Leave blank to keep current value.")
                book["title"] = input(f"New title ({book['title']}): ") or book["title"]
                book["author"] = input(f"New author ({book['author']}): ") or book["author"]
                book["year"] = input(f"New year ({book['year']}): ") or book["year"]
                book["genre"] = input(f"New genre ({book['genre']}): ") or book["genre"]
                is_read_input = input(f"Have you read this book? (yes/no): ").strip().lower()
                if is_read_input in ['yes', 'no']:
                    book["is_read"] = is_read_input == 'yes'

                self.save_books_to_file()
                print(f"Book '{book_title}' updated successfully.")
                return
        print(f"Book '{book_title}' not found in the collection.")

    def show_all_books(self):
        '''Display all books in the collection'''
        if not self.books_list:
            print("No books in the collection.")
            return
        print("Books in the collection:")
        for index, book in enumerate(self.books_list):
            print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']}")
        print()

    def show_reading_status(self):
        '''Display reading status of books'''
        total_books = len(self.books_list)
        completed_books = sum(1 for book in self.books_list if book['is_read'])
        completion_rate = (completed_books / total_books) * 100 if total_books > 0 else 0
        print(f"Total books: {total_books}")
        print(f"Reading progress: {completed_books} books read out of {total_books} ({completion_rate:.2f}%)")

    def start_application(self):
        '''Start the application and display the menu'''
        while True:
            print("\nPersonal Library Management System")
            print("1. Add Book")
            print("2. Delete Book")
            print("3. Find Book")
            print("4. Update Book")
            print("5. Show All Books")
            print("6. Show Reading Status")
            print("7. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.create_new_book()
            elif choice == '2':
                self.delete_book()
            elif choice == '3':
                self.find_book()
            elif choice == '4':
                self.update_book()
            elif choice == '5':
                self.show_all_books()
            elif choice == '6':
                self.show_reading_status()
            elif choice == '7':
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    library = Book_Collection()
    library.start_application()