# intercepting errors with specific type
try:
    handle = open("missing.txt")
    number = int(handle.read())
    
    print(f"file contents: {number}")
    print(f"value of number: {number + 1}")
except IOError:
    print("sorry, we couldn't find that file")
except (ValueError, TypeError): # we wouldn't actually expect a TypeError but tuples enable multiple error catching
    print("sorry, we couldn't convert that string to a number")


# ============================================================ #


# get information about error
try:
    handler = open("missing.txt")
except IOError as error:
    print(f"sorry, we couldn't find that file: {error.strerror}")


# ============================================================ #


# using finally to guarantee a block of code is executed
import os
from typing import ValuesView
temp_handle = open("temp.text", "w")
temp_handle.write("some important text")
temp_handle.close()

try:
    my_handle = open("missing.txt")
    number = int(my_handle.read())
    
    print(f"file contents: {number}")
    print(f"value of number: {number + 1}")
except IOError as error:
    print(f"sorry, we couldn't find that file: {error.strerror}")
except ValueError as error:
    print(f"sorry, we couldn't convert that string to a number: {error.strerror}")
finally:
    os.remove("temp.text")

# finally program structure
"""
try:
    # code will run until exception is raised
except ExceptionTypeOne:
    # code in here will be run if an ExceptionTypeOne is raised in the try block
except ExceptionTypeTwo:
    # code in here will be run if an ExceptionTypeTwo is raised in the try block
else:
    # code in here will be run after the try block if it doesn't raise an exception
finally:
    # code in here will always be run
"""


# ============================================================ #


# exceptions bubble upwards, usually you want to raise an exception to notify programmer
def function_one():
    try:
        return int("sdfsf") + 5
    except ValueError:
        raise ValueError("failed to parse string")

def function_two():
    number = function_one() 
    return number + 2

try:
    print(function_two())
except ValueError as error:
    print(error)


# ============================================================ #


# raising exceptions
import re

def get_at(dna):
    if re.search(r'[^ATCG]', dna):
        raise ValueError("invalid nucleotide")

    return (dna.count("A") + dna.count("T")) / len(dna)

# gracefully skip invalid inputs
sequences = ['ACGTACGTGAC', 'ACTGCTNAACT', 'ATGGCGCTAGC'] 
for sequence in sequences:
    try:
        print(f"AT content for {sequence} is {get_at(sequence)}")
    except ValueError as error:
        print(f"skipping invalid sequence: {sequence}")