from book_directory import book_operations
from user_directory import user_operations
from author_directory import author_operations
from genre_directory import genre_operations

def main_menu():
    while True:
        print("Welcome to the Library Management System!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Genre Operations")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_operations()
        elif choice == '2':
            user_operations()
        elif choice == '3':
            author_operations()
        elif choice == '4':
            genre_operations()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


main_menu()