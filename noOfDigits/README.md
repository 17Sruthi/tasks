PROBLEM STATEMENT
PYTHON PROGRAM TO CHECK NUMBER OF DIGITS IN A GIVEN NUMERIC VALUE 

TEST CASES
1. This program takes first the number of times you wish to run the program. Checks whether the given input is a positive number.
2. If negative input is given it notifies the user about it and again asks for a valid input.
3. If any values whose datatype is not integer is given as input it shows INVALID INPUT and again asks for a valid input.
4. For positive and negative integer numbers the program does not consider starting digit 0 if given as a digit.
5. For float numbers the program calculates the number of digits without considering the decimal point.

LIMITATIONS
1. Float Values have errors as follows
ENTER A NUMBER:000.96
NUMBER OF DIGITS: 5

ENTER A NUMBER:-00.96
NUMBER OF DIGITS: 4

ENTER A NUMBER:0.965500
NUMBER OF DIGITS: 7

OUTPUT OF UNITTESTING

Microsoft Windows [Version 10.0.19042.746]
(c) 2020 Microsoft Corporation. All rights reserved.

C:\Users\HP\Desktop\tasks-main\noOfDigits>test_functionoOfdigits.py

UNIT-TESTING CASE 7: BOOLEAN INPUT
.
UNIT-TESTING CASE 10: VALID INPUT
.
UNIT-TESTING CASE 9: INTEGER INPUT
.
UNIT-TESTING CASE 8: STRING INPUT
.
UNIT-TESTING CASE 1: 0 AS INPUT
.
UNIT-TESTING CASE 4: BOOLEAN INPUT
.
UNIT-TESTING CASE 3: FLOAT INPUT
.
UNIT-TESTING CASE 2: NEGATIVE INPUT
.
UNIT-TESTING CASE 5: STRING INPUT
.
UNIT-TESTING CASE 6: VALID INPUT
.
----------------------------------------------------------------------
Ran 10 tests in 0.004s

OK

C:\Users\HP\Desktop\tasks-main\noOfDigits>