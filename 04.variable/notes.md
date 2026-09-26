# Day 6 - Variables and Data Types

## What is a Variable?

A variable is like a container that holds data. Very similar to how our containers in the kitchen hold sugar, salt, etc.

Creating a variable is like creating a placeholder in memory and assigning it some value.

In Python, it is as easy as writing:

```python
a = 1
b = True
c = "Harry"
d = None
```

These are four variables of different data types.

---

## What is a Data Type?

A data type specifies the type of value a variable holds. This is required in programming to perform various operations without causing an error.

In Python, we can print the type of any variable using the `type()` function:

```python
a = 1
print(type(a))

b = "1"
print(type(b))
```

**Output:**

```text
<class 'int'>
<class 'str'>
```

By default, Python provides the following built-in data types:

---

## 1. Numeric Data: `int`, `float`, `complex`

### `int`

Integer numbers are whole numbers, including positive, negative, and zero.

**Examples:**

```python
3
-8
0
```

### `float`

Float represents decimal numbers.

**Examples:**

```python
7.349
-9.0
0.0000001
```

### `complex`

Complex numbers contain a real part and an imaginary part.

**Example:**

```python
6 + 2j
```

> **Note:** In Python, complex numbers use `j`, not `i`.

---

## 2. Text Data: `str`

`str` stands for **String**.

It is used to store text or a sequence of characters.

**Examples:**

```python
"Hello World!!!"
"Python Programming"
```

---

## 3. Boolean Data: `bool`

Boolean data consists of two values:

```python
True
False
```

**Example:**

```python
is_student = True
is_teacher = False
```

---

## 4. Sequenced Data: `list`, `tuple`

### List

A list is an ordered collection of data with elements separated by commas and enclosed within square brackets `[]`.

Lists are **mutable**, which means they can be modified after creation.

**Example:**

```python
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]

print(list1)
```

**Output:**

```text
[8, 2.3, [-4, 5], ['apple', 'banana']]
```

### Tuple

A tuple is an ordered collection of data with elements separated by commas and enclosed within parentheses `()`.

Tuples are **immutable**, which means they cannot be modified after creation.

**Example:**

```python
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))

print(tuple1)
```

**Output:**

```text
(('parrot', 'sparrow'), ('Lion', 'Tiger'))
```

---

## 5. Mapped Data: `dict`

### Dictionary

A dictionary is a collection of data containing **key-value pairs**.

The key-value pairs are enclosed within curly brackets `{}`.

**Example:**

```python
dict1 = {
    "name": "Sakshi",
    "age": 20,
    "canVote": True
}

print(dict1)
```

**Output:**

```text
{'name': 'Sakshi', 'age': 20, 'canVote': True}
```

---

## Quick Revision

| Data Type | Example | Used For |
|---|---|---|
| `int` | `10` | Whole numbers |
| `float` | `10.5` | Decimal numbers |
| `complex` | `6 + 2j` | Complex numbers |
| `str` | `"Hello"` | Text |
| `bool` | `True` | True/False |
| `list` | `[1, 2, 3]` | Ordered, changeable collection |
| `tuple` | `(1, 2, 3)` | Ordered, unchangeable collection |
| `dict` | `{"name": "Sakshi"}` | Key-value data |