## Question:
## Within this century (2000 - 2099), how many years can have sum of it's positive factors, without repetition?
## Examples:
## 2022 = 1011 + 674 + 337
## 2000 = 1000 + 500 + 400 + 100

## Compiled with Python 3.9

accumulateYears = []
    
def printFactorialYear(year: int) :
    factorial = 2;
    accumulateSum = 0
    accumulateList = []
    while True:
        if year % factorial == 0:
            possibleFactorToSum = int(year / factorial)
            if accumulateSum + possibleFactorToSum <= year:
                accumulateSum = int(accumulateSum + possibleFactorToSum)
                accumulateList.append(possibleFactorToSum)
        factorial+=1
        if accumulateSum == year:
            print(f'year: {year}, sum of: {accumulateList}')
            global accumulateYears
            accumulateYears.append(year)
            break
        if factorial == year:
            break

for year in range(2000, 2099):
    printFactorialYear(year)

print(f'Total years: {len(accumulateYears)}')

