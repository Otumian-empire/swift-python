# Exercise 5 b (Design of a solution)

> continuation of `exercise 5 a (Analysis of a solution)`

In this phase, we try to put together the information we gathered from the analysis we made. Here we may provide a human-readable solution that would be used to implement the solution. Again, we decide what data types and data structures that would be used. So here, we could let the average score be an integer or a float and keep all the test scores in an array ( here a list). What should come in mind is pseudocode ( a.k.a false code). From the analysis we can say:

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

> `label: type` we used is what we discussed in `Exercise 2 ( Datatypes) - Type hinting`

## Note

- Most of these stages are done together because this is a small problem - which we could even implement straight forward
- Remember, it is easier to implement a solution after we have analyzed and chose which approach of the solution gave us the desired outcome, efficiently. This means, there could be more than one solution to solve the problem.

## Practicals

> Tip: look out for the given inputs ( the available parameters), the desired outputs ( what is expected), and the process ( how to get the output).

**Analyse and design a solution for the following problems.**

1. Given that a quadratic equation is of the form, `Ax^2 + Bx + C = 0` , where `A` , `B` , `C` are real parameters such that `A` , `B` is not zero. `A` and `B` are the coefficients of `x`, of second and first degrees respectively and `c` a constant. Find and output the roots of the quadratic equation.

1. Find the Area of a circle of radius, `r`, given that `PI` is `3.143`.

1. A shop keeper sold an item of cost, `$340.00` at `$372.99` including a tax of `$2.99` .find the
   - selling price
   - profit made
   - profit percentage
   - tax percentage

## Summary

- To analyse the problem, look out for the input, output and the process
- In the design stage, we choose what data type a value should be or be returned and a data structure, suitable to hold these values
- We choose a solution that best gives the desired outcome
- The best design is simple and readable
