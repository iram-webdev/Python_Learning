# Recursion in Python

Recursion is the process of defining something in terms of itself.

## Python Recursive Function

In Python, we know that a function can call other functions. It is even possible for a function to call itself. These types of constructs are termed recursive functions.

## Example

```python
def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)

# Driver Code
num = 7
print("Number:", num)
print("Factorial:", factorial(num))
```

## Output

```text
Number: 7
Factorial: 5040
```


# PEP 8 in Python

## 1. What Is PEP 8?

**PEP 8** is the official style guide for Python code. It provides guidelines and best practices for writing readable and consistent Python programs.

PEP 8 was written by Guido van Rossum, Barry Warsaw, and Nick Coghlan.

The main goal of PEP 8 is to make Python code easier to read and maintain.

### What Does PEP Stand For?

PEP stands for **Python Enhancement Proposal**.

A PEP is a document that describes proposed changes, new features, or guidelines related to Python.

## 2. Why Do We Use PEP 8?

PEP 8 helps programmers:

- Write clean and readable code.
- Maintain consistent coding styles.
- Make code easier to understand.
- Work more easily with other programmers.
- Maintain and improve programs.

## 3. Important PEP 8 Guidelines

### 1. Use Meaningful Variable Names

Variable names should clearly describe their purpose.

```python
# Good
student_name = "Iram"

# Not recommended
x = "Iram"
```

### 2. Use Proper Spacing

Use spaces around operators to improve readability.

```python
# Good
total = 10 + 20

# Not recommended
total=10+20
```

### 3. Use Four Spaces for Indentation

Python code blocks should normally use four spaces for each indentation level.

```python
if age >= 18:
    print("You are an adult.")
```

### 4. Use `snake_case` for Variables and Functions

In Python, variable and function names are generally written in lowercase with underscores between words.

```python
student_age = 20

def calculate_sum():
    pass
```

### 5. Use `PascalCase` for Class Names

Class names should generally start each word with a capital letter.

```python
class StudentDetails:
    pass
```

### 6. Use Comments Where Necessary

Comments should explain important or unclear parts of the code.

```python
# Calculate the total price
total_price = price * quantity
```

### 7. Keep Lines a Reasonable Length

PEP 8 recommends limiting most lines to 79 characters to keep code readable.

## 4. The Zen of Python

The **Zen of Python** is a collection of guiding principles for writing Python code.

It was written by Tim Peters and contains 19 aphorisms, with one additional principle famously left unwritten.

These principles encourage simplicity, readability, clarity, and good programming practices.

### The Zen of Python

```text
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## 5. Important Principles Explained

### 1. Explicit Is Better Than Implicit

Write code that clearly shows what it does.

### 2. Simple Is Better Than Complex

Prefer simple solutions over unnecessarily complicated ones.

### 3. Readability Counts

Code should be easy for other programmers to understand.

### 4. Errors Should Never Pass Silently

Handle errors properly instead of ignoring them without a reason.

### 5. Flat Is Better Than Nested

Avoid deeply nested code when a simpler structure can solve the problem.

### 6. There Should Be One Obvious Way to Do It

Prefer clear, consistent solutions that are easy to understand.

## 6. Easter Egg: `import this`

Python has a built-in Easter egg that displays the Zen of Python.

### Example

```python
import this
```

### Output

Running this code displays the Zen of Python in the terminal.

**Note:** An Easter egg is a hidden or playful feature included in software.

## 7. Important Points to Remember

1. PEP stands for Python Enhancement Proposal.
2. PEP 8 is the Python style guide.
3. PEP 8 improves code readability and consistency.
4. PEP 8 was written by Guido van Rossum, Barry Warsaw, and Nick Coghlan.
5. The Zen of Python was written by Tim Peters.
6. The Zen of Python contains 19 aphorisms.
7. `import this` displays the Zen of Python.
8. PEP 8 provides style recommendations; it is not a requirement that every Python program must follow every recommendation exactly.

## Conclusion

PEP 8 helps programmers write clean, consistent, and readable Python code. The Zen of Python provides useful principles for making code simple, clear, and easy to maintain.
