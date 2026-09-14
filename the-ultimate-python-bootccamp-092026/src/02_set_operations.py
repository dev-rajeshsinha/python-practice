demo_set = {1, 4.6, True, "Hello", None}
print(f"Demo Set: {demo_set}")
print(f"Length of Demo Set: {len(demo_set)}")
print(f"ID of Demo Set: {id(demo_set)}")

print()  # Just to add a blank line for better readability
another_set = {0, 4.6, None, False}
print(f"Another Set: {another_set}")
print(f"Length of Another Set: {len(another_set)}")
print(f"ID of Another Set: {id(another_set)}")

print()  # Just to add a blank line for better readability
print(f"Union of Demo Set and Another Set: {demo_set | another_set}")
print(f"ID of Union of Demo Set and Another Set: {id(demo_set | another_set)}")

print()  # Just to add a blank line for better readability
print(f"Intersection of Demo Set and Another Set: {demo_set & another_set}")
print(f"ID of Intersection of Demo Set and Another Set: {id(demo_set & another_set)}")

print()  # Just to add a blank line for better readability
print(f"Difference of Demo Set and Another Set: {demo_set - another_set}")
print(f"ID of Difference of Demo Set and Another Set: {id(demo_set - another_set)}")

print()  # Just to add a blank line for better readability
print(f"Symmetric Difference of Demo Set and Another Set: {demo_set ^ another_set}")
print(
    f"ID of Symmetric Difference of Demo Set and Another Set: {id(demo_set ^ another_set)}"
)

print()  # Just to add a blank line for better readability
print(f"Subset Check (Demo Set <= Another Set): {demo_set <= another_set}")

print()  # Just to add a blank line for better readability
print(f"Superset Check (Demo Set >= Another Set): {demo_set >= another_set}")

print()  # Just to add a blank line for better readability
print(
    f"Disjoint Check (Demo Set.isdisjoint(Another Set)): {demo_set.isdisjoint(another_set)}"
)

print()  # Just to add a blank line for better readability
print(f"Equality Check (Demo Set == Another Set): {demo_set == another_set}")

print()  # Just to add a blank line for better readability
print(f"Inequality Check (Demo Set != Another Set): {demo_set != another_set}")

print()  # Just to add a blank line for better readability
print(f"Demo Set after adding an element 42: {demo_set | {42}}")
# Same operation can be performed using the add method as: demo_set.add(42)
print(f"ID of Demo Set after adding an element 42: {id(demo_set | {42})}")

print()  # Just to add a blank line for better readability
print(f"Demo Set after removing an element 42: {demo_set - {42}}")
# Same operation can be performed using the remove method as: demo_set.remove(42)
print(f"ID of Demo Set after removing an element 42: {id(demo_set - {42})}")

print()  # Just to add a blank line for better readability
print(f"Demo Set after adding multiple elements {7, 8, 9}: {demo_set | {7, 8, 9}}")
# Same operation can be performed using the update method as: demo_set.update({7, 8, 9})
print(
    f"ID of Demo Set after adding multiple elements {7, 8, 9}: {id(demo_set | {7, 8, 9})}"
)

print()  # Just to add a blank line for better readability
print(
    f"Demo Set after removing multiple elements {4.6, None}: {demo_set - {4.6, None}}"
)
# Same operation can be performed using the difference_update method as: demo_set.difference_update({4.6, None})
print(
    f"ID of Demo Set after removing multiple elements {4.6, None}: {id(demo_set - {4.6, None})}"
)

print()  # Just to add a blank line for better readability
print(f"Demo Set after clearing all elements: {demo_set - demo_set}")
# Same operation can be performed using the clear method as: demo_set.clear()
print(f"ID of Demo Set after clearing all elements: {id(demo_set - demo_set)}")
