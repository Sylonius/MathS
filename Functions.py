import math
import sys
import numpy as np
from collections import Counter


#------------------------------------1 through 100------------------------------------------------

def f001_MultiplesOf3Or5(num = 1000):
    """Input an integer "num" then this will sum every integer
    from 0-"num" that is evenly divisible by 3 or 5"""
    sum = 0
    for i in range(num):
        if (i % 3 == 0 or i % 5 == 0):
            sum += i
    return sum
def f002_EvenFibonacciNumbers(_num = 4000000):
    """Input an integer "num" this method will then sum every even integer
    in the fibonacci sequence from 0-"num" """
    sum = 2
    a = 1
    b = 2
    i = 0
    while i < _num:
        nextFib = a + b
        if (nextFib % 2 == 0):
            sum += nextFib
        a = b
        b = nextFib
        i = b
    return sum
def f003_LargestPrimeFactor(_num = 600851475143):
    """finds the largest prime factor of "num" """
    manipulatedNum = _num
    fullyFactored = False
    lst = []
    while fullyFactored == False:
        foundAFactor = False
        i = 2
        while foundAFactor == False:
            if (manipulatedNum % i == 0):
                foundAFactor = True
                manipulatedNum /= i
                lst.append(i)
            i += 1
            if (i == manipulatedNum):
                fullyFactored = True

    lst.sort(reverse=True)
    return lst[0]
def f004_LargestPalindromeProduct(num = 999):
    """Given an integer "num" this method will find the largest Palindrome that
    is the result of choose[0-"num"] * choose[0-"num"] """
    largestPalYet = 0
    for firstNumber in range(num, 0, -1):
        for secondNumber in range(num, 0, -1):
            tempString = str(firstNumber * secondNumber)
            length = len(tempString)
            if (length % 2 == 1 and length != 1):
                tempString = tempString[:math.floor(length / 2)] + tempString[math.ceil((length / 2)):]
                length = len(tempString)
            firstHalf = tempString[:math.floor(length / 2)]
            secondHalf = tempString[math.ceil((length / 2)):]
            secondHalf = secondHalf[::-1]
            if (firstHalf == secondHalf and tempString != "" and tempString != " "):
                if (int(tempString) > int(largestPalYet)):
                    largestPalYet = tempString
    return largestPalYet
def f005_SmallestMultiple(_maxNum = 20, _increment = 1):
    """Second attempt at Q5 using a technique of testing if each item has its divisors in the list then multiplying them together"""
    masterFactorList = [(1,1)]
    for i in range(2, _maxNum + 1, _increment): #starts at 2 and increases by increment each time, it is possible maxNum is not a part of the loop
        factors = Tools.CanonicalPrimeFactorisation(i)
        for factor in factors:
            if factor[0] not in [item[0] for item in masterFactorList]:  # if factor not in masterList
                masterFactorList.append(factor)
            for i in range(len(masterFactorList)):
                if factor[0] == masterFactorList[i][0] and factor[1] > masterFactorList[i][1]: # if referencing same number but different power
                    masterFactorList[i] = factor
    multiplyResult = 1
    for factor in masterFactorList:
        multiplyResult *= (factor[0]**factor[1])
    return multiplyResult
def f005_a1_SmallestMultiple(num2 = 20, num1 = 1, increment = 1):
    """Given an integer, and possibly 2 others. this method will find the
    smallest trianglular number that can evenly divide into each number
    ex: SmallestMultiple(4) would be 12"""
    if (num1 > num2):
        tempNum = num1
        num1 = num2
        num2 = tempNum
    n = 1
    while (True):  # janky do while loop
        didEvenlyDivide = True
        for i in range(num2, num1, -increment):
            if (n % i != 0):
                didEvenlyDivide = False
                break
        if (didEvenlyDivide == False):  # condition
            n += 1
            continue
        else:
            break
    return n
def f006_SumSquareDifference(num1 = 100):
    """Given an integer, this will return (1+2+3 + ... + num)^2 - (1^2 + 2^2 + 3^2 ... + num^2)"""
    sumOfSquares = 0
    for i in range(num1 + 1):
        sumOfSquares += i ** 2
    squareOfSum = 0
    for i in range(num1 + 1):
        squareOfSum += i
    squareOfSum = squareOfSum ** 2
    return squareOfSum - sumOfSquares
def f007_FindPrimeByIndex(_num = 10001):
    """given an index of prime, Ex: 2=1, 3=2, 5=3, 7=4, 11=5 etc. this method will find
        that index using the sieve of Eratosthenes and a max n of "int(n * (math.log(n) + math.log(math.log(n)))) + 1" """
    max = 0
    if _num < 7:
        max = _num ** 2
    else:
        max = int(_num * (math.log(_num) + math.log(math.log(_num)))) + 1
    primeList = Tools.SieveOfEra(max)
    return primeList[_num-1]
def f007_a1_FindPrimeByIndex(num1 = 10001):
    """given an index of prime, Ex: 2=1, 3=2, 5=3, 7=4, 11=5 etc. this method will find
    that index using CheckIfPrime function"""
    currentIndex = 0
    currentNum = 0
    while (currentIndex < num1):
        currentNum += 1
        if (Tools.CheckIfPrime(currentNum)):
            currentIndex += 1
    return currentNum
def f007_a2_FindPrimeByIndex(num1 = 10001):
    """given an index of prime, Ex: 2=1, 3=2, 5=3, 7=4, 11=5 etc. this method fill find
    that index (unused)"""
    currentIndex = 0
    currentNum = 0
    while (currentIndex < num1):
        currentNum += 1
        if (Tools.CheckIfPrime(currentNum)):
            currentIndex += 1
    return currentNum
