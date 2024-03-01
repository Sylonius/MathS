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
        return str(sum)[:_numDigits]

if __name__ == '__main__':
    start_time = time.time()
    print(MathProblems.LargeSum(10,"37107287533902102798797998220837590246510135740250 46376937677490009712648124896970078050417018260538 74324986199524741059474233309513058123726617309629 91942213363574161572522430563301811072406154908250 23067588207539346171171980310421047513778063246676 89261670696623633820136378418383684178734361726757 28112879812849979408065481931592621691275889832738 44274228917432520321923589422876796487670272189318 47451445736001306439091167216856844588711603153276 70386486105843025439939619828917593665686757934951 62176457141856560629502157223196586755079324193331 64906352462741904929101432445813822663347944758178 92575867718337217661963751590579239728245598838407 58203565325359399008402633568948830189458628227828 80181199384826282014278194139940567587151170094390 35398664372827112653829987240784473053190104293586 86515506006295864861532075273371959191420517255829 71693888707715466499115593487603532921714970056938 54370070576826684624621495650076471787294438377604 53282654108756828443191190634694037855217779295145 36123272525000296071075082563815656710885258350721 45876576172410976447339110607218265236877223636045 17423706905851860660448207621209813287860733969412 81142660418086830619328460811191061556940512689692 51934325451728388641918047049293215058642563049483 62467221648435076201727918039944693004732956340691 15732444386908125794514089057706229429197107928209 55037687525678773091862540744969844508330393682126 18336384825330154686196124348767681297534375946515 80386287592878490201521685554828717201219257766954 78182833757993103614740356856449095527097864797581 16726320100436897842553539920931837441497806860984 48403098129077791799088218795327364475675590848030 87086987551392711854517078544161852424320693150332 59959406895756536782107074926966537676326235447210 69793950679652694742597709739166693763042633987085 41052684708299085211399427365734116182760315001271 65378607361501080857009149939512557028198746004375 35829035317434717326932123578154982629742552737307 94953759765105305946966067683156574377167401875275 88902802571733229619176668713819931811048770190271 25267680276078003013678680992525463401061632866526 36270218540497705585629946580636237993140746255962 24074486908231174977792365466257246923322810917141 91430288197103288597806669760892938638285025333403 34413065578016127815921815005561868836468420090470 23053081172816430487623791969842487255036638784583 11487696932154902810424020138335124462181441773470 63783299490636259666498587618221225225512486764533 67720186971698544312419572409913959008952310058822 95548255300263520781532296796249481641953868218774 76085327132285723110424803456124867697064507995236 37774242535411291684276865538926205024910326572967 23701913275725675285653248258265463092207058596522 29798860272258331913126375147341994889534765745501 18495701454879288984856827726077713721403798879715 38298203783031473527721580348144513491373226651381 34829543829199918180278916522431027392251122869539 40957953066405232632538044100059654939159879593635 29746152185502371307642255121183693803580388584903 41698116222072977186158236678424689157993532961922 62467957194401269043877107275048102390895523597457 23189706772547915061505504953922979530901129967519 86188088225875314529584099251203829009407770775672 11306739708304724483816533873502340845647058077308 82959174767140363198008187129011875491310547126581 97623331044818386269515456334926366572897563400500 42846280183517070527831839425882145521227251250327 55121603546981200581762165212827652751691296897789 32238195734329339946437501907836945765883352399886 75506164965184775180738168837861091527357929701337 62177842752192623401942399639168044983993173312731 32924185707147349566916674687634660915035914677504 99518671430235219628894890102423325116913619626622 73267460800591547471830798392868535206946944540724 76841822524674417161514036427982273348055556214818 97142617910342598647204516893989422179826088076852 87783646182799346313767754307809363333018982642090 10848802521674670883215120185883543223812876952786 71329612474782464538636993009049310363619763878039 62184073572399794223406235393808339651327408011116 66627891981488087797941876876144230030984490851411 60661826293682836764744779239180335110989069790714 85786944089552990653640447425576083659976645795096 66024396409905389607120198219976047599490197230297 64913982680032973156037120041377903785566085089252 16730939319872750275468906903707539413042652315011 94809377245048795150954100921645863754710598436791 78639167021187492431995700641917969777599028300699 15368713711936614952811305876380278410754449733078 40789923115535562561142322423255033685442488917353 44889911501440648020369068063960672322193204149535 41503128880339536053299340368006977710650566631954 81234880673210146739058568557934581403627822703280 82616570773948327592232845941706525094512325230608 22918802058777319719839450180888072429661980811197 77158542502016545090413245809786882778948721859617 72107838435069186155435662884062257473692284509516 20849603980134001723930671666823555245252804609722 53503534226472524250874054075591789781264330331690"))
    #print(MathProblems.LargeSum(3,"2000 6363 4000"))

    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", round(execution_time,5), "seconds")
