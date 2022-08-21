# University of Limpopo Student Number

### Description
ULID helps in analysing, creating and accessing Univesity of Limpopo student
numbers. Its flexible, customisable and gives control on what can be 
considered valid student number. That allows it to support even more student
numbers than University of Limpopo already supports.

Its more than just analysing student numbers but it can generate student
numbers and regular expression pattern for matching them. Student numbers
can be incremented to get the next student numbers.

Student numbers can be acccessed from text and files with help of regular
expressions and navaly. Using navaly, it becomes possible to extract 
student numbers from **html**, **pdf**, **docx**, etc. Navaly is not installed with ULID, you will need to manually install it with `pip install navaly`.

Student numbers of 20th centuary are supported in which year is represented
by 2 digits(**Year 2000 bug**). That can be disabled by setting passing
`strict=False` as argument to functions.

### Install
```bash
# ulid is already taken pypi(see issue #2)
pip install ulid
```

### Usage
#### Validate student number
```python
>>> ulid.student_number_valid(202001736)
True
>>> ulid.student_number_valid(9401736)
True
>>> ulid.student_number_valid(203001736)
False
>>> ulid.student_number_valid(203001736, strict=False, end_year=2050)
True
>>> ulid.student_number_valid(202001736, start_year=2021)
False
>>> ulid.student_number_valid(202001736, year_capacity=1000)
False
>>> ulid.student_number_valid(202000985, year_capacity=1000)
True
```

#### Extract year and position
```python
>>> ulid.extract_year(202001736)
2020
>>> ulid.extract_year(8423642)
1984
>>> ulid.extract_position(202001736)
1736
>>> ulid.extract_position(8423642)
23642
>>> ulid.split_student_number(202001736)
('2020', '01736')
>>> ulid.split_student_number(8423642)
('84', '23642')
>>> ulid.split_student_number(202001736, strict=False, year_capacity=100)
('2020017', '36')
```

#### Generate Student numbers
```python
>>> ulid.guess_student_number()
77539464
>>> ulid.guess_student_number()
200380352
>>> ulid.create_student_number(year=2014, position=1607)
201401607
>>> ulid.create_student_number(year=2014, position=1607, strict=False, year_capacity=1000000)
2014001607
>>> list(ulid.create_student_numbers(start_year=2020))[:2]
[202000000, 202000001]
>>> list(ulid.create_student_numbers(start_year=1959))[:2]
[5900000, 5900001]
>>> list(ulid.create_student_numbers(start_year=2020, year_capacity=1000))[:2]
[2020000, 2020001]
>>> list(ulid.create_student_numbers(start_year=2020, start_pos=1000))[:2]
[202001000, 202001001]
```

#### Getting next and previous student number
```python
>>> ulid.next_student_number(202001736)
202001738
>>> ulid.next_student_number(202099999)
202100000
>>> ulid.next_student_number(202399999, end_year=2023)
None
>>> ulid.next_student_number(202399999, end_year=2023, strict=False)
202400000
```

#### Generate student numbers regex pattern
```python
>>> ulid.create_regex_pattern()
'[1-9]\d{1,3}0{0,4}\d{1,5}'
>>> ulid.create_regex_pattern(start_year=2015)
'20[1-2]\d{1}0{0,4}\d{1,5}'
>>> ulid.create_regex_pattern(start_year=2015, end_year=2019)
'201[5-9]0{0,4}\d{1,5}'
>>> ulid.create_regex_pattern(start_year=2020, end_year=2023, start_pos=10000, end_pos=25000)
'202[0-3][1-2]\d{4}'
```

#### Extact student numbers from text
```python
>>> text = '''
First student - 2020736464
second student - 8494637
Third student - 2014736479
Invalid student number - 2012763'''
>>> ulid.extract_student_numbers(text)
[2020736464, 8494637, 2014736479]
>>> ulid.extract_student_numbers(text, start_year=2000)
[2020736464, 2014736479]
>>> ulid.extract_student_numbers(text, end_year=2000)
[8494637]
```

#### Extract student numbers from file
```python
>>> ulid.extract_student_numbers_file("file.txt")
# Output ignored
>>> ulid.extract_student_numbers_file("file.pdf") # requires navaly
# Output ignored
>>> ulid.extract_student_numbers_file("file.docx") # requires navaly
# Output ignored
```


### Default arguments values
```
# Defines what is regarded as valid student number
# Ul student numbers can accomodate 100000 students in a year.
# First student number of year is likely year00000 or year00001.
# That makes first position for year likely 0 or 1(0 was chosen).
year_capacity = 100000
year_first_position = 0

# Defines ranges for years to use.
# 1959 is the year University of Limpopo was founded.
# It may have been called by another name before 2005(before merge)
start_year = 1959
end_year = current_year + 1

# Defines range for student numbers positions to use.
# This has impact on how end part of student number is viewed.
# Which would also influence year part of student numbers.
start_pos = year_first_position
end_pos_ = start_pos + year_capacity - 1

# Requires year of student numbers to be between 1959 and current_year + 1.
# Also makes and requires year part of student number be 2 characters
# if year is less than year 2000(Year 2000 bug).
# Being True allows support for 20th centuary student numbers as caused
# 'Year 2000 bug' or 'Year 2000 problem'.
# Being True allows student numbers to be UL complient.
# Set it to False to break those rules.
strict = True
```
> Not all functions accept all of above arguments.  

### Note
* ULID is not in way any associated with [University of Limpopo]().
* ULID is just a library to help with analysing, generating and accessing
its student numbers.
* ULID was not created based on any written standard but based on small
samples of student numbers and opinions of its author.
