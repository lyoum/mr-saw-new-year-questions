## Question:
## Within this century (2001 - 2100), how many years can have at least 3 sums of it's positive factors, without repetition?
## Examples:
## 2022 = 1011 + 674 + 337
## 2000 = 1000 + 500 + 400 + 100

## Compiled with Python 3.9

accumulateYears = []
    
def printFactorialYear(year: int) :
    factorial = 2;
    accumulateSum = 0
    actualSumList = []
    excludeFactorList = []
    possibleSumList = []
    possibleFactorToSum = 0
    global accumulateYears

    ## Get all possible factors to possibleSumList
    while True:
        if year % factorial == 0:
            possibleFactorToSum = int(year / factorial)
            possibleSumList.append(possibleFactorToSum)
        factorial+=1
        if factorial >= year:
            break
    possibleSumList.append(1) #Every number has 1 as factorial

    ## Get factors to exclude in possibleSumList
    totalPossibleSumOfYear = sum(possibleSumList)
    excludeFactorSum = totalPossibleSumOfYear - year
    for factor in possibleSumList:
        if factor <= excludeFactorSum:
            excludeFactorSum = excludeFactorSum - factor
            excludeFactorList.append(factor)
        if excludeFactorSum == 0:
            break

    ## Get actual sum factors to actualSumList
    ## Get actual years to accumulateYears
    for factor in possibleSumList:
        if factor in excludeFactorList:
            continue
        if accumulateSum + factor <= year:
            accumulateSum = int(accumulateSum + factor)
            actualSumList.append(factor)
        if accumulateSum == year and len(actualSumList) >= 3:
            print(f'year: {year}, is sum of: {actualSumList}')
            accumulateYears.append(year)
            break

for year in range(2001, 2101):
    printFactorialYear(year)

print(f'Total years: {len(accumulateYears)}')

