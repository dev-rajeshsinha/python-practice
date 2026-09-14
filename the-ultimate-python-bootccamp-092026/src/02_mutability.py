x = "Hello"
y = x
print(
    f"Initial Value of X: {x}, ID: {id(x)}"
)  # Initial value of X: Hello, ID: <some_id>
print(
    f"Initial Value of Y: {y}, ID: {id(y)}"
)  # Initial value of Y: Hello, ID: <some_id>

print()  # Just to add a blank line for better readability
x = x + " World"
print(
    f"Updated Value of X: {x}, ID: {id(x)}"
)  # Updated value of X: Hello World, ID: <some_id>
print(
    f"Value of Y after X is updated: {y}, ID: {id(y)}"
)  # Value of Y after X is updated: Hello, ID: <some_id>

# This demonstrates that strings are immutable in Python. When we modify `x`, it creates a new string object, leaving `y` unchanged. Also, the IDs of the objects help us track these changes.

print()  # Just to add a blank line for better readability
demo_list = ["apple", "banana", "cherry"]
print(
    f"Initial Value of demo_list: {demo_list}, ID: {id(demo_list)}"
)  # Initial value of demo_list: ['apple', 'banana', 'cherry'], ID: <some_id>

demo_list.append("date")
print(
    f"Updated Value of demo_list: {demo_list}, ID: {id(demo_list)}"
)  # Updated value of demo_list: ['apple', 'banana', 'cherry', 'date'], ID: <some_id>

# This demonstrates that lists are mutable in Python. When we modify `demo_list`, it changes the same list object, which is reflected in its ID.
