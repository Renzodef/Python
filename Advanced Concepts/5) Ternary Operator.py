"""
Conditional expressions provide the functionality
of if statements while using less code.
They shouldn't be overused, as they can easily reduce readability,
but they are often useful when assigning variables.
Conditional expressions are also known as applications of the ternary operator.
"""

a = 7
b = 1 if a >= 5 else 42
print(b)
