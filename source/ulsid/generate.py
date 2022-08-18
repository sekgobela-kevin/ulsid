'''
Generates student numbers

Author: Sekgobela Kevin
Date: August 2022
Language: Python 3
'''
from . import exceptions
from . import analyse

import typing
import random
import time


#########################################################
# Functions here are meant for assisting main functions.
# They help in getting values from keywords arguments.
# Also with calculating some values from the argumnets.
# Some help in raising exceptions for reuse.
#########################################################

def get_start_year_from_kwargs(**kwargs):
    # Gets start year from arguments else gets default one
    return kwargs.get("start_year", analyse.DEFAULT_START_YEAR)

def get_end_year_from_kwargs(**kwargs):
    # Gets start year from arguments else gets default one
    return kwargs.get("end_year", analyse.DEFAULT_END_YEAR)

def calculate_start_position(year_first_position:int):
    # Calculates start position based on year_first_position
    return year_first_position

def calculate_end_position(start_pos:int, year_capacity:int):
    # Calculates end position from start position and capacity
    return analyse.caculate_last_postion(start_pos, year_capacity)

def get_start_pos_from_kwargs(**kwargs):
    # Gets start year from arguments else calculates it.
    first_position = analyse.get_first_position_from_kwargs(**kwargs)
    return kwargs.get("start_pos", first_position)

def get_end_pos_from_kwargs(**kwargs):
    # Gets start year from arguments else calculates it.
    end_pos = kwargs.get("end_pos", None)
    if end_pos != None:
        return end_pos
    else:
        start_pos = get_start_pos_from_kwargs(**kwargs)
        year_capacity = analyse.get_capacity_from_kwargs(**kwargs)
        return calculate_end_position(start_pos, year_capacity)

def year_range_exception(start_year:int=None, end_year:int=None, 
    strict=True):
    # Returns exception if any or None
    # if start_year > end_year:
    #     err_msg = "Start year {} cant be greater than end year {}"
    #     return ValueError(err_msg.format(start_year, end_year))
    
    # if strict:
    #     if start_year < analyse.DEFAULT_START_YEAR:
    #         err_msg = "Start year {} cant be less than default " +\
    #             "end year {} when strict is enabled."
    #         return ValueError(err_msg.format(end_year, 
    #             analyse.DEFAULT_START_YEAR))
    #     if end_year > analyse.DEFAULT_END_YEAR:
    #         err_msg = "End year {} cant be greater than default " +\
    #             "end year {} when strict is enabled."
    #         return ValueError(err_msg.format(end_year, 
    #             analyse.DEFAULT_END_YEAR))

    # Its still possible for start and end year to be invalid
    if not analyse.year_valid(start_year, strict):
        return exceptions.UnsupportedYearError(start_year)
    if not analyse.year_valid(start_year, strict):
        return exceptions.UnsupportedYearError(end_year)


def year_position_exception(start_pos:int=None, end_pos:int=None, **kwargs):
    # Returns exception if any or None
    # Gets year capacity from arguments else gets default one
    # year_capacity = analyse.get_capacity_from_kwargs(**kwargs)
    # # Gets first position from arguments else gets default one
    # first_position = analyse.get_first_position_from_kwargs(**kwargs)
    # # Calculates max position based on start pos and capacity
    # max_end_pos = analyse.caculate_last_postion(start_pos, year_capacity)
    
    # if start_pos > end_pos:
    #     err_msg = "Start position {} cant be less than end position {}"
    #     error_msg = err_msg.format(start_pos, end_pos)

    # if start_pos < first_position:
    #     err_msg = "Start position {} cant be less than first position {}"
    #     error_msg = err_msg.format(start_pos, first_position)
    #     raise ValueError(error_msg)

    # if end_pos > max_end_pos:
    #     err_msg = "End position {} cant be greater than last position {}"
    #     err_msg = err_msg.format(end_pos, max_end_pos)
    #     raise ValueError(err_msg)

    # Its still possible for start and end position to be invalid
    if not analyse.position_valid(start_pos, **kwargs):
        return exceptions.UnsupportedPositionError(start_pos)
    if not analyse.position_valid(end_pos, **kwargs):
        return exceptions.UnsupportedPositionError(end_pos)

def raise_exception(exception:Exception):
    # Raises exception if exception is not None
    if exception != None:
        raise exception
    else:
        # This is done for linters to avoid 'Code not reachable'
        # or -> NoReturn
        return None

##############################################################
#               End for helpers functions
##############################################################



