demo_frozenset = frozenset({1, 4.6, True, "Hello", None})
print(f"Demo Frozenset: {demo_frozenset}")
print(f"Length of Demo Frozenset: {len(demo_frozenset)}")
print(f"ID of Demo Frozenset: {id(demo_frozenset)}")

print()  # Just to add a blank line for better readability
another_frozenset = frozenset({0, 4.6, None, False})
print(f"Another Frozenset: {another_frozenset}")
print(f"Length of Another Frozenset: {len(another_frozenset)}")
print(f"ID of Another Frozenset: {id(another_frozenset)}")

print()  # Just to add a blank line for better readability
print(
    f"Union of Demo Frozenset and Another Frozenset: {demo_frozenset | another_frozenset}"
)
print(
    f"ID of Union of Demo Frozenset and Another Frozenset: {id(demo_frozenset | another_frozenset)}"
)

print()  # Just to add a blank line for better readability
print(
    f"Intersection of Demo Frozenset and Another Frozenset: {demo_frozenset & another_frozenset}"
)
print(
    f"ID of Intersection of Demo Frozenset and Another Frozenset: {id(demo_frozenset & another_frozenset)}"
)

print()  # Just to add a blank line for better readability
print(
    f"Difference of Demo Frozenset and Another Frozenset: {demo_frozenset - another_frozenset}"
)
print(
    f"ID of Difference of Demo Frozenset and Another Frozenset: {id(demo_frozenset - another_frozenset)}"
)

print()  # Just to add a blank line for better readability
print(
    f"Symmetric Difference of Demo Frozenset and Another Frozenset: {demo_frozenset ^ another_frozenset}"
)
print(
    f"ID of Symmetric Difference of Demo Frozenset and Another Frozenset: {id(demo_frozenset ^ another_frozenset)}"
)

print()  # Just to add a blank line for better readability
print(
    f"Subset Check (Demo Frozenset <= Another Frozenset): {demo_frozenset <= another_frozenset}"
)
print(
    f"Superset Check (Demo Frozenset >= Another Frozenset): {demo_frozenset >= another_frozenset}"
)
print(
    f"Disjoint Check (Demo Frozenset.isdisjoint(Another Frozenset)): {demo_frozenset.isdisjoint(another_frozenset)}"
)
print(
    f"Equality Check (Demo Frozenset == Another Frozenset): {demo_frozenset == another_frozenset}"
)
print(
    f"Inequality Check (Demo Frozenset != Another Frozenset): {demo_frozenset != another_frozenset}"
)
