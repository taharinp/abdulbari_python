# Journal Manager using File Handling

filename = "journal.txt"

while True:
    print("\n--- Journal Manager ---")
    print("1. Add Entry")
    print("2. View Entries")
    print("3. Delete All Entries")
    print("4. Exit")

    choice = input("Enter choice: ")

    # Add Entry
    if choice == "1":
        entry = input("Write your journal entry: ")

        file = open(filename, "a")   # append mode
        file.write(entry + "\n")
        file.close()

        print("Entry Saved!")

    # View Entries
    elif choice == "2":
        try:
            file = open(filename, "r")
            print("\nYour Journal:\n")
            print(file.read())
            file.close()
        except:
            print("No entries found!")

    # Delete Entries
    elif choice == "3":
        file = open(filename, "w")   # write mode clears file
        file.close()
        print("All entries deleted!")

    # Exit
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")