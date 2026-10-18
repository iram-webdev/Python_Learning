
# Dictionary Methods

A dictionary uses several built-in methods for manipulation. They are listed below.

## `update()`

The `update()` method updates the value of a key if the item already exists in the dictionary; otherwise, it creates a new key-value pair.

#### Example:

```python
info = {'name': 'Karan', 'age': 19, 'eligible': True}

print(info)

info.update({'age': 20})
info.update({'DOB': 2001})

print(info)
```

#### Output:

```text
{'name': 'Karan', 'age': 19, 'eligible': True}
{'name': 'Karan', 'age': 20, 'eligible': True, 'DOB': 2001}
```

## Removing Items from a Dictionary

There are a few methods that we can use to remove items from a dictionary.

### `clear()`

The `clear()` method removes all the items from the dictionary.

#### Example:

```python
info = {'name': 'Karan', 'age': 19, 'eligible': True}

info.clear()

print(info)
```

#### Output:

```text
{}
```

### `pop()`

The `pop()` method removes the key-value pair whose key is passed as a parameter.

#### Example:

```python
info = {'name': 'Karan', 'age': 19, 'eligible': True}

info.pop('eligible')

print(info)
```

#### Output:

```text
{'name': 'Karan', 'age': 19}
```

### `popitem()`

The `popitem()` method removes the last key-value pair from the dictionary.

#### Example:

```python
info = {'name': 'Karan', 'age': 19, 'eligible': True, 'DOB': 2003}

info.popitem()

print(info)
```

#### Output:

```text
{'name': 'Karan', 'age': 19, 'eligible': True}
```

### `del`

We can also use the `del` keyword to remove an item from a dictionary.

#### Example:

```python
info = {'name': 'Karan', 'age': 19, 'eligible': True, 'DOB': 2003}

del info['age']

print(info)
```

#### Output:

```text
{'name': 'Karan', 'eligible': True, 'DOB': 2003}
```

If the key is not provided, the `del` keyword will delete the entire dictionary.

#### Example:

```python
info = {'name': 'Karan', 'age': 19, 'eligible': True, 'DOB': 2003}

del info

print(info)
```

#### Output:

```text
NameError: name 'info' is not defined
```
