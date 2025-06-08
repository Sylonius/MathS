import Functions as f
import time
import urllib
import urllib.request
import csv

def test():
    start_time = time.time()
    # myResult = f.DistinctPowers(100,100)
    # print(myResult)
    print(dir(f))
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
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", round(execution_time, 5), "seconds")

def urlToString(_url) -> str:
    myfile = urllib.request.urlopen(_url).read()
    myString = myfile.decode("utf-8")
    return myString

if __name__ == '__main__':
    start_time = time.time()
    print(urlToString("https://projecteuler.net/minimal=problems;csv"))
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", round(execution_time,5), "seconds")


# project Euler API:  https://pfischbeck.de/en/posts/projecteuler-api/
# List of Problems:   https://projecteuler.net/minimal=problems;csv
# personal cookie:    PHPSESSID = 844c2c6049a92dfa61d59200a390d692