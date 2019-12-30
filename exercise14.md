# exercise 14 (List)
We have had our fill with lists but here we kind of go much into it.

## What is a list
As already know, a `list` is a collection of comma seperated objects, where by the collection is delimitered by an opened and closed square bracket.

### Exampls
```python
num_list = [1, 2, 3, 4, 5]

str_list = ['1', '2', 'Jonas', 'maiduguri', 'samoa']

bool_list = [True, False, False, True]
```

## types of list
There are basically two types of list in python, the one dimensional list - a single list and then the multi-dimensional list - this can 2D, 3D, etc

### one Dimensional list
```python
# sample of 1D list
num_list = [1, 2, 3, 4, 5]
```

### multi-dimensional list
```python
# samples of XD list

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

## accessing elements of a list
The elements of a list are indexed from 0 to (n - 1), where n is the size of the list. To access an element from the list, use its index.
    ```python
    my_list = [1, 'gnu', 'swift', 'kickass']
    
    print(my_list[0])  # 1
    print(my_list[1])  # gnu
    print(my_list[2])  # swift
    print(my_list[3])  # kickass

    # list slicing
    # syntax list_obj[start:end] - the end is esclusive
    print(my_list[1:3]) # [gnu, swift]
    print(my_list[0:3]) # [1, gnu, swift]
    print(my_list[:3]) # [1, gnu, swift]
    print(my_list[1:]) # [gnu, swift, kickass]
    ```

## List Operations
1. The `+` operator is used to add ( concatenate) lists
    ```python 
    # Adding one list to another
    my_list = [1,2,3]
    s_list = ['e', 'u', 'o']

    f_list = my_list + s_list

    print(f_list)
    ```
1. `*` operation on a list object multiplies the list n time.
    ```python
    b_list = [2]
    f_list = b_list * 4

    print(f_list)
    ```

1. `in` to check the if an object exists in a list.
    ```python
    my_list = [1,2,3]

    # check if the list contains 4
    if 4 in my_list:
        print('The list has a four')
    else:
        print('well, there is no four')
    
    ```



## Some list functions
* append(obj) - adds object to the end of the list object
* extends(obj) - adds object to the end of the list object as a whole
* index(obj) - returns the index of obj in the list object
* insert(index, obj) - insert obj at index of list object
* pop(index) - removes the element at index or the last element when no index is passed
* remove(obj) - removes the first occurence of obj in the list object
* reverse() - reverses the list in place ( it changes the object)
* count(obj) - counts the number of obj in list object
* sort(reverse=True) - by default sorts list object in numerical order and can also reverse the sorted object by passing the keyword revere=True
* clear() - removes all the elements of the list
* del list_obj[index] - deletes object at index

```python
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

## Practicals
> this is supposed to be fun

* Create a function for each of the following, using any means possible without cutting corners. ( explicitly using built-in function)
    1. `addition` - this function takes two objects as argument,  and returns their sum if they are numbers, that is a float or an int, but when one or both are strings return a concatenation of both. Remember type casting.
    1. `subtraction` - this function takes two objects as argument, returns the resut of subtracting the second from the first.
    1. `division` - this function takes two objects as argument, returns the result from dividing the first by the second. Remember that zero division is not allowed thus check if the second is zero.
    1. `multplication` - this function takes two objects as argument, returns the product of the two.
* Write a function, that takes a list as an argument of various objects, return a list of all the objects that are numbers ( that is integer and float).
* Write a function taking a list of various objects as argument, return the number of each object in the list.
* Write a function that takes a list of integers as an argument, remove ( delete) any element that has the same number type as its `index + 1`. ( If the `index + 1` is even and the element is even remove the element, like while odd except when the `index` is 0), looping though the list `n` times, `n` is the size of the list.
    ```python
    s = [2, 6, 18, 11, 4]
    # 6 is removed - loop 1
    # 18 is removed - loop 2
    # None is removed - loop 3
    # None is removed - loop 4
    # None is removed - loop 5

    s = [2, 11]
    ```
* This practicals is the same as the above but in the above as you remove the elements which passes the condition, the list is changed too. In here, you remove all at a go. ( It is better you use a list rather than a loop in removing the elements and do not remove object by index)
    ```python
    # i = index + 1
    s = [2, 6, 18, 11, 4]
    i = [1, 2,  3,  4, 5]

    # only 6 will be removed
    s = [2, 18, 11, 4]
    ```

## Summary
* A `list` is a collection of comma seperated objects
* A literal list is created, `name_of_list_object = [a, b, c, ... ]`
* There can be a nested list
* Pass the index of the element of interest into a square bracket after the name of the list object. `Eg: list_obj[1]`
* You can use `+` operator to concatenate one list to another
* You can use `*` operator to repeat the list n time. `Eg: list_obj * 3`
* You can check if an object is in a list by using the `in` keyword. `Eg: obj in list_object`
* Use the dot operator to call a list function ( aka method). `Eg: list_object_name.function_name(some args)`