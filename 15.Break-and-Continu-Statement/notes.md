
# Break and Continue Statements in Python

## 1. `break` Statement

The `break` statement is used to **stop a loop immediately**, even if the loop condition is still `True`.

### Syntax
```python
break
```

### Example
```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
```

**Output:**
```text
1
2
```

**Explanation:** When `i` becomes `3`, the loop stops immediately.

---

## 2. `continue` Statement

The `continue` statement is used to **skip the current iteration** and move to the next iteration of the loop.

### Syntax
```python
continue
```

### Example
```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

**Output:**
```text
1
2
4
5
```

**Explanation:** When `i` becomes `3`, that iteration is skipped, but the loop continues.

---

## Difference Between `break` and `continue`

| `break` | `continue` |
|---|---|
| Stops the entire loop. | Skips only the current iteration. |
| No further iterations execute. | The next iteration starts. |
| Used to exit a loop. | Used to skip specific values or cases. |

## Important Points

- Both statements are commonly used with `for` and `while` loops.
- `break` terminates the loop immediately.
- `continue` skips the remaining statements in the current iteration.
