



def smallestDifference1(arrayOne, arrayTwo):
    sDiff=float("inf")
    res=[]
    for i in range(0,len(arrayOne)):
        for j in range(0,len(arrayTwo)):
            diff = abs(arrayOne[i]-arrayTwo[j])
            if diff < sDiff:
                res=[arrayOne[i],arrayTwo[j]]
                sDiff=diff
    return res

def smallestDifference2(arrayOne,arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    print(arrayOne)
    print(arrayTwo)
    i=0
    j=0
    sDiff=float("inf")
    res = []
    while (i < len(arrayOne)) & (j < len(arrayTwo)):
        diff=arrayOne[i] - arrayTwo[j]
        if abs(diff) < sDiff:
            res = [arrayOne[i], arrayTwo[j]]
            sDiff = abs(diff)
        if diff < 0:
            i= i+1
        elif diff==0:
            break
        else:
            j=j+1
    return res

array1=[-1, 5, 10, 20 ,28, 3]
array2=[26,134,135,15,17]
print(smallestDifference2(array1,array2))


if __name__ == '__main__':
    print("https://www.algoexpert.io/questions/Smallest%20Difference")