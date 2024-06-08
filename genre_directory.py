from genre import Genre

genres = []

def genre_operations():
    while True:
        print("\nGenre Operations")
        print("1. Add a new genre")
        print("2. View genre details")
        print("3. Display all genres")
        print("4. Back to the main menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_genre()
        elif choice == '2':
            view_details()
        elif choice == '3':
            display_all_genres()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again!")

def add_genre():
    name = input("Enter genre: ")
    description = input("Enter genre description: ")
    category = input("Enter genre category: ")
    new_genre = Genre(name, description, category)
    genres.append(new_genre)
    print(f"New genre {name}, added successfully!")

def view_details():
    name = input("Enter genre: ")
    for genre in genres:
        if genre.name.lower() == name.lower():
            print(genre.view_details())
            return
    print(f"Genre '{name}' not found.")

def display_all_genres():
    if not genres:
        print("No genres in the library")
    else:
        for genre in genres:
            print(genre)