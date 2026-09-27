# Taking User Input in Python

In Python, we can take input directly from the user by using the **`input()`** function.

The `input()` function always returns the user input as a **string**. Therefore, we need to convert it into another data type when required.

---

## Syntax

```python
variable = input()
```

For example:

```python
name = input()
```

The user can enter a value, and that value will be stored in the `name` variable.

---

## Typecasting User Input

Since the `input()` function returns the value as a string, we can use **typecasting** when we need another data type.

### Integer Input

```python
variable = int(input())
```

### Float Input

```python
variable = float(input())
```

---

## Taking Input with a Message

We can also display a message inside the `input()` function.

This helps the user understand what they need to enter.

### Example

```python
a = input("Enter the name: ")

print(a)
```

### Output

```text
Enter the name: Harry
Harry
```

---

## Example with Integer Input

```python
age = int(input("Enter your age: "))

print("Your age is:", age)
```

### Output

```text
Enter your age: 20
Your age is: 20
```

---

## Example with Float Input

```python
price = float(input("Enter the price: "))

print("Price is:", price)
```

### Output

```text
Enter the price: 99.5
Price is: 99.5
```

---

## Important Point

The `input()` function **always returns a string**.

For example:

```python
age = input("Enter your age: ")

print(type(age))
```

If the user enters `20`, the output will still be:

```text
<class 'str'>
```

To get an integer, use:

```python
age = int(input("Enter your age: "))
```

Now:

```python
print(type(age))
```

Output:

```text
<class 'int'>
```

---

## Easy Trick to Remember

```text
input() → String
int(input()) → Integer
float(input()) → Float
```