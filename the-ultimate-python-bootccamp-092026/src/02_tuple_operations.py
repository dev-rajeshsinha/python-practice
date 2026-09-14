demo_tuple = (1, 4.6, True, "Hello", None)
print(f"Demo Tuple: {demo_tuple}")
print(f"Length of Demo Tuple: {len(demo_tuple)}")
print(f"ID of Demo Tuple: {id(demo_tuple)}")

print()  # Just to add a blank line for better readability
print(f"First element of Demo Tuple: {demo_tuple[0]}")
print(f"Last element of Demo Tuple: {demo_tuple[-1]}")
print(f"Demo Tuple excluding the first element: {demo_tuple[1:]}")
print(f"Demo Tuple excluding the last element: {demo_tuple[:-1]}")

print()  # Just to add a blank line for better readability
print(f"Demo Tuple in reversed order: {demo_tuple[::-1]}")
print(f"ID of Demo Tuple in reversed order: {id(demo_tuple[::-1])}")
print(f"First two elements of Demo Tuple: {demo_tuple[:2]}")
print(f"Last two elements of Demo Tuple: {demo_tuple[-2:]}")

print()  # Just to add a blank line for better readability
print(f"Every second element of Demo Tuple: {demo_tuple[::2]}")
print(f"Every third element of Demo Tuple: {demo_tuple[::3]}")
print(f"Every fourth element of Demo Tuple: {demo_tuple[::4]}")
