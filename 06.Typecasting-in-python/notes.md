# Typecasting in Python

The conversion of one data type into another data type is known as **type casting** or **type conversion** in Python.

Python provides several built-in functions for type casting, such as:

`int()`, `float()`, `str()`, `ord()`, `hex()`, `oct()`, `tuple()`, `set()`, `list()`, `dict()`, etc.

---

# Types of Typecasting

There are **two types of typecasting** in Python:

1. **Explicit Typecasting**
2. **Implicit Typecasting**

---

## 1. Explicit Typecasting

The conversion of one data type into another data type **manually by the programmer** is called explicit typecasting.

It is performed using Python's built-in type conversion functions such as:

- `int()`
- `float()`
- `str()`
- `hex()`
- `oct()`

### Example of Explicit Typecasting

```python
string = "15"
number = 7

string_number = int(string)

sum = number + string_number

print("The Sum of both the numbers is:", sum)
```

### Output

```text
The Sum of both the numbers is: 22
```

### Explanation

Here:

```python
string = "15"
```

`"15"` is a **string**.

We convert it into an integer using:

```python
string_number = int(string)
```

Now `"15"` becomes `15`, so we can perform mathematical operations with it.

```text
"15" → int() → 15
```

---

## 2. Implicit Typecasting

When Python automatically converts one data type into another data type, it is called **implicit typecasting**.

The conversion is performed automatically by the **Python interpreter**.

Python generally converts a smaller or lower-precision data type to a higher-precision data type to avoid data loss.

### Example of Implicit Typecasting

```python
# Integer value
a = 7
print(type(a))

# Float value
b = 3.0
print(type(b))

# Python automatically converts the result to float
c = a + b

print(c)
print(type(c))
```

### Output

```text
<class 'int'>
<class 'float'>
10.0
<class 'float'>
```

### Explanation

Here:

```python
a = 7
```

`a` is an **integer (`int`)**.

```python
b = 3.0
```

`b` is a **float (`float`)**.

When we perform:

```python
c = a + b
```

Python automatically converts the integer `7` into a float:

```text
7 + 3.0 = 10.0
```

Therefore, `c` becomes a **float**.

---

# Difference Between Explicit and Implicit Typecasting

| Explicit Typecasting | Implicit Typecasting |
|---|---|
| Done manually by the programmer | Done automatically by Python |
| Programmer uses functions like `int()`, `float()`, `str()` | Python interpreter performs the conversion |
| Example: `int("15")` | Example: `7 + 3.0` |
| Programmer controls the conversion | Python controls the conversion |

---

## Easy Trick to Remember

**Explicit = I do it manually.**

```python
int("15")
```

**Implicit = Python does it automatically.**

```python
7 + 3.0
```