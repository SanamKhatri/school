import student_database
from Student import Student


def main():
    # if choice==1:
    #     first_name=input("Enter the first name:")
    #     middle_name=input("Enter the middle name:")
    #     last_name=input("Enter the last name:")
    #     address=input("Enter the address:")
    #     contact_no=input("Enter the contact no:")
    #     s=Student(first_name=first_name,middle_name=middle_name,last_name=last_name,address=address,contact_no=contact_no)
    #     is_added=student_database.add_student(s)
    #     if is_added:
    #         print("Data inserted")
    #     else:
    #         print("Data not inserted")
    # s = Student
    # student_database.show_student(s)
    search_roll_no = int(input("Enter the roll no to search "))
    student_detail = student_database.search_student_by_roll_no(search_roll_no)
    print("First Name= "+student_detail[1])
    print("Middle Name= "+student_detail[2])
    print("Last Name= "+student_detail[3])
    print("Address= "+student_detail[4])
    print("Contact No= "+student_detail[5])


if __name__ == '__main__':
    main()
