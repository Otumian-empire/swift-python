# Exercise 17 (Dictionary)

A dictionary just like a list, tuple and a set which is a sequence. A dictionary is rather key-value pair. String, list, etc are number-indexed. A dictionary is key-indexed.

## Structure of a dictionary

```Python
# dict_var = { key : value }

# empty dictionary
my_dict = {}

# profile dictionary
profile = {
    'name': 'John Doe',
    'age': 32,
    'job': 'Software engineer'
}

```

## Casting

Casting is done with `dict()`

```Python
# passing a keyword and a value

# dict(key-word=value, ... )
my_dict = dict(
    name='John Doe',
    age=32,
    job='Software engineer'
)

# convert a list of tuple to a dictionary
my_tupled_list = [('name', 'John Doe'), ('age', 32, ),
                  ('job', 'Software engineer')]
my_dict = dict(my_tupled_list)

print(my_tupled_list)
# output-> {'name': 'John Doe', 'age': 32, 'job': 'Software engineer'}

```

## Indexing and updating a dictionary

Indexing and updating are done just as we would do to a list.

```Python
# consider this dictionary
profile = {
    'name': 'John Doe',
    'age': 32,
    'job': 'Software engineer'
}

# get the name and job
name = profile['name']
job = profile['job']

print(f"Candidates name is {name} and works, {job}")

# update the age
profile['age'] = 30

# add a new key
profile['lang'] = 'Python'

# delete a key to delete a value using - del
del profile['age']

```

## dictionary functions

| Functions                      |                                                                                                                                  description |
| :----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------: |
| clear                          |                                                               deletes all the items in the dictionary, similar to reassigning it to `dict()` |
| copy                           |                                                                                                             returns a copy of the dictionary |
| get( `key` , `default value` ) | returns a value of that key just like dict_object[key] but returns default value when key doesn't exist. This does not update the dictionary |
| items                          |                                                                                                          returns the items in the dictionary |
| values                         |                                                                                                         returns the values of the dictionary |
| keys                           |                                                                                                           returns the keys of the dictionary |
| pop( `key` )                   |                                                                                                      deletes item with the key just like del |
| popitem                        |                                                                                                      deletes the last item in the dictionary |
| setdefault( `key` , `value` )  |                                                                              adds key value to dictionary if key doesn't exist, unlike `get` |

## Examples

```Python
# empty dict
profile = dict()

# add an item - 3 ways use any
profile['name'] = 'John Doe'  # we use this more - simplier

profile.update(age=32)

profile.setdefault('job', 'Software engineer')

print(profile)

# get an item from the dict

# get the keys from a dictionary
profile_keys = profile.keys()
print(profile_keys)
# output-> dict_keys(['name', 'age', 'job'])

# get the values from a dictionary
profile_values = profile.values()
print(profile_values)
# output-> dict_values(['John Doe', 32, 'Software engineer'])

# get the key and value as items
profile_content = profile.items()
print(profile_content)
# do the printing

# get element by key
username = profile['name']
print(f"user name: {username}")

# what if the key doesn't exist
# use get with default value
# profile['height'] -> KeyError
height = profile.get('height', 130)
print(height)  # -> 130

# but height won't be added to the dict
# use set default, update or dict[key] = value
if not 'height' in profile.keys():
    # any of this would work
    profile['height'] = 120
    # profile.update(height = 120)
    # profile.setdefault('height', 120)
else:
    print('Profile updated, height added')

print(profile)

# copy
new_profile = profile.copy()
print(new_profile)

# pop - remove height
profile.pop('height')  # or
# del profile['height']

# delete all items in the dict
profile.popitem()

print(len(new_profile) == len(profile))

```

## Looping through a dictionary

Looping is the same everywhere in a list, set and tuple, in even a string, but for a dictionary, we may loop using a key or and value.

```Python
# consider this sample dictionary
profile = {
    'name': 'John Doe',
    'age': 32,
    'job': 'Software engineer'
}

# looping through keys
for key in profile.keys():
    print(f"key: {key}")

# looping through values
for value in profile.values():
    print(f"value: {value}")

# looping through the items in the dictionary
# we loop through the key and value at the same time
for key, value in profile.items():
    print(f"{key} has a value of {value}")

```

## Practicals

- Write a function that removes items with duplicate values
- Write a function that takes a dictionary as an argument, return another dictionary that has the frequency of the length of the value, if value is `int` or `float`, frequency is the number of digits. Keep the keys of the old as the new.

## Summary

- is a `key-value` pair sequence
- is of structure, `my_dict = {key:value}`
- `dict(name='name')` casts to a dict
- dict_obj[ `key` ] returns the `value` at `key`
- `dict_obj[key] = value` to create new item in dictionary or update
- loop through dictionary by keys, values and items
