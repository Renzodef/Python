"""
One of the most important re methods that use regular expressions is sub.
Syntax:
re.sub(pattern, repl, string, count=0)
This method replaces all occurrences of the pattern in string with repl,
substituting all occurrences, unless count provided.
This method returns the modified string.
"""

import re

str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)
