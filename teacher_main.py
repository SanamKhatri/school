from teacher_add import add_teacher
from teacher_delete import delete_teacher
from teacher_search import search_teacher
from teacher_show import show_teacher
from teacher_update import update_teacher


def teacher_menu():
    teacher_menu = """
            1.Add Teacher
            2.Update Teacher
            3.Search teacher
            4.Delete teacher
            5.Show Teachers"""
    print(teacher_menu)
    teacher_choice = int(input("Enter the choice:"))
    if teacher_choice == 1:
        add_teacher()
    elif teacher_choice == 2:
        update_teacher()
    elif teacher_choice == 3:
        search_teacher()
    elif teacher_choice == 4:
        delete_teacher()
    elif teacher_choice == 5:
        show_teacher()
    else:
        print("Invalid choice")
