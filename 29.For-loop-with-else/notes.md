
# Python - `else` in Loop

As you have learned before, the `else` clause is used along with the `if` statement.

Python allows the `else` keyword to be used with `for` and `while` loops too. The `else` block appears after the body of the loop. The statements in the `else` block are executed after all iterations are completed. The program exits the loop only after the `else` block is executed.

## Syntax

```python
for counter in sequence:
    # Statements inside the for loop block
else:
    # Statements inside the else block
```

## Example

```python
for x in range(5):
    print("Iteration no {} in for loop".format(x + 1))
else:
    print("Else block in loop")

print("Out of loop")
```

## Output

```text
Iteration no 1 in for loop
Iteration no 2 in for loop
Iteration no 3 in for loop
Iteration no 4 in for loop
Iteration no 5 in for loop
Else block in loop
Out of loop
```
