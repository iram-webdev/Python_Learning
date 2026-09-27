# String Methods

Python provides a set of built-in methods that we can use to **modify, check, and work with strings**.

---

## 1. `upper()`

The `upper()` method converts all characters of a string to **uppercase**.

### Example

```python
str1 = "AbcDEfghIJ"

print(str1.upper())
```

### Output

```text
ABCDEFGHIJ
```

---

## 2. `lower()`

The `lower()` method converts all characters of a string to **lowercase**.

### Example

```python
str1 = "AbcDEfghIJ"

print(str1.lower())
```

### Output

```text
abcdefghij
```

---

## 3. `strip()`

The `strip()` method removes **whitespace from the beginning and end** of a string.

### Example

```python
str2 = " Silver Spoon "

print(str2.strip())
```

### Output

```text
Silver Spoon
```

---

## 4. `rstrip()`

The `rstrip()` method removes specified characters from the **end (right side)** of a string.

### Example

```python
str3 = "Hello !!!"

print(str3.rstrip("!"))
```

### Output

```text
Hello 
```

---

## 5. `replace()`

The `replace()` method replaces all occurrences of one string with another string.

### Example

```python
str2 = "Silver Spoon"

print(str2.replace("Sp", "M"))
```

### Output

```text
Silver Moon
```

---

## 6. `split()`

The `split()` method splits a string at the specified separator and returns the separated values as a **list**.

### Example

```python
str2 = "Silver Spoon"

print(str2.split(" "))
```

### Output

```text
['Silver', 'Spoon']
```

---

## 7. `capitalize()`

The `capitalize()` method converts the **first character** of a string to uppercase and converts the remaining characters to lowercase.

### Example

```python
str1 = "hello"

capStr1 = str1.capitalize()

print(capStr1)

str2 = "hello WorlD"

capStr2 = str2.capitalize()

print(capStr2)
```

### Output

```text
Hello
Hello world
```

---

## 8. `center()`

The `center()` method aligns a string to the **center** according to the specified width.

### Example

```python
str1 = "Welcome to the Console!!!"

print(str1.center(50))
```

### Output

```text
            Welcome to the Console!!!             
```

We can also provide a **padding character**.

### Example

```python
str1 = "Welcome to the Console!!!"

print(str1.center(50, "."))
```

### Output

```text
............Welcome to the Console!!!.............
```

---

## 9. `count()`

The `count()` method returns the number of times a specified value occurs in a string.

### Example

```python
str2 = "Abracadabra"

countStr = str2.count("a")

print(countStr)
```

### Output

```text
4
```

---

## 10. `endswith()`

The `endswith()` method checks whether a string **ends with** a specified value.

It returns `True` if the string ends with the given value; otherwise, it returns `False`.

### Example

```python
str1 = "Welcome to the Console !!!"

print(str1.endswith("!!!"))
```

### Output

```text
True
```

We can also check for a value within a specific range by providing the **start and end index**.

### Example

```python
str1 = "Welcome to the Console !!!"

print(str1.endswith("to", 4, 10))
```

### Output

```text
True
```

---

## 11. `find()`

The `find()` method searches for the **first occurrence** of a specified value and returns its index.

If the value is not found, it returns `-1`.

### Example

```python
str1 = "He's name is Dan. He is an honest man."

print(str1.find("is"))
```

### Output

```text
10
```

If the value is not present:

```python
str1 = "He's name is Dan. He is an honest man."

print(str1.find("Daniel"))
```

### Output

```text
-1
```

### `find()` vs `index()`

The main difference is:

- `find()` returns `-1` if the value is not found.
- `index()` raises a `ValueError` if the value is not found.

---

## 12. `index()`

The `index()` method searches for the **first occurrence** of a specified value and returns its index.

If the value is not found, it raises a `ValueError`.

### Example

```python
str1 = "He's name is Dan. Dan is an honest man."

print(str1.index("Dan"))
```

### Output

```text
13
```

If the value is not present:

```python
str1 = "He's name is Dan. Dan is an honest man."

print(str1.index("Daniel"))
```

### Output

```text
ValueError: substring not found
```

---

## 13. `isalnum()`