def f008_LargestProductInASeries(seriesLength = 13, largeNum = open(r"E:\Python IDE\Projects\MathS\Refrence Files\Problem_8.txt", "r").readline()):
    """given a length of numbers and a huge number (given as a string), this method will find the largest
    string of numbers that are adjacent with a length that is given, that give the
    largest number when each character is multipled together"""
    largestResultSoFar = 0
    for set in range(len(largeNum) + 1):
        currentString = largeNum[set: set + seriesLength]
        nums = []
        for index in range(len(currentString)):
            nums.append(int((currentString[index:index + 1])))
        tempResult = 1
        for num in nums:
            tempResult *= num
        if (tempResult > largestResultSoFar):
            largestResultSoFar = tempResult
    return largestResultSoFar
def f009_SpecialPythagoreanTriple(num1 = 1000):
    """Given an integer, this method will find the first set of number where
    a^2 + b^2 = c^2 and a+b+c = num1 then return a*b*c"""
    for a in range(1, num1):
        for b in range(1, num1):
            c = math.sqrt(a ** 2 + b ** 2)
            if ((a + b + c) == num1):
                return int(a * b * c)
    return False
def f010_SummationOfPrimes(_num = 2000000):
    """finds the sum of all the primes below _num ussing the sieve of Eratosthenes"""
    prime = [True] * (_num + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(_num**0.5) + 1):
        if prime[i]:
            for j in range(i*2, _num + 1, i):
                prime[j] = False
    primeList = []
    for i in range(2,_num):
        if prime[i] == True:
            primeList.append(i)
    sum = 0
    for num in primeList:
        sum += num
    return sum
def f010_a1_SummationOfPrimes(num1 = 2000000):
    """finds the sum of all the primes below num1 (unupdated attempt)"""
    num = 0
    for index in range(3, num1, 2):
        if (Tools.CheckIfPrime(index)):
            num += index
            print(index)
    return (num)
def f011_LargestProductInAGrid(_length=4, _str = open(r"E:\Python IDE\Projects\MathS\Refrence Files\Problem_11.txt", "r").read()):
    """Given a 2d array of integers (change in method), this will find the 'connect 4'
    of numbers that gives the largest product then return the product"""
    strGrid = Tools.ParseStrToGrid(20,20, _str)
    intGrid = [[int(x) for x in sub] for sub in strGrid]
    _grid = np.array(intGrid)

    width = _grid.shape[0]
    height = _grid.shape[1]
    largestNumSoFar = 0
    # Test the Up/Down
    for x in range(0, width - 1):
        for y in range(0, height - (_length - 1)):
            tempNum = _grid[y, x] * _grid[y + 1, x] * _grid[y + 2, x] * _grid[y + 3, x]
            if (tempNum > largestNumSoFar):
                largestNumSoFar = tempNum
    # Test the Left/Right
    for x in range(0, width - (_length - 1)):
        for y in range(0, height):
            tempNum = _grid[y, x] * _grid[y, x + 1] * _grid[y, x + 2] * _grid[y, x + 3]
            if (tempNum > largestNumSoFar):
                largestNumSoFar = tempNum
    # Test the TL-BR Diaganol
    for x in range(0, width - (_length - 1)):
        for y in range(0, height - (_length - 1)):
            tempNum = _grid[y, x] * _grid[y + 1, x + 1] * _grid[y + 2, x + 2] * _grid[y + 3, x + 3]
            if (tempNum > largestNumSoFar):
                largestNumSoFar = tempNum
    # Test the TR-BL Diagonal
    for x in range(0, width - (_length - 1)):
        for y in range(0, height - (_length - 1)):
            tempNum = _grid[y + 3, x] * _grid[y + 2, x + 1] * _grid[y + 1, x + 2] * _grid[y, x + 3]
            if (tempNum > largestNumSoFar):
                largestNumSoFar = tempNum
    return largestNumSoFar
def f012_HighlyDivisibleTriangularNumber(_numFactors = 500):
    """finds the first "triangle number" to have over _numFactors factors"""
    done = False
    index = 0
    while (not done or index > 1000000):
        index += 1
        sum = int((index / 2) * (1 + index))
        length = len(Tools.GetFactors(sum))
        if (length > math.floor(_numFactors / 2)):
            done = True
            return sum
def f013_LargeSum(_numDigits = 10, _str = open(r"E:\Python IDE\Projects\MathS\Refrence Files\Problem_13.txt", "r").read()):
    """this method will add all the numbers in _str, then find the first _numDigits digits in it. """
    objects = Tools.ListOfObjects(_str,"\n")
    sum = 0
    for i in objects:
        sum += int(i)
    #print(sys.getsizeof(sum))
    return str(sum)[:_numDigits]
def f014_LongestColatzSequence(_num = 999999):
    """Find the integer from 1-_num that has the longest chain
    using the Colatz Sequence"""
    longestIndex = 0
    longestChain = 0
    hasBeenReferenced = [False] * (_num+1)
    for i in range(_num, 1, -1):
        if not hasBeenReferenced[i]:
            tempList = Tools.GetColatzSequence(i)
            for item in tempList:
                if item <= _num:
                    if not hasBeenReferenced[item]:
                        hasBeenReferenced[item] = True
            if len(tempList) > longestChain:
                longestIndex = i
                longestChain = len(tempList)
    return longestIndex
def f015_LatticePaths(_num = 20):
    """litteraly just n choose n/2 with n being the total moves which is _num * 2"""
    n = _num * 2
    r = (int)(n / 2)
    return (int)(math.factorial(n) / (math.factorial(r) ** 2))
def f016_PowerDigitSum(_num = 1000):
    """This will find the sum of each individual digit in 2^_num"""
    number = 2 ** _num
    strNum = str(number)
    sumNum = 0
    for i in strNum:
        sumNum += (int)(i)
    return sumNum
def f017_NumberLetterCounts(_num = 1000):
    """this method finds the sum of all the letters in
    "one" + "two" + "three" +...+_num"""
    totalLength = 0
    for i in range(1, _num + 1):
        strToBeParsed = Tools.NumberToWords(i)
        parsedArray = strToBeParsed.split(' ')
        parsedString = ""
        for i in parsedArray:
            parsedString += i
        tempLength = len(parsedString)
        totalLength += tempLength
    return totalLength
