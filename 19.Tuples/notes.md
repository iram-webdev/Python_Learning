
# Tuples in Python

## 1. Introduction to Tuples

A tuple is a built-in data type in Python used to store multiple items in a single variable.

A tuple is:
- **Ordered:** Elements maintain their insertion order.
- **Immutable:** Elements cannot be changed after the tuple is created.
- **Allow duplicates:** The same element can appear multiple times.
- **Heterogeneous:** It can store different data types.
- **Indexed:** Elements can be accessed using their index.

### Example

```python
t = (10, 20, 30, 40)

print(t)
print(type(t))
```

**Output:**

```text
(10, 20, 30, 40)
<class 'tuple'>
```

---

## 2. Creating a Tuple

Tuples are commonly created using parentheses `()` with elements separated by commas.

### Example 1: Tuple with Multiple Elements

```python
t = (1, 2, 3, 4, 5)
print(t)
```

**Output:**

```text
(1, 2, 3, 4, 5)
```

### Example 2: Tuple with Different Data Types

```python
t = (10, "Python", 3.14, True)
print(t)
```

**Output:**

```text
(10, 'Python', 3.14, True)
```

### Example 3: Empty Tuple

An empty tuple contains no elements.

```python
t = ()
print(t)
print(type(t))
```

**Output:**

```text
()
<class 'tuple'>
```

### Example 4: Tuple Without Parentheses

Parentheses are optional in many tuple assignments. The commas create the tuple.

```python
t = 10, 20, 30

print(t)
print(type(t))
```

**Output:**

```text
(10, 20, 30)
<class 'tuple'>
```

---

## 3. Creating a Tuple with One Element

To create a single-element tuple, you must include a comma after the element.

### Correct Way

```python
t = (10,)

print(t)
print(type(t))
```

**Output:**

```text
(10,)
<class 'tuple'>
```

### Incorrect Way

```python
t = (10)

print(t)
print(type(t))
```

**Output:**

```text
10
<class 'int'>
```

**Important:** `(10)` is an integer, whereas `(10,)` is a tuple.

---

## 4. Accessing Tuple Elements (Indexing)

Indexing is used to access individual elements of a tuple.

Python uses zero-based indexing, which means the first element has index `0`.

Consider the following tuple:

```python
t = (10, 20, 30, 40, 50)
```

### Positive Indexing

| Element | Index |
|---|---:|
| 10 | 0 |
| 20 | 1 |
| 30 | 2 |
| 40 | 3 |
| 50 | 4 |

**Example:**

```python
t = (10, 20, 30, 40, 50)

print(t[0])
print(t[2])
print(t[4])
```

**Output:**

```text
10
30
50
```

### Negative Indexing

Negative indexing accesses elements from the end of a tuple.

- `-1` refers to the last element.
- `-2` refers to the second-last element.
- `-3` refers to the third-last element.

**Example:**

```python
t = (10, 20, 30, 40, 50)

print(t[-1])
print(t[-2])
print(t[-3])
```

**Output:**

```text
50
40
30
```

**Important:** Accessing an index outside the valid range raises an `IndexError`.

---

## 5. Tuple Slicing

Slicing is used to access a range of elements from a tuple.

### Syntax

```python
tuple[start:stop:step]
```

- `start`: Index where slicing begins; included.
- `stop`: Index where slicing ends; excluded.
- `step`: Number of positions to move each time.

### Example 1: Basic Slicing

```python
t = (10, 20, 30, 40, 50)

print(t[1:4])
```

**Output:**

```text
(20, 30, 40)
```

The element at index `4` is excluded.

### Example 2: Slicing from the Beginning

```python
t = (10, 20, 30, 40, 50)

print(t[:3])
```

**Output:**

```text
(10, 20, 30)
```

### Example 3: Slicing to the End

```python
t = (10, 20, 30, 40, 50)

print(t[2:])
```

**Output:**

```text
(30, 40, 50)
```

### Example 4: Using Step

```python
t = (10, 20, 30, 40, 50, 60)

print(t[::2])
```

**Output:**

```text
(10, 30, 50)
```

### Example 5: Reversing a Tuple Using Slicing

```python
t = (10, 20, 30, 40, 50)

print(t[::-1])
```

**Output:**

```text
(50, 40, 30, 20, 10)
```

