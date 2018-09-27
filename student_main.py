import student_database
from Student import Student
from student_search import search_student
from student_show import show_student
from student_update import update_student
from student_add import add_student
from student_delete import delete_student


def student_menu():
    student_menu = """
                    1.Add Student
                    2.Search Student
                    3.Update Student
                    4.Delete Student
                    5.Show Student"""
    print(student_menu)
    student_choice = int(input("Enter the choice:"))
    if student_choice == 1:
        add_student()
    elif student_choice == 2:
        search_student()
    elif student_choice == 3:
        update_student()
    elif student_choice == 4:
        delete_student()
    elif student_choice==5:
        show_student()
    else:
        print("Invalid choice")