The `isalnum()` method returns `True` if the entire string contains only **letters (A-Z, a-z) and numbers (0-9)**.

If spaces, symbols, or punctuation are present, it returns `False`.

### Example

```python
str1 = "WelcomeToTheConsole"

print(str1.isalnum())
```

### Output

```text
True
```

---

## 14. `isalpha()`

The `isalpha()` method returns `True` if the entire string contains only **alphabetic characters**.

If numbers, spaces, or punctuation are present, it returns `False`.

### Example

```python
str1 = "Welcome"

print(str1.isalpha())
```

### Output

```text
True
```

---

## 15. `islower()`

The `islower()` method returns `True` if all cased characters in the string are lowercase.

Otherwise, it returns `False`.

### Example

```python
str1 = "hello world"

print(str1.islower())
```

### Output

```text
True
```

---

## 16. `isprintable()`

The `isprintable()` method returns `True` if all characters in the string are printable.

If the string contains non-printable characters, it returns `False`.

### Example

```python
str1 = "We wish you a Merry Christmas"

print(str1.isprintable())
```

### Output

```text
True
```

---

## 17. `isspace()`

The `isspace()` method returns `True` if the string contains only whitespace characters such as spaces or tabs.

Otherwise, it returns `False`.

### Example

```python
str1 = "        "

print(str1.isspace())

str2 = "\t"

print(str2.isspace())
```

### Output

```text
True
True
```

---

## 18. `istitle()`

The `istitle()` method returns `True` if the first letter of each word is uppercase and the remaining letters follow title-case rules.

Otherwise, it returns `False`.

### Example 1

```python
str1 = "World Health Organization"

print(str1.istitle())
```

### Output

```text
True
```

### Example 2

```python
str2 = "To kill a Mocking bird"

print(str2.istitle())
```

### Output

```text
False
```

---

## 19. `isupper()`

The `isupper()` method returns `True` if all cased characters in the string are uppercase.

Otherwise, it returns `False`.

### Example

```python
str1 = "WORLD HEALTH ORGANIZATION"

print(str1.isupper())
```

### Output

```text
True
```

---

## 20. `startswith()`

The `startswith()` method checks whether a string **starts with** a specified value.

It returns `True` if the string starts with the given value; otherwise, it returns `False`.

### Example

```python
str1 = "Python is an Interpreted Language"

print(str1.startswith("Python"))
```

### Output

```text
True
```

---

## 21. `swapcase()`

The `swapcase()` method changes the case of characters:

- Uppercase → Lowercase
- Lowercase → Uppercase

### Example

```python
str1 = "Python is an Interpreted Language"

print(str1.swapcase())
```

### Output

```text
pYTHON IS AN iNTERPRETED lANGUAGE
```

---

## 22. `title()`

The `title()` method converts the first character of each word to uppercase and the remaining characters to lowercase.

### Example

```python
str1 = "He's name is Dan. Dan is an honest man."

print(str1.title())
```

### Output

```text
He'S Name Is Dan. Dan Is An Honest Man.
```

---

# Quick Revision Table

| Method | Use |
|---|---|
| `upper()` | Converts string to uppercase |
| `lower()` | Converts string to lowercase |
| `strip()` | Removes whitespace from beginning and end |
| `rstrip()` | Removes characters from the right side |
| `replace()` | Replaces a string with another string |
| `split()` | Splits a string into a list |
| `capitalize()` | Capitalizes the first character |
| `center()` | Centers the string |
| `count()` | Counts occurrences of a value |
| `endswith()` | Checks the ending of a string |
| `find()` | Finds the first occurrence; returns `-1` if not found |
| `index()` | Finds the first occurrence; raises an error if not found |
| `isalnum()` | Checks for letters and numbers |
| `isalpha()` | Checks for alphabetic characters |
| `islower()` | Checks whether characters are lowercase |
| `isprintable()` | Checks whether characters are printable |
| `isspace()` | Checks whether string contains only whitespace |
| `istitle()` | Checks whether string is in title case |
| `isupper()` | Checks whether characters are uppercase |
| `startswith()` | Checks the beginning of a string |
| `swapcase()` | Swaps uppercase and lowercase |
| `title()` | Converts text to title case |