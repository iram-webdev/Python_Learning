# Python Sets

Sets are unordered collections of data items. They store multiple items in a single variable. Set items are separated by commas and enclosed within curly brackets `{}`. Sets are mutable, meaning you can add or remove items after creation, but you cannot change individual elements in place. Sets do not contain duplicate items.

#### Example:

```python
info = {"Carla", 19, False, 5.9, 19}
print(info)
```

#### Output:
```text
{False, 19, 5.9, 'Carla'}
```

Here, we see that the items of a set may appear in any order, and hence they cannot be accessed using index numbers. Also, sets do not allow duplicate values.

**Quick Quiz:** Try to create an empty set. Check using the `type()` function whether the type of your variable is a set.

## Accessing Set Items

### Using a For Loop

You can access items of a set using a `for` loop.

#### Example:

```python
info = {"Carla", 19, False, 5.9}

for item in info:
    print(item)
```

#### Output:
```text
False
Carla
19
5.9
```


# Sets in Python

## 1. What is a Set?

A **set** in Python is a built-in data type used to store multiple items in a single variable.

A set is:
- **Unordered:** Items do not have a fixed position or guaranteed order.
- **Unindexed:** We cannot access elements using indexes like `my_set[0]`.
- **Unique:** Duplicate elements are automatically removed.
- **Mutable:** We can add or remove elements after creating a set.
- **Heterogeneous:** A set can contain different data types, such as integers, strings, and floats.

### Example

```python
numbers = {1, 2, 3, 4, 5}
print(numbers)
```

**Output:**

```text
{1, 2, 3, 4, 5}
```

> Note: Since sets are unordered, do not depend on the order in which elements are displayed.

---

## 2. Creating a Set

We can create a set by placing comma-separated values inside curly braces `{}`.

### Example 1: Set with Integers

```python
numbers = {10, 20, 30, 40}
print(numbers)
```

### Example 2: Set with Strings

```python
fruits = {"apple", "banana", "mango"}
print(fruits)
```

### Example 3: Set with Duplicate Values

```python
numbers = {1, 2, 2, 3, 3, 4}
print(numbers)
```

**Output:**

```text
{1, 2, 3, 4}
```

Duplicate values are automatically removed.

### Example 4: Creating an Empty Set

```python
my_set = set()
print(my_set)
print(type(my_set))
```

**Output:**

```text
set()
<class 'set'>
```

**Important:** `{}` creates an empty dictionary, not an empty set. Use `set()` to create an empty set.

---

## 3. Accessing Set Elements

Sets do not support indexing or slicing because they are unordered.

### Incorrect Example

```python
numbers = {10, 20, 30}
print(numbers[0])
```

This raises a `TypeError`.

### Correct Example: Using a Loop

```python
numbers = {10, 20, 30}

for number in numbers:
    print(number)
```

**Output:** The elements are printed, but their order is not guaranteed.

### Checking Whether an Element Exists

```python
fruits = {"apple", "banana", "mango"}

print("apple" in fruits)
print("orange" in fruits)
```

**Output:**

```text
True
False
```

---

## 4. Adding Elements to a Set

Python provides two main methods to add elements to a set.

### A. `add()`

Adds one element to the set.

```python
numbers = {1, 2, 3}
numbers.add(4)

print(numbers)
```

**Output:**

```text
{1, 2, 3, 4}
```

Adding an element that already exists does not create a duplicate.

```python
numbers = {1, 2, 3}
numbers.add(2)

print(numbers)
```

### B. `update()`

Adds multiple elements from an iterable, such as another set, list, or tuple.

```python
numbers = {1, 2, 3}
numbers.update([4, 5, 6])

print(numbers)
```

**Output:**

```text
{1, 2, 3, 4, 5, 6}
```

---

## 5. Removing Elements from a Set

### A. `remove()`

Removes an element. Raises a `KeyError` if the element does not exist.

```python
numbers = {1, 2, 3, 4}
numbers.remove(3)

print(numbers)
```

### B. `discard()`

Removes an element if it exists. Does not raise an error if the element is missing.

