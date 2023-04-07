import re

# Define the pattern to match
pattern = "^[a-zA-Z0-9\s]+$"

# Test string to match against the pattern
string = "Hello @Good Morning"

# Use the `search()` function to check if the string matches the pattern
result = re.search(pattern, string)

# Check if a match was found
if result:
    print("The string matches the pattern.")
else:
    print("The string does not match the pattern.")