def f018_MaximumPathSumOne(_str = open(r"E:\Python IDE\Projects\MathS\Refrence Files\Problem_18.txt", "r").read()):
    """Given a string that is a triangle in shape, this function will find the greatest path"""
    objects = Tools.ListOfObjects(_str, "\n")
    gridHeight = 15
    pyramid = Tools.ParseStrToGrid(gridHeight, gridHeight, _str)
    # print(pyramid)
    grid = np.empty((gridHeight, gridHeight), dtype=object)
    for i in range(gridHeight - 1, -1, -1):
        for j in range(0, gridHeight):
            # done from left to right, bottom to top
            if (i + 2 > gridHeight):  # if to low
                grid[i, j] = pyramid[i, j]  # be your own value(you are at the bottom)
            elif (j - 1 < gridHeight - (gridHeight - i)):  # not to far to the right
                num1 = int(pyramid[i, j]) + int(grid[i + 1, j + 1])
                num2 = int(pyramid[i, j]) + int(grid[i + 1, j])
                greaterNum = num1
                if num2 > num1:
                    greaterNum = num2
                grid[i, j] = str(greaterNum)  # be the value of the two below values
    # print(grid)
    # return(grid[0,0])
    return (grid[0][0])
def f019_CountingSundays(_startYear = 1901, _endYear = 2000):
    """Making a function that returns how many Sundays fell on the first of the month during the twentieth century"""
    """using the fact that we can figure out the first of every day given just Jan 1, we can calculate Jan 1 by simply running (365 + leap) % 7"""
    sundayCount = 0
    for year in range(_startYear, _endYear+1):
        monthArray = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
        centuryNums = [2, 0, 5, 3]
        leapYears = math.floor((year % 100) / 4)
        centuryNum = centuryNums[math.floor((year % 400) / 100)]
        doomsdayNumber = (centuryNum + leapYears + (year % 100)) % 7
        #print(year, "|", doomsdayNumber)
        janFirst = (doomsdayNumber -2)
        if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
            janFirst -= 1
            for month in range(2,12):
                monthArray[month] += 1
                monthArray[month] % 7
        janFirst = janFirst % 7
        for month in range(12):
            if (monthArray[month] + janFirst) % 7 == 0:
                print("year ", year, "|month ", month+1, " was a sunday")
                sundayCount += 1
        #print(year, "|", janFirst)
    return sundayCount
def f020_FactorialDigitSum(_num = 100):
    """Adds the digits of the factorial of _num"""
    nums = Tools.factorial(_num)
    numsStr = str(nums)
    total = 0
    for i in numsStr:
        total += int(i)
    return total
def f021_AmicableNumbers(_num = 10000):
    listOfPairs = []
    for i in range(1, _num + 1):
        divisors = Tools.GetProperDivisors(i)
        divisorSum = 0
        for j in divisors:
            divisorSum += j
        listOfPairs.append((i, divisorSum))
        # works up to here
    amicableSum = 0
    for item in listOfPairs:
        if item[0] != item[1]:  # if both values are not the same
            tempTuple = (item[1], item[0])
            if tempTuple in listOfPairs:
                amicableSum += item[0]

    return amicableSum
def f022_NamesScores(fileString = open(r"E:\Python IDE\Projects\MathS\Refrence Files\Problem_22.txt", "r").read()):
    myList = fileString.split(",")
    myList.sort()
    increment = 0
    for item in myList:
        item = item[1:-1]
        myList[increment] = item
        increment += 1

    nameIncrement = 0
    totalValue = 0
    for item in myList:
        nameIncrement += 1
        wordVal = 0
        for char in item:
            wordVal += ord(char) - 64
        totalValue += (wordVal * nameIncrement)

    return totalValue
def f023_NonAbundantSums():
    abundantList = []
    for i in range(11, 28124):
        tempList = Tools.GetProperDivisors(i)
        listTotal = 0
        for item in tempList:
            listTotal += item
        if listTotal > i:
            abundantList.append(i)
    #print(abundantList)
    #print(len(abundantList))

    sum = 0
    sumList = []
    for i in abundantList:
        j = 0
        aj = 0
        while (i+aj) <= 28124:
            aj = abundantList[j]
            sumList.append(i+aj)
            #print("added i" +str(i) + "|j " + str(aj))
            j += 1
    #print("computed sums!")
    #print(len(sumList))
    uniqueList = list(set(sumList))
    #print("computed uniques")
    for i in range(1,28124):
        if i not in uniqueList:
            sum += i
            #print("sum " + str(sum))
    return sum
def f024_LexicographicPermutations(_size = 10, permutationIndex = 999999):
    """When listing all permutations in numerical order find the purmutationIndex in that order"""
    myList = Tools.AllPermutations(_size)
    return myList[permutationIndex]
def f025_ThousandDigitFibonacciNumber(_digits = 1000):
    """returns the index of the first fibonacci number that is _digits digits long"""
    attempts = 0
    fibboLen = 0
    checkTuple = (1, 1)
    while (fibboLen < _digits and attempts < 1000000):
        attempts += 1
        checkTuple = Tools.FibonacciHelper(checkTuple)
        fibboLen = len(str(checkTuple[1]))
    return attempts + 2  # to account for starting tuple add 2
def f026_ReciprocalCycles(_size = 999):
    """for 1/n where n goes from 1 to _size find the longest cycle and returns n"""
    # uses a really cool method where the first instance of 10^k mod n = 1 then k is number of repeating digits
    # just make sure that the number n is coprime with 10, if not then use only the coprime part ex: 28 = 2^2 * 7 so just use 7
    largestIndexSoFar = (0, 0)
    for n in range(2, _size + 1):
        number1HasBeenReached = False
        k = 0
        primeFactors = Tools.PrimeFactorisation(n)
        if not (2 in primeFactors or 5 in primeFactors):
            while not number1HasBeenReached and k <= n:
                k += 1
                result = 10 ** k % n
                if result == 1:
                    if k > largestIndexSoFar[0]:
                        largestIndexSoFar = (k, n)
                        number1HasBeenReached = True
                        #print("The number " + str(n) + " repeats " + str(k) + " times.")
                    else:
                        break
    return largestIndexSoFar[1]
