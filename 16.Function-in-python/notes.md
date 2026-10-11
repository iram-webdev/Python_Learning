
# Functions in Python

## 1. What is a Function?

A **function** is a reusable block of code that performs a specific task. Instead of writing the same code repeatedly, we can define a function and call it whenever needed.

### Example

```python
def greet():
    print("Hello, Iram!")

greet()
greet()
```

**Output:**

```text
Hello, Iram!
Hello, Iram!
```

**Explanation:**

- `def` is the keyword used to define a function.
- `greet` is the function name.
- `()` contains parameters, if any.
- The indented code is the function body.
- `greet()` calls or executes the function.

**Important:** Defining a function does not execute its body. The function runs when it is called.

---

## 2. Syntax of a Function

```python
def function_name(parameters):
    # Function body
    statements
    return value
```

- `def`: Defines a function.
- `function_name`: Name of the function.
- `parameters`: Inputs accepted by the function; optional.
- `return`: Sends a result back to the caller; optional.

---

## 3. Types of Functions in Python

Python functions can be broadly classified into two categories.

### A. Built-in Functions

Built-in functions are already provided by Python. We can use them directly without defining them.

**Examples:** `print()`, `len()`, `max()`, `min()`, `sum()`, `type()`, `input()` and `range()`.

```python
print("Hello")
print(len("Python"))
print(max(10, 20, 30))
```

**Output:**

```text
Hello
6
30
```

### B. User-defined Functions

User-defined functions are created by programmers using the `def` keyword.

```python
def add():
    print(10 + 20)

add()
```

**Output:**

```text
30
```

---

## 4. Function Without Parameters

A function without parameters does not accept inputs through its parameter list.

```python
def welcome():
    print("Welcome to Python!")

welcome()
```

**Output:**

```text
Welcome to Python!
```

---

## 5. Function With Parameters

Parameters are variables written inside the parentheses when defining a function. They receive values when the function is called.

```python
def greet(name):
    print("Hello", name)

greet("Iram")
greet("Rahul")
```

**Output:**

```text
Hello Iram
Hello Rahul
```

### Parameter vs Argument

- **Parameter:** A variable in the function definition.
- **Argument:** An actual value passed when calling the function.

```python
def square(number):  # number is a parameter
    print(number * number)

square(5)  # 5 is an argument
```

**Output:**

```text
25
```

---

## 6. Function With a Return Statement

The `return` statement sends a result back to the place where the function was called.

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

**Output:**

```text
30
```

### Difference Between `print()` and `return`

- `print()` displays a value on the screen.
- `return` sends a value back so it can be stored, reused, or processed further.

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result * 2)
```

**Output:**

```text
16
```

**Important Points:**

- A function can return a value using `return`.
- A function can return multiple values, commonly as a tuple.
- Statements after an executed `return` are not run.
- If no value is explicitly returned, Python returns `None`.

---

## 7. Default Arguments

A default argument has a value assigned in the function definition. If the caller does not provide that argument, Python uses the default value.

```python
def greet(name="Friend"):
    print("Hello", name)

greet()
greet("Iram")
```

**Output:**

```text
Hello Friend
Hello Iram
```

Here, `"Friend"` is the default value of `name`.

---

## 8. Keyword Arguments

Keyword arguments pass values by specifying parameter names. Their order does not matter when all arguments are passed by keyword.

```python
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=20, name="Iram")
```

**Output:**

```text
Name: Iram
Age: 20
```

---

## 9. Positional Arguments

Positional arguments are assigned to parameters according to their position.

```python
def subtract(a, b):
    print(a - b)

subtract(10, 4)
```

**Output:**

```text
6
```

Here, `a = 10` and `b = 4`.

**Note:** The order matters for positional arguments.

---

## 10. Arbitrary Arguments: `*args`

Use `*args` when a function needs to accept any number of positional arguments.

```python
def add_numbers(*args):
    print(sum(args))

add_numbers(10, 20)
add_numbers(10, 20, 30, 40)
```

**Output:**

```text
30
100
```

**Important:** Inside the function, `args` is a tuple. The name `args` is conventional; the `*` enables this behavior.

---

## 11. Arbitrary Keyword Arguments: `**kwargs`

Use `**kwargs` when a function needs to accept any number of keyword arguments.

```python
def display_details(**kwargs):
    print(kwargs)

