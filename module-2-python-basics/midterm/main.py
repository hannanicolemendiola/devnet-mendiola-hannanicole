"""
Midterm Practical Exam — Pet Adoption Records Manager
Student: Mendiola, Hanna Nicole L.
"""

pets = []

print("=== Pet Adoption Records Manager ===")

def display_menu():
    print("What do you want to do?\nEnter number to proceed:")
    choice = input(" [1] Add a pet\n [2] View all pets\n [3] Count available vs. adopted\n [4] Find a pet\n [5] Remove pet\n [6] Exit\n")
    print(choice)

def add_pet(pet_list):
    # ask for name, animal type, status — build the string, add to the list
    print("=== ADD PET ===")
    pet_name = input("Enter the following details:\n Name: ")
    pet_type = input(" Animal Type: ")
    pet_status = input(" Status: ")

def view_pets(pet_list):
    # loop through and print every pet — handle empty list
    pass

def count_available_adopted(pet_list):
    # loop through, count Available vs Adopted, return both
    pass

def find_pet(pet_list):
    # ask for a name, search the list, print result or "not found"
    pass

def remove_pet(pet_list):
    # your code here
    pass

def main():
    running = True
    while running:
        display_menu()
        if choice == 1:
            add_pet()
        elif choice == 2:
            view_pets()
        elif choice == 3:
            count_available_adopted()
        elif choice == 4:
            find_pet()
        elif choice == 5:
            remove_pet()
        elif choice == 6:
            running = False
        # use if/elif to call the right function based on choice
        # set running = False when the user picks Exit
main()
