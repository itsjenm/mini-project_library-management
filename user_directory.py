from user import User

users = []

def user_operations():
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back to the main menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_user()
        elif choice == '2':
            view_details()
        elif choice == '3':
            display_all()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again")


def add_user():
    name = input("Enter user's name: ")
    library_id = input("Enter library id: ")
    new_user = User(name, library_id)
    users.append(new_user)
    print(f"User {name} added successfully!")


def view_details():
    library_id = input("Enter library ID of the user to view details: ")
    for user in users:
        if user.library_id() == library_id:
            print(user.view_details())
            return
    print(f"User with library ID {library_id} not found.")

def display_all():
    if not users:
        print("No users in the library.")
    else:
        for user in users:
            print(user)