'''
Generates student numbers

Author: Sekgobela Kevin
Date: August 2022
Language: Python 3
'''
from . import exceptions
from . import analyse

import random
import time


# Year UL started to operate
DEFAULT_START_YEAR = 1959
# Current year
DEFAULT_END_YEAR = time.gmtime(time.time()).tm_year + 1



def guess_position(start_pos:int=None, end_pos:int=None, **kwargs):
    # Guesses position to be used with student number

    # Gets year capacity from arguments else gets default one
    year_capacity = kwargs.get("year_capacity", 
        analyse.DEFAULT_YEAR_CAPACITY)
    # Gets first position from arguments else gets default one
    first_position = kwargs.get("year_first_position", 
        analyse.DEFAULT_YEAR_FIRST_POS)

    # Updates start_pos if not provided on argumnets
    if start_pos == None:
        start_pos = first_position
    
    # Calculates max position based on start pos and capacity
    max_end_pos = analyse.caculate_last_postion(start_pos, year_capacity)
    
    # Updates end_pos if not provided on argumnets
    if end_pos == None:
        end_pos = max_end_pos

    # Raises exceptions if values dont match
    # Its important to raise exceptions to help find bugs.
    if start_pos > end_pos:
        err_msg = "Start position {} cant be less than end position {}"
        error_msg = err_msg.format(start_pos, end_pos)

    if start_pos < first_position:
        err_msg = "Start position {} cant be less than first position {}"
        error_msg = err_msg.format(start_pos, first_position)
        raise ValueError(error_msg)

    if end_pos > max_end_pos:
        err_msg = "End position {} cant be greater than max position {}"
        err_msg = err_msg.format(end_pos, max_end_pos)
        raise ValueError(err_msg)
    
    # Uses start pos and end pos to guess position
    return random.randint(start_pos, end_pos)

def guess_position_part(start_pos:int=None, end_pos:int=None, **kwargs):
    # Guesses position part to be used with student number
    position = guess_position(start_pos, end_pos, **kwargs)
    return analyse.position_to_position_part(position, **kwargs)


def guess_year(start_year:int=None, end_year:int=None, strict=True):
    # Guesses year to be used with student number
    if start_year == None:
        start_year = DEFAULT_START_YEAR
    if end_year == None:
        end_year = DEFAULT_END_YEAR

    if start_year > end_year:
        err_msg = "Start year {} cant be greater than end year {}"
        raise ValueError(err_msg.format(start_year, end_year))
    
    if strict:
        if start_year < DEFAULT_START_YEAR:
            err_msg = "Start year {} cant be less than default " +\
                "end year {} when strict is enabled."
        if end_year > DEFAULT_END_YEAR:
            err_msg = "End year {} cant be greater than default " +\
                "end year {} when strict is enabled."
            raise ValueError(err_msg.format(end_year, DEFAULT_END_YEAR))

    return random.randint(start_year, end_year)

def guess_year_part(start_year:int=None, end_year:int=None, strict=True):
    # Guesses year part to be used with student number
    year = guess_year(start_year, end_year, strict)
    return analyse.year_to_year_part(year, strict)


def guess_student_number(
    start_year:int=None, 
    end_year:int=None, 
    start_pos:int=None, 
    end_pos:int=None, 
    strict=True,
    **kwargs):
    # Guesses student number limited by provided arguments
    year_part = guess_year_part(start_year, end_year, strict)
    position_part = guess_position_part(start_pos, end_pos, **kwargs)
    return year_part + position_part
    

if __name__ == "__main__":
    student_number = 202264623
    print(guess_student_number(strict=False, end_year=3013))
