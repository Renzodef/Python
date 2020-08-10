"""
Another important metacharacter is |.
This means "or", so red|blue matches either "red" or "blue".
"""

import re

pattern = r"gr(a|e)y"

match = re.match(pattern, "gray")
if match:
    print("Match 1")

match = re.match(pattern, "grey")
if match:
    print("Match 2")

match = re.match(pattern, "griy")
if match:
    print("Match 3")
