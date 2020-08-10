"""
Named parameters to a function can be made optional
by giving them a default value.
These must come after named parameters without a default value.
"""


def function(x, y, food="spam"):
    print(food)


function(1, 2)
function(3, 4, "egg")