```python
numbers = {1, 2, 3, 4}
numbers.discard(5)

print(numbers)
```

### C. `pop()`

Removes and returns an arbitrary element from the set.

```python
numbers = {10, 20, 30}
removed = numbers.pop()

print(removed)
print(numbers)
```

The removed element is not guaranteed to be the smallest or largest.

### D. `clear()`

Removes all elements from the set.

```python
numbers = {1, 2, 3}
numbers.clear()

print(numbers)
```

**Output:**

```text
set()
```

### E. `del`

Deletes the entire set variable.

```python
numbers = {1, 2, 3}
del numbers
```

After deletion, using `numbers` raises a `NameError` unless the variable is defined again.

---

## 6. Set Operations

Set operations allow us to combine sets, find common elements, and identify differences.

Consider these two sets:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

### A. Union

**Union** returns all unique elements from both sets.

Symbol: `|`

Method: `union()`

```python
print(A | B)
print(A.union(B))
```

**Output:**

```text
{1, 2, 3, 4, 5, 6}
{1, 2, 3, 4, 5, 6}
```

### B. Intersection

**Intersection** returns elements common to both sets.

Symbol: `&`

Method: `intersection()`

```python
print(A & B)
print(A.intersection(B))
```

**Output:**

```text
{3, 4}
{3, 4}
```

### C. Difference

**Difference** returns elements present in the first set but absent from the second.

Symbol: `-`

Method: `difference()`

```python
print(A - B)
print(B - A)
```

**Output:**

```text
{1, 2}
{5, 6}
```

The order of the sets matters when calculating a difference.

### D. Symmetric Difference

Returns elements that belong to either set, but not to both.

Symbol: `^`

Method: `symmetric_difference()`

```python
print(A ^ B)
print(A.symmetric_difference(B))
```

**Output:**

```text
{1, 2, 5, 6}
{1, 2, 5, 6}
```

---

## 7. Set Comparison Methods

### A. `issubset()`

Checks whether every element of one set is present in another set.

```python
A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))
```

**Output:**

```text
True
```

The operator `<=` can also check for a subset.

### B. `issuperset()`

Checks whether a set contains every element of another set.

```python
A = {1, 2, 3, 4}
B = {1, 2}

print(A.issuperset(B))
```

**Output:**

```text
True
```

The operator `>=` can also check for a superset.

### C. `isdisjoint()`

Returns `True` if two sets have no common elements.

```python
A = {1, 2, 3}
B = {4, 5, 6}

print(A.isdisjoint(B))
```

**Output:**

```text
True
```

---

## 8. Updating Sets with Set Operations

These methods modify the original set.

### A. `update()`

Adds elements from other iterables.

```python
A = {1, 2}
A.update({3, 4})

print(A)
```

### B. `intersection_update()`

Keeps only elements common to the set and the given iterable.

```python
A = {1, 2, 3, 4}
A.intersection_update({3, 4, 5})

print(A)
```

**Output:**

```text
{3, 4}
```

### C. `difference_update()`

Removes elements found in the given iterable.

```python
A = {1, 2, 3, 4}
A.difference_update({3, 4})

print(A)
```

**Output:**

```text
{1, 2}
```

### D. `symmetric_difference_update()`

Keeps elements that occur in either set, but not both.

```python
A = {1, 2, 3}
A.symmetric_difference_update({3, 4})

print(A)
```

**Output:**

```text
{1, 2, 4}
```

---

## 9. Set Methods Summary

| Method | Purpose |
|---|---|
| `add(x)` | Adds one element |
| `update(iterable)` | Adds multiple elements |
| `remove(x)` | Removes an element; raises an error if missing |
| `discard(x)` | Removes an element without an error if missing |
| `pop()` | Removes and returns an arbitrary element |
| `clear()` | Removes all elements |
| `union()` | Combines unique elements |
| `intersection()` | Finds common elements |
| `difference()` | Finds elements only in the first set |
| `symmetric_difference()` | Finds elements in either set but not both |
| `issubset()` | Checks whether a set is a subset |
| `issuperset()` | Checks whether a set is a superset |
| `isdisjoint()` | Checks whether sets have no common elements |
| `intersection_update()` | Keeps common elements in the original set |
| `difference_update()` | Removes matching elements from the original set |
| `symmetric_difference_update()` | Updates the set with non-common elements |
| `copy()` | Creates a shallow copy of the set |

