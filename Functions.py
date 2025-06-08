import math
import sys
import numpy as np


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
    print(lst)
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
def f005_SmallestMultiple(num2 = 20, num1 = 1, increment = 1):
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
def f007_FindPrimeByIndex(num1 = 10001):
    """given an index of prime, Ex: 2=1, 3=2, 5=3, 7=4, 11=5 etc. this method fill find
    that index"""
    currentIndex = -1
    currentNum = 0
    while (currentIndex < num1):
        currentNum += 1
        if (HelperFunctions.CheckIfPrime(currentNum)):
            currentIndex += 1
    return currentNum
def f008_LargestProductInASeries(seriesLength, _largeNum):
    """given a length of numbers and a huge number (given as a string), this method will find the largest
    string of numbers that are adjacent with a length that is given, that give the
    largest number when each character is multipled together"""
    largestResultSoFar = 0
    for set in range(len(_largeNum) + 1):
        currentString = _largeNum[set: set + seriesLength]
        nums = []
        for index in range(len(currentString)):
            nums.append(int((currentString[index:index + 1])))
        tempResult = 1
        for num in nums:
            tempResult *= num
        if (tempResult > largestResultSoFar):
            largestResultSoFar = tempResult
    return largestResultSoFar
def f009_SpecialPythagoreanTriple(num1):
    """Given an integer, this method will find the first set of number where
    a^2 + b^2 = c^2 and a+b+c = num1 then return a*b*c"""
    for a in range(1, num1):
        for b in range(1, num1):
            c = math.sqrt(a ** 2 + b ** 2)
            if ((a + b + c) == num1):
                return a * b * c
    return False
def f010_SummationOfPrimes(num1):
    """finds the sum of all the primes below num1"""
    num = 0
    for index in range(2, num1):
        if (HelperFunctions.CheckIfPrime(index)):
            num += index
    return (num)
def f011_LargestProductInAGrid(_grid, _length=4):
    """Given a 2d array of integers, this will find the 'connect 4'
    of numbers that gives the largest product then return the product"""
    for i in _grid:
        i = int(i)
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
def f012_HighlyDivisibleTriangularNumber(_numFactors):
    """finds the first "triangle number" to have over _numFactors factors"""
    done = False
    index = 0
    while (not done or index > 1000000):
        index += 1
        sum = int((index / 2) * (1 + index))
        length = len(HelperFunctions.GetFactors(sum))
        if (length > math.floor(_numFactors / 2)):
            done = True
            return sum
def f013_LargeSum(_numDigits, _str):
    """this method will add all the numbers in _str, then find the first _numDigits digits in it. """
    objects = HelperFunctions.ListOfObjects(_str)
    sum = 0
    for i in objects:
        sum += int(i)
    print(sys.getsizeof(sum))
    return str(sum)[:_numDigits]
def f014_LongestColatzSequence(_num):
    """Find the integer from 1-_num that has the longest chain
    using the Colatz Sequence"""
    longestIndex = 0
    longestChain = 0
    exclusiveList = []
    for i in range(_num, 1, -1):
        tempList = HelperFunctions.GetColatzSequence(i)
        if len(tempList) > longestChain:
            longestIndex = i
            longestChain = len(tempList)
    return longestIndex
def f015_LatticePaths(_num):
    """litteraly just n choose n/2"""
    n = _num
    r = (int)(n / 2)
    return (int)(math.factorial(n) / (math.factorial(r) ** 2))
def f016_PowerDigitSum(_num):
    """This will find the sum of each individual digit in 2^_num"""
    number = 2 ** _num
    strNum = str(number)
    sumNum = 0
    for i in strNum:
        sumNum += (int)(i)
    return sumNum
def f017_NumberLetterCounts(_num):
    """this method finds the sum of all the letters in
    "one" + "two" + "three" +...+_num"""
    totalLength = 0
    for i in range(1, _num + 1):
        strToBeParsed = HelperFunctions.NumberToWords(i)
        parsedArray = strToBeParsed.split(' ')
        parsedString = ""
        for i in parsedArray:
            parsedString += i
        tempLength = len(parsedString)
        totalLength += tempLength
    return totalLength
def f018_MaximumPathSumOne(_str):
    """Given a string that is a triangle in shape, this function will find the greatest path"""
    gridHeight = 15
    pyramid = HelperFunctions.ParseStrToGrid(gridHeight, gridHeight, _str)
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
    return (grid)
def f019_CountingSundays(self):
    pass
def f020_FactorialDigitSum(_num):
    """Adds the digits of the factorial of _num"""
    nums = HelperFunctions.factorial(_num)
    numsStr = str(nums)
    total = 0
    for i in numsStr:
        total += int(i)
    return total
def f021_AmicableNumbers(_num):
    listOfPairs = []
    for i in range(1, _num + 1):
        divisors = HelperFunctions.GetProperDivisors(i)
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
def f022_NamesScores(self):
    namesFile = open(r"E:\Python IDE\Projects\MathS\Refrence Files\names.txt", "r")
    fileString = namesFile.read()
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
def f023_NonAbundantSums(self):
    abundantList = []
    for i in range(11, 28124):
        tempList = HelperFunctions.GetProperDivisors(i)
        listTotal = 0
        for item in tempList:
            listTotal += item
        if listTotal > i:
            abundantList.append(i)
    tempTotal = 0
    for checkNums in range(1, 28124):
        numCantBeWritten = True
        for abundantNums in abundantList:
            neededNum = checkNums - abundantNums
            if (neededNum in abundantList) and numCantBeWritten:
                numCantBeWritten = False
        if numCantBeWritten:
            tempTotal += checkNums
    return tempTotal
def f024_LexicographicPermutations(_size):
    myList = HelperFunctions.AllPermutations(_size)
    return myList[999999]
