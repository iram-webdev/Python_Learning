
# F-String in Python

## 1. What is an F-String?

An **f-string** stands for **Formatted String Literal**.

In Python, an f-string is used to insert variables and expressions directly inside a string.

To create an f-string, write the letter `f` before the opening quotation mark and put variables inside curly braces `{}`.

### Syntax

```python
f"Text {variable}"
```

## 2. Why Do We Use F-Strings?

F-strings are used to:

- Insert variables into a string.
- Display the values of variables.
- Perform calculations inside a string.
- Make code simple and readable.

## 3. Example: Using a Variable

```python
name = "Iram"

print(f"My name is {name}")
```

**Output:**

```text
My name is Iram
```

**Explanation:** The value of `name` is inserted inside the string using `{name}`.

## 4. Example: Using Multiple Variables

```python
name = "Iram"
age = 21

print(f"My name is {name} and I am {age} years old.")
```

**Output:**

```text
My name is Iram and I am 21 years old.
```

**Explanation:** We can use multiple variables inside an f-string.

## 5. Example: Performing Calculations

We can also perform calculations inside curly braces `{}`.

```python
a = 10
b = 20

print(f"The sum of {a} and {b} is {a + b}")
```

**Output:**

```text
The sum of 10 and 20 is 30
```

**Explanation:** The expression `{a + b}` calculates the sum and displays the result.

## 6. Example: Taking User Input

```python
name = input("Enter your name: ")

print(f"Hello, {name}!")
```

**Output:**

```text
Enter your name: Iram
Hello, Iram!
```

**Explanation:** The name entered by the user is displayed in the message.

## 7. Example: Using F-Strings with Conditions

```python
marks = 85

if marks >= 40:
    print(f"You passed with {marks} marks.")
else:
    print(f"You failed with {marks} marks.")
```

**Output:**

```text
You passed with 85 marks.
```

## 8. F-String vs Normal String

### Without F-String

```python
name = "Iram"

print("My name is", name)
```

**Output:**

```text
My name is Iram
```

### With F-String

```python
name = "Iram"

print(f"My name is {name}")
```

**Output:**

```text
My name is Iram
```

Both produce the same output, but f-strings make it easier to combine text and variables in one string.

## 9. Important Points to Remember

1. F-string stands for Formatted String Literal.
2. Write `f` before the opening quotation mark.
3. Use curly braces `{}` to insert variables.
4. You can insert multiple variables into one f-string.
5. You can perform calculations inside `{}`.
6. F-strings make code easier to read.
7. F-strings are not necessary when printing only fixed text.
8. F-strings were introduced in Python 3.6.

## 10. Practice Questions

1. Create an f-string to display your name and age.
2. Use an f-string to display the sum of two numbers.
3. Take a user's name as input and print a welcome message.
4. Create an f-string to display the price of a product.
5. Write a program to display a student's name and marks using an f-string.

## Conclusion

F-strings provide a simple way to insert variables and expressions into strings in Python. They make programs shorter, cleaner, and easier to understand.




# F-String in Python

## 1. What is an F-String?

An **f-string** stands for **Formatted String Literal**.

In Python, an f-string is used to insert variables and expressions directly inside a string.

To create an f-string, write the letter `f` before the opening quotation mark and put variables inside curly braces `{}`.

### Syntax

```python
f"Text {variable}"
```

## 2. Why Do We Use F-Strings?

F-strings are used to:

- Insert variables into a string.
- Display the values of variables.
- Perform calculations inside a string.
- Make code simple and readable.

## 3. Example: Using a Variable

```python
name = "Iram"

print(f"My name is {name}")
```

**Output:**

```text
My name is Iram
```

**Explanation:** The value of `name` is inserted inside the string using `{name}`.

## 4. Example: Using Multiple Variables

```python
name = "Iram"
age = 21

print(f"My name is {name} and I am {age} years old.")
```

**Output:**

```text
My name is Iram and I am 21 years old.
```

**Explanation:** We can use multiple variables inside an f-string.

## 5. Example: Performing Calculations

We can also perform calculations inside curly braces `{}`.

```python
a = 10
b = 20

print(f"The sum of {a} and {b} is {a + b}")
```

**Output:**

```text
The sum of 10 and 20 is 30
```

**Explanation:** The expression `{a + b}` calculates the sum and displays the result.

## 6. Example: Taking User Input

```python
name = input("Enter your name: ")

print(f"Hello, {name}!")
```

**Output:**

```text
Enter your name: Iram
Hello, Iram!
```

**Explanation:** The name entered by the user is displayed in the message.

## 7. Example: Using F-Strings with Conditions

```python
marks = 85

if marks >= 40:
    print(f"You passed with {marks} marks.")
else:
    print(f"You failed with {marks} marks.")
```

**Output:**

```text
You passed with 85 marks.
```

## 8. F-String vs Normal String

### Without F-String

```python
name = "Iram"

print("My name is", name)
```

**Output:**

```text
My name is Iram
```

### With F-String

```python
name = "Iram"

print(f"My name is {name}")
```

**Output:**

```text
My name is Iram
```

Both produce the same output, but f-strings make it easier to combine text and variables in one string.

## 9. Important Points to Remember

1. F-string stands for Formatted String Literal.
2. Write `f` before the opening quotation mark.
3. Use curly braces `{}` to insert variables.
4. You can insert multiple variables into one f-string.
5. You can perform calculations inside `{}`.
6. F-strings make code easier to read.
7. F-strings are not necessary when printing only fixed text.
8. F-strings were introduced in Python 3.6.

## 10. Practice Questions

1. Create an f-string to display your name and age.
2. Use an f-string to display the sum of two numbers.
3. Take a user's name as input and print a welcome message.
4. Create an f-string to display the price of a product.
5. Write a program to display a student's name and marks using an f-string.

## Conclusion

F-strings provide a simple way to insert variables and expressions into strings in Python. They make programs shorter, cleaner, and easier to understand.
