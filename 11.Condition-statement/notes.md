
# Conditional Statements in Python

## Introduction

Conditional statements are used to make decisions in a program based on whether a condition is `True` or `False`.

Python provides the following types of conditional statements:

1. `if` statement
2. `if-else` statement
3. `if-elif-else` statement
4. Nested `if-else` statement

---

## 1. if Statement

### Definition
The `if` statement executes a block of code only when the given condition is `True`.

### Syntax

```python
if condition:
    # Code to execute if condition is True
```

### Example

```python
age = 20

if age >= 18:
    print("You are eligible to vote.")
```

### Output

```text
You are eligible to vote.
```

### Explanation
- The condition `age >= 18` is `True`.
- Therefore, the code inside the `if` block executes.
- If the condition is `False`, the block is skipped.

---

## 2. if-else Statement

### Definition
The `if-else` statement executes one block when the condition is `True` and another block when the condition is `False`.

### Syntax

```python
if condition:
    # Code if condition is True
else:
    # Code if condition is False
```

### Example

```python
number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

### Output

```text
Odd number
```

### Explanation
- The expression `7 % 2` returns `1`.
- Therefore, the condition is `False`.
- The `else` block executes and prints `Odd number`.

---

## 3. if-elif-else Statement

### Definition
The `if-elif-else` statement is used to check multiple conditions. Python executes the block of the first condition that evaluates to `True`.

### Syntax

```python
if condition1:
    # Code for condition1
elif condition2:
    # Code for condition2
elif condition3:
    # Code for condition3
else:
    # Code if all conditions are False
```

### Example

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")
```

### Output

```text
Grade B
```

### Explanation
- `marks >= 90` is `False`.
- `marks >= 75` is `True`.
- Python prints `Grade B` and skips the remaining branches.

### Important Points
- Multiple `elif` statements can be used.
- The `else` block is optional.
- The correct order is `if-elif-else`.
- Only the first matching branch executes.

---

## 4. Nested if-else Statement

### Definition
A nested conditional statement is a conditional statement placed inside another conditional statement.

It is useful when one decision depends on the result of another decision.

### Syntax

```python
if condition1:
    if condition2:
        # Code if both conditions are True
    else:
        # Code if condition1 is True
        # but condition2 is False
else:
    # Code if condition1 is False
```

### Example

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("You can enter.")
    else:
        print("Please bring your ID.")
else:
    print("You are underage.")
```

### Output

```text
You can enter.
```

### Explanation
1. The outer condition `age >= 18` is `True`.
2. Python enters the outer `if` block.
3. The inner condition `has_id` is also `True`.
4. Therefore, the output is `You can enter.`

### Important Points
- A conditional statement can be placed inside another conditional statement.
- Proper indentation is essential.
- Nested statements can contain `if`, `if-else`, or `if-elif-else` structures.

---

## Difference Between Conditional Statements

| Statement | Purpose |
|---|---|
| `if` | Executes code when a condition is `True`. |
| `if-else` | Chooses between two blocks of code. |
| `if-elif-else` | Checks multiple conditions. |
| Nested `if-else` | Checks a condition inside another condition. |

---

## Important Rules

1. Use a colon (`:`) after `if`, `elif`, and `else`.
2. Use proper indentation to define code blocks.
3. `elif` can be used multiple times.
4. `else` does not require a condition.
5. Conditions evaluate to `True` or `False`.
6. Python checks conditional branches from top to bottom.

---

## Practice Questions

1. Write a program to check whether a number is positive.
2. Write a program to check whether a number is even or odd.
3. Write a program to find the greatest of three numbers.
4. Write a program to assign grades based on marks.
5. Write a program to check voting eligibility using nested `if-else`.
6. Write a program to check whether a number is positive, negative, or zero.

---

## Conclusion

Conditional statements are an essential part of Python programming. They allow programs to make decisions and execute different blocks of code depending on specified conditions.
