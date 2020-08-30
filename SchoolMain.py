
import schooldb
database = schooldb.Database()
username = input("Enter your name: ")
password= input(" Enter your password: ")
if username == "admin" and password == "1234":
    while True:
        operation = input(" Enter add record,get record, delete record, change gpa, change name, exit ")

        if operation.lower() == "add record":
            student_id= input("Enter the student_id ")
            name= input("Enter name ")
            gpa= float(input("Enter gpa"))
            record = schooldb.Record(name, student_id, gpa)
            database.addrecord(record)
        elif operation.lower() == "delete record":
            student_id = input("Enter the student_id ")
            database.remove_record(student_id)
        elif operation.lower() == "change name":
            student_id = input("Enter the student_id ")
            name = input("Enter name ")
            database.change_name(student_id, name)
        elif operation.lower() == "change gpa":
            student_id = input("Enter the student_id ")
            gpa = float(input("Enter gpa "))
            database.change_gpa(student_id, gpa)

        elif operation.lower() == "get record":
            student_id = input("Enter the student_id ")
            print(database.get_record(student_id))

        elif operation.lower() == "exit":
            break






