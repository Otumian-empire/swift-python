# Exercise 14 ( List)
We have had our fill with lists but here we would kind of go much into it.

As already we know, a `list` is a collection of comma seperated objects, where by the collection is delimitered by an opened and closed square bracket.

## Examples

``` Python
num_list = [1, 2, 3, 4, 5]

str_list = ['1', '2', 'Jonas', 'maiduguri', 'samoa']

bool_list = [True, False, False, True]
```

## kinds of list

There are basically two kinds of list in Python, the one dimensional list - a single list and then the multi-dimensional list or nested list - these are 2D, 3D, etc

### One Dimensional list

``` Python
# sample of 1D list
num_list = [1, 2, 3, 4, 5]
```

### Multi-dimensional list

``` Python
# samples of XD list - form some int x >= 1

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

The elements of a list are indexed from `0 to (n - 1)` , where `n` is the size of the list. To access an element from the list, use the elements index.

``` Python
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

For a multi-dimensional list of say `x` , we provide `x` indices instead.

``` Python
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

Try thinking in rows and columns with multi-dimensional lists

``` Python

my_list = [
    [1, 2, 3, 4],
    ['go', 'py', 'js', 'kt']
]

# 4 is in row 1 column 4 .
# knowing well that index starts from 0 , we substract 1 from the rows and cols
# thus 4 can be indexed with [1-1][4-1]=[0][3]
```

## List slicing

List slicing allows us to sublist the list object - slice the list from one `index` to another. Think about slicing of an actual bread.

Just like indexing, but here we provide a range, a `start` and an `end` with a colon, `:` , Something similiar to, `list_obj[start:end]` . List slicing works like the `range(start, end)` function, the `end` is exclusive.

``` Python
my_list = [1, 'gnu', 'swift', 'kickass']

print(my_list[1:3]) # [gnu, swift]
print(my_list[0:3]) # [1, gnu, swift]
print(my_list[:3]) # [1, gnu, swift]
print(my_list[1:]) # [gnu, swift, kickass]
```

## List Operations

The addition operator, `+` operator is used to add ( concatenate) lists.

``` Python
# Adding one list to another

my_list = [1, 2, 3]
s_list = ['e', 'u', 'o']

f_list = my_list + s_list

print(f_list)

``` 

The multiplication operator, `*` on a list object multiplies the list `n` time, for some integer value `n` > 1.

```Python
b_list = [2]
f_list = b_list * 4

print(f_list)
```

The `in` operator, checks if an object exists in a list ( or an iterable object).

``` Python
my_list = [1, 2, 3]

# check if the list contains 4
# or 4 is in the list

if 4 in my_list:
    print('The list has a four')
else:
    print('well, there is no four')
```

## Some list functions

| Function | Description |
|:-------- | ----------:|
| append(obj) | adds object to the end of the list object |
| extends(obj) | adds object to the end of the list object as a whole|
| index(obj) | returns the index of obj in the list object|
| insert(index, obj) | insert obj at index of list object|
| pop(index) | removes the element at index or the last element when no index is passed|
| remove(obj) | removes the first occurence of obj in the list object|
| reverse() | reverses the list in place ( it changes the object)|
| count(obj) | counts the number of obj in list object|
| sort(reverse=True) | by default sorts list object in numerical order and can also reverse the sorted object by passing the keyword revere=True|
| clear() | removes all the elements of the list|
| del list_obj[index] | deletes object at index|

``` Python
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
name_list.sort(reverse = True)

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

* Create a function for each of the following, using any means possible without cutting corners.( no using of built-in function - we have go to try harder)
    1. `addition` - this function takes two objects as argument,  and returns their sum if they are numbers, that is a float or an int.
    1. `subtraction` - this function takes two objects as argument, returns the resut of subtracting the second from the first.
    1. `division` - this function takes two objects as argument, returns the result from dividing the first by the second. Remember that zero division is not allowed thus check if the second is zero.
    1. `multplication` - this function takes two objects as argument, returns the product of the two.

* Write a function, that takes a list of various objects as an argument, return a list of all the objects that are numbers ( that is integer and float).

* Write a function taking a list of various objects as argument, return the number of each object in the list.

* Write a function that takes a list of integers as an argument, remove ( delete) any element that has the same parity as its `index + 1` .( If the `index + 1` is even and the element is even, remove the element. If number is odd and `index + 1` is odd, remove element, except when the `index` is 0), looping `n -1` times, where `n` is the size of the list.

``` Python
s = [2, 6, 18, 11, 4]
# 6 is removed - loop 1

s = [2, 18, 11, 4]
# 18 is removed - loop 2

s = [2, 11, 4]
# None is removed - loop 3

s = [2, 11, 4]
# None is removed - loop 4

s = [2, 11]
```

* This practical is the same as the above but in the above as we remove the elements which passes the condition, the list is changed too. We don't want to remove the element as the list chnages - that in a way does really suffices. Consider the code below:

``` Python
# i = index + 1
s = [2, 6, 18, 11, 4]
i = [1, 2,  3,  4, 5]

# only 6 will be removed because it is in parity with its index + 1
s = [2, 18, 11, 4]
```

## Summary

* A `list` is a collection of comma seperated objects
* A literal list is created, `name_of_list_object = [a, b, c, ... ]` 
* There can be a nested list
* Pass the index of the element of interest into a square bracket after the name of the list object. `Eg: list_obj[1]` returns the element at that index
* We can use `+` operator to concatenate one list to another
* We can use `*` operator to repeat the list n time. `Eg: list_obj * 3` 
* We can check if an object is in a list by using the `in` keyword. `Eg: obj in list_object` , this returs a boolean value
* Use the dot operator to call a list function ( aka method). `Eg: list_object_name.function_name(some args)` 

