'''
Exception classes for ulid

Author: Sekgobela Kevin
Date: August 2022
Language: Python 3
'''
import typing

class UlidError(Exception):
    '''Base class for ulid exceptions'''
    pass

class StudentNumberError(UlidError):
    '''Base class for exceptions regarding student numbers'''
    def __init__(self, student_number: int) -> None:
        self.student_number = student_number
        error_msg = self.create_error_message()
        super().__init__(error_msg)

    def create_error_message(self):
        err_msg = "There is problem with student number {student_id}"
        return err_msg.format(student_id=self.student_number)

class InvalidStudentNumber(StudentNumberError):
    '''Student number is invalid'''
    def create_error_message(self):
        err_msg = "Student number {student_id} is invalid"
        return err_msg.format(student_id=self.student_number)

class UnsupportedStudentNumber(StudentNumberError):
    '''Student number is valid but not supported'''
    def create_error_message(self):
        err_msg = "Student number {student_id} is not supported"
        return err_msg.format(student_id=self.student_number)


class StudentNumberPartError(StudentNumberError):
    '''Exceptions regarding parts of student number'''
    part_name = "Part"
    
    def __init__(self, part: str, student_number:int=None) -> None:
        self.part = part
        super().__init__(student_number)

    def create_error_message(self):
        if self.student_number == None:
            student_number = ""
        else:
            student_number = self.student_number
        err_msg = "{part_name} {part} of student number " +\
            "{student_id} is invalid"
        return err_msg.format(
            part=self.part, 
            student_id=student_number, 
            part_name=self.part_name
        )


class YearPartError(StudentNumberPartError):
    '''Exception regarding year part of student number'''
    part_name = "Year part"

class PositionPartError(StudentNumberPartError):
    '''Exception regarding position part of student number'''
    part_name = "Posetion part"
