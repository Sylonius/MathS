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

if __name__ == '__main__':
    print(MathProblems.LargestProductInASeries(13,"7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"))
    #start_time = time.time()
    #your function here
    #end_time = time.time()
    #execution_time = end_time - start_time
    #print("Execution time:", round(execution_time,5), "seconds")