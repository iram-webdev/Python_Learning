
# Match-Case Statement in Python

## 1. Introduction

The `match-case` statement is used to compare a value against different patterns and execute the code associated with the first matching pattern.

It was introduced in **Python 3.10**.

In other programming languages, such as C, C++ and Java, a similar feature is known as `switch-case`.

Python does not have a `switch` keyword. Instead, it provides the `match-case` statement.

### Key Points

- `match` is used to check a value.
- `case` defines a pattern to match.
- `case _` acts as a default case in simple examples.
- Only the first matching case is executed.

---

## 2. Syntax

```python
match expression:
    case pattern1:
        # Code for pattern1

    case pattern2:
        # Code for pattern2

    case _:
        # Default case
```

### Explanation

- `match expression:` evaluates the expression.
- `case pattern1:` checks whether the value matches the first pattern.
- Additional `case` blocks can be added.
- `case _:` matches anything not matched by an earlier case.

---

## 3. Example 1: Match a Number

```python
number = 2

match number:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Invalid number")
```

### Output

```text
Two
```

### Explanation

The value of `number` is `2`.

Python checks the cases and finds that `case 2` matches. Therefore, it prints `Two`.

---

## 4. Example 2: Display the Day of the Week

```python
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")
```

### Output

```text
Wednesday
```

### Explanation

The value of `day` is `3`, so the program prints `Wednesday`.

If the value is outside the defined cases, `case _` executes.

---

## 5. Example 3: Simple Calculator

```python
a = 10
b = 5
operator = "+"

match operator:
    case "+":
        print("Result:", a + b)
    case "-":
        print("Result:", a - b)
    case "*":
        print("Result:", a * b)
    case "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid operator")
```

### Output

```text
Result: 15
```

### Explanation

The value of `operator` is `"+"`.

Therefore, the matching case adds `a` and `b` and prints the result.

The division case also checks that the divisor is not zero.

---

## 6. Example 4: Menu-Driven Program

```python
choice = 2

match choice:
    case 1:
        print("You selected Home")
    case 2:
        print("You selected Profile")
    case 3:
        print("You selected Settings")
    case 4:
        print("You selected Logout")
    case _:
        print("Invalid choice")
```

### Output

```text
You selected Profile
```

### Explanation

The value of `choice` is `2`, so the program executes `case 2`.

This approach is useful for menu-driven programs with fixed options.

---

## 7. Example 5: Match Multiple Values

Python allows multiple literal values to be matched using the `|` pattern.

```python
day = 6

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid day")
```

### Output

```text
Weekend
```

### Explanation

The `|` symbol in a pattern means that either value can match.

Since `day` is `6`, the program prints `Weekend`.

**Note:** Here, `|` is part of pattern matching. It is not the normal Boolean `or` keyword.

---

## 8. Example 6: Match a String

```python
command = "start"

match command:
    case "start":
        print("Program started")
    case "stop":
        print("Program stopped")
    case "pause":
        print("Program paused")
    case _:
        print("Unknown command")
```

### Output

```text
Program started
```

### Explanation

Python compares the value of `command` with each string pattern. Since the value is `"start"`, the first case matches.

String matching is case-sensitive. For example, `"Start"` and `"start"` are different strings.

---

## 9. Difference Between if-elif-else and match-case

| if-elif-else | match-case |
|---|---|
| Checks conditions that evaluate to True or False. | Matches values against patterns. |
| Useful for ranges and complex conditions. | Useful for fixed values and structured patterns. |
| Available in older Python versions. | Requires Python 3.10 or later. |
| Uses `if`, `elif` and `else`. | Uses `match` and `case`. |

### Example Using if-elif-else

```python
number = 2

if number == 1:
    print("One")
elif number == 2:
    print("Two")
else:
    print("Other")
```

### Equivalent Example Using match-case

```python
number = 2

match number:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Other")
```

Both programs print:

```text
Two
```

---

## 10. Important Rules

1. `match-case` was introduced in Python 3.10.
2. The `match` statement is followed by an expression and a colon.
3. Each `case` is followed by a pattern and a colon.
4. Indentation is required to define code blocks.
5. `case _` is commonly used as the default case.
6. Only the first matching case is executed.
7. Multiple values can be matched using the `|` pattern.
8. String patterns are case-sensitive.
9. Unlike a traditional C-style switch statement, Python's `match-case` does not use `break` between cases.
10. The `match-case` statement supports more than simple value comparisons; it can also match structured data and patterns.

---

## 11. Practice Questions

1. Write a program to display a month name using its number.
2. Write a program to create a calculator using `match-case`.
3. Write a program to display a day name using a number from 1 to 7.
4. Write a menu-driven program for addition, subtraction, multiplication and division.
5. Write a program to match commands such as `"start"`, `"stop"` and `"restart"`.
6. Write a program that matches multiple values using the `|` pattern.
7. Rewrite a simple `if-elif-else` program using `match-case`.

---

## Conclusion

The `match-case` statement is a useful feature in Python for matching values against patterns. It can make programs with multiple fixed choices easier to read and organize.

Use `if-elif-else` when checking ranges or general conditions, and consider `match-case` when matching specific values or structured patterns.
