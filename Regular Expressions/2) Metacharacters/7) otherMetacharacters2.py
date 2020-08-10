"""
The metacharacter + is very similar to *,
except it means "one or more repetitions",
 as opposed to "zero or more repetitions".
"""

import re

pattern = r"g+"

if re.match(pattern, "g"):
    print("Match 1")

if re.match(pattern, "gggggggggggggg"):
    print("Match 2")

if re.match(pattern, "abc"):
    print("Match 3")
