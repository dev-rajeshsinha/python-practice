demo_dictionary = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Demo Dictionary: {demo_dictionary}")
print(f"Length of Demo Dictionary: {len(demo_dictionary)}")
print(f"ID of Demo Dictionary: {id(demo_dictionary)}")

print()  # Just to add a blank line for better readability
another_dictionary = {"name": "Bob", "age": 25, "city": "Los Angeles"}
print(f"Another Dictionary: {another_dictionary}")
print(f"Length of Another Dictionary: {len(another_dictionary)}")
print(f"ID of Another Dictionary: {id(another_dictionary)}")

print()  # Just to add a blank line for better readability
print(f"Keys of Demo Dictionary: {list(demo_dictionary.keys())}")
print(f"Keys of Another Dictionary: {list(another_dictionary.keys())}")
print(f"Values of Demo Dictionary: {list(demo_dictionary.values())}")
print(f"Values of Another Dictionary: {list(another_dictionary.values())}")
print(f"Items of Demo Dictionary: {list(demo_dictionary.items())}")
print(f"Items of Another Dictionary: {list(another_dictionary.items())}")

print()  # Just to add a blank line for better readability
# Accessing dictionary elements
print(f"Accessing 'name' from Demo Dictionary: {demo_dictionary['name']}")
print(f"Accessing 'age' from Another Dictionary: {another_dictionary['age']}")
print(f"Accessing 'city' from Demo Dictionary: {demo_dictionary['city']}")
print(f"Accessing 'city' from Another Dictionary: {another_dictionary['city']}")

print()  # Just to add a blank line for better readability
# Using get() method to access dictionary elements safely
print(
    f"Accessing 'name' from Demo Dictionary using get(): {demo_dictionary.get('name', "Name Not Found")}"
)
print(
    f"Accessing 'age' from Another Dictionary using get(): {another_dictionary.get('age', "Age Not Found")}"
)
print(
    f"Accessing 'city' from Demo Dictionary using get(): {demo_dictionary.get('city', "City Not Found")}"
)
print(
    f"Accessing 'city' from Another Dictionary using get(): {another_dictionary.get('city', "City Not Found")}"
)

print()  # Just to add a blank line for better readability
# Modifying dictionary elements
demo_dictionary["age"] = 31
another_dictionary["city"] = "San Francisco"
print(f"Modified Demo Dictionary: {demo_dictionary}")
print(f"ID of Modified Demo Dictionary: {id(demo_dictionary)}")
print(f"Modified Another Dictionary: {another_dictionary}")
print(f"ID of Modified Another Dictionary: {id(another_dictionary)}")

print()  # Just to add a blank line for better readability
# Adding new elements to dictionaries
demo_dictionary["email"] = "alice@example.com"
another_dictionary["email"] = "bob@example.com"
print(f"Demo Dictionary after adding 'email': {demo_dictionary}")
print(f"ID of Demo Dictionary after adding 'email': {id(demo_dictionary)}")
print(f"Another Dictionary after adding 'email': {another_dictionary}")
print(f"ID of Another Dictionary after adding 'email': {id(another_dictionary)}")

print()  # Just to add a blank line for better readability
# Removing elements from dictionaries
del demo_dictionary["email"]
del another_dictionary["email"]
print(f"Demo Dictionary after removing 'email': {demo_dictionary}")
print(f"ID of Demo Dictionary after removing 'email': {id(demo_dictionary)}")
print(f"Another Dictionary after removing 'email': {another_dictionary}")
print(f"ID of Another Dictionary after removing 'email': {id(another_dictionary)}")

print()  # Just to add a blank line for better readability
print(
    f"Removing 'email' from Demo Dictionary: {demo_dictionary.pop('email', 'Email Not Found')}"
)
print(f"Demo Dictionary after removing 'email': {demo_dictionary}")
print(f"ID of Demo Dictionary after removing 'email': {id(demo_dictionary)}")

print()  # Just to add a blank line for better readability
print(f"Removing last element from Demo Dictionary: {demo_dictionary.popitem()}")
print(f"Demo Dictionary after removing last element: {demo_dictionary}")
print(f"ID of Demo Dictionary after removing last element: {id(demo_dictionary)}")

print()  # Just to add a blank line for better readability
# Clearing all elements from dictionaries
demo_dictionary.clear()
another_dictionary.clear()
print(f"Demo Dictionary after clearing: {demo_dictionary}")
print(f"ID of Demo Dictionary after clearing: {id(demo_dictionary)}")
print(f"Another Dictionary after clearing: {another_dictionary}")
print(f"ID of Another Dictionary after clearing: {id(another_dictionary)}")
