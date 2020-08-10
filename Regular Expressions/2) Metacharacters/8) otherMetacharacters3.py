"""
The metacharacter ? means "zero or one repetitions".
"""

import re

pattern = r"ice(-)?cream"

if re.match(pattern, "ice-cream"):
    print("Match 1")

if re.match(pattern, "icecream"):
    print("Match 2")

if re.match(pattern, "ice--cream"):
    print("Match 3")

if re.match(pattern, "ice--ice"):
    print("Match 4")
