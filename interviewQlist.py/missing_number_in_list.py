def missingNumber(myList,totalCount):
    expectedSum = totalCount * ((totalCount + 1) / 2)
    actualSum = 0
    for i in myList:
        actualSum += i
    return int(expectedSum - actualSum)

list=[1,2,4]
x=missingNumber(list,4)
print(x)

