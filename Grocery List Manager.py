grocery_list = []

file = open("grocery_list.txt", "r")
grocery_list = [line.strip() for line in file]
file.close()

running = True

while running:
    print("==== Grocery List Manager ==== ")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

    choice = input("= Enter your choice =>")

    if choice == "1":
        item = input("-- Enter the item to add --").lower()
        grocery_list.append(item)
        print(f"{item} added to the grocery list.")

    elif choice == "2":
        print("== Grocery List == ")
        for idx, item in enumerate(grocery_list, start=1):
            print(f"{idx}. {item}")
        remove_number = input("- Enter the number of the item to remove ->")
        remove_number = int(remove_number)-1
        if 0 <= remove_number < len(grocery_list):
            removed_item = grocery_list.pop(remove_number)
            print(f"{removed_item} has been removed from the grocery list.")
        else:
            print("Invalid item number.")

    elif choice == "3":
        if grocery_list:
            print("==== Grocery List ==== ")
            for idx, item in enumerate(grocery_list, start=1):
                print(f"{idx}. {item}")
        else:
            print("-= Your grocery list is empty. =- ")

    elif choice == "4":
        running = False
        print("==== Exiting Grocery List Manager. Goodbye! ====")

    else:
        print("Invalid choice, please select a valid option.")

file = open("grocery_list.txt", "w")
for item in grocery_list:
    file.write(f"{item} \n")
file.close()
