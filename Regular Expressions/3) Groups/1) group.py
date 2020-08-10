"""
The content of groups in a match can be accessed using the group function.
A call of group(0) or group() returns the whole match.
A call of group(n), where n is greater than 0,
returns the nth group from the left.
The method groups() returns all groups up from 1.
"""

import re

pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghijklmnop")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())
