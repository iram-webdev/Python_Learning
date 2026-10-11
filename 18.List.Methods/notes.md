
# List Methods in Python

## Introduction

In Python, list methods are built-in functions used to perform different operations on lists, such as adding, removing, sorting, and copying elements.

Example:

```python
lst = [1, 2, 3, 4]
```

## 1. `append()`

The `append()` method adds one element at the end of a list.

**Syntax:**

```python
list.append(element)
```

**Example:**

```python
lst = [1, 2, 3]
lst.append(4)

print(lst)
```

**Output:**

```text
[1, 2, 3, 4]
```

**Important:** `append()` adds only one element at a time.

---

## 2. `extend()`

The `extend()` method adds all elements from another iterable to the end of a list.

**Example:**

```python
lst = [1, 2, 3]
lst.extend([4, 5])

print(lst)
```

**Output:**

```text
[1, 2, 3, 4, 5]
```

**Difference between `append()` and `extend()`:**

```python
a = [1, 2]
a.append([3, 4])
print(a)

b = [1, 2]
b.extend([3, 4])
print(b)
```

**Output:**

```text
[1, 2, [3, 4]]
[1, 2, 3, 4]
```

---

## 3. `insert()`

The `insert()` method adds an element at a specific index.

**Syntax:**

```python
list.insert(index, element)
```

**Example:**

```python
lst = [10, 20, 40]
lst.insert(2, 30)

print(lst)
```

**Output:**

```text
[10, 20, 30, 40]
```

Here, `30` is inserted at index `2`.

---

## 4. `remove()`

The `remove()` method removes the first occurrence of a specified value.

**Example:**

```python
lst = [1, 2, 3, 2, 4]
lst.remove(2)

print(lst)
```

**Output:**

```text
[1, 3, 2, 4]
```

**Important:** If the value appears multiple times, only its first occurrence is removed. If the value is not present, Python raises a `ValueError`.

---

## 5. `pop()`

The `pop()` method removes and returns an element from a list.

- Without an index, it removes the last element.
- With an index, it removes the element at that index.

**Example 1: Without an index**

```python
lst = [10, 20, 30, 40]
lst.pop()

print(lst)
```

**Output:**

```text
[10, 20, 30]
```

**Example 2: With an index**

```python
lst = [10, 20, 30, 40]
lst.pop(1)

print(lst)
```

**Output:**

```text
[10, 30, 40]
```

Here, the element at index `1`, which is `20`, is removed.

---

## 6. `clear()`

The `clear()` method removes all elements from a list.

**Example:**

```python
lst = [1, 2, 3, 4]
lst.clear()

print(lst)
```

**Output:**

```text
[]
```

The list becomes empty.

---

## 7. `index()`

The `index()` method returns the index of the first occurrence of a specified value.

**Example:**

```python
lst = [10, 20, 30, 20]
print(lst.index(20))
```

**Output:**

```text
1
```

**Important:** Indexing starts from `0`. If the value is not found, Python raises a `ValueError`.

---

## 8. `count()`

The `count()` method returns how many times a value appears in a list.

**Example:**

```python
lst = [1, 2, 3, 1, 1, 4]
print(lst.count(1))
```

**Output:**

```text
3
```

Here, `1` appears three times.

---

## 9. `sort()`

The `sort()` method sorts the original list in ascending order by default.

**Example 1: Ascending order**

```python
lst = [5, 2, 8, 1, 4]
lst.sort()

print(lst)
```

**Output:**

```text
[1, 2, 4, 5, 8]
```

**Example 2: Descending order**

```python
lst = [5, 2, 8, 1, 4]
lst.sort(reverse=True)

print(lst)
```

**Output:**

```text
[8, 5, 4, 2, 1]
```

**Important:** `sort()` changes the original list and returns `None`.

---

## 10. `reverse()`

The `reverse()` method reverses the order of elements in the original list.

**Example:**

```python
lst = [1, 2, 3, 4]
lst.reverse()

print(lst)
```

**Output:**

```text
[4, 3, 2, 1]
```

**Important:** `reverse()` does not sort the list; it simply reverses its current order.

---

## 11. `copy()`

The `copy()` method creates a shallow copy of a list.

**Syntax:**

```python
new_list = original_list.copy()
```

**Example:**

```python
lst = [1, 2, 3, 6, 5, 4, 6, 1, 1]

new_lst = lst.copy()

print(lst)
print(new_lst)
```

**Output:**

```text
[1, 2, 3, 6, 5, 4, 6, 1, 1]
[1, 2, 3, 6, 5, 4, 6, 1, 1]
```

**Why use `copy()`?**

```python
lst = [1, 2, 3]
new_lst = lst.copy()

new_lst.append(4)

print(lst)
print(new_lst)
```

**Output:**

```text
[1, 2, 3]
[1, 2, 3, 4]
```

Changing the copied list does not change the original list when modifying top-level elements.

**Important:** `copy()` creates a shallow copy, not a deep copy.

---

## 12. `len()` — Built-in Function

`len()` is a built-in Python function, not a list method. It returns the number of elements in a list.

**Example:**

```python
lst = [10, 20, 30, 40]
print(len(lst))
```

**Output:**

```text
4
```

---

## Summary of List Methods

| Method | Use |
|---|---|
| `append()` | Adds one element at the end |
| `extend()` | Adds elements from an iterable |
| `insert()` | Adds an element at a specific index |
| `remove()` | Removes the first occurrence of a value |
| `pop()` | Removes and returns an element |
| `clear()` | Removes all elements |
| `index()` | Finds the index of the first occurrence |
| `count()` | Counts occurrences of a value |
| `sort()` | Sorts the original list |
| `reverse()` | Reverses the current order |
| `copy()` | Creates a shallow copy |

## Important Points

1. Lists are mutable, which means their elements can be changed.
2. List indexing starts from `0`.
3. `append()` adds one element, while `extend()` adds elements from an iterable.
4. `remove()` removes by value, while `pop()` removes by index (or the last element by default).
5. `sort()` changes the original list.
6. `reverse()` reverses the current order without sorting.
7. `copy()` creates a shallow copy.
8. `len()` is a built-in function, not a list method.
9. Methods such as `append()`, `sort()`, and `reverse()` modify the original list and return `None`.

## Practice Questions

1. Create a list and add `100` at the end using `append()`.
2. Add multiple elements using `extend()`.
3. Insert `50` at index `2`.
4. Remove the first occurrence of `1` from `[1, 2, 1, 3, 1]`.
5. Find how many times `6` appears in `[1, 6, 2, 6, 3, 6]`.
6. Sort `[8, 3, 1, 7, 2]` in descending order.
7. Reverse a list using `reverse()`.
8. Copy a list and add an element to the copied list. Check whether the original list changes.

---

## Conclusion

Python list methods make it easier to add, remove, search, sort, reverse, and copy list elements. Understanding these methods helps in writing clear and efficient Python programs.
