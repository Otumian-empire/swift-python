# Exercise 5 c (Implementation of a solution)

In this stage, we write the code based on the design and then go further on to test and debug our code. We are going to change the design to a valid Python code.

```Python
'''
The inputs:
    totalNumberStudent: int = 5
    listOfScore: list = 40, 78, 91, 59 and 12
    overallScore: int = 100

The processes:
    sumOfScores: float = sum of all the elements in listOfScore
    averageOfScores: float = sumOfScores / totalNumberStudent
    numberAboveAverage = number of elements greater than the average
    numberBelowAverage = number of elements less than the average

The output:
    sumOfScores: float
    averageOfScores: float
    numberAboveAverage: int
    numberBelowAverage: int
'''
```

## Code 1

```Python
# The inputs
totalNumberStudent = 5

# the scores of the five students
# our listOfScore
s1 = 40
s2 = 78
s3 = 91
s4 = 59
s5 = 12

overallScore = 100

# sum of all the elements in listOfScore
sumOfScores = s1 + s2 + s3 + s4 + s5

# the average
averageOfScores = sumOfScores / totalNumberStudent

# the number of students who had a score greater than the average
# initialize two variables, numberAboveAverage and numberBelowAverage to zero
# compare each student score with the average
# if the score is greater than the average, add one to numberAboveAverage else (it may mean is equal to or less than) do nothing here.

numberAboveAverage = 0

if s1 > averageOfScores:
    numberAboveAverage += 1

if s2 > averageOfScores:
    numberAboveAverage += 1

if s3 > averageOfScores:
    numberAboveAverage += 1

if s4 > averageOfScores:
    numberAboveAverage += 1

if s5 > averageOfScores:
    numberAboveAverage += 1

numberBelowAverage = 0

if s1 < averageOfScores:
    numberBelowAverage += 1

if s2 < averageOfScores:
    numberBelowAverage += 1

if s3 < averageOfScores:
    numberBelowAverage += 1

if s4 < averageOfScores:
    numberBelowAverage += 1

if s5 < averageOfScores:
    numberBelowAverage += 1

# the outputs
print("The sum of all the scores is", sumOfScores)
print("The average score is", averageOfScores)
print(numberAboveAverage, "scored above average")
print(numberBelowAverage, "scored below average")
```

## Code 2

```Python
# The inputs
totalNumberStudent = 5

# the scores of the five students
# here we use a data structure known as a list
# compare this to the other, s1, s2, s3, s4, s5
# which is simpler
listOfScore = [40, 78, 91, 59, 12]

overallScore = 100

# sum of all the elements in listOfScore
# We will use a loop and initialize sumOfScores to zero
sumOfScores = 0

for score in listOfScore:
    sumOfScores += score

# the average
averageOfScores = sumOfScores / totalNumberStudent

# the number of students who had a score above than the average
# initialize two variables, numberAboveAverage and numberBelowAverage to zero
# compare each student score with the average
# if the score is greater than the average, add one to numberAboveAverage
# else (it may mean is equal to or less than) so we check if it is less than
# else it will be equal, which is of no interest to do nothing.
# we will use a loop here also

numberAboveAverage = 0
numberBelowAverage = 0

for score in listOfScore:
    if score > averageOfScores:
        numberAboveAverage += 1

    if score < averageOfScores:
        numberBelowAverage += 1

# the outputs
print("The sum of all the scores is", sumOfScores)
print("The average score is", averageOfScores)
print(numberAboveAverage, "scored above average")
print(numberBelowAverage, "scored below average")
```

## Practicals

Implement the design from the practicals in `exercise 5 b (Design of a solution)`

## Summary

- Implementation phase is where we code the design from the analysis
- Implementation is not the last phase of software development
- We have to test, maintain and document our programs to make the software
