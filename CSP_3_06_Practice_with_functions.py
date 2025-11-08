#Herons Formula
import math

#returns the square root of the number n
def root(n):
    return math.sqrt(n)

#Takes in the 3 side lengths of a triangle as arguments and returns half of
#the perimeter of a triangle.
def semiPerimeter(num1,num2,num3):
    return(num1/2+num2/2+num3/2)

    pass
# number1=int(input("Give me an number"))
# number2=int(input("Give me an number"))
# number3=int(input("Give me an number"))
# ans=semiPerimeter(number1,number2,number3)
# print(ans)

def multiplyDifferences(s,num1,num2,num3):
    return s*(s-num1)*(s-num2)*(s-num3)
    pass

#Given the 3 sides of a triangle return the area.
#use herons formula
#Use the functions above.
def herons(num1,num2,num3):
    semi=semiPerimeter(num1, num2, num3)
    Area = multiplyDifferences(semi, num1,num2,num3)
    return math.sqrt(Area)
    return
# number4=int(input("Give me an number"))
# number5=int(input("Give me an number"))
# number6=int(input("Give me an number"))
# ans1=herons(number4,number5,number6)
# print(ans1)

#quadratic equation

#takes in a number as an argument and returns that number multiplied by 2.
def denominator(num1):
    return num1*2
    pass
# number7=int(input("Give me an number"))
# ans2=denominator(number7)
# print(ans2)
#Takes in two arguments. multiply the first argument by negative 1. Then
#return the modified first argument added and subtracted by the second argument.
def plusMinus(num1,num2):
    negative=num1*(-1)
    return negative+num2, negative-num2
pass

#takes in three numbers as arguments. The first and third multiplied together then
#multiplied by 4.Then subtract that result from the second argument squared.
#Return the overall result.
def mainCalc(num1,num2,num3):
    product1=num1*num3*4
    squared=num2*num2
    return squared-product1
    pass

#The below function should take the inputs of the quadratic equation and return the result
#Make sure to use all the formulas from this section.
def quadratic(num1,num2,num3):
    a,b = (plusMinus(num2,(math.sqrt(mainCalc(num1,num2,num3)))))

    return a/(2*num1),b/(2*num1)
    pass
