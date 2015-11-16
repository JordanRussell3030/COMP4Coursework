lesson_list = ["Trigonometry 1", "Trigonometry 2", "Trigonometry 3", "Pythagoras 1", "Pythagoras 2"]
homework_list = ["H1", "H2", "H3", "H4", "H5"]
l_topic_list = ["Easy Trigonometry 1", "ET2", "Medium Trig 1", "MT2", "MT3", "HT1", "etc"]
h_topic_list = ["Easy Trig 1", "ET2", "ET3", "MT1", "MT2", "MT3", "HT1", "HT2", "HT3", "etc"]
easy_trig_1_list = ["Easy 1.1", "Easy 1.2", "Easy 1.3"]
easy_trig_2_list = ["Easy 2.1", "Easy 2.2", "Easy 2.3"]
easy_trig_3_list = ["Easy 3.1", "Easy 3.2", "Easy 3.3"]
med_trig_1_list = ["Medium 1.1", "Medium 1.2", "Medium 1.3"]
med_trig_2_list = ["Medium 2.1", "Medium 2.2", "Medium 2.3"]
med_trig_3_list = ["Medium 3.1", "Medium 3.2", "Medium 3.3"]

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
                display_lesson_topic_menu(l_topic_list)
                valid = True
            elif option == 2:
                display_homework_topic_menu(h_topic_list)
                valid = True
            elif option == 3:
                display_database()
                valid = True
            else:
                print("Please select a valid option")
        except ValueError:
            print("Please input a valid data type")

def display_lesson_topic_menu(l_topic_list):
    print()
    print("Please select a topic")
    print()
    print("1. Easy Trigonometry 1")
    print("2. Easy Trigonometry 2")
    print("3. Easy Trigonometry 3")
    print()
    print("4. Medium Trigonometry 1")
    print("5. Medium Trigonometry 2")
    print("6. Medium Trigonometry 3")
    print()
    valid = False
    while not valid:
        try:
            option = int(input("Topic selected: "))
            if option == 1:
                option = display_easy_trig_1(easy_trig_1_list)
                valid = True
            elif option == 2:
                option = display_easy_trig_2(easy_trig_2_list)
                valid = True
            elif option == 3:
                option = display_easy_trig_3(easy_trig_3_list)
                valid = True
            elif option == 4:
                option = display_medium_trig_1(med_trig_1_list)
                valid = True
            elif option == 5:
                option = display_medium_trig_2(med_trig_2_list)
                valid = True
            elif option == 6:
                option = display_medium_trig_3(med_trig_3_list)
                valid = True
            else:
                print("Please select a valid option")
        except ValueError:
            print("Please input a valid data type")

def display_homework_topic_menu(h_topic_list):
    pass

def display_easy_trig_1(easy_trig_1_list):
    print()
    print("Please select a lesson")
    print()
    print("1. Easy Trigonometry 1.1")
    print("2. Easy Trigonometry 1.2")
    print("3. Easy Trigonometry 1.3")
    print()
    valid = False
    while not valid:
        try:
            option = int(input("Lesson selected: "))
            if option == 1:
                print("easy_trig_1.1()")
                valid = True
            elif option == 2:
                print("easy_trig_1.2()")
                valid = True
            elif option == 3:
                print("easy_trig_1.3()")
                valid = True
            else:
                print("Please select a valid option")
        except ValueError:
            print("Please input a valid data type")

def display_easy_trig_2(easy_trig_2_list):
    print()
    print("Please select a lesson")
    print()
    print("1. Easy Trigonometry 2.1")
    print("2. Easy Trigonometry 2.2")
    print("3. Easy Trigonometry 2.3")
    print()
    valid = False
    while not valid:
        try:
            option = int(input("Lesson selected: "))
            if option == 1:
                print("easy_trig_2.1()")
                valid = True
            elif option == 2:
                print("easy_trig_2.2()")
                valid = True
            elif option == 3:
                print("easy_trig_2.3()")
                valid = True
            else:
                print("Please select a valid option")
        except ValueError:
            print("Please input a valid data type")

def display_easy_trig_3(easy_trig_3_list):
    print()
    print("Please select a lesson")
    print()
    print("1. Easy Trigonometry 3.1")
    print("2. Easy Trigonometry 3.2")
    print("3. Easy Trigonometry 3.3")
    print()
    valid = False
    while not valid:
        try:
            option = int(input("Lesson selected: "))
            if option == 1:
                print("easy_trig_3.1()")
                valid = True
            elif option == 2:
                print("easy_trig_3.2()")
                valid = True
            elif option == 3:
                print("easy_trig_3.3()")
                valid = True
            else:
                print("Please select a valid option")
        except ValueError:
            print("Please input a valid data type")

def display_medium_trig_1(med_trig_1_list):
    print()
    print("Please select a lesson")
    print()
    print("1. Medium Trigonometry 1.1")
    print("2. Medium Trigonometry 1.2")
    print("3. Medium Trigonometry 1.3")
    print()
    valid = False
    while not valid:
        try:
            option = int(input("Lesson selected: "))
            if option == 1:
                print("medium_trig_1.1()")
                valid = True
            elif option == 2:
                print("medium_trig_1.2()")
                valid = True
            elif option == 3:
                print("medium_trig_1.3()")
                valid = True
            else:
                print("Please select a valid option")
        except ValueError:
            print("Please input a valid data type")

def display_medium_trig_1(med_trig_1_list):
    print()
    print("Please select a lesson")
    print()
    print("1. Medium Trigonometry 1.1")
    print("2. Medium Trigonometry 1.2")
    print("3. Medium Trigonometry 1.3")
    print()
    valid = False
    while not valid:
        try:
            option = int(input("Lesson selected: "))
            if option == 1:
                print("medium_trig_2.1()")
                valid = True
            elif option == 2:
                print("med_trig_2.2()")
                valid = True
            elif option == 3:
                print("med_trig_2.3()")
                valid = True
            else:
                print("Please select a valid option")
        except ValueError:
            print("Please input a valid data type")

def display_medium_trig_1(med_trig_1_list):
    print()
    print("Please select a lesson")
    print()
    print("1. Medium Trigonometry 1.1")
    print("2. Medium Trigonometry 1.2")
    print("3. Medium Trigonometry 1.3")
    print()
    valid = False
    while not valid:
        try:
            option = int(input("Lesson selected: "))
            if option == 1:
                print("medium_trig_3.1()")
                valid = True
            elif option == 2:
                print("med_trig_3.2()")
                valid = True
            elif option == 3:
                print("med_trig_3.3()")
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
        
    
