lesson_list = ["Trigonometry 1", "Trigonometry 2", "Trigonometry 3", "Pythagoras 1", "Pythagoras 2"]
homework_list = ["H1", "H2", "H3", "H4", "H5"]

def menu():
    print()
    print("Welcome to the GCSE Trigonometry and Pythagoras teaching program")
    print()
    print("What would you like to do next? ")
    print()
    print("1. Lessons")
    print("2. Homework")
    print("3. Progress")
    print()
    print("Please select an option")
    print()
    option = select_option()

def select_option():
    print()
    valid = False
    while not valid:
        try:
            option = int(input("Option selected: "))
            if option == 1:
                display_lesson_menu(lesson_list)
                valid = True
            elif option == 2:
                display_homework_menu(homework_list)
                valid = True
            elif option == 3:
                display_database()
                valid = True
            else:
                print("Please select a valid option")
        except ValueError:
            print("Please input a valid data type")

def display_lesson_menu(lesson_list):
    print()
    print("Please select a lesson to view")
    print()
    for index, lesson in enumerate(lesson_list):
        print("{0}. {1}".format(index + 1, lesson))
    option = select_lesson(lesson_list)
    

def display_homework_menu(homework_list):
    print()
    print("Please select a homework to complete")
    print()
    for index, homework in enumerate(homework_list):
        print("{0}. {1}".format(index + 1, homework))
    option = select_homework(homework_list)

def display_database():
    pass

def select_lesson(lesson_list):
    print()
    valid = False
    while not valid:
        try:
            option = int(input("Lesson selected: "))
            if option in range(1, len(lesson_list) + 1):
                valid = True
                print("Success") #run lesson
            else:
                print("Please select a valid option")
        except ValueError:
            print("Please input a valid data type")

def select_homework(homework_list):
    print()
    valid = False
    while not valid:
        try:
            option = int(input("Homework selected: "))
            if option in range(1, len(homework_list ) + 1):
                valid = True
                print("Success") #run homework
            else:
                print("Please select a valid option")
        except ValueError:
            print("Please input a valid data type")        

def main():
    menu()

if __name__ == "__main__":
    main()
        
    