display_details(name="Iram", age=20, city="Patna")
```

**Output:**

```text
{'name': 'Iram', 'age': 20, 'city': 'Patna'}
```

**Important:** Inside the function, `kwargs` is a dictionary. The name `kwargs` is conventional; the `**` enables this behavior.

---

## 12. The `pass` Statement in a Function

The `pass` statement does nothing. It is useful as a placeholder when the function body has not been implemented yet.

```python
def my_function():
    pass

my_function()
```

**Output:** No output.

The program runs without an error because `pass` is a valid statement.

---

## 13. Local and Global Variables

### A. Local Variable

A variable created inside a function is generally local to that function.

```python
def show():
    message = "Hello Python"
    print(message)

show()
```

**Output:**

```text
Hello Python
```

The variable `message` is local to `show()`.

### B. Global Variable

A variable defined outside a function is a global variable.

```python
name = "Iram"

def show():
    print(name)

show()
print(name)
```

**Output:**

```text
Iram
Iram
```

### Using the `global` Keyword

The `global` keyword allows a function to reassign a global variable.

```python
count = 10

def update():
    global count
    count = 20

update()
print(count)
```

**Output:**

```text
20
```

**Note:** Use global variables carefully. Passing values through parameters and returning results often makes code easier to understand and test.

---

## 14. Docstrings in Python

A **docstring** is a string written at the beginning of a function body to describe what the function does.

```python
def square(number):
    """Return the square of a number."""
    return number * number

print(square(4))
print(square.__doc__)
```

**Output:**

```text
16
Return the square of a number.
```

Docstrings help document functions and can be accessed through the `__doc__` attribute.

---

## 15. Type Hints in Functions

Type hints indicate the expected types of parameters and return values. Python does not automatically enforce these types.

```python
def add(a: int, b: int) -> int:
    return a + b

print(add(5, 10))
```

**Output:**

```text
15
```

Here, `a: int` and `b: int` suggest integer inputs, while `-> int` suggests an integer return value.

---

## 16. Lambda Functions

A **lambda function** is a small anonymous function written using the `lambda` keyword. It contains a single expression.

### Syntax

```python
lambda arguments: expression
```

### Example

```python
square = lambda x: x * x

print(square(5))
```

**Output:**

```text
25
```

The same operation using a regular function:

```python
def square(x):
    return x * x

print(square(5))
```

**Output:**

```text
25
```

Lambda functions are useful for short expressions, but regular functions are usually clearer for complex logic.

---

## 17. Recursive Functions

A **recursive function** is a function that calls itself. It needs a **base case** to stop the recursion.

### Example: Factorial

The factorial of 5 is:

`5! = 5 × 4 × 3 × 2 × 1 = 120`

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
```

**Output:**

```text
120
```

**Explanation:**

- The base case returns `1` when `n` is `0` or `1`.
- Otherwise, the function calls itself with `n - 1`.
- The results are multiplied until the base case is reached.

**Important:** Without a proper base case, recursion may continue until Python raises a `RecursionError`.

---

## 18. Benefits of Functions

1. **Code reusability:** Write code once and call it many times.
2. **Modularity:** Divide a large program into smaller parts.
3. **Readability:** Make programs easier to understand.
4. **Maintainability:** Update logic in one place.
5. **Testing and debugging:** Test smaller units of code independently.

---

## 19. Important Rules to Remember

- Use `def` to define a regular function.
- A function executes when it is called.
- The function body must be indented.
- Parameters receive values through arguments.
- `return` sends a result back to the caller.
- A function without an explicit return value returns `None`.
- Default parameters must come after required parameters in a normal function definition.
- `*args` collects extra positional arguments into a tuple.
- `**kwargs` collects extra keyword arguments into a dictionary.
- A recursive function calls itself and needs a suitable stopping condition.
- Python also supports lambda functions for short expressions.

---

## 20. Practice Questions

Try solving these questions yourself.

1. Create a function that prints `"Hello, World!"`.
2. Create a function that takes two numbers and prints their sum.
3. Create a function that returns the square of a number.
4. Create a function that checks whether a number is even or odd.
5. Create a function that returns the largest of three numbers.
6. Create a function with a default parameter for a person's name.
7. Create a function that accepts any number of arguments and returns their sum.
8. Create a recursive function to calculate the factorial of a number.
9. Create a lambda function to calculate the cube of a number.
10. Write a function that returns both the sum and product of two numbers.

---

## Conclusion

Functions are an essential part of Python programming. They help us organize code, reuse logic, accept inputs, return results, and build larger programs efficiently.

**Recommended Next Topic:** Function arguments, return values, and scope in greater depth.
