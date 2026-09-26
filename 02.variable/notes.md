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
# Python Data Types

Python has **7 main categories of built-in data types**.

---

## 1. Numeric Data Types

Numeric data types are used to store numbers.

- `int` → Integer numbers
- `float` → Decimal numbers
- `complex` → Complex numbers

**Example:**

```python
age = 20
price = 99.5
z = 2 + 3j

print(age)
print(price)
print(z)
```

**Output:**

```text
20
99.5
(2+3j)
```

---

## 2. Sequence Data Types

Sequence data types are used to store multiple values in an **ordered manner**.

- `str` → String/Text
- `list` → Ordered and changeable collection
- `tuple` → Ordered and unchangeable collection
- `range` → Sequence of numbers

**Example:**

```python
name = "Iram"
marks = [80, 90, 85]
numbers = (1, 2, 3)
x = range(5)

print(name)
print(marks)
print(numbers)
print(x)
```

---

## 3. Mapping Data Type

Mapping data type stores data in **key-value pairs**.

- `dict` → Dictionary

**Example:**

```python
student = {
    "name": "Iram",
    "age": 20
}

print(student)
```

**Output:**

```text
{'name': 'Iram', 'age': 20}
```

Here:

- `"name"` is the **key**
- `"Iram"` is the **value**
- `"age"` is the **key**
- `20` is the **value**

---

## 4. Set Data Types

Set data types are used to store **unique values**.

Duplicate values are automatically removed.

- `set` → Mutable set
- `frozenset` → Immutable set

**Example:**

```python
numbers = {1, 2, 3, 4}

print(numbers)
```

**Output:**

```text
{1, 2, 3, 4}
```

---

## 5. Boolean Data Type

Boolean data type represents only **two values: `True` or `False`**.

- `bool` → Boolean value

**Example:**

```python
is_student = True
is_teacher = False

print(is_student)
print(is_teacher)
```

**Output:**

```text
True
False
```

---

## 6. Binary Data Types

Binary data types are used to store and work with **binary or raw data**.

- `bytes` → Immutable sequence of bytes
- `bytearray` → Mutable sequence of bytes
- `memoryview` → Provides access to the memory of binary data

**Example:**

```python
data = bytes([65, 66, 67])

numbers = bytearray([65, 66, 67])

print(data)
print(numbers)
```

**Output:**

```text
b'ABC'
bytearray(b'ABC')
```

---

## 7. None Type

`NoneType` represents the **absence of a value**.

- `NoneType` → No value

**Example:**

```python
result = None

print(result)
print(type(result))
```

**Output:**

```text
None
<class 'NoneType'>
```

`None` means that the variable currently does not contain any actual value.

---

# Quick Revision Table

| No. | Category | Data Types |
|---:|---|---|
| 1 | **Numeric** | `int`, `float`, `complex` |
| 2 | **Sequence** | `str`, `list`, `tuple`, `range` |
| 3 | **Mapping** | `dict` |
| 4 | **Set** | `set`, `frozenset` |
| 5 | **Boolean** | `bool` |
| 6 | **Binary** | `bytes`, `bytearray`, `memoryview` |
| 7 | **None** | `NoneType` |

---

## Easy Trick to Remember

**Numeric → Sequence → Mapping → Set → Boolean → Binary → None**

### Short Form:

**N → S → M → S → B → B → N**
