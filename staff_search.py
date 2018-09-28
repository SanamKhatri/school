import staff_database


def search_staffer():
    search_menu = """
            1.By Name
            2.By Address
            3.By Contact No
            4.By Postt
            """
    print(search_menu)
    search_choice = int(input("Enter the choice"))
    if search_choice == 1:
        staff_name = input("Enter the name of the staff to search")
        staff_detail = staff_database.staff_search_by_name(staff_name)
        if staff_detail:
            print("The Staff Details are")
            print("Name={}" + staff_detail[1])
            print("Address={}" + staff_detail[2])
            print("Contact No={}" + staff_detail[3])
            print("Salary={}" + staff_detail[4])
            print("Subject={}" + staff_detail[5])
            print("Sex={}" + staff_detail[6])
        else:
            print("The name is not in database")
    elif search_choice == 2:
        staff_address = input("Enter the address of the staff to search")
        staff_detail = staff_database.staff_search_by_address(staff_address)
        if staff_detail:
            print("The Staff Details are")
            print("Name={}" + staff_detail[1])
            print("Address={}" + staff_detail[2])
            print("Contact No={}" + staff_detail[3])
            print("Salary={}" + staff_detail[4])
            print("Subject={}" + staff_detail[5])
            print("Sex={}" + staff_detail[6])
        else:
            print("The name is not in database")
    elif search_choice == 3:
        staff_contact_no = int(input("Enter the contact no of the staff to search"))
        staff_detail = staff_database.staff_search_by_contact_no(staff_contact_no)
        if staff_detail:
            print("The Staff Details are")
            print("Name={}" + staff_detail[1])
            print("Address={}" + staff_detail[2])
            print("Contact No={}" + staff_detail[3])
            print("Salary={}" + staff_detail[4])
            print("Subject={}" + staff_detail[5])
            print("Sex={}" + staff_detail[6])
        else:
            print("The name is not in database")
    elif search_choice == 4:
        staff_subject = input("Enter the post of the staff to search")
        staff_detail = staff_database.staff_search_by_subject(staff_subject)
        if staff_detail:
            print("The Staff Details are")
            print("Name={}" + staff_detail[1])
            print("Address={}" + staff_detail[2])
            print("Contact No={}" + staff_detail[3])
            print("Salary={}" + staff_detail[4])
            print("Subject={}" + staff_detail[5])
            print("Sex={}" + staff_detail[6])
        else:
            print("The name is not in database")
    else:
        print("Invalid Choice")
