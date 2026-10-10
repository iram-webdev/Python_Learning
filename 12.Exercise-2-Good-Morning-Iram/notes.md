
# Python Program: Greeting Based on Current Time

## Question

Create a Python program capable of greeting you with "Good Morning", "Good Afternoon", and "Good Evening". The program should use the `time` module to get the current hour.

---

## 1. Introduction

Python provides a built-in `time` module that allows us to work with time-related operations.

We can use the `time` module to get the current time and display an appropriate greeting based on the current hour.

For example:
- Morning: Good Morning!
- Afternoon: Good Afternoon!
- Evening: Good Evening!

---

## 2. Python Program

```python
import time

hour = int(time.strftime("%H"))

if hour < 12:
    print("Good Morning!")

elif hour < 17:
    print("Good Afternoon!")

else:
    print("Good Evening!")
```

---

## 3. Output

The output depends on the current hour when the program runs.

Example:

```text
Good Morning!
```

Other possible outputs:

```text
Good Afternoon!
```

```text
Good Evening!
```

---

## 4. Explanation of the Program

### Step 1: Import the time Module

```python
import time
```

The `import` statement imports Python's built-in `time` module.

It provides functions for working with time.

### Step 2: Get the Current Hour

```python
hour = int(time.strftime("%H"))
```

This statement gets the current hour and stores it in the variable `hour`.

- `time.strftime()` formats the current time as a string.
- `%H` represents the hour in 24-hour format (`00` to `23`).
- `int()` converts the returned string into an integer.
- The variable `hour` stores the resulting integer.

Example:

```python
hour = int("10")
print(hour)
print(type(hour))
```

Output:

```text
10
<class 'int'>
```

### Step 3: Use the if Statement

```python
if hour < 12:
    print("Good Morning!")
```

If the current hour is less than 12, the program prints `Good Morning!`.

### Step 4: Use the elif Statement

```python
elif hour < 17:
    print("Good Afternoon!")
```

If the first condition is false and the hour is less than 17, the program prints `Good Afternoon!`.

This covers the hours from 12:00 PM to 4:59 PM.

### Step 5: Use the else Statement

```python
else:
    print("Good Evening!")
```

If neither of the previous conditions is true, the program prints `Good Evening!`.

This covers the hours from 5:00 PM to 11:59 PM.

---

## 5. Understanding strftime()

### Definition

The `strftime()` function converts date and time information into a formatted string.

Its name stands for **string format time**.

### Syntax

```python
time.strftime(format)
```

### Example

```python
import time

current_hour = time.strftime("%H")
print(current_hour)
```

Possible output:

```text
10
```

The actual output depends on the current time.

**Important:** `strftime()` returns a string, so we use `int()` when we need to compare the hour numerically.

---

## 6. Important strftime() Format Codes

| Format Code | Meaning | Example |
|---|---|---|
| `%H` | Hour in 24-hour format | `14` |
| `%I` | Hour in 12-hour format | `02` |
| `%M` | Minutes | `35` |
| `%S` | Seconds | `09` |
| `%p` | AM or PM | `PM` |
| `%d` | Day of the month | `10` |
| `%m` | Month number | `10` |
| `%Y` | Four-digit year | `2026` |
| `%A` | Full weekday name | `Saturday` |
| `%B` | Full month name | `October` |

---

## 7. Example: Display the Current Time

```python
import time

current_time = time.strftime("%I:%M:%S %p")
print(current_time)
```

Possible output:

```text
10:35:09 AM
```

Explanation:

- `%I` displays the hour in 12-hour format.
- `%M` displays minutes.
- `%S` displays seconds.
- `%p` displays AM or PM.

---

## 8. Greeting Conditions

The program uses the following conditions:

| Condition | Greeting |
|---|---|
| `hour < 12` | Good Morning! |
| `hour < 17` after the first condition fails | Good Afternoon! |
| All previous conditions are false | Good Evening! |

### How the Conditions Work

1. Python checks the `if` condition first.
2. If it is `True`, the corresponding greeting is printed.
3. Otherwise, Python checks the `elif` condition.
4. If that condition is also `False`, the `else` block executes.

Only one greeting is printed because the program uses an `if-elif-else` chain.

---

## 9. Important Points to Remember

1. `time` is a built-in Python module.
2. Use `import time` to import the module.
3. `time.strftime("%H")` returns the current hour as a string.
4. `%H` uses the 24-hour clock, ranging from `00` to `23`.
5. `int()` converts a numeric string into an integer.
6. `if-elif-else` is used to select the appropriate greeting.
7. Python executes only the first matching branch.
8. The output depends on the current system time and timezone.
9. This example treats hours before 12 as morning, 12–16 as afternoon, and 17–23 as evening.
10. Hours from midnight to 5:59 AM will also produce `Good Morning!` in this program.

---

## 10. Practice Questions

1. Write a Python program to display the current hour using the `time` module.
2. Write a program to display the current time in 12-hour format.
3. Write a program to display the current date using `strftime()`.
4. Write a program to display the current day and month.
5. Modify the greeting program to display `Good Night!` after 9 PM.

---

## Conclusion

The `time` module helps us work with the current time in Python. The `strftime()` function extracts and formats time information, while `if-elif-else` selects the appropriate greeting based on the current hour.
