# shopping list
shopping_list = ["Milk", "Bread", "Eggs"]
user_list = 1
while True:

    user_list = int(input(
        "\nOptions:\n1. View list\n2. Add items\n3. Remove items\n4. Search for an item\n5. Exit\n"))
    if user_list == 1:
        print(shopping_list)
    elif user_list == 2:
        adding = input("What else do u need to add? (separate with commas) ")
        items = adding.split(",")
        for item in items:
            shopping_list.append(item.strip())
        print(shopping_list)
    elif user_list == 3:
        print(f"Here is the current shopping list :{shopping_list}")
        rem = input("What do you wanna remove? ")
        new_items = rem.split(",")
        for new_item in new_items:
            new_item = new_item.strip()
            if new_item in new_items:
                shopping_list.remove(new_item)
            else:
                print(f"{new_item} is not in shopping list.")
        print(shopping_list)
    elif user_list == 4:
        search = input("What item do you need? ").strip()
        if search in shopping_list:
            print("\n Found")
        else:
            print("\n Not found")
    else:
        print("Goodbye!")
        break
