'''
Generates student numbers

Author: Sekgobela Kevin
Date: August 2022
Language: Python 3
'''
from . import analyse
import random
import time


# Year UL started to operate
START_YEAR = 1959

# Current year
CURRENT_YEAR = time.gmtime(time.time()).tm_year


def guess_position(start_pos:int=None, end_pos:int=None):
    # Guesses position to be used with student number
    if start_pos == None:
        start_pos = analyse._YEAR_FIRST_POSITION
    if end_pos == None:
        end_pos = analyse._YEAR_CAPACITY
    return random.randrange(start_pos, end_pos)

def guess_position_part(start_pos:int=None, end_pos:int=None, **kwargs):
    # Guesses position part to be used with student number
    position = guess_position(start_pos, end_pos)
    return analyse.position_to_position_part(position, **kwargs)


def guess_year(start_year:int=None, end_year:int=None):
    # Guesses year to be used with student number
    if start_year == None:
        start_year = START_YEAR
    if end_year == None:
        end_year = CURRENT_YEAR + 1
    return random.randrange(start_year, end_year)

def guess_year_part(start_year:int=None, end_year:int=None, strict=True):
    # Guesses year part to be used with student number
    year = guess_year(start_year, end_year)
    return analyse.year_to_year_part(year, strict)


def guess_student_number(
    start_year:int=None, 
    end_year:int=None, 
    strict=True, 
    start_pos:int=None, 
    end_pos:int=None, 
    **kwargs):
    year_part = guess_year_part(start_year, end_year, strict)
    position_part = guess_position_part(start_pos, end_pos, **kwargs)
    return year_part + position_part
    


if __name__ == "__main__":
    student_number = 202264623
    print(guess_student_number(strict=False, end_pos=1000,year_capacity=40))
