import sys

from Teacher import Teacher
from student_database import connection


def add_teacher(teacher_object):
    is_added = False
    db = connection()
    sql = "insert into teacher(name,address,contact_no,salary,subject,sex) values ('{}','{}','{}','{}','{}','{}')".format(
        teacher_object.getName(), teacher_object.getAddress(), teacher_object.getContactNo(),
        teacher_object.getSalary(), teacher_object.getSubject(), teacher_object.getSex)
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


def teacher_search_by_name(name):
    db = connection()
    sql = "select * from teacher where name='{}'".format(name)
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        t = Teacher(name=result[1], address=result[2],
                    contact_no=result[3], salary=result[4], subject=result[5], sex=result[6])
        t.setSN(result[0])
    return result
    return t


def teacher_search_by_contact_no(contact_no):
    db = connection()
    sql = "select * from teacher where contact_no='{}'".format(contact_no)
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        t = Teacher(name=result[1], address=result[2],
                    contact_no=result[3], salary=result[4], subject=result[5], sex=result[6])
        t.setSN(result[0])
    return result
    return t


def teacher_search_by_address(address):
    db = connection()
    sql = "select * from teacher where address='{}'".format(address)
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        t = Teacher(name=result[1], address=result[2],
                    contact_no=result[3], salary=result[4], subject=result[5], sex=result[6])
        t.setSN(result[0])
    return result
    return t


def teacher_search_by_subject(subject):
    db = connection()
    sql = "select * from teacher where subject='{}'".format(subject)
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        t = Teacher(name=result[1], address=result[2],
                    contact_no=result[3], salary=result[4], subject=result[5], sex=result[6])
        t.setSN(result[0])
    return result
    return t


def delete_by_name(teacher_object):
    is_deleted = False
    db = connection()
    sql = "delete from teacher where name='{}'".format(teacher_object.getName())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_deleted = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_deleted


def delete_by_address(teacher_object):
    is_deleted = False
    db = connection()
    sql = "delete from teacher where address='{}'".format(teacher_object.getAddress())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_deleted = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_deleted


def delete_by_subject(teacher_object):
    is_deleted = False
    db = connection()
    sql = "delete from teacher where subject='{}'".format(teacher_object.getSubject())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_deleted = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_deleted


def show_teacher(teacher_object):
    is_shown = False
    db = connection()
    sql = "select * from teacher"
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_shown = True
    except:
        print(sys.exc_info())
    finally:
        db.close()


def update_name(teacher_object):
    is_updated = False
    db = connection()
    sql = "update teacher set name='{}' where s.n='{}'".format(teacher_object.getName(), teacher_object.getSN())
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


def update_address(teacher_object):
    is_updated = False
    db = connection()
    sql = "update teacher set address='{}' where s.n='{}'".format(teacher_object.getAddress(), teacher_object.getSN())
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


def update_subject(teacher_object):
    is_updated = False
    db = connection()
    sql = "update teacher set subject='{}' where s.n='{}'".format(teacher_object.getSubject(), teacher_object.getSN())
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


def update_contact_no(teacher_object):
    is_updated = False
    db = connection()
    sql = "update teacher set contact_no='{}' where s.n='{}'".format(teacher_object.getContactNo(),
                                                                     teacher_object.getSN())
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


def update_salary(teacher_object):
    is_updated = False
    db = connection()
    sql = "update teacher set salary='{}' where s.n='{}'".format(teacher_object.getName(), teacher_object.getSN())
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
def getTeacherDetails(sn):
    db = connection()
    sql = "select * from teacher where s.n='{}'".format(sn)
    cursor = db.cursor()
    cursor.execute(sql)
    original_teacher = cursor.fetchone()
    if (original_teacher):
        t = Teacher(name=original_teacher[1], address=original_teacher[2], contact_no=original_teacher[3],salary=original_teacher[4],subject=original_teacher[5],sex=original_teacher[6])
        t.setSn(original_teacher[0])
    return original_teacher
    return t
