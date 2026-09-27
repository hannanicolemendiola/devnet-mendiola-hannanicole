"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Mendiola, Hanna Nicole L.
Date: September 27, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Control flow in Python talks about how the
program will run based on certain
conditions. For example, you have an app
that asks for your age. Its code includes a
condition where if the age is 18 or above,
the program will recognize that you are an
adult. But if the age is below 18, it will
recognize that you are a minor.

============================================
KEY VOCABULARY
============================================
- condition: a standard that a developer
will assign to the program for it to decide
what or which block of code will be ran.
- if / elif / else: "if" is used to check if
a condition is true. If not, it will proceed 
on the "elif" code blocks. "elif" can be
more than one. And if no condition was met
among all the "if" and "elif" statements,
the "else" code block will be ran.
- comparison operator: used to compare data
and can return True or False depending on
the compared data.
- match: similar to if / elif / else, but
for much more specific conditions.
- boolean expression: a block of code
that would return True or False based on
the condition.

============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

average = 92

if average >= 90:
    print("Outstanding")
elif average >= 75:
    print("Passed")
else:
    print("Failed")    


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
I often use only one equal sign in making
conditional statements checking equality,
which are wrong in this context. For
comparison, two equal signs (==) are needed
to check equality.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
This topic is connected to almost every
aspect of Python programming, but I
specifically pinpoint functions, because
since making conditional statements are
lengthy, using functions can make the code
shorter and easier to read.
"""
