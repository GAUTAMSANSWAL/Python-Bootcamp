# Regular expressions (regex) are powerful tools for pattern matching in strings. Python's re module provides support for regex.

import re
text = "The rain in Spain stays mainly in the plain."

# search for a pattern
match = re.search('in', text)
if match:
    print("match found")
    print("start index:", match.start())
    print("end index:", match.end())

# finding similar words like "ain" rain, spain, plain
matches = re.findall('in', text, re.IGNORECASE)
print("matches found:", matches)


'''
\b -	Word boundary (ensures we match full words, not parts of words)
\w+ -	One or more word characters (letters, digits, underscores)
\b -	Word boundary (ensures we match entire words)
'''

# find all words that has "ain" in it
matches = re.findall(r'\b\w*ain\w*\b', text, re.IGNORECASE)
print("matches found:", matches)