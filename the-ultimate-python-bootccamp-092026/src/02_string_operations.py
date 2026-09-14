demo_string = " This is a demo string with a special character @ "
print(f"Demo String: {demo_string}")
print(f"Length of Demo String: {len(demo_string)}")

print()  # Just to add a blank line for better readability
print(f"Demo String in Uppercase: {demo_string.upper()}")
print(f"Demo String is uppercase: {demo_string.isupper()}")
print(f"Demo String in Lowercase: {demo_string.lower()}")
print(f"Demo String is lowercase: {demo_string.islower()}")
print(f"Demo String in Title Case: {demo_string.title()}")
print(f"Demo String is title case: {demo_string.istitle()}")

print()  # Just to add a blank line for better readability
print(f"Demo String without leading and trailing spaces: {demo_string.strip()}")
print(f"Demo String replaced '@' with '#': {demo_string.replace('@', '#')}")
print(f"Does the Demo String start with 'This': {demo_string.startswith('This')}")
print(f"Does the Demo String end with '@': {demo_string.endswith('@')}")
print(f"Index of '@' in Demo String: {demo_string.find('@')}")
print(f"Count of 'a' in Demo String: {demo_string.count('a')}")
print(f"Demo String split into words: {demo_string.split()}")

print()  # Just to add a blank line for better readability
print(f"Demo String is alphanumeric: {demo_string.isalnum()}")
print(f"Demo String is alphabetic: {demo_string.isalpha()}")
print(f"Demo String is numeric: {demo_string.isnumeric()}")
print(f"Demo String is whitespace: {demo_string.isspace()}")
print(f"Demo String is printable: {demo_string.isprintable()}")

print()  # Just to add a blank line for better readability
print(f"Demo String in reversed order: {demo_string[::-1]}")
print(f"First Character of Demo String: {demo_string[0]}")
print(f"Last Character of Demo String: {demo_string[-1]}")

print()  # Just to add a blank line for better readability
print(f"Substring from index 5 to 10 of Demo String: {demo_string[5:11]}")
print(f"Substring from start to index 10 of Demo String: {demo_string[:11]}")
print(f"Substring from index 5 to end of Demo String: {demo_string[5:]}")
print(f"Substring from start to end of Demo String: {demo_string[:]}")

print()  # Just to add a blank line for better readability
print(f"Every second character of Demo String: {demo_string[::2]}")
print(f"Every third character of Demo String: {demo_string[::3]}")
print(f"Every fourth character of Demo String: {demo_string[::4]}")
print(f"Every fifth character of Demo String: {demo_string[::5]}")
print(f"Every sixth character of Demo String: {demo_string[::6]}")
