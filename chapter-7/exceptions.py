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

