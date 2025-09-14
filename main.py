import Functions
import Functions as f
import time
import requests

def test(_start, _end):
    """Tests the chosen functions in the "Functions" file. goes from Project Euler question _start to _end (inclusive, exclusive)"""
    answerFile = open(r"E:\Python IDE\Projects\MathS\Refrence Files\Answers.txt", "r")
    answerArray = []
    incorrectArray = []
    for line in answerFile:
        line = line[:-1]
        lineArr = line.split(". ")
        try:
            answerArray.append(lineArr[1])
        except IndexError:
            answerArray.append("No answer yet")
    #print(answerArray)
    timeArray = []
    for i in range(_start, _end):
        start_time = time.time()
        testedAnswer = str(runFunction(i, True))[:-1]
        #print("The tested answer is " + str(testedAnswer) + " | The actual answer is " + str(answerArray[i-1]))
        if (testedAnswer == answerArray[i-1]):
            #print(str(i) + " is good")
            pass
        else:
            print(str(i) + " is incorrect")
            incorrectArray.append((str(i),str(testedAnswer),str(answerArray[i-1])))

        end_time = time.time()
        execution_time = end_time - start_time
        timeArray.append((execution_time,i))
        print("Problem: " + str(i) + "|Execution time:", round(execution_time, 5), "seconds")
    print("--------------Incorrect-Answers-----------------------")
    if len(incorrectArray) == 0:
        print("There are no incorrect answers")
    else:
        for incorrectVal in incorrectArray:
            print(" For question " + incorrectVal[0] + " the tested answer is\t" + incorrectVal[1] + "\n\t\t\t\tThe actual answer is\t" + incorrectVal[2])

    timeArray.sort(reverse = True)
    print("-------------Best-Questions-To-Fix--------------------")
    for timeVal in timeArray:
        print("Question number " + str(timeVal[1]) + " took " + str(round(timeVal[0],2)) + " seconds.")

    # myResult = f.DistinctPowers(100,100)
    # print(myResult)
    # print(math1To99.PrimeFactorisation(28))
    # print(MathProblems.LongestColatzSequence(999999))
    # print(MathProblems.NumberLetterCounts(10))
    # 262,534,975,000,787,038
    # print(MathProblems.NumberToWords(342))
    # print(MathProblems1to99.NumberLetterCounts(1000))
    ##print(MathProblems800to899.ChessSliders(6,12))
    ##print(MathProblems800to899.ComputeAllPowersUpTo(1000000))
    # print(MathProblems1to99.GetFactors(1000)) 128 3
    # print(MathProblems1to99.AmicableNumbers(10000))
    # print(MathProblems1to99.NumberSprialDiagonals(501))
    # print(MathProblems1to99.GetProperDivisors(64))
    # print(MathProblems1to99.GetFactors(9))
    # print(tuple())
    # print(MathProblems.LargeSum(3,"2000 6363 4000"))
    # print(MathProblems1to99.NonAbundantSums(None))
    # print(MathProblems1to99.NamesScores(None))
    # print(MathProblems1to99.AlphabeticalOrder(["hya","whatyouMean?","","--+=[ahjsd}","wowsas!!!","a","a","A","b","B"]))
    # print(CommonlyUsedFunctions.fibLog(5))

def runFunction(_num, _shouldReturn = True, runBad = False):
    """Only runs functions that start with "f" """
    functionList = dir(f)
    returnString = ""
    for func in functionList:
        try:
            if (int(func[1:4]) == _num and (runBad or func[5] != "a")):
                executionString = "f." + func + "()"
                start_time = time.time()
                if _shouldReturn:
                    returnString += str(eval(executionString)) + "\n"     #exec("print(" + executionString + ")")
                else:
                    exec(executionString)
                end_time = time.time()
                execution_time = end_time - start_time
                if runBad:
                    print(executionString, " took ", round(execution_time, 5), "seconds")
        except ValueError:
            pass
    if _shouldReturn:
        return returnString
    else:
        return "No Return Value Expected by main"
def runAllFunctions(_shouldReturn = False, runBad = False):
    """Only runs functions that start with "f" """
    functionList = dir(f)
    for func in functionList:
        if (func[0] == "f" and (runBad or func[5] != "a")):
            executionString = "f." + func + "()"
            if _shouldReturn:
                return(eval("print(" + executionString + ")"))
            else:
                exec(executionString)
def urlToString(_url) -> str:
    cookies = {'PHPSESSID': "844c2c6049a92dfa61d59200a390d692"}
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(_url, cookies=cookies, headers=headers)
    webpage = response.text
    return webpage

if __name__ == '__main__':
    start_time = time.time()


    #print(Functions.Tools.CheckIfPandigital(12))
    #print(runAllFunctions())

    #print(runFunction(35, True, True))
    test(1,30)  #inclusive, exclusive


    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", round(execution_time,5), "seconds")

#print(urlToString("https://projecteuler.net/minimal=problems;csv"))

# project Euler API:  https://pfischbeck.de/en/posts/projecteuler-api/
# List of Problems:   https://projecteuler.net/minimal=problems;csv
# personal cookie:    PHPSESSID = 844c2c6049a92dfa61d59200a390d692

# location and code to edit reference files:
# open(r"E:\Python IDE\Projects\MathS\Refrence Files\FileNameHere.extension", "r")