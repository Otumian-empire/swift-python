# exercise 5 b (Design of a solution)
> continaution of `exercise 5 a (Analysis of a solution)`

In this phase, we try to put together the information we gathered from the Anaylsis we made. Here we made provide a human readable solution that would easily be used to implement the solution. Again, we decide what data types and data structures would be used. So here, we could let the average score be an integer or a float and keep all the test scores in an array ( here a list). What should come in mind is a pseudocode ( a.k.a falsecode). From the analysis we can say:

```
The inputs:
    totalNumberStudent: int = 5`
    listOfScore: list = 40, 78, 91, 59 and 12 
    overallScore: int = 100

The processes:
    sumOfScores: float = sum of all the elements in listOfScore
    averageOfScores: float = sumOfScores / totalNumberStudent
    numberAboveAverage = number of elements greater than the average
    numberBelowAverage = number of elements less than the average

The output:
    sumOfScores
    averageOfScores
    numberAboveAverage
    numberBelowAverage
```

### Note

```
label : int - means object is of data type int ( integer). This is a just a conversion we have choose, you what you think makes it easier for you.
generally, label: type = value, where value is of type, type so label will return a value of type, type.
```

## Note
* Most of these stages are done together, because this is a small problem - which you could even implement straight forward
* Remember, it is absolutely easier to implement a solution after you have analyzed and chose which approach of the solution gave you the desired outcome, efficiently. This means, there could be more than one solution to solve the problem.

## Practicals
> Tip: look out for the given inputs ( the available parameters), the desired outputs ( what is expected), and the process ( how to get the output).

**Analyse and design a solution for the following problems.**
1. Given that a quadratic equation is of the form, `Ax^2 + Bx + C = 0`, where `A`, `B`, `C` are real parameters such that `A`, `B` is not zero. `A` and `B` are the co-efficients of `x`, of second and first degrees respectively and `c` a constant. Find and output the roots of the quadratic equation.

1. Find the Area of a circle of radius, `r`, given that `PI` is `3.143`.

1. A shop keeper sold an item of cost, `$340.00` at `$372.99` including a tax of `$2.99`. find the 
    * selling price
    * profit made
    * profit percentage
    * tax percentage

## Summary
* To analyse the problem, look out for the input, output and the process
* In the design stage, you choose what data type a value should be or be returned and a data structure, suitable to hold the values
* You choose a solution that best gives the desired outcome
* The best design is simple and readable