def f027_QuadraticPrimes(_size = 1000):
    """for a given size find the formula of n^2 + an + b that gives the most consecutive prime numbers and return a * b"""
    bestSoFar = (0, 0, 0)  # in (a, b, consecutiveTerms)
    for a in range(-_size + 1, _size):
        for b in range(-_size, _size + 1):
            testMax = (bestSoFar[2]**2 + a * bestSoFar[2] + b)
            if (testMax > 1):   #optimisation because if the new test is negative at best then we don't need to check it
                #if (Tools.CheckIfPrime(testMax)):
                    consecutiveTerms = 0
                    n = 0
                    stillConsecutive = True
                    while stillConsecutive:
                        #print(a)
                        isPrime = Tools.CheckIfPrime(abs(n ** 2 + a * n + b))
                        #if bestSoFar[2] == 71 and a == b and a > 990:
                            #pass
                        if isPrime:
                            n += 1
                            consecutiveTerms += 1
                            if consecutiveTerms > bestSoFar[2]:
                                bestSoFar = (a, b, consecutiveTerms)
                        else:
                            stillConsecutive = False
    return bestSoFar[0] * bestSoFar[1]
def f028_NumberSprialDiagonals(_radius = 501):
    """This number finds the sum of the diagonals when a spiral is formed
    by numbers that increase steadily """
    total = 0
    for i in range(0, 4):
        for n in range(2, _radius + 1):
            total += ((2 * n - 1) ** 2 - (2 * i * (n - 1)))
    total += 1
    return total
def f029_DistinctPowers(_aMax = 100, _bMax = 100):
    """for all combinations of a^b find the number of unique combinations"""
    masterList = []
    for a in range(2, _aMax + 1):
        for b in range(2, _bMax + 1):
            tempFactors = Tools.PrimeFactorisation(a)
            tempList = []
            tempList += tempFactors
            for power in range(b - 1):
                tempList += tempFactors
            tempList.sort()
            masterList.append(tempList)
    seen = []
    for item in masterList:
        if item not in seen:
            seen.append(item)
    # return seen
    return len(seen)
def f030_DigitFifthPowers(_power = 5):
    """This function finds every number where the sum of its digits to a given
    power are equal to the number itself, then sums all those numbers"""
    powerArray = [0,1]
    canBeWritten = []
    for i in range(2,10):
        powerArray.append(i ** _power)
    for i in range(2,powerArray[9]*_power):
        strVal = str(i)
        tempSum = 0
        for charVal in strVal:
            tempSum +=  int(powerArray[int(charVal)])
        if tempSum == i:
            canBeWritten.append(i)
    sum = 0
    for item in canBeWritten:
        sum += item
    return sum
def f031_CoinSums(_goal = 200, _coins = [1,2,5,10,20,50,100,200], _index = 0):
    """This function tries to find every possible combination
    of coins that will lead to the goal value, AI assisted"""
    if _goal == 0:
        return 1
    if _goal < 0:
        return 0

    ways = 0
    for i in range(_index, len(_coins)):
        ways += f031_CoinSums(_goal - _coins[i], _coins, i)
    return ways
def f032_PandigitalProducts():
    """This function will find every number where it has a factor set that
    when the product, multiplier, and multiplicad are together they contain
    the digits 1-9"""
    goodList = []
    for x in range(1,10): #must be a 1 digit number by a 4 digit number
        for y in range(1000,10000):
            i = x*y
            strVal = str(x) + str(y) + str(i)
            strVal = ''.join(sorted(strVal))
            if strVal == "123456789":
                if(i not in goodList):
                    goodList.append(i)

    for x in range(1,100): #must be a 2 digit number by a 3 digit number
        for y in range(100,1000):
            i = x*y
            strVal = str(x) + str(y) + str(i)
            strVal = ''.join(sorted(strVal))
            if strVal == "123456789":
                if(i not in goodList):
                    goodList.append(i)

    sum = 0
    for i in goodList:
        sum += i
    return sum
def f033_DigitCancellingFractions():
    """This function will find all fractions where if you remove the
    same digit from the bottom and top you get the same as a version of that fraction
    ex: 49/98 = 4/8 so just remove the 9, it then sums the simplified fractions and returns the denominator"""
    fracList = []
    for x in range(1,10):
        for y in range(2,10):
            for changeNum in range(1,10):
                decVal = float(x)/float(y)
                if decVal < 1:
                    tryVals = []
                    tryVals.append((x*10 + changeNum, y*10 + changeNum))
                    tryVals.append((x*10 + changeNum, y + changeNum*10))
                    tryVals.append((x + changeNum*10, y*10 + changeNum))
                    tryVals.append((x + changeNum*10, y + changeNum*10))
                    for frac in tryVals:
                        tempDecVal = float(frac[0])/float(frac[1])
                        if tempDecVal == decVal:
                            fracList.append(frac)
    num = 1
    den = 1
    for fraction in fracList:
        num *= fraction[0]
        den *= fraction[1]
    simplified = Tools.SimplifyFraction(num,den)
    return simplified[1]




                #try each possibility       #this bit is just unnessesary without larger numbers being needed
                #for xPos in Tools.AllPermutations(2):
                #    for yPos in Tools.AllPermutations(2):
                #        for x1 in xPos:
                #            for y1 in yPos:  #try everycombo of every permutation, which turns out to only be 4 for 2 and 2
