from author import Author

authors = []

def author_operations():
    while True:
        print("\nAuthor Operations")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Back to the main menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_author()
        elif choice == '2':
            view_author()
        elif choice == '3':
            display_all_authors()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again")


def add_author():
    name = input("Enter authors name: ")
    biography = input("Enter authors biography: ")
    new_author = Author(name, biography)
    authors.append(new_author)
    print(f"New author, {name}, added successfully!")

def view_author():
    name = input("Enter author's name: ")
    for author in authors:
        if author.name.lower() == name.lower():
            print(author.view_details())
            return
    print(f"Author with the name {name} not found.")

def display_all_authors():
    if not authors:
        print("No authors in the library.")
    else:
        for author in authors:
            print(author)

