# What are Strings?

In Python, anything that is enclosed between **single quotes (`' '`)** or **double quotes (`" "`)** is considered a **string**.

A string is a sequence of characters used to store text.

Strings can contain letters, numbers, symbols, and spaces.

---

## Example

```python
name = "Harry"

print("Hello, " + name)
```

### Output

```text
Hello, Harry
```

---

## Single Quotes and Double Quotes

It does not matter whether you enclose your string in **single quotes** or **double quotes**. The output remains the same.

### Example

```python
name1 = "Harry"
name2 = 'Harry'

print(name1)
print(name2)
```

### Output

```text
Harry
Harry
```

---

## Using Quotes Inside a String

Sometimes, we need to use quotation marks inside a string.

For example:

```text
He said, "I want to eat an apple".
```

We can use **single quotes** outside the string so that double quotes can be used inside.

### Example

```python
print('He said, "I want to eat an apple".')
```

### Output

```text
He said, "I want to eat an apple".
```

---

# Multiline Strings

If a string contains multiple lines, we can create it using **triple quotes** (`""" """`).

### Example

```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)
```

### Output

```text
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
```

---

# Accessing Characters of a String

In Python, a string is a sequence of characters.

Each character has an **index**, and indexing starts from **0**.

Square brackets `[]` are used to access individual characters of a string.

### Example

```python
name = "Harry"

print(name[0])
print(name[1])
```

### Output

```text
H
a
```

### String Indexing

For the string `"Harry"`:

| Character | H | a | r | r | y |
|---|---:|---:|---:|---:|---:|
| Index | 0 | 1 | 2 | 3 | 4 |

So:

```python
name[0]  # H
name[1]  # a
name[2]  # r
```

---

# Looping Through a String

We can loop through a string using a **`for` loop**.

### Example

```python
name = "Harry"

for character in name:
    print(character)
```

### Output

```text
H
a
r
r
y
```

The above code prints all the characters in the string **one by one**.

---

## Easy Trick to Remember

```text
String → Collection of characters
Index → Starts from 0
[] → Used to access characters
for loop → Used to go through characters one by one
```
