def create_file(filename):
    with open(filename, 'w') as f:
        print("File created successfully.")

def write_file(filename):
    data = input("Enter data to write: ")
    with open(filename, 'w') as f:
        f.write(data + "\n")
    print("Data written successfully.")

def append_file(filename):
    data = input("Enter data to append: ")
    with open(filename, 'a') as f:
        f.write(data + "\n")
    print("Data appended successfully.")

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            print("\n--- File Content ---")
            print(f.read())
    except FileNotFoundError:
        print("File not found! Please create the file first.")

def main():
    filename = input("Enter filename: ")

    while True:
        print("\n1. Create File\n2. Write\n3. Append\n4. Read\n5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            create_file(filename)
        elif choice == '2':
            write_file(filename)
        elif choice == '3':
            append_file(filename)
        elif choice == '4':
            read_file(filename)
        elif choice == '5':
            print("Program ended.")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
