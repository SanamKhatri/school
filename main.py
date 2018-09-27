import student_database
from Student import Student


def main():
    menu="""
            1.Student
            2.Teacher
            3.Staff"""
    print(menu)
    choice=int(input("Enter the choice:"))
    if choice==1:
        student_menu="""
                1.Add Student
                2.Search Student
                3.Update Student
                4.Delete Student"""
        print(student_menu)
        student_choice=int(input("Enter the choice:"))
        if student_choice==1:
            name=input("Enter the name of the student:")
            address=input("Enrer the address of the student:")
            contact_no=input("Enter the contact no of the student")
            
if __name__ == '__main__':
    main()
