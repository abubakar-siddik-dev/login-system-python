from auth import register, login
from loan import apply_loan, view_loans


def user_menu(username):
    while True:
        print("\n=== USER MENU ===")
        print("1. Apply Loan")
        print("2. View Loans")
        print("3. Logout")

        choice = input("Choose: ")

        if choice == "1":
            apply_loan(username)
        elif choice == "2":
            view_loans(username)
        elif choice == "3":
            break
        else:
            print("Invalid choice")


def main():
    while True:
        print("\n=== SYSTEM ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                user_menu(user)
        elif choice == "3":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