---

## 10. The `copy()` Method

The `copy()` method creates a shallow copy of a set.

```python
original = {1, 2, 3}
new_set = original.copy()

new_set.add(4)

print(original)
print(new_set)
```

**Output:**

```text
{1, 2, 3}
{1, 2, 3, 4}
```

Adding an element to `new_set` does not change `original`.

---

## 11. Frozen Set in Python

A **frozenset** is an immutable version of a set. Once created, its elements cannot be added or removed.

### Example

```python
numbers = frozenset([1, 2, 3, 3, 4])

print(numbers)
print(type(numbers))
```

The duplicate `3` is removed.

### Operations on a Frozenset

Frozensets support operations such as union, intersection, difference, and symmetric difference.

```python
A = frozenset([1, 2, 3])
B = frozenset([3, 4, 5])

print(A.union(B))
print(A.intersection(B))
```

### Difference Between Set and Frozenset

| Set | Frozenset |
|---|---|
| Mutable | Immutable |
| Supports `add()` and `remove()` | Does not support `add()` or `remove()` |
| Cannot be used as a dictionary key | Can be used as a dictionary key |
| Written using `{}` or `set()` | Created using `frozenset()` |

---

## 12. Important Rules for Sets

1. Sets do not allow duplicate elements.
2. Sets do not support indexing or slicing.
3. Set elements must be hashable.
4. Lists and dictionaries cannot be elements of a set because they are unhashable.
5. Tuples can be set elements if all their contents are hashable.
6. Sets are mutable, but their elements must be hashable.
7. A set can contain different data types.
8. Use `set()` to create an empty set.
9. Use `in` and `not in` to check membership.
10. Use `frozenset()` when an immutable set is required.

### Example: Invalid Set Element

```python
# This raises a TypeError because a list is unhashable.
my_set = {[1, 2], [3, 4]}
```

### Example: Valid Tuple Element

```python
my_set = {(1, 2), (3, 4)}
print(my_set)
```

---

## 13. Practical Example: Removing Duplicates from a List

Sets are useful when we want to remove duplicate values.

```python
numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = set(numbers)

print(unique_numbers)
```

**Output:** The set contains only `1`, `2`, `3`, `4`, and `5`.

If you need a list again:

```python
unique_list = list(set(numbers))
print(unique_list)
```

**Note:** The original list's order is not guaranteed to be preserved when converting through a set. To remove duplicates while preserving order, use:

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(dict.fromkeys(numbers))

print(unique_numbers)
```

**Output:**

```text
[1, 2, 3, 4, 5]
```

---

## 14. Advantages of Sets

- Automatically remove duplicate elements.
- Quickly check whether an element exists in a set.
- Perform union, intersection, and difference operations conveniently.
- Useful for comparing collections of unique items.

## 15. Limitations of Sets

- Do not support indexing or slicing.
- Do not guarantee a fixed iteration order.
- Cannot contain unhashable elements such as lists or dictionaries.
- Are unsuitable when duplicates or positional order are important.

---

## 16. Practice Questions

1. Create a set containing five numbers.
2. Remove duplicate values from a list using a set.
3. Add an element to a set using `add()`.
4. Add multiple elements using `update()`.
5. Remove an element using both `remove()` and `discard()`.
6. Find the union of two sets.
7. Find the intersection of two sets.
8. Find the difference between two sets.
9. Find the symmetric difference between two sets.
10. Check whether one set is a subset of another.
11. Check whether two sets are disjoint.
12. Create a frozenset and explain why its elements cannot be changed.

---

## Conclusion

Sets in Python are useful when we need a collection of unique elements and want to perform operations such as union, intersection, and difference. Remember that sets are unordered, mutable, and do not support indexing. Use a frozenset when an immutable set is needed.