def f034_DigitFactorials():
    """Finds the sum of all numbers which are equal
    to the sum of the factorial of their digits."""
    #the max is when each digit is 9 and 9! * digits < len(str(digits))
    #from testing the number must be less than 2,540,160, a blog from raw.org makes the max 1499999
    factorialList = []
    fullSum = 0
    for i in range(0,10):
        factorialList.append(Tools.factorial(i))
    for i in range(3,1499999): #don't count 1 or 2 as they are not sums.
        tempSum = 0
        for digit in str(i):
            tempSum += factorialList[int(digit)]
        if i == tempSum:
            fullSum += tempSum
    return fullSum
def f035_CircularPrimes(_maxNum = 100):
    """This Function finds all primes where all circular permutation of
    that number are a prime and returns how many there are"""
    doubles = []
    PrimeList = Tools.SieveOfEra(_maxNum)
    PrimeListCopy = list(PrimeList)
    for prime in PrimeListCopy:
        circularPrimes = Tools.CircularNumbers(prime)
        for circle in circularPrimes:
            if circle not in PrimeList:
                if prime in PrimeList:
                    PrimeList.remove(prime)
                break
            else:
                doubles.append(circle)
                if prime in PrimeListCopy:
                    PrimeListCopy.remove(prime)
    #PrimeList.append(doubles)
    print(PrimeList)
    return len(PrimeList)
def f035_a1_CircularPrimes(_maxNum = 100):
    """This Function finds all primes where all circular permutation of
    that number are a prime and returns how many there are (unused)"""
    PrimeList = Tools.SieveOfEra(_maxNum)
    for prime in PrimeList[:]:
        circularPrimes = Tools.CircularNumbers(prime)
        for circle in circularPrimes:
            if circle not in PrimeList:
                PrimeList.remove(prime)
                break
    return len(PrimeList)
def f036_DoubleBasePalidromes(_max = 1000000):
    DoubleBasePalindromeList = []
    pals = Tools.GeneratePalindromes(_max)
    for pal in pals:
        print(bin(int(pal))[2:])
        if Tools.CheckIfPalindrome(bin(int(pal))[2:]):
            DoubleBasePalindromeList.append(pal)
    sum = 0
    for item in DoubleBasePalindromeList:
        sum += int(item)
    return sum
def f037_TruncatablePrimes():
    goodPrimeList = []
    PrimeList = Tools.SieveOfEra(800000) #i'm just assuming this is enough *wink*
    #PrimeList = PrimeList[4:]           #each number may only contain the digits 2,3,5, and 7
    for prime in PrimeList:              #this means a new max comps of 4^6 or 4096
        prime = str(prime)
        #print(prime)
        stillPrime = True
        for i in range(1,len(str(prime))):
            if int(prime[i:]) not in PrimeList or int(prime[:len(str(prime))-i]) not in PrimeList:
                badVal1 = prime[i:]
                badVal2 = prime[:len(str(prime))-i]
                stillPrime = False
        if stillPrime:
            goodPrimeList.append(prime)
    goodPrimeList = goodPrimeList[4:]
    sum = 0
    for item in goodPrimeList:
        sum += int(item)
    return sum
