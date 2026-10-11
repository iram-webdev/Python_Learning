
# Lists in Python

## 1. What is a List?

A **list** is a built-in data type in Python used to store multiple items in a single variable.

Lists are:
- **Ordered:** Items maintain their position.
- **Mutable:** Items can be changed after creation.
- **Allow duplicates:** The same value can appear multiple times.
- **Flexible:** A list can contain different data types.

### Example

```python
fruits = ["Apple", "Banana", "Mango"]
print(fruits)
```

**Output:**
```text
['Apple', 'Banana', 'Mango']
```

---

## 2. Creating a List

Lists are created using square brackets `[]`, with items separated by commas.

```python
numbers = [10, 20, 30, 40]
names = ["Iram", "Rahul", "Aman"]
mixed = [10, "Python", 3.5, True]
empty = []

print(numbers)
print(names)
print(mixed)
print(empty)
```

**Output:**
```text
[10, 20, 30, 40]
['Iram', 'Rahul', 'Aman']
[10, 'Python', 3.5, True]
[]
```

---

## 3. Accessing List Items (Indexing)

Indexing is used to access individual items in a list.

- Positive indexing starts from `0`.
- Negative indexing starts from `-1` at the end.

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits[0])
print(fruits[2])
print(fruits[-1])
print(fruits[-2])
```

**Output:**
```text
Apple
Mango
Orange
Mango
```

**Important:** Accessing an index that does not exist raises an `IndexError`.

---

## 4. Slicing a List

Slicing is used to access a portion of a list.

### Syntax

```python
list_name[start:stop:step]
```

- `start`: Starting index; included.
- `stop`: Ending index; excluded.
- `step`: Interval between items.

### Example

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])
```

**Output:**
```text
[20, 30, 40]
[10, 20, 30]
[30, 40, 50]
[50, 40, 30, 20, 10]
```

---

## 5. Modifying List Items

Lists are mutable, which means we can change their items after creation.

```python
fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange"

print(fruits)
```

**Output:**
```text
['Apple', 'Orange', 'Mango']
```

We can also replace multiple items using slicing.

```python
numbers = [10, 20, 30, 40]

numbers[1:3] = [200, 300]

print(numbers)
```

**Output:**
```text
[10, 200, 300, 40]
```

---

## 6. Adding and Removing List Items

Python allows us to add new items to a list and remove existing items.

### Adding Items

```python
fruits = ["Apple", "Banana"]

fruits.append("Mango")
print(fruits)
```

**Output:**
```text
['Apple', 'Banana', 'Mango']
```

### Removing Items

```python
fruits = ["Apple", "Banana", "Mango"]

fruits.remove("Banana")
print(fruits)
```

**Output:**
```text
['Apple', 'Mango']
```

**Important:** Lists can be modified after creation by adding, changing, or removing items.

---

## 7. Finding the Length of a List

The built-in `len()` function returns the number of items in a list.

```python
fruits = ["Apple", "Banana", "Mango"]

print(len(fruits))
```

**Output:**
```text
3
```

---

## 8. Checking Whether an Item Exists

The `in` operator checks whether an item exists in a list.

```python
fruits = ["Apple", "Banana", "Mango"]

print("Banana" in fruits)
print("Orange" in fruits)
```

**Output:**
```text
True
False
```

---

## 9. Looping Through a List

We can use a `for` loop to access each item in a list.

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

**Output:**
```text
Apple
Banana
Mango
```

We can also access list items using indexes.

```python
numbers = [10, 20, 30]

for i in range(len(numbers)):
    print(numbers[i])
```

**Output:**
```text
10
20
30
```

---

## 10. Sorting a List

Sorting arranges list items in a particular order.

```python
numbers = [40, 10, 30, 20]

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)
```

**Output:**
```text
[10, 20, 30, 40]
[40, 30, 20, 10]
```

**Important:** Sorting changes the original list.

---

## 11. List Concatenation and Repetition

### A. Concatenation (`+`)

Combines two lists into a new list.

```python
a = [1, 2]
b = [3, 4]

print(a + b)
```

**Output:**
```text
[1, 2, 3, 4]
```

### B. Repetition (`*`)

Repeats the items of a list.

```python
numbers = [1, 2]

print(numbers * 3)
```

**Output:**
```text
[1, 2, 1, 2, 1, 2]
```

---

## 12. List Comprehension

**List comprehension** is a concise way to create a new list using an expression and an iterable. It can also include an optional condition.

### Syntax

```python
new_list = [expression for item in iterable]
```

### Example 1: Squares of Numbers

```python
squares = [x * x for x in range(1, 6)]

print(squares)
```

**Output:**
```text
[1, 4, 9, 16, 25]
```

### Example 2: Even Numbers

```python
even = [x for x in range(1, 11) if x % 2 == 0]

print(even)
```

**Output:**
```text
[2, 4, 6, 8, 10]
```

List comprehension often makes code shorter than using a separate loop.

---

## 13. Nested Lists

A nested list is a list that contains another list as an item.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])
print(matrix[1][2])
```

**Output:**
```text
[1, 2, 3]
6
```

Here, `matrix[1][2]` accesses the item at index `2` of the inner list at index `1`.

---

## 14. Important Rules to Remember

- Lists are created using square brackets `[]`.
- List indexing starts at `0`.
- Negative indexing starts at `-1`.
- Lists are ordered and mutable.
- Lists allow duplicate values and mixed data types.
- List slicing accesses a portion of a list.
- Lists can be modified after creation.
- `len()` returns the number of items.
- The `in` operator checks whether an item exists.
- List comprehension provides a concise way to create lists.
- Accessing an invalid index raises an `IndexError`.

---

## 15. Practice Questions

Try solving these questions yourself.

1. Create a list of five numbers and print it.
2. Print the first and last items of a list.
3. Print the first three items using slicing.
4. Change an item in a list.
5. Add a new item to a list.
6. Remove an item from a list.
7. Find the length of a list.
8. Sort a list in ascending and descending order.
9. Create a list of squares from 1 to 10 using list comprehension.
10. Create a list containing only even numbers from 1 to 20.
11. Create a nested list and access an item inside it.
12. Combine two lists using concatenation.

---

## Conclusion

Lists are one of the most useful data structures in Python. They allow us to store, access, modify, and process multiple items efficiently.

**Recommended Next Topic:** Tuples in Python.
