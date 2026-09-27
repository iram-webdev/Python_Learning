# Operators

Python has different types of operators for different operations.

To create a calculator, we require **arithmetic operators**.

---

# Arithmetic Operators

Arithmetic operators are used to perform mathematical operations such as addition, subtraction, multiplication, and division.

| Operator | Operator Name | Example |
|---|---|---|
| `+` | Addition | `15 + 7` |
| `-` | Subtraction | `15 - 7` |
| `*` | Multiplication | `5 * 7` |
| `**` | Exponentiation | `5 ** 3` |
| `/` | Division | `5 / 3` |
| `%` | Modulus | `15 % 7` |
| `//` | Floor Division | `15 // 7` |

---

# Exercise

Let's create a simple calculator using arithmetic operators.

```python
n = 15
m = 7

ans1 = n + m
print("Addition of", n, "and", m, "is", ans1)

ans2 = n - m
print("Subtraction of", n, "and", m, "is", ans2)

ans3 = n * m
print("Multiplication of", n, "and", m, "is", ans3)

ans4 = n / m
print("Division of", n, "and", m, "is", ans4)

ans5 = n % m
print("Modulus of", n, "and", m, "is", ans5)

ans6 = n // m
print("Floor Division of", n, "and", m, "is", ans6)
```

## Output

```text
Addition of 15 and 7 is 22
Subtraction of 15 and 7 is 8
Multiplication of 15 and 7 is 105
Division of 15 and 7 is 2.142857142857143
Modulus of 15 and 7 is 1
Floor Division of 15 and 7 is 2
```

---

# Explanation

Here, `n` and `m` are two variables in which integer values are stored.

```python
n = 15
m = 7
```

The variables `ans1`, `ans2`, `ans3`, `ans4`, `ans5`, and `ans6` contain the results of different arithmetic operations.

| Variable | Operation | Result |
|---|---|---:|
| `ans1` | Addition | `22` |
| `ans2` | Subtraction | `8` |
| `ans3` | Multiplication | `105` |
| `ans4` | Division | `2.142857...` |
| `ans5` | Modulus | `1` |
| `ans6` | Floor Division | `2` |

---

## Important

### Modulus `%`

Modulus gives the **remainder** after division.

```python
15 % 7
```

**Output:**

```text
1
```

Because:

```text
15 ÷ 7 = 2 remainder 1
```

### Floor Division `//`

Floor division gives the **whole-number part of the division**.

```python
15 // 7
```

**Output:**

```text
2
```

### Exponentiation `**`

Exponentiation is used to calculate the power of a number.

```python
5 ** 3
```

**Output:**

```text
125
```

Because:

```text
5 × 5 × 5 = 125
```