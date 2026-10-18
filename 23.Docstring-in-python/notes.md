
# Docstrings in Python

## 1. What Are Docstrings?

A **docstring** (Documentation String) is a string literal used to describe the purpose of a Python module, function, method, or class.

A docstring is written immediately after the definition of a function, class, or module.

Docstrings are usually written using triple quotes (`""" """` or `''' '''`).

## 2. Example of a Docstring

```python
def square(n):
    '''Takes in a number n and returns the square of n.'''
    print(n ** 2)

square(5)
```

### Output

```text
25
```

### Explanation

- `def square(n):` defines a function.
- The triple-quoted string is the docstring.
- `print(n ** 2)` prints the square of the number.
- `square(5)` calls the function with the value `5`.

**Note:** The docstring does not appear in the output automatically. It describes the function.

## 3. A Detailed Docstring Example

Docstrings can contain detailed information about a function, including its parameters, return value, and examples.

```python
def add(num1, num2):
    """
    Add two numbers.

    Parameters
    ----------
    num1 : int
        The first number.
    num2 : int
        The second number.

    Returns
    -------
    int
        The sum of the two numbers.

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(10, -10)
    0
    """
    return num1 + num2

print(add(2, 2))
```

### Output

```text
4
```

### Explanation

- **Parameters:** Describe the inputs given to the function.
- **Returns:** Describes the value returned by the function.
- **Examples:** Shows examples of how to use the function.

## 4. Python Comments vs Docstrings

### Comments

Comments are used to explain code and help programmers understand its purpose.

Comments begin with the `#` symbol.

```python
# This function calculates the square of a number
def square(n):
    return n ** 2
```

Python ignores comments during execution.

### Docstrings

Docstrings describe the purpose and functionality of modules, functions, methods, and classes.

```python
def square(n):
    """Returns the square of a number."""
    return n ** 2
```

Docstrings are stored by Python and can be accessed using the `__doc__` attribute.

### Difference Between Comments and Docstrings

| Comments | Docstrings |
|---|---|
| Begin with `#`. | Usually written using triple quotes. |
| Explain particular lines or sections of code. | Document modules, functions, methods, and classes. |
| Ignored by the Python interpreter. | Stored as documentation on the object. |
| Cannot be accessed through `__doc__`. | Can be accessed through `__doc__`. |

## 5. The `__doc__` Attribute

The `__doc__` attribute is used to access the docstring of a module, function, method, or class.

### Example

```python
def square(n):
    '''Takes in a number n and returns the square of n.'''
    return n ** 2

print(square.__doc__)
```

### Output

```text
Takes in a number n and returns the square of n.
```

### Explanation

- `square.__doc__` retrieves the docstring of the `square()` function.
- It displays the documentation written inside the triple quotes.

## 6. Important Points to Remember

1. Docstring stands for Documentation String.
2. Docstrings explain the purpose of modules, functions, methods, and classes.
3. A docstring must be the first statement inside the function, class, or module to be recognized as its docstring.
4. Triple quotes (`""" """` or `''' '''`) are commonly used for docstrings.
5. A docstring does not automatically appear in the program output.
6. The `__doc__` attribute can be used to access a docstring.
7. Docstrings can describe parameters, return values, and usage examples.
8. Comments and docstrings serve different purposes.

## Conclusion

Docstrings make Python code easier to understand and maintain. They provide documentation about what a function, class, method, or module does. The `__doc__` attribute allows us to access this documentation.