def f025_ThousandDigitFibonacciNumber(_digits):
    """returns the index of the first fibonacci number that is _digits digits long"""
    attempts = 0
    fibboLen = 0
    checkTuple = (1, 1)
    while (fibboLen < _digits and attempts < 1000000):
        attempts += 1
        checkTuple = HelperFunctions.FibonacciHelper(checkTuple)
        fibboLen = len(str(checkTuple[1]))
    return attempts + 2  # to account for starting tuple add 2
def f026_ReciprocalCycles(_size):
    """for 1/n where n goes from 1 to _size find the longest cycle and returns n"""
    # uses a really cool method where the first instance of 10^k mod n = 1 then k is number of repeating digits
    # just make sure that the number n is coprime with 10, if not then use only the coprime part ex: 28 = 2^2 * 7 so just use 7
    largestIndexSoFar = (0, 0)
    for n in range(2, _size + 1):
        number1HasBeenReached = False
        k = 0
        primeFactors = HelperFunctions.PrimeFactorisation(n)
        if not (2 in primeFactors or 5 in primeFactors):
            while not number1HasBeenReached and k <= n:
                k += 1
                result = 10 ** k % n
                if result == 1:
                    if k > largestIndexSoFar[0]:
                        largestIndexSoFar = (k, n)
                        number1HasBeenReached = True
                        print("The number " + str(n) + " repeats " + str(k) + " times.")
                    else:
                        break
    return largestIndexSoFar[1]
def f027_QuadraticPrimes(_size):
    """for a given size find the formula of n^2 + an + b that gives the most consecutive prime numbers and return a * b"""
    bestSoFar = (0, 0, 0)  # in (a, b, consecutiveTerms)
    for a in range(-_size + 1, _size + 2):
        for b in range(-_size, _size + 1):
            consecutiveTerms = 0
            n = 0
            stillConsecutive = True
            while stillConsecutive:
                isPrime = HelperFunctions.CheckIfPrime(abs(n ** 2 + a * n + b))
                if isPrime:
                    n += 1
                    consecutiveTerms += 1
                    if consecutiveTerms > bestSoFar[2]:
                        bestSoFar = (a, b, consecutiveTerms)
                        print(bestSoFar)
                else:
                    stillConsecutive = False
    return bestSoFar[0] * bestSoFar[1]
def f028_NumberSprialDiagonals(_radius):
    total = 0
    for i in range(0, 4):
        for n in range(2, _radius + 1):
            total += ((2 * n - 1) ** 2 - (2 * i * (n - 1)))
    total += 1
    return total
def f029_DistinctPowers(_aMax, _bMax):
    """for all combinations of a^b find the number of unique combinations"""
    masterList = []
    for a in range(2, _aMax + 1):
        for b in range(2, _bMax + 1):
            tempFactors = HelperFunctions.PrimeFactorisation(a)
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
#------------------------------------101 through 200----------------------------------------------
#------------------------------------201 through 300----------------------------------------------
#------------------------------------301 through 400----------------------------------------------
#------------------------------------401 through 500----------------------------------------------
#------------------------------------501 through 600----------------------------------------------
#------------------------------------601 through 700----------------------------------------------
#------------------------------------701 through 800----------------------------------------------
#------------------------------------801 through 900----------------------------------------------
def ChessSliders(_n, _k):
    HelperFunctions.choose(_n * _n, _k)
def ComputeAllPowersUpTo(_num):
    """returns an array with every single power up to _num"""
    arr = []
    for i in range(1, _num + 1):
        arr.append(i ** 2)
    return arr

#------------------------------------Other Functions----------------------------------------------
class HelperFunctions:
    def CheckIfPrime(_num):
        """Helper method to check if num1 is a prime number"""
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
        factors = HelperFunctions.GetFactors(_num)
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
    def ListOfObjects(_objects):
        """Seperates a string into a list by the charachter "space" """
        list = []
        num = -1
        tempObjects = _objects
        for i in _objects:
            num += 1
            if (i == " "):
                list.append(tempObjects[:num])
                tempObjects = tempObjects[num:]
                num = 0
        list.append(tempObjects)
        return list
    def GetColatzSequence(_num):
        """given an integer, this will return a list of all the numbers
        that lead to 1, including 1 using a recursive setup"""
        list = []
        list.append(_num)
        while (_num != 1):
            if (_num % 2) == 0:
                _num = (int)(_num / 2)
            else:
                _num = (3 * _num) + 1
            list.append(_num)
        return list
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

        print(resultString)
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
                    print("nothin")

                # is current num smaller than last?
                if numberizedArray[i][0] < numberizedArray[i - 1][0]:
                    # swap and repeat
                    tempArray = numberizedArray[i]
                    numberizedArray[i] = numberizedArray[i - 1]
                    numberizedArray[i - 1] = tempArray
                    print("swap")

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
                                print("Swap at level " + iterationValue)
                        iterationValue += 1
                    print("equal")

        return numberizedArray
    def AllPermutationsHelper(prefix, remaining, results):  # AI Generated
        if not remaining:
            results.append(prefix)
            return
        for i in range(len(remaining)):
            HelperFunctions.AllPermutationsHelper(
                prefix + remaining[i],
                remaining[:i] + remaining[i + 1:],
                results
            )
    def AllPermutations(_numberOfItems):
        digits = ''.join(str(i) for i in range(_numberOfItems))
        results = []
        HelperFunctions.AllPermutationsHelper('', digits, results)
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
    def pow(x,n):
        return x**n
    def choose(_n,_k):
        nFac = HelperFunctions.factorial(_n)
        kFac = HelperFunctions.factorial(_k)
        nMinKFac = HelperFunctions.factorial((_n-_k))
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