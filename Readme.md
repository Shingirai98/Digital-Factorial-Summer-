# Digital Factorial Summer 
## Shingirai Denver Maburutse

### Overview
As a programmer writes code they are not only looking to have a program that works, they are also making sure it fully utilizes the memory and time resources effectively.

The function of this code is to find the sum of a digitized factorial product. The user inputs a value. The value is then changed to an integer in order for it to be acted upon by mathematical functions and operations.
In order for the factorial product to be separated to digits it first needs to be an iteratable type. Therefore it is type casted to a string. The list function was then used to separate the string into a list of characters. After listifying the factorial, the mapping function was then used to convert the characters to integers in order to be able to use the numpy library onto the list. 
The numpy sum function is then used to add the constituent elements in the numpy array

To make the program as space efficient as possible, there was no assignment operator utilization whatsoever. The functional programming paradigm was used to limit memory allocation to pointers alone. The caveat was having code that is slightly more challenging to read but this was mitigated by very descriptive comments. A Lambda function was used to write an anonymous function that recursively calcultes the factorial of a number (user-input)

## Requirements
* Use python3
* Use numpy for math operations 
* Do not cast variables
* Containerize with Docker 

## Functions used
* cast: type casts a list from one type to another
  * args -> (i)arr - input array to be type casted  (ii) datatype - type to be passed to

* fact: a recursive function to calculate a factorial of an input integer
  * args ->num - input integer to be calculated factorial from 

* summing: Calculates the sum of array constituents
  * args ->arr - input array to be summed up