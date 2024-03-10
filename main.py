import math
import time
import sys
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
        strTemp = (_str.split("\n"))
        _str = ""
        for i in strTemp:
            _str += i + " "
        _str = _str[0:len(_str)-1]
        print(_str)
        grid = np.empty((_rows,_columns), dtype=object)
        splitStr = _str.split(" ")
        for row in range(0,_rows):
            for column in range(0,_columns):
                grid[row, column] = splitStr[((row * _columns) + column)]
        return grid
    def LargestProductInAGrid(_grid, _length = 4):
        """Given a 2d array of integers, this will find the 'connect 4'
        of numbers that gives the largest product then return the product"""
        for i in _grid:
            i = int(i)
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
    def HighlyDivisibleTriangularNumber(_numFactors):
        """finds the first "triangle number" to have over _numFactors factors"""
        done = False
        index = 0
        while(not done or index > 1000000):
            index += 1
            sum = int((index/2) * (1+index))
            length = len(MathProblems.GetFactors(sum))
            if(length > math.floor(_numFactors/2)):
                done = True
                return sum
    def GetFactors(_num):
        """Gets the Factors of _num"""
        list = []
        numsToBeTested = _num/2
        for i in range(1,math.ceil(numsToBeTested)):
            if(i > numsToBeTested):
                break
            if (_num%i == 0):
                divNum = int(_num/i)
                list.append((i,divNum))
                numsToBeTested =  divNum
        uniqueList = []
        for i in list:
            new_tup = ()
            for k in reversed(i):
                new_tup = new_tup + (k,)
            if new_tup not in uniqueList:
                uniqueList.append(i)
        return uniqueList
    def ListOfObjects(_objects):
        """Seperates a string into a list by the charachter "space" """
        list = []
        num = -1
        tempObjects = _objects
        for i in _objects:
            num += 1
            if(i == " "):
                list.append(tempObjects[:num])
                tempObjects = tempObjects[num:]
                num = 0
        list.append(tempObjects)
        return list
    def LargeSum(_numDigits, _str):
        """this method will add all the numbers in _str, then find the first _numDigits digits in it. """
        objects = MathProblems.ListOfObjects(_str)
        sum = 0
        for i in objects:
            sum += int(i)
        print(sys.getsizeof(sum))
        return str(sum)[:_numDigits]
    def GetColatzSequence(_num):
        """given an integer, this will return a list of all the numbers
        that lead to 1, including 1 using a recursive setup"""
        list = []
        list.append(_num)
        while(_num != 1):
            if (_num % 2) == 0:
                _num = (int)(_num/2)
            else:
                _num = (3*_num)+1
            list.append(_num)
        return list
    def LongestColatzSequence(_num):
        """Find the integer from 1-_num that has the longest chain
        using the Colatz Sequence"""
        longestIndex = 0
        longestChain = 0
        exclusiveList = []
        for i in range(_num, 1, -1):
            tempList = MathProblems.GetColatzSequence(i)
            if len(tempList) > longestChain:
                longestIndex = i
                longestChain = len(tempList)
        return longestIndex
    def LatticePaths(_num):
        """litteraly just n choose n/2"""
        n = _num
        r = (int)(n/2)
        return (int)(math.factorial(n)/(math.factorial(r)**2))
    def PowerDigitSum(_num):
        number = 2**_num
        strNum = str(number)
        sumNum = 0
        for i in strNum:
            sumNum += (int)(i)
        return sumNum

if __name__ == '__main__':
    start_time = time.time()
    #print(MathProblems.LongestColatzSequence(999999))
    print(MathProblems.PowerDigitSum(1000))
    #print(MathProblems.LargeSum(3,"2000 6363 4000"))

    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", round(execution_time,5), "seconds")
