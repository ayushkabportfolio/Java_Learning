You cannot access items in a set by referring to an index or a key.

1.
But you can loop through the set items using a for loop,
    or ask if a specified value is present in a set, by using the in keyword.

set1 = {"apple", "banana", "cherry"}
for x in set1:
    print(x)
#banana
# cherry
# apple

set1 = {"apple", "banana", "cherry"}
print("banana" in set1)
#True

set1 = {"apple", "banana", "cherry"}
print("banana" not in set1)
#False

---Change Items---
Once a set is created, you --cannot change-- its items, but you can add new items.