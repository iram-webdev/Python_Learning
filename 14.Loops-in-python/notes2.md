
# Do-While Loop in Python

## What is a Do-While Loop?

A **do-while loop** executes a block of code at least once, regardless of the condition. After executing the code, it checks the condition to decide whether to repeat the loop.

It is also known as an **exit-controlled loop** because the condition is checked at the end.

**Note:** Python does not have a built-in `do-while` loop, but we can emulate its behavior using a `while` loop and a `break` statement.

## How to Emulate a Do-While Loop in Python?

We can use `while True` to create a loop that continues until a `break` statement stops it.

### Example

```python
while True:
    number = int(input("Enter a positive number: "))
    print(number)

    if not number > 0:
        break
```

### Output

```text
Enter a positive number: 1
1
Enter a positive number: 4
4
Enter a positive number: -1
-1
```

### Explanation

1. `while True` creates a loop that continues indefinitely unless stopped.
2. The user enters a number, which is printed.
3. The condition `if not number > 0` checks whether the number is not positive.
4. If the number is zero or negative, `break` terminates the loop.
5. The loop body executes at least once because the condition to stop it is checked after the input and print statements.

## Important Points

- Python does not directly support a built-in do-while loop.
- A do-while loop executes its body at least once.
- We can emulate it using `while True` and `break`.
- The condition for stopping the loop is checked at the end of each iteration.
