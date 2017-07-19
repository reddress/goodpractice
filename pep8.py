# https://www.python.org/dev/peps/pep-0008/

# Continuation lines

foo = long_function_name(var_one, var_two,
                         var_three)  # OK

def long_function_name(
        var_one,
        var_two, var_three):
    print(var_one)  # OK


# 'if' across multiple lines

if (this_is_one_thing and
    that_is_another):
    do_something()  # No extra indentation


my_list = [
    1, 2, 3,
    4, 5, 6,
    ]

result = some_function(
    'a', 'b',
    'c', 'd', 'e',
    )

# Break formulas before a binary operator

income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction)

# Blank lines

Surround top-level function and class defintions with two blank lines

Method defintions inside a class are surrounded by a single blank line

# TODO ... sections skipped ...
          
# Comments

# Use two spaces after a sentence-ending period.  Like this.
# Actually, no. Chicago says one space. 

# Include a space between # and the comment.

# Use inline comments sparingly. Separate code from inline comments
# with at least two spaces.


# Documentation strings (docstrings)

# Write docstrings for all public modules, functions, classes, and methods.  

# See PEP 257
# https://www.python.org/dev/peps/pep-0257/

# A docstring is a string literal that occurs as the first statement in a module, function, class, or method defintion. It becomes the __doc__ special attribute of that object.


# One-line docstring

def kos_root():
    """Return the pathname of the KOS root directory."""
    global kos_root

    # Observations:
    #
    # Always use triple quotes
    # The closing quotes are on the same line
    # No blank line before or after the docstring
    # The docstring is a phrase ending in a period. It prescribes the function or method's effect as a command, not a description.

def function(a, b):
    """Do something and return a list."""
    return [a * 10, b]


# Multi-line docstrings

def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    if real == 0.0 and imag == 0.0:
        return complex_zero
    return (real, imag)
    

