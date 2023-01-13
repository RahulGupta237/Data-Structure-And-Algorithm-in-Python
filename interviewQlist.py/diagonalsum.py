def sumDiagonal(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i][i]
    return sum
tdlist=[[1,2,3],[4,5,6],[7,8,9]]
print(sumDiagonal(tdlist))