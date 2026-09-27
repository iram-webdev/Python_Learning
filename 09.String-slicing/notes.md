# String Slicing & Operations on String

---

# Length of a String

We can find the length of a string using the **`len()`** function.

## Example

```python
fruit = "Mango"

len1 = len(fruit)

print("Mango is a", len1, "letter word.")
```

## Output

```text
Mango is a 5 letter word.
```

---

# String as an Array

A string is a sequence of characters. Each character has an **index**, which allows us to access individual characters or parts of a string.

### Example

```python
pie = "ApplePie"

print(pie[:5])
print(pie[6])  # Returns the character at the specified index
```

## Output

```text
Apple
i
```

> **Note:** The method of specifying the start and end index to access a part of a string is called **slicing**.

---

# String Slicing

String slicing is used to access a specific part of a string.

### Syntax

```python
string[start:end]
```

- `start` → Starting index
- `end` → Ending index (**not included**)

## Slicing Example

```python
pie = "ApplePie"

print(pie[:5])      # Slicing from Start
print(pie[5:])      # Slicing till End
print(pie[2:6])     # Slicing in between
print(pie[-8:])     # Slicing using negative index
```

## Output

```text
Apple
Pie
pleP
ApplePie
```

---

# Understanding String Slicing

For the string:

```python
pie = "ApplePie"
```

The indexes are:

| Character | A | p | p | l | e | P | i | e |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Positive Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| Negative Index | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |

### Example

```python
print(pie[0:5])
```

Output:

```text
Apple
```

Here, index `0` is included, but index `5` is not included.

---

# Loop Through a String

Strings are sequences of characters and are **iterable**. Therefore, we can use a `for` loop to go through each character of a string.

## Example

```python
alphabets = "ABCDE"

for i in alphabets:
    print(i)
```

## Output

```text
A
B
C
D
E
```

The `for` loop prints each character of the string **one by one**.

---

# Quick Revision

| Operation | Example | Meaning |
|---|---|---|
| `len()` | `len("Mango")` | Finds the length of a string |
| `string[index]` | `pie[2]` | Accesses one character |
| `string[start:end]` | `pie[1:4]` | Slices a part of a string |
| `string[:end]` | `pie[:5]` | Slices from the beginning |
| `string[start:]` | `pie[5:]` | Slices until the end |
| `for` loop | `for i in pie:` | Goes through characters one by one |