import math
import time

class CommonlyUsedFunctions:
    def pow(x,n):
        return x**n

class MathProblems:
    def MultiplesOf3Or5(num):
        """Input an integer "num" then this will sum every integer
        from 0-"num" that is evenly divisible by 3 or 5"""
        sum = 0
        for i in range(num):
            if (i%3 == 0 or i%5 == 0):
                sum += i
        return sum
    def EvenFibonacciNumbers(self):
        """Input an integer "num" this method will then sum every even integer
        in the fibonacci sequence from 0-"num" """
        sum = 2
        a = 1
        b = 2
        i = 0
        while i < 4000000:
            nextFib = a + b
            if(nextFib%2 == 0):
                sum += nextFib
            a = b
            b = nextFib
            i = b
        return sum
    def LargestPrimeFactor(num):
        """finds the largest prime number of "num" """
        manipulatedNum = num
        fullyFactored = False
        lst = []
        while fullyFactored == False:
            foundAFactor = False
            i = 2
            while foundAFactor == False:
                if(manipulatedNum % i == 0):
                    foundAFactor = True
                    manipulatedNum /= i
                    lst.append(i)
                i += 1
                if(i == manipulatedNum):
                    fullyFactored = True

        lst.sort(reverse=True)
        print(lst)
        return  lst[0]
    def LargestPalindromeProduct(num):
        """Given an integer "num" this method will find the largest Palindrome that
        is the result of choose[0-"num"] * choose[0-"num"] """
        largestPalYet = 0
        for firstNumber in range(num,0,-1):
            for secondNumber in range(num, 0, -1):
                tempString = str(firstNumber * secondNumber)
                length = len(tempString)
                if(length%2 == 1 and length != 1):
                    tempString = tempString[:math.floor(length/2)] + tempString[math.ceil((length/2)):]
                    length = len(tempString)
                firstHalf = tempString[:math.floor(length/2)]
                secondHalf = tempString[math.ceil((length/2)):]
                secondHalf = secondHalf[::-1]
                if(firstHalf == secondHalf and tempString != "" and tempString != " "):
                    if(int(tempString) > int(largestPalYet)):
                        largestPalYet = tempString
        return largestPalYet
    def SmallestMultiple(num2, num1 = 1, increment = 1):
        if(num1 > num2):
            tempNum = num1
            num1 = num2
            num2 = tempNum
        n = 1
        while (True): #janky do while loop
            didEvenlyDivide = True
            for i in range(num2,num1,-increment):
                if(n % i != 0):
                    didEvenlyDivide = False
                    break
            if (didEvenlyDivide == False): #condition
                n += 1
                continue
            else:
                break
        return n

if __name__ == '__main__':
    for i in range(1,20):
        start_time = time.time()
        print(MathProblems.SmallestMultiple(i), i)
        end_time = time.time()
        execution_time = end_time - start_time
        print("Execution time:", round(execution_time,5), "seconds")