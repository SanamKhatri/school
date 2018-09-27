import student_database


def search_student():
    search_menu = """
                            1.By Roll No
                            2.By Name
                            3.By Address
                            4.By Contact No"""
    print(search_menu)
    search_choice = int(input("Enter by what you want to search:"))
    if search_choice == 1:
        search_roll_no = int(input("Enter the roll no to search:"))
        student_detail = student_database.search_student_by_roll_no(search_roll_no)
        if student_detail:
            print("The student details is")
            print("Roll No={}" + student_detail[0])
            print("Name={}" + student_detail[1])
            print("Address={}" + student_detail[2])
            print("Contact No={}" + student_detail[3])
        else:
            print("The entered roll no is not in database")
    elif search_choice == 2:
        search_name = input("Enter the name to search:")
        student_detail = student_database.search_student_by_name(search_name)
        if student_detail:
            print("The student details is")
            print("Roll No={}" + student_detail[0])
            print("Name={}" + student_detail[1])
            print("Address={}" + student_detail[2])
            print("Contact No={}" + student_detail[3])
        else:
            print("The entered roll no is not in database")
    elif search_choice == 3:
        search_address = input("Enter the address to search:")
        student_detail = student_database.search_student_by_address(search_address)
        if student_detail:
            print("The student details is")
            print("Roll No={}" + student_detail[0])
            print("Name={}" + student_detail[1])
            print("Address={}" + student_detail[2])
            print("Contact No={}" + student_detail[3])
        else:
            print("The entered roll no is not in database")
    elif search_choice == 4:
        search_contact_no = input("Enter the contact no to search:")
        student_detail = student_database.search_by_contact_no(search_contact_no)
        if student_detail:
            print("The student details is")
            print("Roll No={}" + student_detail[0])
            print("Name={}" + student_detail[1])
            print("Address={}" + student_detail[2])
            print("Contact No={}" + student_detail[3])
        else:
            print("The entered roll no is not in database")
    else:
        print("Invalid choice")