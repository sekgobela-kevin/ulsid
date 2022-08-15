'''
Analyses and breaks-down student numbers

Author: Sekgobela Kevin
Date: August 2022
Language: Python 3
'''
import typing
from . import exceptions


_YEAR_CAPACITY = 100000
_YEAR_FIRST_POSITION = 0

def calculate_position_length(
    year_first_position: typing.Union[int, None] = None, 
    year_capacity: typing.Union[int, None] = None):
    # Calculates length(chars) position part of student number.
    # year_first_position: first position for the year.
    # year_capacity: maximum student that can be accomodated in a year.
    if year_first_position ==  None:
        year_first_position = _YEAR_FIRST_POSITION
    if year_capacity == None:
        year_capacity = _YEAR_CAPACITY
    # Calculates length of digits that can handle capacity of students
    # starting at year_first_position.
    difference = (year_capacity - year_first_position) - 1
    return len(str(difference))
    
def position_part_to_position(position_part: str, *args, **kwargs):
    # Convert position part to position integer
    position_length = calculate_position_length(*args, **kwargs)
    if len(position_part) == position_length:
        return int(position_part)
    else:
        raise exceptions.PositionPartError(position_part)

def position_to_position_part(position: int, *args, **kwargs):
    # Convert position integer to its position part
    position_length = calculate_position_length(*args, **kwargs)
    return str(position).zfill(position_length)

def year_part_to_year(year_part: str, strict=True):
    # Convert position integer to its position part
    if strict and len(year_part) == 2:
        return int("19"+year_part)
    elif len(year_part) >= 4:
        return int(year_part)
    else:
        raise exceptions.YearPartError(year_part)

def year_to_year_part(year: int, strict=True):
    # Convert year integer to its year part
    year_str = str(year)
    if len(year_str) >= 4:
        if strict and year_str.startswith("19"):
            return year_str[2:]
        return year_str
    else:
        err_msg = "Year {year} should atleast contain 4 digits"
        raise ValueError(err_msg.format(year=year))
    
        
def extract_position_part(student_number: int, *args, **kwargs):
    # Extracts position part of student number
    student_number: str = str(student_number)
    position_length = calculate_position_length(*args, **kwargs)
    position_part = student_number[position_length*-1:]
    # Position part should have same digits length as position_length
    if len(position_part) == position_length:
        return position_part
    else:
        raise exceptions.PositionPartError(position_part, student_number)

def extract_year_part(student_number: int, *args, **kwargs):
    # Extracts year part of student number
    student_number: str = str(student_number)
    position_length = calculate_position_length(*args, **kwargs)
    year_part = student_number[:position_length*-1]
    # Year part should be atleast 2 or 4+ digits
    if len(year_part) == 2 or len(year_part) >= 4:
        return year_part
    else:
        # Year of student number should contain 2 or 4+ chars.
        # Years with 0, 1 or 3 are considered invalid.
        raise exceptions.YearPartError(year_part, student_number)

def extract_position(student_number: int, *args, **kwargs):
    # Extracts posetion part of student number
    position_part = extract_position_part(student_number, *args, **kwargs)
    try:
        return position_part_to_position(position_part, *args, **kwargs)
    except exceptions.PositionPartError:
        raise exceptions.PositionPartError(position_part, student_number)

def extract_year(student_number: int, *args, **kwargs):
    # Extracts year of student number
    year_part = extract_year_part(student_number, *args, **kwargs)
    try:
        return year_part_to_year(year_part, *args, **kwargs)
    except exceptions.YearPartError:
        # Re-raise exception with student number included
        raise exceptions.YearPartError(year_part, student_number)


def split_student_number(student_number: int, *args, **kwargs):
    # Splits student number into 2 parts representing year and 
    # application position
    position_part = extract_position_part(student_number, *args, **kwargs)
    year_part = extract_year_part(student_number, *args, **kwargs)
    return year_part, position_part

def student_number_valid(student_number: int, *args, **kwargs):
    # Checks if student number is valid
    try:
        # If student number can be split then its valid
        split_student_number(student_number, *args, **kwargs)
    except exceptions.StudentNumberError:
        return False
    else:
        return True


if __name__ == "__main__":
    print(student_number_valid(str(8529216)))

