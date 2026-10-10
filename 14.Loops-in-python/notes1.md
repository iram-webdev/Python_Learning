
# Loops in Python

## 1. Introduction

Loops in Python are used to execute a block of code repeatedly.

They help us avoid writing the same code multiple times.

For example, instead of writing five separate `print()` statements, we can use a loop to print a message five times.

### Types of Loops in Python

Python provides two main types of loops:

1. `for` loop
2. `while` loop

Python also supports nested loops, in which one loop is placed inside another loop.

---

## 2. for Loop

### Definition

A `for` loop is used to iterate over a sequence, such as a string, list, tuple, or range of numbers.

### Syntax

```python
for variable in sequence:
    # Code to execute
```

### Example 1: Print Numbers

```python
for i in range(1, 6):
    print(i)
```

### Output

```text
1
2
3
4
5
```

### Explanation

- `range(1, 6)` generates numbers from 1 to 5.
- The variable `i` takes each value one by one.
- The `print()` statement displays each value.

**Note:** The ending value in `range()` is excluded.

### Example 2: Iterate Over a String

```python
name = "Python"

for character in name:
    print(character)
```

### Output

```text
P
y
t
h
o
n
```

### Example 3: Iterate Over a List

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

### Output

```text
Apple
Banana
Mango
```

---

## 3. while Loop

### Definition

A `while` loop repeatedly executes a block of code as long as the given condition is `True`.

### Syntax

```python
while condition:
    # Code to execute
```

### Example 1: Print Numbers

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

### Output

```text
1
2
3
4
5
```

### Explanation

1. Initially, `i = 1`.
2. Python checks whether `i <= 5`.
3. If the condition is `True`, the number is printed.
4. `i += 1` increases the value of `i` by 1.
5. The loop stops when `i` becomes 6.

**Important:** Always ensure that the loop condition eventually becomes `False`, unless an infinite loop is intentional.

### Example 2: Countdown

```python
count = 5

while count >= 1:
    print(count)
    count -= 1

print("Time's up!")
```

### Output

```text
5
4
3
2
1
Time's up!
```

---

## 4. The range() Function

### Definition

The `range()` function generates a sequence of integers. It is commonly used with `for` loops.

### Syntax

```python
range(start, stop, step)
```

- `start`: Starting value; defaults to 0 when omitted.
- `stop`: Ending boundary, which is excluded.
- `step`: Difference between consecutive values; defaults to 1.

### Example 1: range(stop)

```python
for i in range(5):
    print(i)
```

### Output

```text
0
1
2
3
4
```

### Example 2: range(start, stop)

```python
for i in range(2, 7):
    print(i)
```

### Output

```text
2
3
4
5
6
```

### Example 3: range(start, stop, step)

```python
for i in range(2, 11, 2):
    print(i)
```

### Output

```text
2
4
6
8
10
```

### Example 4: Reverse Counting

```python
for i in range(5, 0, -1):
    print(i)
```

### Output

```text
5
4
3
2
1
```

**Note:** The step can be negative to generate a decreasing sequence.

---

## 5. Nested Loops

### Definition

A nested loop is a loop placed inside another loop.

The inner loop executes for each iteration of the outer loop, unless control flow changes this behavior.

### Example

```python
for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)
```

### Output

```text
1 1
1 2
2 1
2 2
3 1
3 2
```

### Explanation

- The outer loop runs with `i = 1, 2, 3`.
- For every outer iteration, the inner loop runs with `j = 1, 2`.
- Therefore, six pairs are printed.

### Example: Star Pattern

```python
for i in range(1, 5):
    print("*" * i)
```

### Output

```text
*
**
***
****
```

---

## 6. break Statement

### Definition

The `break` statement immediately terminates the nearest enclosing loop.

### Example

```python
for i in range(1, 6):
    if i == 4:
        break
    print(i)
```

### Output

```text
1
2
3
```

### Explanation

When `i` becomes 4, the `break` statement terminates the loop. Therefore, 4 and 5 are not printed.

---

## 7. continue Statement

### Definition

The `continue` statement skips the remaining statements in the current iteration and moves to the next iteration of the loop.

### Example

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

### Output

```text
1
2
4
5
```

### Explanation

When `i` is 3, the `continue` statement skips `print(i)`. The loop then continues with the next value.

---

## 8. pass Statement

### Definition

The `pass` statement does nothing. It is used as a placeholder when a statement is syntactically required but no action needs to be performed yet.

### Example

```python
for i in range(1, 6):
    if i == 3:
        pass
    print(i)
```

### Output

```text
1
2
3
4
5
```

### Explanation

The `pass` statement does not skip an iteration or terminate the loop. Execution continues normally.

---

## 9. Difference Between for and while Loops

| for Loop | while Loop |
|---|---|
| Iterates over a sequence or iterable. | Repeats while a condition is `True`. |
| Commonly used when iterating over items or a range. | Commonly used when repetition depends on a condition. |
| Often used when the sequence is known. | Often used when the stopping point depends on changing conditions. |
| Can iterate directly over strings and lists. | Requires a condition that controls repetition. |

---

## 10. Difference Between break, continue, and pass

| Statement | Purpose |
|---|---|
| `break` | Terminates the nearest enclosing loop. |
| `continue` | Skips to the next iteration of the nearest enclosing loop. |
| `pass` | Does nothing; execution continues normally. |

---

## 11. The else Clause in Loops

Python allows an `else` clause with both `for` and `while` loops.

The loop's `else` block executes when the loop finishes normally, but not when the loop is terminated by `break`.

### Example

```python
for i in range(1, 4):
    print(i)
else:
    print("Loop completed")
```

### Output

```text
1
2
3
Loop completed
```

### Example with break

```python
for i in range(1, 5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed")
```

### Output

```text
1
2
```

The `else` block does not execute because the loop ended with `break`.

---

## 12. Important Rules to Remember

1. Python has two main loop types: `for` and `while`.
2. A colon (`:`) is required after the loop statement.
3. Proper indentation is required inside a loop.
4. `range()` excludes its stop value.
5. `break` terminates the nearest enclosing loop.
6. `continue` skips the current iteration's remaining statements.
7. `pass` is a placeholder and does not change the loop's flow.
8. Nested loops contain one loop inside another.
9. A `while` loop needs a condition that controls its repetition.
10. A loop's `else` clause does not execute if the loop terminates through `break`.

---

## 13. Practice Questions

Try solving these questions yourself:

1. Print numbers from 1 to 10 using a `for` loop.
2. Print numbers from 10 to 1 using a `while` loop.
3. Print all even numbers from 1 to 50.
4. Calculate the sum of numbers from 1 to 100.
5. Print the multiplication table of a number.
6. Find the factorial of a number using a loop.
7. Reverse a string using a loop.
8. Count the vowels in a string.
9. Print a right-angled triangle star pattern.
10. Print numbers from 1 to 10, skipping 5 using `continue`.
11. Stop a loop when the value reaches 7 using `break`.
12. Use nested loops to print a multiplication table from 1 to 5.

---

## Conclusion

Loops are an essential part of Python programming. They help execute repetitive tasks efficiently and reduce code duplication.

The `for` loop is commonly used to iterate over sequences, while the `while` loop repeats as long as a condition remains `True`.

Understanding loops, nested loops, `range()`, `break`, `continue`, and `pass` provides a strong foundation for solving programming problems.
