# Task 1, 2, and 3


shopping_list = []

def add_item(shopping_list):
    item = input("What would you like to add to the list? ")
    shopping_list.append(item)
    print(shopping_list)
def remove_item(shopping_list):
    item = input("What would you like to remove? ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(shopping_list)
    else:
        print(f"{item} is not in your inventory.")
        print(shopping_list)

def main(shopping_list):
    print("""
    Please choose from the list below:
            1. add an item
            2. remove an item
            3. see list
        """)
    while True:
        response = input("What number would you like? ")
        if response == "1":
            add_item(shopping_list)
        elif response == "2":
            remove_item(shopping_list)
        elif response == "3":
            print("Perfect, here it is. ")
            print(shopping_list)

main(shopping_list)
