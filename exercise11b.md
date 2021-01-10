# Excercise 11 b (While Loop)

> This is a continuation of `exercise 11 a (For Loop)`

## While loop

A while loop executes its body until a condition is met or as far as a condition is still valid.

Structure of a `while` loop

```Python
while condition:
    # do something
```

Reference `Exercise 10 (Conditions)` here.

`condition` can be the result of a relational or boolean expression.

### Example 1

Let's print hello world three times

```python
i = 0

while i < 3:
    print("Hello world")
    i += 1
```

### Example 2

Printing numbers from `1` to `10`

```python
# start from 0
number = 0

while number < 10:
    number += 1
    print(number)


# start from 1
number = 1

while number < 11:
    print(number)
    number += 1
```

### Example 3

Let's look at another snippet that prints the string, `<number> is even` if the number is even else it prints the number.

```python
number = 0

while number < 20:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(number)

    number += 1
```

What do you think would happen when we comment out `number += 1`?

### Example 4

A snippet for finding the average of five numbers.

```python
s = 0
i = 0
end = 5

while i < end:
    n = int(input("Enter a positive number: "))

    s += n
    i += 1

avg = s / end

print(f"Average: {avg}")
```

### Structure looping

We shall be looping through an iterable using a `while` loop. We shall be implementing the same code in the `for` loop.

#### Example 1

This snippet prints out each character of the string on a new line.

```python
# looping through `name` using index
name = "John Doe"

i = 0
end = len(name)

while i < end:
    print(name[i])
    i += 1
```

#### Example 2

In this snippet, we will take a long space-separated `string` and print out the words and their corresponding number of characters.

```python
# we will not be using any function
text = "looping through name without index"

size = 0
word = ""
start = 0
end = len(text)  # `len` to find the length of the string

while start < end:
    ch = text[start]

    if ch != " ":
        size += 1
        word += ch
    else:
        print(f"{word} = {size}")
        size = 0
        word = ""

    start += 1
```

In the snippet above we use the `len` function to find the length of the `text`. Let's see another implementation where the number of lines is less.

```python
text = "looping through name without index"

words = text.split()
end = len(words)
start = 0

while start < end:
    word = words[start]
    print(f"{word} = {len(word)}")

    start += 1
```

#### Note

- In the above code, without `start += 1`, the loop becomes an infinite loop. A loop that would never terminate and we would be print only the first element.
- Also assume we just say, `while True:` instead of `while start < end:`, will also not terminate.

## Break and Continue

### Break

`break` when used in a loop breaks out of the loop.

#### Example 1

```python
text = "looping through name without index"

words = text.split()
end = len(words)
start = 0

while True:
    if start < end:
        word = words[start]
        print(f"{word} = {len(word)}")

        start += 1
    else:
        break
```

In the above snippet, we introduced `if` and `else` whereby in the `else` block, we `break` from the loop.

#### Example 2

The snippet below takes in several inputs, counts them, finds the sum and the average. When the input id `done`, the number of input, sum and average is printed out as the loop breaks.

```python
s = 0
i = 0

while True:
    n = input("Enter a positive number: ")

    if n == "done":
        break

    s += int(n)
    i += 1

avg = s / i

print(f"Freq: {i}, Sum: {s}, Average: {avg}")
```

### Continue

`continue` when used in a loop skips the current iteration. Unlike the `break`, do not break out of the loop.

#### Example

a program that prints all the numbers between 1 to 100 inclusive, excepts those that are a multiple of 4 and 7. We shall use `loop` and `continue` here.

```python
for i in range(1, 101):
    if i % 4 == 0 or i % 7 == 0:
        continue
    print(i)
```

Modify this snippet, using a `while` loop.

## Practicals

- write a lift-off program using a loop.
  ```bash
  Enter liftoff time: 3
  lift off in
  3 2 1 0 - liftoff!
  ```
- Given a string of alphabets, from `a - z`, use a loop to print out the vowels ( Tips: `string of vowels, loop, condition` )
- A snail is at the bottom of a 30 foot well. Every hour the snail can climb up 3 feet, then immediately slide back down 2 feet. Write a program to find how many hours it takes for the snail to get out of the well?

## Summary

- A loop is used for repetition
- There are two types of loops, `for` and `while` loop
- `for` loop is best used when we know the range of execution
- `while` loop is best when the repetition is based on a condition
- we can nest one loop into another
- `break` terminates the loop and `continue` skips the current iteration
