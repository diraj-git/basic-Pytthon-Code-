"""
This class makes record object.
"""
class Record:
    """
    This creates records object. and tell what parameter you pass in.
    parameter we pass in are : prameters( name , id gpa)
    based on gpa we assigned the self.in_on_probation.
    """
    def __init__(self, name ,student_id,gpa):
        self.name = name
        self.student_id = student_id
        self.gpa = gpa
        if gpa <2.5:
            self.is_on_probation = True
        else:
            self.is_on_probation = False

    """
    It does basically redable string for records.    
    """
    def __str__(self):
        return str(self.name)+"    "+str(self.student_id)+"    "+str(self.gpa)
"""

This class stores all of the records. 
"""
class Database:
    def __init__(self, records={}):
        self.records = records

    def addrecord(self, record):
        try:
            self.records[record.student_id]=record
        except Exception as e:
            print("Something went wrong")

    def change_gpa(self,student_id, gpa):
        try:
            self.records[student_id].gpa = gpa
            if gpa <2.5:
                self.is_on_probation = True
            else:
                self.is_on_probation = False
        except Exception as e:
            print("Something went wrong")

    def remove_record(self,student_id):
        try:
            del self.records[student_id]
        except Exception as e:
            print("Something went wrong")

    def change_name(self,student_id, name):
        try:
            self.records[student_id].name = name
        except Exception as e:
            print("Something went wrong")

    def get_record(self,student_id):
        try:
            return str(self.records[student_id])
        except Exception as e:
            print("Something went wrong")







