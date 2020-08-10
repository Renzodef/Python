"""
Regular expressions in Python can be accessed using the re module,
which is part of the standard library.
After you've defined a regular expression,
the re.match function can be used to determine whether it matches
at the beginning of a string.
If it does, match returns an object representing the match,
if not, it returns None.
To avoid any confusion while working with regular expressions,
we would use raw strings as r"expression".
Raw strings don't escape anything,
which makes use of regular expressions easier.
"""

import re

pattern = r"spam"

if re.match(pattern, "spamspamspam"):
    print("Match")
else:
    print("No match")
