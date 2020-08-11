# Count number of occurences of a letter in a string.

import pprint

# Text to count characters in
message = "It was bright cold day in April, and the clocks where striking thirteen."

# Initialize empty dictionary
count = {}


for character in message.upper():
    count.setdefault(character, 0)
    count[character] += 1


# pprint ("prettty print"?) has some automatic formatting and ordering
pprint.pprint(count)

# not sure what pformat is
text = pprint.pformat(count)
print(text)

