def split_expense():
    total = float(input("Enter total expense amount: "))
    people = int(input("Enter number of people: "))
    share = total / people
    print("Each person should pay:", share)

def main():
    while True:
        print("1. Split Expense")
        print("2. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            split_expense()
        elif choice == "2":
            break
        else:
            print("Invalid option")

main()
