# Exercise 11 a (For Loop)

There comes a need to repeat certain processes for a particular number of times or for as long as a particular condition holds as we write our codes. So, say we have,

```python
print("hello world!")
```

and we want to repeat this line three times, we would do,

```python
print("hello world!")
print("hello world!")
print("hello world!")
```

or we can do,

```python
print("Hello world!\n" * 3)
```

Say, we want a user to enter a positive number then maybe perform some computation on it, how do we keep prompting the user that we need a positive number?

```python
# assume in all cases, the user enters a number
num = int(input("Enter a positive number: "))

if num > 0:
    print(f"Great, {num} + 2 = {num + 2}")
```

In this case, the user would have to run the program again, every time they enter a non-positive number.

What if we have to do it like 100 times, 1000 times? We will need a loop.

Here we would look into loops ( also known as iterations). There are two types of loops in Python. These are the:

- `for` loop
- `while` loop

## Range

A new keyword, not that strange, is `range`. `range` takes three arguments: `start, stop and jump`. `stop` can be called `end` and `jump`, `step`.

```python
range(0, 5, 1) # start=0, end=5, step=1
range(-5, 2, 2) # start=5, end=2, step=2
```

`range` produces a sequence of numbers from `start` to `end - 1`, increasing `start` `step` times. So `range(0, 5, 1)` will produce: `0, 1, 2, 3, 4`, starting from `0`, then `0 + 1`, which is the step. `range(-5, 2, 2)` will produce: `-5, -3, -1, 1`. This continues as far as the number is less than `end`. `range` can take `start and end` and by default, `step` is `1`. As such `range(0, 5)` is the same as `range(0, 5, 1)`. `range` can take `end` and by default, `start` is `0` and `step` is `1`. `range(0, 5, 1)` is the same as `range(5)`. `range(3) = 0, 1, 2`. One thing is that, the number are produced as far as `start` is less than `end`.

## For loop

Usually, a `for` loop is used when we know the number of times we need to loop. Something like when the loop should end - looping for a particular number of times.

### Structure of a `for` loop

```Python
for element in some_structure:
    # do something
```

The `element` is a name we have used to refer to the current object (element) in the `some_structure`. `index` or `i` is mostly used. `some_structure` is an object which can be iterated upon. Some example of iterable are `set` , `list` , `dict` , `str` , `range`, etc.

#### Range looping

Let's print numbers from `1 to 10`, using the range function.

```python
for number in range(10):
    print(number)
```

This will print a vertical list of numbers from `0` to `9`. We wanted to print from `1` to `10`. We can add `1` to `number` then `print` it or we can `start` from `1` and `end` on `11`.

```python
for number in range(10):
    print(number + 1)

for number in range(1, 11):
    print(number)
```

We can print even numbers from `2` to `20` excluded.

```python
for number in range(2, 20, 2):
    print(number)
```

You should modify the above code to print odd numbers.

Let's look at another snippet that prints the string, `<number> is even` if the number is even else it prints the number.

```python
for number in range(20):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(number)
```

`20` will be excluded. Modify the code to include `20`.

At this moment, we should be able to print a lot of `Hello world!`s without rewriting the print statement.

```python
# print hello world three times
for i in range(3):
    print("hello world!")
```

#### Structure Looping

We have discussed `strings` already. Do you recall string indexing, where we pass some number into a square bracket to get a character of the string at that position?

```python
name = "John Doe"

# looping through `name` using index
end = len(name)
for i in range(end):
    print(name[i])

# looping through name without index
# this is looping through the structure itself
for ch in name:
    print(ch)
```

#### Concept of iterating - lamely

Say we have a string and it is an iterable (this permits the looping on the string).

```python
lang = "Python"

for ch in lang:
    print(ch)
```

There is a pointer, should we assume. This pointer here is `ch`, which points to the first element in the iterable (here, a string - lang) if there is any. The first character is `P` so `P` is printed out. The pointer then checks if there is another element. If there is, the pointer, `ch` is assigned that element. This process continues until there is no next element.

#### Example 1

A program the accepts five integer inputs from the user and prints the sum and average.

```python
s = 0
for i in range(5):
    n = int(input("Enter a positive number: "))

    s = s + n
    # s += n

avg = s / 5

print(f"Average: {avg}")
```

With sample input and output

```sh
Enter a positive number: 2
Enter a positive number: 3
Enter a positive number: 4
Enter a positive number: 7
Enter a positive number: 8
Average: 4.8
```

#### Example 2

In this snippet, we will take a long space-separated `string` and print out the words and their corresponding number of characters.

```python
# we are will not be using any function
text = "looping through name without index"

size = 0
word = ""

for ch in text:
    if ch != " ":
        size += 1
        word += ch
    else:
        print(f"{word} = {size}")
        size = 0
        word = ""

```

There above snippet can be reduced to just three lines.

```python
text = "looping through name without index"

for word in text.split():
    print(f"{word} = {len(word)}")

```
