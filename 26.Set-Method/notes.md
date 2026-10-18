# Joining Sets

Sets in Python work more or less in the same way as sets in mathematics. We can perform operations like union and intersection on sets, just like in mathematics.

## I. `union()` and `update()`

The `union()` and `update()` methods return or combine all items that are present in the two sets. The `union()` method returns a new set, whereas the `update()` method adds items from another set into the existing set.

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

cities3 = cities.union(cities2)
print(cities3)
```

#### Output:

```text
{'Tokyo', 'Madrid', 'Kabul', 'Seoul', 'Berlin', 'Delhi'}
```

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

cities.update(cities2)
print(cities)
```

#### Output:

```text
{'Berlin', 'Madrid', 'Tokyo', 'Delhi', 'Kabul', 'Seoul'}
```

## II. `intersection()` and `intersection_update()`

The `intersection()` and `intersection_update()` methods return or keep only the items that are common to both sets. The `intersection()` method returns a new set, whereas the `intersection_update()` method updates the existing set.

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

cities3 = cities.intersection(cities2)
print(cities3)
```

#### Output:

```text
{'Madrid', 'Tokyo'}
```

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

cities.intersection_update(cities2)
print(cities)
```

#### Output:

```text
{'Tokyo', 'Madrid'}
```

## III. `symmetric_difference()` and `symmetric_difference_update()`

The `symmetric_difference()` and `symmetric_difference_update()` methods return or keep only the items that are not common to both sets. The `symmetric_difference()` method returns a new set, whereas the `symmetric_difference_update()` method updates the existing set.

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

cities3 = cities.symmetric_difference(cities2)
print(cities3)
```

#### Output:

```text
{'Seoul', 'Kabul', 'Berlin', 'Delhi'}
```

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

cities.symmetric_difference_update(cities2)
print(cities)
```

#### Output:

```text
{'Kabul', 'Delhi', 'Berlin', 'Seoul'}
```

## IV. `difference()` and `difference_update()`

The `difference()` and `difference_update()` methods return or keep only the items that are present in the original set but not in the other set. The `difference()` method returns a new set, whereas the `difference_update()` method updates the existing set.

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}

cities3 = cities.difference(cities2)
print(cities3)
```

#### Output:

```text
{'Tokyo', 'Madrid', 'Berlin'}
```

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}

print(cities.difference(cities2))
```

#### Output:

```text
{'Tokyo', 'Berlin', 'Madrid'}
```



# Set Methods

There are several built-in methods used for the manipulation of sets. They are explained below.

## `isdisjoint()`

The `isdisjoint()` method checks whether the items of a given set are present in another set. This method returns `False` if any items are common; otherwise, it returns `True`.

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

print(cities.isdisjoint(cities2))
```

#### Output:

```text
False
```

## `issuperset()`

The `issuperset()` method checks whether all the items of a particular set are present in the original set. It returns `True` if all the items are present; otherwise, it returns `False`.

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}

print(cities.issuperset(cities2))

cities3 = {"Seoul", "Madrid", "Kabul"}
print(cities.issuperset(cities3))
```

#### Output:

```text
False
False
```

## `issubset()`

The `issubset()` method checks whether all the items of the original set are present in a particular set. It returns `True` if all the items are present; otherwise, it returns `False`.

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}

print(cities2.issubset(cities))
```

#### Output:

```text
True
```

## `add()`

If you want to add a single item to a set, use the `add()` method.

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")

print(cities)
```

#### Output:

```text
{'Tokyo', 'Helsinki', 'Madrid', 'Berlin', 'Delhi'}
```

## `update()`

If you want to add more than one item, simply create another set or use any other iterable object, such as a list, tuple, or dictionary, and use the `update()` method to add its elements to the existing set.

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}

cities.update(cities2)
print(cities)
```

#### Output:

```text
{'Seoul', 'Berlin', 'Delhi', 'Tokyo', 'Warsaw', 'Helsinki', 'Madrid'}
```

## `remove()` / `discard()`

We can use the `remove()` and `discard()` methods to remove items from a set.

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")

print(cities)
```

#### Output:

```text
{'Delhi', 'Berlin', 'Madrid'}
```

The main difference between `remove()` and `discard()` is that if we try to remove an item that is not present in the set, `remove()` raises an error, whereas `discard()` does not raise an error.

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}

cities.remove("Seoul")
print(cities)
```

#### Output:

```text
KeyError: 'Seoul'
```

## `pop()`

This method removes an arbitrary item from the set. The catch is that we do not know which item gets removed because sets are unordered. However, we can access the removed item if we assign the `pop()` method to a variable.

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}

item = cities.pop()

print(cities)
print(item)
```

#### Output:

```text
{'Tokyo', 'Delhi', 'Berlin'}
Madrid
```

## `del`

`del` is not a method; rather, it is a keyword that deletes the set variable entirely.

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}

del cities
print(cities)
```

#### Output:

```text
NameError: name 'cities' is not defined
```

We get an error because the variable `cities` has been deleted, and there is no variable called `cities` that contains a set.

What if we do not want to delete the entire set, but only want to delete all the items within that set?

## `clear()`

This method clears all the items in the set and leaves an empty set.

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}

cities.clear()
print(cities)
```

#### Output:

```text
set()
```

## Check If an Item Exists

You can also check whether an item exists in a set or not.

#### Example:

```python
info = {"Carla", 19, False, 5.9}

if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
```

#### Output:

```text
Carla is present.
```