**Important:** Slicing creates a new tuple; it does not modify the original tuple.

---

## 6. Immutability of Tuples

Tuples are immutable, which means their elements cannot be changed, added, or removed after creation.

### Example: Trying to Change an Element

```python
t = (10, 20, 30)

t[1] = 100

print(t)
```

**Output:**

```text
TypeError
```

Python raises a `TypeError` because tuple elements cannot be assigned new values.

### How to Create a Modified Tuple

You can create a new tuple using slicing or concatenation.

```python
t = (10, 20, 30)

new_t = t[:1] + (100,) + t[2:]

print(new_t)
```

**Output:**

```text
(10, 100, 30)
```

The original tuple remains unchanged.

**Important:** A tuple can contain a mutable object, such as a list. That inner list can be modified, even though the tuple's own elements cannot be reassigned.

---

## 7. Tuple Concatenation

Concatenation combines two or more tuples using the `+` operator.

### Example

```python
t1 = (1, 2, 3)
t2 = (4, 5, 6)

t3 = t1 + t2

print(t3)
```

**Output:**

```text
(1, 2, 3, 4, 5, 6)
```

The original tuples remain unchanged.

---

## 8. Tuple Repetition

The `*` operator repeats the elements of a tuple a specified number of times.

### Example

```python
t = (1, 2, 3)

print(t * 3)
```

**Output:**

```text
(1, 2, 3, 1, 2, 3, 1, 2, 3)
```

---

## 9. Checking Membership in a Tuple

The `in` and `not in` operators check whether an element exists in a tuple.

### Example 1: Using `in`

```python
t = (10, 20, 30, 40)

print(20 in t)
print(50 in t)
```

**Output:**

```text
True
False
```

### Example 2: Using `not in`

```python
t = (10, 20, 30, 40)

print(50 not in t)
```

**Output:**

```text
True
```

---

## 10. Iterating Through a Tuple

A `for` loop can be used to access each element of a tuple.

### Example

```python
t = (10, 20, 30, 40)

for item in t:
    print(item)
```

**Output:**

```text
10
20
30
40
```

### Iterating with Index

```python
t = ("Apple", "Banana", "Mango")

for i in range(len(t)):
    print(i, t[i])
```

**Output:**

```text
0 Apple
1 Banana
2 Mango
```

---

## 11. Important Tuple Methods

Python provides two built-in tuple methods: `count()` and `index()`.

### A. `count()`

The `count()` method returns the number of times a specified element appears in a tuple.

**Example:**

```python
t = (1, 2, 3, 2, 4, 2)

print(t.count(2))
```

**Output:**

```text
3
```

The element `2` appears three times.

### B. `index()`

The `index()` method returns the index of the first occurrence of a specified element.

**Example:**

```python
t = (10, 20, 30, 20, 40)

print(t.index(20))
```

**Output:**

```text
1
```

The first occurrence of `20` is at index `1`.

**Important:** If the specified element is absent, `index()` raises a `ValueError`.

---

## 12. Useful Built-in Functions for Tuples

The following are Python built-in functions, not tuple methods.

### A. `len()`

Returns the number of elements in a tuple.

```python
t = (10, 20, 30, 40)

print(len(t))
```

**Output:**

```text
4
```

### B. `max()`

Returns the largest element.

```python
t = (10, 50, 20, 40)

print(max(t))
```

**Output:**

```text
50
```

### C. `min()`

Returns the smallest element.

```python
t = (10, 50, 20, 40)

print(min(t))
```

**Output:**

```text
10
```

### D. `sum()`

Returns the sum of numeric elements.

```python
t = (10, 20, 30, 40)

print(sum(t))
```

**Output:**

```text
100
```

### E. `sorted()`

Returns a new list containing the sorted elements of a tuple.

```python
t = (40, 10, 30, 20)

result = sorted(t)

print(result)
print(t)
```

**Output:**

```text
[10, 20, 30, 40]
(40, 10, 30, 20)
```

**Important:** `sorted()` returns a list, not a tuple, and leaves the original tuple unchanged.

---

## 13. Tuple Packing and Unpacking

### A. Tuple Packing

Tuple packing means combining multiple values into a single tuple.

```python
student = "Iram", 21, "CSE"

print(student)
```

**Output:**

```text
('Iram', 21, 'CSE')
```

### B. Tuple Unpacking

