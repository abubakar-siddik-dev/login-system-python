from utils import load_data, save_data


def apply_loan(username):
    data = load_data()

    loan_type = input("Loan type (personal/home/etc): ")
    amount = input("Loan amount: ")
    duration = input("Duration (months): ")

    loan = {
        "type": loan_type,
        "amount": amount,
        "duration": duration
    }

    data["users"][username]["loans"].append(loan)
    save_data(data)

    print("✅ Loan applied successfully")


def view_loans(username):
    data = load_data()
    loans = data["users"][username]["loans"]

    if not loans:
        print("No loans found")
        return

    print("\n📋 Your Loans:")
    for i, loan in enumerate(loans, 1):
        print(f"{i}. {loan['type']} | {loan['amount']} | {loan['duration']} months")