def guess_position(start_pos:int=None, end_pos:int=None, **kwargs):
    # Guesses position to be used with student number

    # Gets year capacity from arguments else gets default one
    year_capacity = analyse.get_capacity_from_kwargs(**kwargs)
    # Gets first position from arguments else gets default one
    first_position = analyse.get_first_position_from_kwargs(**kwargs)

    # Updates start_pos if not provided on argumnets
    if start_pos == None:
        start_pos = calculate_start_position(first_position)
    
    # Updates end_pos if not provided on argumnets
    if end_pos == None:
        end_pos = analyse.caculate_last_postion(start_pos, year_capacity)

    # Raises exception if any
    exception = year_position_exception(start_pos, end_pos, **kwargs)
    raise_exception(exception)

    # Uses start pos and end pos to guess position
    return random.randint(start_pos, end_pos)

def guess_position_part(start_pos:int=None, end_pos:int=None, **kwargs):
    # Guesses position part to be used with student number
    position = guess_position(start_pos, end_pos, **kwargs)
    return analyse.position_to_position_part(position, **kwargs)


def guess_year(start_year:int=None, end_year:int=None, strict=True):
    # Guesses year to be used with student number
    if start_year == None:
        start_year = get_start_year_from_kwargs()
    if end_year == None:
        end_year = get_end_year_from_kwargs()

    # Raises exception if any regarding argumets
    exception = year_range_exception(start_year, end_year, strict)
    raise_exception(exception)

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

def create_position_parts_regex(   
    start_pos:int=None, 
    end_pos:int=None, 
    **kwargs):
    # Creates regex pattern position part of student number.
    # The pattern is enough to filter a lot of other digits in 
    # regex string without guarantee that matched regex string is 
    # valid position part as specified by argumets.
    # In most cases it will perform as expected but issue may be with
    # leading zeros.
    if start_pos == None:
        start_pos = get_start_pos_from_kwargs(**kwargs)
    if end_pos == None:
        end_pos = get_end_pos_from_kwargs(start_pos=start_pos, **kwargs)

    # Raises exception if any regarding provided argumnets
    exception = year_position_exception(start_pos, end_pos, **kwargs)
    raise_exception(exception)

    # Calculates length of digits to use in regex pattern
    min_position_length = len(str(start_pos))
    max_position_length = len(str(end_pos))
    max_leading_zeros = max_position_length - min_position_length
    # Creates pattern for matching leading zeros
    # Matched leading zeros wont always mean position part is valid.
    if max_leading_zeros != 0:
        leading_zeros_pattern = "0{" + ",{}".format(max_leading_zeros) + "}"
    else:
        leading_zeros_pattern = ""
    # Creates pattern for matching position integer
    position_pattern = "[{}-{}]".format(start_pos, end_pos)
    # Combines the to patterns to create pattern for position part.
    return leading_zeros_pattern + position_pattern

def create_year_part_regex(   
    start_year:int=None, 
    end_year:int=None, 
    strict=True):
    if start_year == None:
        start_year = get_start_year_from_kwargs()
    if end_year == None:
        end_year = get_end_year_from_kwargs()

    # Raises exception if any regarding argumets
    exception = year_range_exception(start_year, end_year, strict)
    raise_exception(exception)

    
    # Creates start parts for years to use on patterns
    start_year_part = analyse.year_to_year_part(start_year, strict)
    end_year_part = analyse.year_to_year_part(end_year, strict)

    # Handles case were its strict
    # Strict may result in year part having 2 digits(Year 2000 problem)
    # Its worth it to ensure regex pattern take that into account.
    if strict and len(start_year_part) == 2 and len(end_year_part) != 2:
        # 2000 is the year in which student numbers changed.
        # Related to 'Year 2000 problem' or "Millennium Bug"
        pattern = "([{start_year_part}-{before_y2k_year_part}]" +\
            "|[{y2k_year}-{end_year_part}])"
        pattern = pattern.format(
            start_year_part = start_year_part, 
            before_y2k_year_part = analyse.year_to_year_part(
                analyse.BEFORE_Y2K_YEAR),
            y2k_year_part = analyse.year_to_year_part(analyse.Y2K_YEAR),
            y2k_year = analyse.Y2K_YEAR,
            end_year_part = end_year_part)
    else:
        pattern = "[{}-{}]".format(start_year_part, end_year_part) 
    return pattern

def create_regex_pattern(    
    start_year:int=None, 
    end_year:int=None, 
    start_pos:int=None, 
    end_pos:int=None, 
    strict=True,
    **kwargs):
    # Creates regex pattern for student numbers
    years_part_pattern = create_year_part_regex(start_year, end_year, 
        strict)
    positions_pattern = create_position_parts_regex(
        start_pos, end_pos, **kwargs
    )
    return years_part_pattern + positions_pattern




if __name__ == "__main__":
    student_number = 202264623
    print(guess_student_number(strict=False, start_pos=10, end_pos=100))
    print(create_regex_pattern(strict=False, start_pos=10, end_pos=100))
