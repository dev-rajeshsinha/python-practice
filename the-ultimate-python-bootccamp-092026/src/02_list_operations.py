demo_list = [1, 4.6, True, "Hello", None]
print(f"Demo List: {demo_list}")
print(f"Length of Demo List: {len(demo_list)}")

print()  # Just to add a blank line for better readability
print(f"First element of Demo List: {demo_list[0]}")
print(f"Last element of Demo List: {demo_list[-1]}")
print(f"Demo List excluding the first element: {demo_list[1:]}")
print(f"Demo List excluding the last element: {demo_list[:-1]}")

print()  # Just to add a blank line for better readability
print(f"Demo List in reversed order: {demo_list[::-1]}")
print(f"First two elements of Demo List: {demo_list[:2]}")
print(f"Last two elements of Demo List: {demo_list[-2:]}")

print()  # Just to add a blank line for better readability
print(f"Every second element of Demo List: {demo_list[::2]}")
print(f"Every third element of Demo List: {demo_list[::3]}")
print(f"Every fourth element of Demo List: {demo_list[::4]}")

print()  # Just to add a blank line for better readability
print(f"Insert 99 at index 2: {demo_list[:2] + [99] + demo_list[2:]}")
# Same operation can be performed using the insert method as: demo_list.insert(2, 99)

print()  # Just to add a blank line for better readability
print(f"Remove element at index 2: {demo_list[:2] + demo_list[3:]}")
# Same operation can be performed using the pop method as: demo_list.pop(2)

print()  # Just to add a blank line for better readability
print(f"Append 42 to Demo List: {demo_list + [42]}")
# Same operation can be performed using the append method as: demo_list.append(42)

print()  # Just to add a blank line for better readability
print(f"Remove element with value 4.6: {[item for item in demo_list if item != 4.6]}")
# Same operation can be performed using the remove method as: demo_list.remove(4.6)

print()  # Just to add a blank line for better readability
print(
    f"Remove element with value 'Hello': {[item for item in demo_list if item != 'Hello']}"
)
# Same operation can be performed using the remove method as: demo_list.remove('Hello')

print()  # Just to add a blank line for better readability
print(f"Extend Demo List with [7, 8, 9]: {demo_list + [7, 8, 9]}")
# Same operation can be performed using the extend method as: demo_list.extend([7, 8, 9])

print()  # Just to add a blank line for better readability
print(f"Repeat Demo List twice: {demo_list * 2}")
# Same operation can be performed using a loop as: demo_list.extend(demo_list)

print()  # Just to add a blank line for better readability
print(f"Clear Demo List: {[]}")
# Same operation can be performed using the clear method as: demo_list.clear()
