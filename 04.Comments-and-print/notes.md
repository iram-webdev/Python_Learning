# Python Comments

A comment is a part of the coding file that the programmer does not want to execute. Rather, the programmer uses it to either explain a block of code or to avoid the execution of a specific part of code while testing.

## Single-Line Comments

To write a comment, just add a `#` at the start of the line.

### Example 1

```python
# This is a 'Single-Line Comment'
print("This is a print statement.")
```

**Output:**
```text
This is a print statement.
```

### Example 2

```python
print("Hello World !!!")  # Printing Hello World
```

**Output:**
```text
Hello World !!!
```

### Example 3

```python
print("Python Program")
# print("Python Program")
```

**Output:**
```text
Python Program
```

---

## Multi-Line Comments

To write multi-line comments, you can use `#` at each line or you can use a multiline string.

### Example 1: The use of `#`

```python
# It will execute a block of code if a specified condition is true.
# If the condition is false then it will execute another block of code.

p = 7

if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")
```

**Output:**
```text
p is greater than 5.
```

### Example 2: The use of Multiline String

```python
"""
This is an if-else statement.
It will execute a block of code if a specified condition is true.
If the condition is false then it will execute another block of code.
"""

p = 7

if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")
```

**Output:**
```text
p is greater than 5.
```

---

# Escape Sequence Characters

To insert characters that cannot be directly used in a string, we use an **escape sequence character**.

An escape sequence character is a backslash `\` followed by the character you want to insert.

An example of a character that cannot be directly used in a string is a double quote inside a string that is surrounded by double quotes.

### Example

```python
print("This doesnt "execute")
```

The above code gives an error because the double quote ends the string.

To solve this, we use `\"`.

```python
print("This will \" execute")
```

---

# More on Print Statement

The syntax of a print statement looks something like this:

```python
print(object(s), sep=separator, end=end, file=file, flush=flush)
```

## Other Parameters of Print Statement

| Parameter | Description |
|---|---|
| `object(s)` | Any object, and as many as you like. It will be converted to a string before being printed. |
| `sep='separator'` | Specifies how to separate the objects if there is more than one. Default is a space `' '`. |
| `end='end'` | Specifies what to print at the end. Default is `'\n'` (line feed). |
| `file` | An object with a write method. Default is `sys.stdout`. |
| `flush` | Specifies whether the output is forcibly flushed. |

### Example

```python
print("Hello", "World", sep="-")
```

**Output:**
```text
Hello-World
```

### Example of `end`

```python
print("Hello", end=" ")
print("World")
```

**Output:**
```text
Hello World
```
