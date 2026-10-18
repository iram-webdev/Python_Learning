# Python Dictionaries

Dictionaries are ordered collections of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets `{}`.

#### Example:

```python id="2j4n7p"
info = {'name': 'Karan', 'age': 19, 'eligible': True}
print(info)
```

#### Output:

```text id="j8k2mx"
{'name': 'Karan', 'age': 19, 'eligible': True}
```

## Accessing Dictionary Items

### I. Accessing Single Values

Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in square brackets or by using the `get()` method.

#### Example:

```python id="m3q5vx"
info = {'name': 'Karan', 'age': 19, 'eligible': True}

print(info['name'])
print(info.get('eligible'))
```

#### Output:

```text id="v6r1nz"
Karan
True
```

### II. Accessing Multiple Values

We can print all the values in the dictionary using the `values()` method.

#### Example:

```python id="a7k9pd"
info = {'name': 'Karan', 'age': 19, 'eligible': True}

print(info.values())
```

#### Output:

```text id="x2m5qw"
dict_values(['Karan', 19, True])
```

### III. Accessing Keys

We can print all the keys in the dictionary using the `keys()` method.

#### Example:

```python id="c4n8ty"
info = {'name': 'Karan', 'age': 19, 'eligible': True}

print(info.keys())
```

#### Output:

```text id="p9w3jh"
dict_keys(['name', 'age', 'eligible'])
```

### IV. Accessing Key-Value Pairs

We can print all the key-value pairs in the dictionary using the `items()` method.

#### Example:

```python id="r5u1lk"
info = {'name': 'Karan', 'age': 19, 'eligible': True}

print(info.items())
```

#### Output:

```text id="h6b2zs"
dict_items([('name', 'Karan'), ('age', 19), ('eligible', True)])
```

# Python Dictionaries

## 1. What is a Dictionary?

A dictionary is a built-in data type in Python used to store multiple items in a single variable.

Dictionary items are stored as **key-value pairs**, separated by commas and enclosed within curly brackets `{}`.

### Example:

```python
info = {
    "name": "Karan",
    "age": 19,
    "eligible": True
}

print(info)
```

### Output:

```text
{'name': 'Karan', 'age': 19, 'eligible': True}
```

## 2. Important Properties of Dictionaries

- Dictionaries store data in key-value pairs.
- Dictionaries are ordered collections and preserve insertion order.
- Dictionaries are mutable, meaning their contents can be changed.
- Dictionary keys must be unique.
- Duplicate keys are not allowed; if a key is repeated, its latest value is retained.
- Dictionary values can contain duplicate data.
- Keys must be hashable, such as strings, integers, or suitable tuples.
- Values can be of any data type.
- Dictionaries can contain different data types in the same collection.
- Dictionaries do not support numerical indexing like lists.

## 3. Creating a Dictionary

We can create a dictionary using curly brackets `{}`.

### Example:

```python
student = {
    "name": "Aman",
    "age": 20,
    "course": "B.Tech"
}

print(student)
```

### Output:

```text
{'name': 'Aman', 'age': 20, 'course': 'B.Tech'}
```

## 4. Empty Dictionary

An empty dictionary contains no key-value pairs.

### Example:

```python
student = {}

print(student)
print(type(student))
```

### Output:

```text
{}
<class 'dict'>
```

## 5. Dictionary Keys and Values

Each dictionary item consists of two parts:

- **Key:** Identifies an item in the dictionary.
- **Value:** Stores the data associated with that key.

### Example:

```python
student = {
    "name": "Aman",
    "age": 20
}
```

Here, `"name"` and `"age"` are keys, while `"Aman"` and `20` are their respective values.

## 6. Accessing Dictionary Values

Dictionary values are accessed using their keys.

### Example:

```python
student = {
    "name": "Aman",
    "age": 20
}

print(student["name"])
print(student["age"])
```

### Output:

```text
Aman
20
```

If a key does not exist, accessing it with square brackets raises a `KeyError`.

## 7. Adding and Updating Items

Dictionaries are mutable, so we can add new key-value pairs and update existing values.

### Example:

```python
student = {"name": "Aman", "age": 20}

student["course"] = "B.Tech"
student["age"] = 21

print(student)
```

### Output:

```text
{'name': 'Aman', 'age': 21, 'course': 'B.Tech'}
```

## 8. Removing Items

We can remove individual key-value pairs or delete the entire dictionary variable.

### Example:

```python
student = {"name": "Aman", "age": 20}

del student["age"]

print(student)
```

### Output:

```text
{'name': 'Aman'}
```

## 9. Checking Whether a Key Exists

The `in` and `not in` operators can check whether a key exists in a dictionary.

### Example:

```python
student = {"name": "Aman", "age": 20}

print("name" in student)
print("city" not in student)
```

### Output:

```text
True
True
```

By default, these operators check dictionary keys, not values.

## 10. Nested Dictionaries

A nested dictionary is a dictionary that contains other dictionaries as values.

### Example:

```python
students = {
    "student1": {
        "name": "Aman",
        "age": 20
    },
    "student2": {
        "name": "Riya",
        "age": 21
    }
}

print(students["student1"]["name"])
```

### Output:

```text
Aman
```

## 11. Dictionary Comprehension

Dictionary comprehension provides a concise way to create dictionaries.

### Example:

```python
squares = {x: x**2 for x in range(1, 6)}

print(squares)
```

### Output:

```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## 12. Advantages of Dictionaries

- Store related information using meaningful keys.
- Retrieve values using keys.
- Allow modification of data after creation.
- Represent structured data clearly.
- Useful for storing student records, product details, and configuration data.

## 13. Important Points to Remember

- Dictionaries use `{}` to enclose key-value pairs.
- Each key is associated with a value using a colon `:`.
- Items are separated by commas.
- Keys must be unique and hashable.
- Values can be duplicated and can have different data types.
- Dictionaries preserve insertion order.
- Dictionaries are mutable.
- Accessing a missing key with square brackets raises a `KeyError`.
- An empty dictionary is represented by `{}`.
- Nested dictionaries can store complex structured information.

## 14. Practice Questions

1. Create a dictionary containing your name, age, and course.
2. Explain the difference between keys and values.
3. Explain why dictionary keys must be unique.
4. Create an empty dictionary and check its type.
5. Add a new item and update an existing item.
6. Check whether a particular key exists.
7. Create a nested dictionary for two students.
8. Create a dictionary containing the squares of numbers from 1 to 5 using dictionary comprehension.

## Conclusion

Dictionaries are an important Python data type used to store information as key-value pairs. They are ordered, mutable, and useful when data needs to be accessed through meaningful keys.