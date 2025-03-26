# from mypackage.module1 import add
# from mypackage.module2 import mul

# print(add(6,5))
# print(mul(6,5))

### Assignment 12: Using `__init__.py`

# Modify the `mypackage` package to include an `__init__.py` file that imports the functions from `module1` and `module2`. Write code to use these functions.
# from mypackage.__init__ import add,mul
# print(add(6,5))
# print(mul(6,5))

# ### Assignment 13: Importing from a Package

# Write code to import and use the functions from `mypackage` without explicitly importing `module1` and `module2`.
from mypackage import add, mul  # No need to import module1 or module2

print(add(6, 5))  # Output: 11
print(mul(6, 5))  # Output: 30

# ### Assignment 14: Relative Imports

# Create a subpackage named `subpackage` within `mypackage` and move `module2` into `subpackage`. Modify the import statements in `__init__.py` to use relative imports. Write code to use the functions from both modules.
from mypackage import add, mul  # No need to import module1 or module2

print(add(6, 5))  # Output: 11
print(mul(6, 5))  # Output: 30


# ### Assignment 15: Handling Package Import Errors

# Write code that attempts to import a non-existent function from `mypackage` and gracefully handles the import error by printing an error message.

try:
    from mypackage import non_existent_function  # This function does not exist
except ImportError:
    print("Error: The function 'non_existent_function' could not be found in 'mypackage'. Please check the function name or package.")
