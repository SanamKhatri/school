import student_database
from Student import Student


def add_student():
    name = input("Enter the name of the student:")
    address = input("Enter the address of the student:")
    contact_no = input("Enter the contact no of the student:")
    s = Student(name=name, address=address, contact_no=contact_no)
    is_inserted = student_database.add_student(s)
    if is_inserted:
        print("Data have been inserted")
    else:
        print("Data have not been inserted")