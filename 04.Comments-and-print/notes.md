\# Day 5 - Comments, Escape Sequences \& Print in Python



Today I learned about:



\* Python Comments

\* Single-Line Comments

\* Multi-Line Comments

\* Escape Sequence Characters

\* `print()` Statement

\* Parameters of the `print()` Function



\---



\# 1. Python Comments



A \*\*comment\*\* is a part of the code that Python does not execute.



Comments are mainly used to:



\* Explain the code

\* Make code easier to understand

\* Temporarily prevent a line of code from executing

\* Help other programmers understand the program



\---



\## 1.1 Single-Line Comments



To write a single-line comment, use the `#` symbol at the beginning of the line.



\### Example 1



```python

\# This is a single-line comment



print("This is a print statement.")

```



\### Output



```text

This is a print statement.

```



The line starting with `#` is ignored by Python.



\---



\### Example 2



A comment can also be written after a statement.



```python

print("Hello World!!!")  # Printing Hello World

```



\### Output



```text

Hello World!!!

```



\---



\### Example 3



We can use a comment to temporarily stop a line from executing.



```python

print("Python Program")



\# print("Python Program")

```



\### Output



```text

Python Program

```



The second `print()` does not execute because it is commented out.



\---



\# 2. Multi-Line Comments



Multi-line comments can be written in different ways.



One simple way is to use `#` at the beginning of every line.



\### Example 1



```python

\# It will execute a block of code if a specified condition is true.

\# If the condition is false, it will execute another block of code.



p = 7



if p > 5:

&#x20;   print("p is greater than 5.")

else:

&#x20;   print("p is not greater than 5.")

```



\### Output



```text

p is greater than 5.

```



\---



\## Multi-Line String



Triple quotes (`""" """` or `''' '''`) can also be used to create a multi-line string.



\### Example 2



```python

"""

This is an if-else statement.

It checks whether p is greater than 5.

"""



p = 7



if p > 5:

&#x20;   print("p is greater than 5.")

else:

&#x20;   print("p is not greater than 5.")

```



\### Output



```text

p is greater than 5.

```



> \*\*Note:\*\* Triple-quoted text is technically a multi-line string, not a special comment syntax. It is commonly used for documentation and docstrings.



\---



\# 3. Escape Sequence Characters



An \*\*escape sequence\*\* is a special combination of characters that starts with a backslash (`\\`).



It is used to represent special characters or perform special formatting inside a string.



\## Important Escape Sequences



| Escape Sequence | Meaning      | Example                                                    |

| --------------- | ------------ | ---------------------------------------------------------- |

| `\\n`            | New Line     | `Hello\\nWorld` → Hello and World appear on different lines |

| `\\t`            | Tab Space    | `Hello\\tWorld` → Adds a tab space                          |

| `\\\\`            | Backslash    | `C:\\\\Python` → `C:\\Python`                                 |

| `\\'`            | Single Quote | `I\\'m` → `I'm`                                             |

| `\\"`            | Double Quote | `\\"Hello\\"` → `"Hello"`                                    |



\---



\## Example 1 - New Line (`\\n`)



```python

print("Hello\\nWorld")

```



\### Output



```text

Hello

World

```



`\\n` moves the text to a new line.



\---



\## Example 2 - Tab (`\\t`)



```python

print("Hello\\tWorld")

```



\### Output



```text

Hello    World

```



`\\t` adds a tab space.



\---



\## Example 3 - Backslash (`\\\\`)



```python

print("C:\\\\Python")

```



\### Output



```text

C:\\Python

```



`\\\\` is used when we want to print an actual backslash.



\---



\## Example 4 - Single Quote (`\\'`)



```python

print('I\\'m learning Python')

```



\### Output



```text

I'm learning Python

```



`\\'` allows us to use a single quote inside a string surrounded by single quotes.



\---



\## Example 5 - Double Quote (`\\"`)



```python

print("She said \\"Hello\\"")

```



\### Output



```text

She said "Hello"

```



`\\"` allows us to use double quotes inside a string surrounded by double quotes.



\---



\# 4. More on the `print()` Statement



The basic syntax of the `print()` function is:



```python

print(object(s), sep=separator, end=end, file=file, flush=flush)

```



The `print()` function is used to display output on the screen.



\### Simple Example



```python

print("Hello Python")

```



\### Output



```text

Hello Python

```



\---



\# 5. Parameters of the `print()` Function



\## 1. `object(s)`



The `object(s)` are the values that we want to print.



We can print one or more objects.



```python

print("Hello", "Python")

```



\### Output



```text

Hello Python

```



\---



\## 2. `sep`



`sep` means \*\*separator\*\*.



It specifies what should be placed between multiple objects.



The default separator is a space.



\### Example



```python

print("Hello", "Python", sep="-")

```



\### Output



```text

Hello-Python

```



\---



\## 3. `end`



`end` specifies what should be printed at the end of the `print()` statement.



The default value of `end` is a new line (`\\n`).



\### Example



```python

print("Hello", end=" ")

print("Python")

```



\### Output



```text

Hello Python

```



Normally, the first `print()` would move to the next line. Here, `end=" "` tells Python to add a space instead.



\---



\## 4. `file`



The `file` parameter specifies where the output should be written.



By default, the output is displayed on the screen.



For beginners, it is enough to remember:



```python

print("Hello")

```



prints the output on the screen by default.