Tuple unpacking assigns tuple elements to separate variables.

```python
student = ("Iram", 21, "CSE")

name, age, branch = student

print(name)
print(age)
print(branch)
```

**Output:**

```text
Iram
21
CSE
```

**Important:** The number of variables must match the number of elements being unpacked, unless extended unpacking with `*` is used.

---

## 14. Converting Other Data Types to a Tuple

The `tuple()` built-in function converts an iterable into a tuple.

### Example 1: List to Tuple

```python
lst = [1, 2, 3, 4]

t = tuple(lst)

print(t)
```

**Output:**

```text
(1, 2, 3, 4)
```

### Example 2: String to Tuple

```python
text = "Python"

t = tuple(text)

print(t)
```

**Output:**

```text
('P', 'y', 't', 'h', 'o', 'n')
```

---

## 15. Nested Tuples

A nested tuple is a tuple that contains another tuple as an element.

### Example

```python
t = ((1, 2), (3, 4), (5, 6))

print(t[0])
print(t[1][0])
```

**Output:**

```text
(1, 2)
3
```

- `t[0]` returns the first inner tuple.
- `t[1][0]` returns the first element of the second inner tuple.

---

## 16. Difference Between List and Tuple

| Feature | List | Tuple |
|---|---|---|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Mutability | Mutable | Immutable |
| Order | Ordered | Ordered |
| Duplicates | Allowed | Allowed |
| Indexing | Supported | Supported |
| Slicing | Supported | Supported |
| Methods | Many methods | Two methods: `count()` and `index()` |
| Adding elements | Methods such as `append()` | No direct append method |
| Removing elements | Methods such as `remove()` and `pop()` | No direct removal methods |
| Typical use | Data that may change | Data that should remain fixed |

### Example

```python
# List
lst = [1, 2, 3]
lst.append(4)
print(lst)

# Tuple
t = (1, 2, 3)
print(t)
```

**Output:**

```text
[1, 2, 3, 4]
(1, 2, 3)
```

---

## 17. When Should You Use a Tuple?

Use a tuple when:

1. You want to store an ordered collection of values that should not be reassigned.
2. You want to represent fixed records, such as coordinates or RGB values.
3. You want to return multiple values from a function.
4. You need an immutable sequence that can be used as a dictionary key, provided all its elements are hashable.

Example:

```python
coordinates = (10, 20)

print(coordinates[0])
print(coordinates[1])
```

**Output:**

```text
10
20
```

---

## 18. Important Points to Remember

1. A tuple is an ordered and immutable collection.
2. Tuples allow duplicate elements and different data types.
3. A single-element tuple requires a trailing comma.
4. Positive indexing starts from `0`; negative indexing starts from `-1`.
5. Slicing extracts a portion of a tuple.
6. `count()` counts occurrences of an element.
7. `index()` returns the first matching index.
8. `len()`, `max()`, `min()`, `sum()`, `sorted()`, and `tuple()` are built-in functions, not tuple methods.
9. Tuple concatenation uses `+`; repetition uses `*`.
10. Tuple unpacking assigns elements to separate variables.
11. A tuple can contain mutable objects, such as lists.
12. A tuple with only hashable elements can be used as a dictionary key.

---

## 19. Practice Questions

Try solving these questions without looking at the answers.

1. Create a tuple containing five integers.
2. Create an empty tuple and print its type.
3. Create a tuple containing only one element.
4. Access the third element of a tuple using indexing.
5. Access the last element using negative indexing.
6. Extract the first three elements using slicing.
7. Reverse a tuple using slicing.
8. Count how many times `2` appears in `(1, 2, 3, 2, 4, 2)`.
9. Find the index of `30` in `(10, 20, 30, 40)`.
10. Join two tuples using concatenation.
11. Repeat a tuple three times.
12. Check whether `50` exists in a tuple.
13. Print every element of a tuple using a `for` loop.
14. Convert a list into a tuple.
15. Unpack a tuple into three variables.
16. Explain why a tuple does not support `append()`.
17. Explain the difference between `count()` and `index()`.
18. What is the difference between `sorted(t)` and a list's `sort()` method?

---

## Conclusion

Tuples are useful when you need an ordered collection whose elements should not be reassigned. Understanding tuple creation, indexing, slicing, immutability, methods, packing, unpacking, and built-in functions will help you write better Python programs.
