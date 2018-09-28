import teacher_database


def search_teacher():
    search_menu="""
            1.By Name
            2.By Address
            3.By Contact No
            4.By Subject
            """
    print(search_menu)
    seach_choice=int(input("Enter the choice"))
    if seach_choice==1:
        teacher_name=input("Enter the name of the teacher to search")
        teacher_detail=teacher_database.teacher_search_by_name(teacher_name)
        if teacher_detail:
            print("The Teacher Details are")
            print("Name={}" + teacher_detail[1])
            print("Address={}" + teacher_detail[2])
            print("Contact No={}" + teacher_detail[3])
            print("Salary={}" + teacher_detail[4])
            print("Subject={}" + teacher_detail[5])
            print("Sex={}" + teacher_detail[6])
        else:
            print("The name is not in database")
    elif seach_choice==2:
        teacher_address=input("Enter the address of the teacher to search")
        teacher_detail=teacher_database.teacher_search_by_address(teacher_address)
        if teacher_detail:
            print("The Teacher Details are")
            print("Name={}" + teacher_detail[1])
            print("Address={}" + teacher_detail[2])
            print("Contact No={}" + teacher_detail[3])
            print("Salary={}" + teacher_detail[4])
            print("Subject={}" + teacher_detail[5])
            print("Sex={}" + teacher_detail[6])
        else:
            print("The name is not in database")
    elif seach_choice==3:
        teacher_contact_no=int(input("Enter the contact no of the teacher to search"))
        teacher_detail=teacher_database.teacher_search_by_contact_no(teacher_contact_no)
        if teacher_detail:
            print("The Teacher Details are")
            print("Name={}" + teacher_detail[1])
            print("Address={}" + teacher_detail[2])
            print("Contact No={}" + teacher_detail[3])
            print("Salary={}" + teacher_detail[4])
            print("Subject={}" + teacher_detail[5])
            print("Sex={}" + teacher_detail[6])
        else:
            print("The name is not in database")
    elif seach_choice==4:
        teacher_subject=input("Enter the subject of the teacher to search")
        teacher_detail=teacher_database.teacher_search_by_subject(teacher_subject)
        if teacher_detail:
            print("The Teacher Details are")
            print("Name={}" + teacher_detail[1])
            print("Address={}" + teacher_detail[2])
            print("Contact No={}" + teacher_detail[3])
            print("Salary={}" + teacher_detail[4])
            print("Subject={}" + teacher_detail[5])
            print("Sex={}" + teacher_detail[6])
        else:
            print("The name is not in database")
    else:
        print("Invalid Choice")