"""
Find:

Union
Intersection
Difference (A - B)
Difference (B - A)
Symmetric Difference
    """

A = {1,2,3,4,5}
B = {4,5,6,7,8}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(B.difference(A))
print(A.symmetric_difference(B))


# Find common elements using sets.
list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]

print(set(list1).intersection(set(list2)))