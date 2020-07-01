# Exercise 15 (Tuple)
A tuple is a comma seperated objects and by conversion delimited by an open and closed brackets - parentheses, `()` . A tuple is just like a `list` but a tuple is immutable - can not be altered after creation unlike a list.

## Structure of a Tuple

``` Python
sample_tuple = 1, 2, 3

# a tuple with brackets
tuple_with_bracket = (1, 2, 3)

# thus an empty tuple
empty_tuple = ()  # an empty list, []

# empty tuple object
tup_object = tuple()

# to verify this try type(sample_tuple) and type(tuple_with_bracket)
# we should see some with tuple
```

### Note

A single element tuple can be created by simply ending the statement with a comma

``` Python
# this is also a tuple
single_element_tuple = 1,

# or
single_element_tuple = (1,)
print(type(single_element_tuple))

# but this is not a tuple
not_single_element_tuple = 1

# nor is this
not_single_element_tuple = (1)
print(type(not_single_element_tuple))
```

## Pros and Cons of a Tuple

Most of the thing we wish to do to a list, we may do to a tuple. Some of the things we can't do to a tuple is to mutate it - change it's content after initialization.

``` Python
my_tuple = (1, 2, 3)

# indexing
first_element = my_tuple[0]

# reassigning
# TypeError: 'tuple' object does not support item assignment
my_tuple[0] = 4

# len, max, min
tuple_size = len(my_tuple)

# sequence unpacking
# this is another way to unpack the tuple
# this is also feasible for a list
first_el, second_el, third_el = my_tuple

# this is just like a multiple assignment
first_el, second_el, third_el = 1, 2, 3

# nested tuple
nest_tuple = (my_tuple, ('john', 'mic', 'Dorris'), 'New zealand')

# can not append nor extend
# AttributeError
sample_tup = 1,
sample_tup.append(2)
sample_tup.extend((2,3))

# but we can contatenate with +=
sample_tup += 2, 3
print(sample_tup)  # (1, 2, 3)

# What happended was that we concatenated 1, and 2, 3 and 
# assigned it to sample_tup, we basically created a new tuple
```

## Casting

we may cast - convert any iterable - a sequential object such as a `list` and `string` to a tuple but not a number because we can not loop over numbers. This can be done using `tuple(sequence)` .

``` Python
# casting a list to a tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)

my_str = 'Hello world'
tuple_str = tuple(my_str)
print(tuple_str)
# output-> ('H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd')
```

## Practicals

Try to implement the practicals in `Exercise 14 ( List)` using tuple.

## Summary

* A `tuple` is an immutable list, delimetered by parentheses
* Sample tuple, `my_tuple = (1, 2, 3)` 
* `tuple` does not have the `append` and `extend` method
* Make a sequence a `tuple` by casting it. `tuple('I am a string')` 

