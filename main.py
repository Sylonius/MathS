import math
import time
import numpy as np

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
        """Given an integer, and possibly 2 others. this method will find the smallest number that
        can evenly divide into each number ex: SmallestMultiple(4) would be 12"""
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
    def SumSquareDifference(num1):
        """Given an integer, this will return (1+2+3 + ... + num)^2 - (1^2 + 2^2 + 3^2 ... + num^2)"""
        sumOfSquares = 0
        for i in range(num1+1):
            sumOfSquares += i**2
        squareOfSum = 0
        for i in range(num1+1):
            squareOfSum += i
        squareOfSum = squareOfSum**2
        return squareOfSum-sumOfSquares
    def FindPrimeByIndex(num1):
        """given an index of prime, Ex: 2=1, 3=2, 5=3, 7=4, 11=5 etc. this method fill find
        that index"""
        currentIndex = -1
        currentNum = 0
        while(currentIndex < num1):
            currentNum += 1
            if(MathProblems.CheckIfPrime(currentNum)):
                currentIndex += 1
        return currentNum
    def CheckIfPrime(num1):
        """Helper method to check if num1 is a prime number"""
        isStillPrime = True
        for i in range (2, math.ceil((num1 + 2)/2)):
            if (num1 % i == 0):
                isStillPrime = False
                break
        return isStillPrime
    def LargestProductInASeries(seriesLength, _largeNum):
        """given a length of numbers and a huge number (given as a string), this method will find the largest
        string of numbers that are adjacent with a length that is given, that give the
        largest number when each character is multipled together"""
        largestResultSoFar = 0
        for set in range (len(_largeNum) + 1):
            currentString = _largeNum[set: set + seriesLength]
            nums = []
            for index in range(len(currentString)):
                nums.append(int((currentString[index:index+1])))
            tempResult = 1
            for num in nums:
                tempResult *= num
            if(tempResult > largestResultSoFar):
                largestResultSoFar = tempResult
        return largestResultSoFar
    def SpecialPythagoreanTriple(num1):
        """Given an integer, this method will find the first set of number where
        a^2 + b^2 = c^2 and a+b+c = num1 then return a*b*c"""
        for a in range(1,num1):
            for b in range(1,num1):
                c = math.sqrt(a**2 + b**2)
                if((a+b+c) == num1):
                    return a*b*c
        return False
    def SummationOfPrimes(num1):
        """finds the sum of all the primes below num1"""
        num = 0
        for index in range(2,num1):
            if(MathProblems.CheckIfPrime(index)):
                num += index
        return(num)
    def ParseStrToGrid(_rows, _columns, _str):
        """Given 3 integers and a string, this method will
         parse that string then return a 2D array (pretty self-explanatory)"""
        grid = np.empty((_rows,_columns), dtype=object)
        splitStr = _str.split(" ")
        for row in range(0,_rows):
            for column in range(0,_columns):
                grid[row,column] = int(splitStr[((row*_columns)+column)])
        return grid
    def LargestProductInAGrid(_grid, _length = 4):
        """Given a 2d array of integers, this will find the 'connect 4'
        of numbers that gives the largest product then return the product"""
        width = _grid.shape[0]
        height = _grid.shape[1]
        largestNumSoFar = 0
        #Test the Up/Down
        for x in range(0,width-1):
            for y in range(0, height - (_length-1)):
                tempNum = _grid[y, x] * _grid[y + 1, x] * _grid[y + 2, x] * _grid[y + 3, x]
                if(tempNum > largestNumSoFar):
                    largestNumSoFar = tempNum
        #Test the Left/Right
        for x in range(0,width-(_length-1)):
            for y in range(0,height):
                tempNum = _grid[y, x] * _grid[y, x + 1] * _grid[y, x + 2] * _grid[y, x + 3]
                if (tempNum > largestNumSoFar):
                    largestNumSoFar = tempNum
        # Test the TL-BR Diaganol
        for x in range(0,width-(_length-1)):
            for y in range(0, height-(_length - 1)):
                tempNum = _grid[y,x] * _grid[y+1,x+1] * _grid[y+2,x+2] * _grid[y+3,x+3]
                if (tempNum > largestNumSoFar):
                    largestNumSoFar = tempNum
        #Test the TR-BL Diagonal
        for x in range(0,width-(_length-1)):
            for y in range(0, height-(_length - 1)):
                tempNum = _grid[y+3,x] * _grid[y+2,x+1] * _grid[y+1,x+2] * _grid[y,x+3]
                if (tempNum > largestNumSoFar):
                    largestNumSoFar = tempNum
        return largestNumSoFar
if __name__ == '__main__':
   # print(MathProblems.ParseStrToGrid(3,2, 2, "hynflajidhfoipuasdhvzlbvdghklqwejghevjioh weiorjhalwjkfhlwkjf"))
     print(MathProblems.LargestProductInAGrid(MathProblems.ParseStrToGrid(20,20,"08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48")))
    #start_time = time.time()
    #your function here
    #end_time = time.time()
    #execution_time = end_time - start_time
    #print("Execution time:", round(execution_time,5), "seconds")