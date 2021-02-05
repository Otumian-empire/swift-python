# Exercise 14 ( List)

We have had our fill with lists but here we would kind of go much into it.

As already we know, a `list` is a collection of comma-separated objects, whereby the collection is delimited by an opened and closed square bracket.

## Examples

```Python
num_list = [1, 2, 3, 4, 5]

str_list = ['1', '2', 'Jonas', 'maiduguri', 'samoa']

bool_list = [True, False, False, True]

```

## kinds of list

There are two kinds of lists in Python - loosely speaking, the one-dimensional list - a single list and then the multi-dimensional list or nested list - these are 2D, 3D, etc.

### One Dimensional list

```Python
# sample of 1D list
num_list = [1, 2, 3, 4, 5]

```

### Multi-dimensional list

Samples of XD list - for some int X >= 1.

```Python
# 2d list
list_list = [
    [1, 2, 3, 4, 5],
    ['1', '2', 'Jonas', 'maiduguri', 'samoa']
]

# 3d list
list_list = [
    [1, 2, 3, 4, 5],
    ['1', '2', 'Jonas', 'maiduguri', 'samoa'],
    [True, False, False, True]
]

```

## Accessing elements of a list

The elements of a list are indexed from `0 to (n - 1)`, where `n` is the size of the list. To access an element from the list, use the element's index.

```Python
# index =  0    1      2        3
my_list = [1, 'gnu', 'swift', 'kickass']

print(my_list[0])  # 1
print(my_list[1])  # gnu
print(my_list[2])  # swift
print(my_list[3])  # kickass

# using negative indices 0 as if moving backwards from `0`
print(my_list[-1])  # kickass
print(my_list[-2])  # swift
print(my_list[-4])  # 1

```

For a multi-dimensional list of say `x`, we provide `x` indices instead.

```Python
# this is a 2D list
my_list = [
    [1, 2, 3, 4],
    ['go', 'py', 'js', 'kt']
]

# we use 2 indices
# the first goes into the main list
# the second the branch list

print(my_list[0])  # -> [1, 2, 3, 4]
print(my_list[1])  # -> ['go', 'py', 'js', 'kt']

print(my_list[0][0])  # -> 1
print(my_list[1][2])  # -> 'js'

```

### Note

Try thinking in rows and columns with multi-dimensional lists.

```Python
my_list = [
    [1, 2, 3, 4],
    ['go', 'py', 'js', 'kt']
]

# we know that `4`, is in row 1 column 4.
# knowing well that index starts from 0, we subtract 1 from the rows and cols
# thus 4 can be indexed with [1-1][4-1]=[0][3]

```

## List slicing

List slicing allows us to sublist the list object - slice the list from one `index` to another.

Just like indexing, but here we provide a range, a `start` and an `end` with a colon, `:`, something similar to, `list_obj[start : end]`. List slicing works like the `range(start, end)` function, the `end` is exclusive.

```Python
my_list = [1, 'gnu', 'swift', 'kickass']

print(my_list[1:3])  # [gnu, swift]
print(my_list[0:3])  # [1, gnu, swift]

# since `start` is not given, it starts from the first
# element to `end`
print(my_list[:3])  # [1, gnu, swift]

# since `end` is not given, it starts from 1 to the last
# element in the list
print(my_list[1:])  # [gnu, swift, kickass]

```

## List Operations

### Concatenate

The addition operator, `+`, is used to add (concatenate) lists.

```Python
# Adding one list to another

my_list = [1, 2, 3]
s_list = ['e', 'u', 'o']

f_list = my_list + s_list

print(f_list)

```

### Repetition

The multiplication operator, `*` on a list object multiplies the list elements `n` time, for some integer value `n` > 1.

```Python
b_list = [2]
f_list = b_list * 4

print(f_list)  # [2, 2, 2, 2]

a_list = [1, "one"]
e_list = a_list * 4

print(e_list)  # [1, 'one', 1, 'one', 1, 'one', 1, 'one']

```

### `in`

The `in` operator, checks if an object exists in a list ( or an iterable object).

```Python
my_list = [1, 2, 3]

# check if the list contains 4
# or 4 is in the list

if 4 in my_list:
    print('The list has a four')
else:
    print('well, there is no four')

```

## Some list functions

| Function              |                                                                                                               Description |
| :-------------------- | ------------------------------------------------------------------------------------------------------------------------: |
| `append(obj)`         |                                                                              adds an object to the end of the list object |
| `extends(obj)`        |                                                                   adds an object to the end of the list object as a whole |
| `index(obj)`          |                                                                               returns the index of obj in the list object |
| `insert(index, obj)`  |                                                                                        insert obj at index of list object |
| `pop(index)`          |                                                  removes the element at index or the last element when no index is passed |
| `remove(obj)`         |                                                                    removes the first occurrence of obj in the list object |
| `reverse()`           |                                                                       reverses the list in place ( it changes the object) |
| `count(obj)`          |                                                                                   counts the number of obj in list object |
| `sort(reverse=True)`  | by default sorts list object in numerical order and can also reverse the sorted object by passing the keyword revere=True |
| `clear()`             |                                                                                      removes all the elements of the list |
| `del list_obj[index]` |                                                                                                   deletes object at index |

### Using list functions

```Python
name_list = ['john']

# append
name_list.append('Doe')

# extends
ext_list = ['dev', 'ubuntu']
name_list.extends(ext_list)

# index
third_el = name_list[2]

# insert
name_list.insert(0, third_el)

# pop
name_list.pop()  # removes last object
name_list.pop(len(name_list) - 1)

# remove
name_list.remove('Doe')

# reverse
name_list.reverse()

# count
name_list.count('Doe`)

# sort
name_list.sort()

# sort reverse
name_list.sort(reverse=True)

# clear
name_list.clear()

# or just set name_list to an empty list
name_list = []

# del
# an alternative to remove
del name_list[1]

```

### Note

`del name_list` would delete `name_list` from memory.

## Practicals

> this is supposed to be fun

- Create a function for each of the following (no using of built-in function - we have to try our best):

  1. `addition` - this function takes two objects as an argument and returns their sum if they are numbers, that is a float or an int.
  1. `subtraction` - this function takes two objects as an argument, returns the result of subtracting the second from the first.
  1. `division` - this function takes two objects as an argument, returns the result from dividing the first by the second. Remember that zero division is not allowed thus check if the second is zero.
  1. `multiplication` - this function takes two objects as an argument, returns the product of the two.

- Write a function, that takes a list of various objects as an argument, return a list of all the objects that are numbers (that is integer and float).

- Write a function taking a list of various objects as an argument, return the number of each object in the list. (This is also known as the frequency counter)

- Write a function that takes a list of integers as an argument, return a list of the elements with the same parity as their index. Returning list must have the first element.

  ```Python
  s = [2, 6, 18, 11, 4]

  # final output
  [2, 18, 11, 4]
  ```

- Write a function that takes a list of integers as input, then return a list of the integers, with the same parity as the first element, include the first element.

## Summary

- A `list` is a collection of comma-separated objects
- A literal list is created, `name_of_list_object = [a, b, c, ... ]`
- There can be a nested list
- Pass the index of the element of interest into a square bracket after the name of the list object. `Eg: list_obj[1]` returns the element at that index
- We can use the `+` operator to concatenate one list to another
- We can use `*` operator to repeat the list n time. `Eg: list_obj * 3`
- We can check if an object is in a list by using the `in` keyword. `Eg: obj in list_object`, this returns a boolean value
- Use the dot operator to call a list function (aka method). `Eg: list_object_name.function_name(some args)`
