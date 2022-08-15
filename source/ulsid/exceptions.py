'''
Exception classes for ulid

Author: Sekgobela Kevin
Date: August 2022
Language: Python 3
'''

class UlidError(Exception):
    '''Base class for ulid exceptions'''
    pass

class StudentNumberError(UlidError):
    '''Base class for exceptions regarding student numbers'''
    def __init__(self, student_number: int) -> None:
        error_msg = self.create_error_message(student_number)
        super().__init__(error_msg)

    def create_error_message(self, student_number: int):
        err_msg = "There is problem with student number {student_id}"
        return err_msg.format(student_id=student_number)

class InvalidStudentNumber(StudentNumberError):
    '''Student number is invalid'''
    def create_error_message(self, student_number: int):
        err_msg = "Student number {student_id} is invalid"
        return err_msg.format(student_id=student_number)

class UnsupportedStudentNumber(StudentNumberError):
    '''Student number is valid but not supported'''
    def create_error_message(self, student_number: int):
        err_msg = "Student number {student_id} is not supported"
        return err_msg.format(student_id=student_number)


class YearPartError(StudentNumberError):
    '''Exception regarding year part of student number'''
    def create_error_message(self, student_number: int):
        err_msg = "Year part of student number {student_id} is invalid"
        return err_msg.format(student_id=student_number)

class PositionPartError(StudentNumberError):
    '''Exception regarding position part of student number'''
    def create_error_message(self, student_number: int):
        err_msg = "Position part of student number {student_id} is invalid"
        return err_msg.format(student_id=student_number)