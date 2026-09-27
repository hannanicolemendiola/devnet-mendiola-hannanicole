"""
Module 2 — Lesson 1: Variables & Data Types
Student: Mendiola, Hanna Nicole L.
Date: September 27, 2026

============================================
WHAT IS THIS TOPIC? 
============================================
This topic talks about how we store data in
the program and how we classify them.
Variables are like containers that store
them. And these data have different types,
which serve different purposes.

============================================
KEY VOCABULARY
============================================
- variable: a container that stores data
- data type: how data in a variable is classified
- int: a whole number
- float: a number with decimals
- string: characters, words, phrases or paragraphs read as text
- boolean: true or false

============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""
number = 202
decimal = 0.1
text = "Ayelle"
check = True

print(f"{number} - {type(number)}")
print(f"{decimal} - {type(decimal)}")
print(f"{text} - {type(text)}")
print(f"{check} - {type(check)}")

print(number / 3)

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
A common mistake I make is when using
if-else statements after a block of code
where the user is asked for a number input,
where I sometimes forget that "input()"
always returns a string. The fix is to
either put "input()" inside "int()", or make
the if-else statement conditions have
quotations (e.g., if choice == "1":).

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
This connects to the next lesson, which is
control flow, that includes comparison,
if-else statements, match statements,
and more, because knowing what data type to
use is necessary in the next lessons.
"""
