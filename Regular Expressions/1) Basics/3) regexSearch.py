"""
The regex search returns an object with several methods
that give details about it.
These methods include group which returns the string matched,
start and end which return the start and ending positions of the first match,
and span which returns the start and end positions
of the first match as a tuple.
"""

import re

pattern = r"pam"

match = re.search(pattern, "eggspamsausage")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())
