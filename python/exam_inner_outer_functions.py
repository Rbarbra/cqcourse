"""Inner and Outer functions
Create two functions that work with the parameters a and b.
The first should calculate the sum of a and b.
The second one should call the first function and
then add the square of a to the result of the first function.
 Return this result added by 5.
 Please write down the definitions of the two functions."""
import math

# we define a simple function, called mathfunc that takes two
# parameters a and b, than calculates the sum and the sum will be added to the square
#a then add to the result 5

def sumfunc(a,b):
    # First we calculate addition and create two local variables
    # to store the results.
    result =  a+b
    return result
    #result = (a + b)+ a*a
    #final_result = result+5

    #return sumup, result, final_result

def sqrtfunc(a,b):
    result = sumfunc(a,b)
    result2 = result + math.sqrt(a)
    result3 = result2 + 5
    return result3

Var1 = 10
Var2 = 16

result = sqrtfunc(Var1, Var2)
# Now we can print out the result
print(result)
