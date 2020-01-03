# Exercise 16 (Set)
A set is a mutable sequence with no duplicates. Just like a list, but no duplicate. A set is delimited by open and close curly brackets.

## Structure of a set

``` python
# set structure

sample_set = {1, 2, 3}

# empty list
empty_list = set()

# the above empty set is not the same as {}
```

## Casting

You may cast any sequence to a set by passing the sequence as an argument to `set()` . This returns a unique elements of the sequence.

``` python
# str to set
name = "Gangliona Messian"
set_str = set(name)
print(set_str)
# output-> {'e', 'o', 'i', 'l', 'M', 'g', 'n', ' ', 's', 'a', 'G'}

my_list = [1, 2, 3]
my_set = set(my_list)
print(my_set)
# output-> {1, 2, 3}
```

## Set operations and functions

Assume we have two sets, A anf B.
| Operator | Function      | description |
| :------- | :------:      | ----------: |
| `&` | intersection  | returns elements in both sets |
| `|` | union         | returns elements in either set |
| `-` | difference    | returns elements in set A that are not in B |
| `^` | symmetric_difference | returns elements that are not in both sets |
| `>=` | issuperset    | returns True if A is a super set of B, else False |
| `<=` | issubset      | returns True if A is a subset set of B, else False |
|      | disjoint      | returns is both sets have nothing in common |
|          | add           | adds an element to the set, just like append in list |
|          | update        | adds a sequence to the set, just like extend in list |
|          | discard       | removes an element from the list                     |
|          | remove        | just like discard but returns an error when the element doesn't exist |

## Examples

``` python
# Let our two sets be
set_a = {1, 2, 3, 6}
set_b = {3, 4, 5, 6}

# intersection -> {3, 6}
fintersec_ab = set_a.intersection(set_b)
ointersec_ab = set_a & set_b

print('intesection: ', fintersec_ab == ointersec_ab)

# union -> {1, 2, 3, 4, 5, 6}
funion_ab = set_a.union(set_b)
ounion_ab = set_a | set_b

print('union: ', funion_ab == ounion_ab)

# difference
fdiff_ab = a.difference(b)  # output-> {1, 2}
odiff_ab = a - b  # output-> {1, 2}

fdiff_ba = b.difference(a)  # output-> {4, 5}
odiff_ba = b - a  # output-> {4, 5}

# symmetric difference
symm_diff = a.symmetric_difference(b)
print(symm_diff)  # output-> {1, 2, 4, 5}

# upperset and subset
is_a_super_set = a.issuperset(b) == (a >= b)
print(is_a_super_set)  # False

is_a_subset_set = a.issubset(b) == (a <= b)
print(is_a_subset_set)  # False

# disjoint
a.disjoint(b)  # output-> False

# add
set_a.add(8)
print(set_a)  #output-> {1, 2, 3, 6, 8}

# update
update_ab = set_a.update(set_b)  # output-> {1, 2, 3, 4, 5, 6, 8}

# discard
set_a.discard(1)  # output-> {2, 3, 4, 5, 6, 8}
set_a.discard(10)  # output-> {2, 3, 4, 5, 6, 8}

# remove
set_a.remove(2)  # output-> {3, 4, 5, 6, 8}
set_a.remove(2)  # error-> KeyError
```

## Practicals

Implement your own version of 

    - Intersection
    - Union
    - difference
    - symmetric_difference
    - delete like discard or remove ( ignore the KeyError thing)
    - update
    - isset - it check is a sequence has no duplicate ( remember `count` )

> make use of all the we've learns.

## Summary

* A set is just more like a list but with no duplicates
* Sample set, `my_set = {1,3,4}` 
* cast a sequence to a set, `set(sequence)` 

