import sys

import pymysql
from Student import Student


def connection():
    dbconnection = pymysql.connect("localhost", "root", "", "school")
    return dbconnection


def add_student(student_object):
    is_added = False
    db = connection()
    sql = "insert into student(name,address,contact_no) values ('{}','{}','{}')".format(
        student_object.getName(), student_object.getAddress(), student_object.getContactNo())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_added = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_added


def show_student(student_object):
    is_shown = False
    db = connection()
    sql = "select * from student"
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for r in result:
        print("Roll No={}".format(r[0]))
        print("Name={}".format(r[1]))
        print("Address={}".format(r[2]))
        print("Contact No={}".format(r[3]))
    try:
        cursor.execute(sql)
        db.commit()
        is_shown = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_shown


def search_student_by_roll_no(roll_no):
    db = connection()
    sql = "select * from student where roll_no='{}'".format(roll_no)
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        s = Student(name=result[1], address=result[2],
                    contact_no=result[3])
        s.setRollNo(result[0])
    return result
    return s


def search_student_by_name(name):
    db = connection()
    sql = "select * from student where name='{}'".format(name)
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        s = Student(name=result[1], address=result[2],
                    contact_no=result[3])
        s.setRollNo(result[0])
    return result
    return s


def search_student_by_address(address):
    db = connection()
    sql = "select * from student where address='{}'".format(address)
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        s = Student(name=result[1], address=result[2],
                    contact_no=result[3])
        s.setRollNo(result[0])
    return result
    return s


def search_by_contact_no(contact_no):
    db = connection()
    sql = "select * from student where contact_no='{}'".format(contact_no)
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        s = Student(name=result[1], address=result[2],
                    contact_no=result[3])
        s.setRollNo(result[0])
    return result
    return s


def delete_by_name(student_object):
    is_delete = False
    db = connection()
    sql = "delete from student where name='{}'".format(student_object.getName())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_delete = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_delete


def delete_by_address(student_object):
    is_delete = False
    db = connection()
    sql = "delete from student where address='{}'".format(student_object.getAddress())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_delete = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_delete


def delete_by_contact_no(student_object):
    is_delete = False
    db = connection()
    sql = "delete from student where contact_no='{}'".format(student_object.getContactNo())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_delete = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_delete


def getStudentDetails(roll_no):
    db = connection()
    sql = "select * from student where roll_no='{}'".format(roll_no)
    cursor = db.cursor()
    cursor.execute(sql)
    original_student = cursor.fetchone()
    if (original_student):
        s = Student(name=original_student[1], address=original_student[2], contact_no=original_student[3])
        s.setRollNo(original_student[0])
    return original_student
    return s


def update_by_name(student_object):
    is_updated = False
    db = connection()
    sql = "update student set name='{}' where roll_no='{}'".format(student_object.getName(), student_object.getRollNo())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_updated = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_updated


def update_by_address(student_object):
    is_updated = False
    db = connection()
    sql = "update student set address='{}' where roll_no='{}'".format(student_object.getAddress(),
                                                                      student_object.getRollNo())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_updated = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_updated


def update_by_contact_no(student_object):
    is_updated = False
    db = connection()
    sql = "update student set contact_no='{}' where roll_no='{}'".format(student_object.getContactNo(),
                                                                         student_object.getRollNo())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_updated = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_updated


def update_by_name_and_address(student_object):
    is_updated = False
    db = connection()
    sql = "update student set name='{}', address='{}', contact_no='{}' where roll_no='{}'".format(
        student_object.getName(),
        student_object.getAddress(),
        student_object.getContactNo(),
        student_object.getRollNo())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_updated = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_updated


def update_by_name_and_contact_no(student_object):
    is_updated = False
    db = connection()
    sql = "update student set name='{}',contact_no='{}' where roll_no='{}'".format(student_object.getName(),
                                                                                   student_object.getContactNo(),
                                                                                   student_object.getRollNo())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_updated = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_updated


def update_by_address_and_contact_no(student_object):
    is_updated = False
    db = connection()
    sql = "update student set address='{}',contact_no='{}' where roll_no='{}'".format(student_object.getAddress(),
                                                                                      student_object.getContactNo(),
                                                                                      student_object.getRollNo())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_updated = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_updated


def update_by_name_address_and_contact_no(student_object):
    is_updated = False
    db = connection()
    sql = "update student set name='{}',address='{}',contact_no='{}' where roll_no='{}'".format(
        student_object.getName(), student_object.getAddress(), student_object.getContactNo(),
        student_object.getRollNo())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_updated = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_updated


def show_student(student_object):
    is_shown = False
    db = connection()
    sql = "select * from student"
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for r in result:
        print("Roll No={}".format(r[0]))
        print("Name={}".format(r[1]))
        print("Address={}".format(r[2]))
        print("Contact No={}".format(r[3]))
    try:
        cursor.execute(sql)
        db.commit()
        is_shown = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_shown