def f038_PandigitalMultiples():
    """This function returns the largest pandigital number that can be made
     by concatenating multiples of a number by values of n"""
    panList = []
    for i in range(1,9999):  #examination proves that the max num must be at most 4 digits
        tempStr = ""
        for n in range(1, (9 // len(str(i)))+1): #without calculating any overflow, we can calculate the bounds of n by
            # max = 9 // len(str(i)), any more than this and you have too many digits
            # min = 2, The problem stated n must be greater than 1
            tempStr += str(i*n)
            if len(tempStr) == 9:
                if Tools.CheckIfPandigital(tempStr):
                    panList.append(tempStr)
    panList.sort()
    return panList[-1]
def f039_IntegerRightTriangles(_maxPerimeter = 1001):
    """This function finds the triangles with a permiter below a number and returns for which value
    of perimeter is the number of solutions maximised"""
    #The function to find a side length with a given perimeter and side length is
    #a + sqrt(a^{2}+b^{2}) = p-b for a given b and p, derived from a^2 + b^2 = c^2 and p = a+b+c
    maxSolutionsPerim = (120,3) #perim and numSolutions
    for p in range(3,_maxPerimeter):
        tempSolutions = (p,0)
        for b in range(1,p): #b must less than p
            #the above equation solved for a is (p*(p-(2*b)))/(2*(p-b))
            a = float(p*(p-(2*b)))/float(2*(p-b))
            if a == round(a):
                tempSolutions = (tempSolutions[0], tempSolutions[1]+1)
        if tempSolutions[1] > maxSolutionsPerim[1]:
            maxSolutionsPerim = tempSolutions
    return maxSolutionsPerim[0]
def f040_ChampernownesConstant(_max = 1000000):
    """This function multiplies the 1st, 10th, 100th... to _max digit
    of Champernowne's Constant, be aware that there is almost certainly a more
    algorithmic way of doing this. but it works well enough"""
    superString = ""
    for i in range(1,_max+1):
        superString += str(i)
    product = 1
    for power in range(1, len(str(_max))+1):
        #print(superString[10**(power-1)-1], "is the ",10**(power-1))
        product *= int(superString[10**(power-1)-1])
    return product
def f041_PandigitalPrime():
    """This function returns the largest pandigital prime by testing each num"""
    for numChars in range(9,0,-1):
        pans = Tools.AllPermutations(numChars, True)
        #print(len(pans))
        index = 0
        while index > -len(pans):
            index -= 1
            #print(int(pans[index]))
            if Tools.CheckIfPrime(int(pans[index])):
                return pans[index]
    return "None found"
def f042_CodedTriangleNumbers(_fileString = open(r"E:\Python IDE\Projects\MathS\Refrence Files\Problem_42.txt", "r").read()):
    """"""
    nameArray = _fileString.split('","')
    nameArray[0] = nameArray[0][1:]
    nameArray[-1] = nameArray[-1][:len(nameArray[-1])-1]
    numberArray = []
    for name in nameArray:
        #ord of A is 65
        wordVal = 0
        for char in name:
            wordVal += ord(char)-64
        numberArray.append(wordVal)
    #print(numberArray)
    numberArray.sort(reverse=True)
    maxNum = numberArray[0]
    index = 2
    triangleNums = [1]
    while triangleNums[-1] < maxNum:
        triangleNums.append(int((.5 * (index * (index+1)))))
        #print(triangleNums[index-1])
        index += 1
    numberOfValidWords = 0
    for name in numberArray:
        if name in triangleNums:
            numberOfValidWords += 1
    return numberOfValidWords
def f04s3_SubStringDivisibility():
    """I realised that my other version of this function had a core flaw and decided to start over
    after 2 hours :(, it is also kind of slow"""
    allowedDigits = []
    primeList = Tools.SieveOfEra(17)
    for i in range(10):
        tempTuple = ()
        for j in range(10):
            tempTuple += (j,)
        allowedDigits.append(tempTuple)
    listOfValidPandigitals = Tools.GeneratePandigitals(allowedDigits, False)
    # check each pandigital for divisibility purposes
    for pandigitalNum in listOfValidPandigitals:
        thisNumGood = True
        for primeIndex in range(len(primeList)):
            if int(str(pandigitalNum)[1 + primeIndex:4 + primeIndex]) % primeList[primeIndex] != 0:
                thisNumGood = False
                break
        if thisNumGood:
            print(pandigitalNum, " is also a good")
def f043_SubStringDivisibility():
    """Find all pandigital numbers that have the patern where their 3 digit substrings are divisible by primes
    This function will return the sum of all 0-9 pandigital numbers with this property"""
    #perms = Tools.AllPermutations(10)
    primeList = Tools.SieveOfEra(17)
    allowedDigits = [(0,1,2,3,4,5,6,7,8,9)]+[()]*9
    for primeIndex in range(len(primeList)):
        tripletAllowedDigits = ["","",""]
        tempNum = 0
        while tempNum < 1000:
            tempNum += primeList[primeIndex]
            if tempNum > 1000:
                break
            tempNumStr = "0" * (3 - len(str(tempNum)))+str(tempNum)
            print(tempNumStr)
            for i in range(3):
                tripletAllowedDigits[i] += tempNumStr[i]
        for digitSetIndex in range(len(tripletAllowedDigits)):
            tempAllowedDigits = ()
            for i in range(10):
                if str(i) in tripletAllowedDigits[digitSetIndex]:
                    tempAllowedDigits += (i,)
            tripletAllowedDigits[digitSetIndex] = tempAllowedDigits
        for i in range(3):
            #if allowedDigits[i+primeIndex+1] == "":
            #print(allowedDigits[i+primeIndex+1])
            #print(tripletAllowedDigits[i])
            allowedDigits[i+primeIndex+1] += tripletAllowedDigits[i]
    print(allowedDigits)
    #used AI to help generate the recursive section of this code
    listOfValidPandigitals = Tools.GeneratePandigitals(allowedDigits, False)
    #check each pandigital for divisibility purposes
    for pandigitalNum in listOfValidPandigitals:
        thisNumGood = True
        for primeIndex in range(len(primeList)):
            if int(str(pandigitalNum)[1+primeIndex:4+primeIndex]) % primeList[primeIndex] != 0:
                thisNumGood = False
                break
        if thisNumGood:
            print(pandigitalNum, " is also a good")

    return #len(perms)

#------------------------------------101 through 200----------------------------------------------
#------------------------------------201 through 300----------------------------------------------
#------------------------------------301 through 400----------------------------------------------
#------------------------------------401 through 500----------------------------------------------
#------------------------------------501 through 600----------------------------------------------
#------------------------------------601 through 700----------------------------------------------
#------------------------------------701 through 800----------------------------------------------
#------------------------------------801 through 900----------------------------------------------
def ChessSliders(_n, _k):
    Tools.choose(_n * _n, _k)
def ComputeAllPowersUpTo(_num):
    """returns an array with every single power up to _num"""
    arr = []
    for i in range(1, _num + 1):
        arr.append(i ** 2)
    return arr

#------------------------------------Other Functions----------------------------------------------
class Tools:
    def a1_CheckIfPrime(_num):
        """method to check in _num is a prime number using the sieve of Eratotshenese which is slower for many instances"""
        res = Tools.SieveOfEra(_num)
        if len(res) > 0:
            if res[-1] == _num:
                return True
        return False
    def CheckIfPrime(_num):
        """Helper method to check if _num is a prime number"""
        isStillPrime = True
        if _num <= 1:
            isStillPrime = False
        else:
            for i in range(2, math.ceil((_num + 2) / 2)):
                if (_num % i == 0):
                    isStillPrime = False
                    break
        return isStillPrime
    def GetProperDivisors(_num):
        factors = Tools.GetFactors(_num)
        pureList = []
        for i in factors:
            for j in range(2):
                pureList.append(i[j])
        pureList = sorted(pureList)
        pureList = pureList[:-1]
        uniqueList = []
        for i in pureList:
            tempNum = i
            if i not in uniqueList:
                uniqueList.append(i)
        return uniqueList
    def ParseStrToGrid(_rows, _columns, _str):
        """Given 3 integers and a string, this method will
         parse that string then return a 2D array (pretty self-explanatory)"""
        strTemp = (_str.split("\n"))
        grid = np.empty((_rows, _columns), dtype=object)
        for i in range(0, len(strTemp)):
            items = strTemp[i].split(" ")
            for j in range(0, len(items)):
                grid[i, j] = items[j]
                # if(Grid[i,j] == None):
                # Grid[i,j] = 0
        # print(grid)
        return grid
    def GetFactors(_num):
        """Gets the Factors of _num"""
        list = []
        numsToBeTested = _num ** (1 / 2)
        for i in range(1, math.ceil(numsToBeTested) + 1):
            if (i > numsToBeTested):
                break
            if (_num % i == 0):
                divNum = int(_num / i)
                list.append((i, divNum))
                numsToBeTested = divNum
        uniqueList = []
        for i in list:
            new_tup = ()
            for k in reversed(i):
                new_tup = new_tup + (k,)
            if new_tup not in uniqueList:
                uniqueList.append(i)
        return uniqueList
    def ListOfObjects(_objects, _parseString = " "):
        """Seperates a string into a list by the character given """
        list = []
        num = -1
        tempObjects = _objects
        for i in _objects:
            num += 1
            if (i == _parseString):
                list.append(tempObjects[:num])
                tempObjects = tempObjects[num:]
                num = 0
        list.append(tempObjects)
        return list
    def GetColatzSequence(_num):
        """given an integer, this will return a list of all the numbers
        that lead to 1, including 1 using a recursive setup"""
        if _num >= 1:
            list = []
            list.append(_num)
            while (_num != 1):
                if (_num % 2) == 0:
                    _num = (int)(_num / 2)
                else:
                    _num = (3 * _num) + 1
                list.append(_num)
            return list
        else:
            raise ValueError("Value can't be below 1")
    def NumberToWords(_num):
        """This function will take an integer and return a string equal to
        the "British" usage of the spoken number"""
        specialTerms = {
            "0": "",
            "1": "one",
            "2": "two",
            "3": "three",
            "4": "four",
            "5": "five",
            "6": "six",
            "7": "seven",
            "8": "eight",
            "9": "nine",
            "00": "",
            "10": "ten",
            "11": "eleven",
            "12": "twelve",
            "13": "thirteen",
            "14": "fourteen",
            "15": "fifteen",
            "16": "sixteen",
            "17": "seventeen",
            "18": "eighteen",
            "19": "nineteen",
            "20": "twenty",
            "30": "thirty",
            "40": "forty",
            "50": "fifty",
            "60": "sixty",
            "70": "seventy",
            "80": "eighty",
            "90": "ninety"
        }
        si = str(_num)  # string integer
        resultString = ""
        tempTriad = ["", "", ""]

        numZeros = 3 - (len(si) % 3)  # turn the number into a "triad-able" format
        if (numZeros == 3):
            numZeros = 0
        for i in range(numZeros):
            si = "0" + si

        thals = (len(si) / 3) - 1  # how many thals are in the whole thing?

        loopIndex = 0
        for digit in si:  # loops over every digit
            loopIndex += 1
            tempTriad[(loopIndex % 3) - 1] = digit  # sets the proper index of the triad to the next digit
            if (loopIndex % 3 == 0):  # loops over every triad
                # print(tempTriad)   #start of triad parsing
                triadString = ""

                # The string for the specific 3 numbers ex: 123 = one hundred and twenty three
                if (thals == 0 and loopIndex > 3):
                    triadString += "and "
                if (tempTriad[0] != "0"):
                    if (tempTriad[1] != "0" or tempTriad[2] != "0"):
                        triadString = specialTerms[tempTriad[0]] + " hundred and "
                    else:
                        triadString = specialTerms[tempTriad[0]] + " hundred "
                if (tempTriad[1] == "1"):
                    triadString = triadString + specialTerms[tempTriad[1] + tempTriad[2]]
                elif (tempTriad[1] == "0"):
                    triadString = triadString + specialTerms[tempTriad[2]]
                else:
                    triadString = triadString + specialTerms[tempTriad[1] + "0"] + " " + specialTerms[tempTriad[2]]

                if triadString == "and ":
                    triadString = ""
                # sets the proper "thal" suffix
                match thals:
                    case 0:
                        thalWord = ""
                    case 1:
                        thalWord = "thousand"
                    case 2:
                        thalWord = "million"
                    case 3:
                        thalWord = "billion"
                    case 4:
                        thalWord = "trillion"
                    case 5:
                        thalWord = "quadrillion"
                # adds the proper "thal" suffix
                if triadString != " ":
                    triadString += " " + thalWord;
                    resultString += triadString + " "
                if thals == 0:
                    resultString = resultString[:-2]
                # print(triadString)
                # print(resultString)
                thals -= 1
                tempTriad = ["", "", ""]

        #print(resultString)
        return resultString
    def AlphabeticalOrder(_strArray):
        numberizedArray = []
        longestSubArray = 0
        for stringItem in _strArray:
            if len(stringItem) > 0:
                if (len(stringItem) > longestSubArray):
                    longestSubArray = len(stringItem)
                tempArray = []
                for character in stringItem:
                    tempArray.append(int(str(ord(character))))
                numberizedArray.append(tempArray)
            else:
                # print(None)
                pass
        alphabatizedArray = []

        for j in range(len(numberizedArray)):
            for i in range(1, len(numberizedArray)):
                # is current num bigger than last?
                if numberizedArray[i][0] > numberizedArray[i - 1][0]:
                    # do nothing
                    pass
                    #print("nothin")

                # is current num smaller than last?
                if numberizedArray[i][0] < numberizedArray[i - 1][0]:
                    # swap and repeat
                    tempArray = numberizedArray[i]
                    numberizedArray[i] = numberizedArray[i - 1]
                    numberizedArray[i - 1] = tempArray
                    #print("swap")

                # is current num same as last?
                if numberizedArray[i][0] == numberizedArray[i - 1][0]:
                    # don't swap but repeat with next item in sub array
                    discoveredGreaterValue = False
                    reachedMaxValue = False
                    iterationValue = 1
                    while not discoveredGreaterValue and not reachedMaxValue:
                        if (iterationValue > len(numberizedArray[i]) and len(numberizedArray[i - 1])):
                            pass
                        if (iterationValue > len(numberizedArray[i])):
                            pass
                        if (iterationValue > len(numberizedArray[i - 1])):
                            pass
                        curVal = numberizedArray[i][iterationValue]
                        lastVal = numberizedArray[i - 1][iterationValue]
                        if curVal != lastVal:
                            discoveredGreaterValue = True
                            if curVal < lastVal:
                                tempArray = numberizedArray[i]
                                numberizedArray[i] = numberizedArray[i - 1]
                                numberizedArray[i - 1] = tempArray
                                #print("Swap at level " + iterationValue)
                        iterationValue += 1
                    #print("equal")

        return numberizedArray
    def AllPermutationsHelper(prefix, remaining, results):  # AI Generated
        if not remaining:
            results.append(prefix)
            return
        for i in range(len(remaining)):
            Tools.AllPermutationsHelper(
                prefix + remaining[i],
                remaining[:i] + remaining[i + 1:],
                results
            )
    def AllPermutations(_numberOfItems, startWith1 = False):
        digits = ''
        if startWith1:
            digits = ''.join(str(i) for i in range(1,_numberOfItems+1))
        else:
            digits = ''.join(str(i) for i in range(_numberOfItems))
        results = []
        Tools.AllPermutationsHelper('', digits, results)
        return results
    def FibonacciHelper(_tuple):
        _a = _tuple[0]
        _b = _tuple[1]
        return (_b, _a + _b)
    def PrimeFactorisation(_num):
        factorList = []
        k = 1
        while k <= _num:
            k += 1
            if _num % k == 0:
                _num = _num / k
                factorList.append(k)
                k = 1
        return factorList
    def CanonicalPrimeFactorisation(_num):
        factorList = []
        k = 1
        while k <= _num:
            k += 1
            if _num % k == 0:
                isSet = False
                index = -1
                for set in factorList:
                    index += 1
                    if set[0] == k:
                        factorList[index] = (set[0],set[1] + 1)
                        isSet = True
                if not isSet:
                    factorList.append((k,1))
                _num = _num / k
                k = 1
        return factorList
    def SieveOfEra(_num):
        """Returns a list of all primes below or at _num"""
        primeList = []
        if(_num > 0):
            prime = [True] * (_num + 1)
            prime[0] = prime[1] = False
            for i in range(2, int(_num ** 0.5) + 1):
                if prime[i]:
                    for j in range(i * 2, _num + 1, i):
                        prime[j] = False
            for i in range(2, _num+1):
                if prime[i] == True:
                    primeList.append(i)
        return primeList
    def SimplifyFraction(_numerator, _denominator):
        numFac = Counter(Tools.PrimeFactorisation(_numerator))
        denFac = Counter(Tools.PrimeFactorisation(_denominator))
        commonMultiple = 1
        for factor in numFac:
            if factor in denFac:
                minPower = min(numFac[factor], denFac[factor])
                commonMultiple *= factor ** minPower
        return (_numerator//commonMultiple, _denominator//commonMultiple)
    def CircularNumbers(_num):
        """Takes a number and provides every permutation of that number that is in the circular sequence"""
        numList = []
        strNum = str(_num)
        strLen = len(strNum)
        for i in range(strLen):
            tempString = strNum[i:strLen] + strNum[0:i]
            numList.append(int(tempString))
        return numList
    def GeneratePalindromes(_max):
        """assuming that _max is a power of 10, this quickly finds every possible
        palindrome and returns a sorted list"""
        palList = []
        for i in range(1,10):
            palList.append(str(i))
        for i in range(1,10**((len(str(_max))//2))):
            i = str(i)
            palList.append(i + i[::-1]) #add the case where even digits ex: 24-42
            if int(i) > 9:
                palList.append(i + i[len(i)-2::-1]) #add the case where odd digits ex: 2-4-2
        palList.sort()
        return palList
    def CheckIfPalindrome(_num):
        _num = str(_num)
        length = len(_num)
        if _num[:length//2] == _num[:(math.ceil(length/2))-1:-1]:
            return True
        return False
    def CheckIfPandigital(_num, _includeZero = False):
        numsSorted = "".join(sorted(str(_num)))
        if not _includeZero and "0" in numsSorted:
            return False
        if "." in numsSorted:
            numsSorted = numsSorted[1:]
        desiredString = "123456789"
        if _includeZero:
            desiredString = "0123456789"
        desiredString = desiredString[:len(numsSorted)]
        if numsSorted == desiredString:
            return True
        return False

    def GeneratePandigitals(_allowed, _index0IsRightmost=True):
        """
        AI generated function for the assistance of the recursion section of Q 43.
        Builds all valid pandigital numbers based on allowed digits per position.
        By default index 0 is treated as the rightmost digit (units). If your input
        list has index 0 as the leftmost (most-significant) digit, call with
        _index0IsRightmost = False.
        """
        # ensure we work on a list and ensure index 0 is rightmost inside the function
        if _index0IsRightmost:
            _allowed_proc = list(_allowed)  # index 0 == rightmost
        else:
            _allowed_proc = list(reversed(_allowed))  # flip so index 0 becomes rightmost

        results = []

        def Backtrack(_pos=0, _used=None, _digits=None):
            if _used is None:
                _used = set()
            if _digits is None:
                _digits = [None] * len(_allowed_proc)

            # base case: filled every position
            if _pos == len(_allowed_proc):
                # assemble number: index i is worth 10**i because index 0 is units
                number = sum(d * (10 ** i) for i, d in enumerate(_digits))
                results.append(number)
                return

            # try each allowed digit for this position if not already used
            for d in _allowed_proc[_pos]:
                if d in _used:
                    continue
                _digits[_pos] = d
                _used.add(d)
                Backtrack(_pos + 1, _used, _digits)
                _used.remove(d)
                _digits[_pos] = None

        Backtrack()
        return results

    def pow(x,n):
        return x**n
    def choose(_n,_k):
        nFac = Tools.factorial(_n)
        kFac = Tools.factorial(_k)
        nMinKFac = Tools.factorial((_n-_k))
        return int(nFac/(kFac*nMinKFac))
    def factorial(_i):
        retNum = 1
        for i in range(2,_i+1):
            retNum *= i
        return retNum
    def fibLog(_e):
        log = 1
        num = 0
        a = 0
        b = 1
        while log < _e:
            c = a+b
            a=b
            b=c
            #print(c)
            num += 1
            log = math.log(num, 10)