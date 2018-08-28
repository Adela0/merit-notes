"""


Project:     Data Types Notes
Author:      Mr. Buckley
Last update: 8/25/2018
Description: Goes over comments, int, float, str, and type casting  
"""

# *** COMMENTS ***
# This is a comment (with a "#")
# Comments are only for the user's eyes, the program doesn't read them.
# Describe what sections of code do with a comment.
"""
This is a
multiline comment
"""

# *** DATA TYPE: INTEGER ***
# TODO: An integer number (no decimal)
integer = 5
print (integer)
print(type(integer))

# *** DATA TYPE: FLOAT ***
# TODO: A decimal number
decimal = 4.385
print(type(decimal))

# *** DATA TYPE: STRING ***
# TODO: A string of characters enclosed in quotes
word = "These are my words"
print(word)
print(type(word))

# *** TYPE CASTING ***
# This converts one type to another

# TODO: Cast float to int
decimal = 3.1415974627890
dec_to_int = int(decimal)
print(dec_to_int)
# TODO: Cast int to string
number = 4
print(int(number) + 4)

# TODO: Cast number string to int

# TODO: Input demo (str to float)
print("Give me a freaking decimal and I'll add 1 to it")
number = input(float)
print(number + 1)