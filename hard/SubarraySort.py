def subarraySort(array):
    # Write your code here.
    sArray = array.copy()
    sArray.sort()
    fromInd = -1
    toInd = -1
    for i in range(0, len(sArray)):
        if sArray[i] != array[i]:
            fromInd = i
            break

    for j in range(len(sArray)-1, 0, -1):
        if sArray[j] != array[j]:
            toInd=j
            break


    return [fromInd, toInd]


def subarraySort2(array):
    # Write your code here.
    i = 0
    j = len(array) - 1
    res = [-1, -1]
    while i < j:
        left = array[i]
        right = array[j]
        if left < right:
            i = i + 1
        else:
            j = j - 1
    return res


pass

array=[1, 2, 4, 7, 10, 11, 7, 12, 6, 7,16, 18, 19]
res=subarraySort2(array)
print(res)

if __name__ == '__main__':
    print("https://www.algoexpert.io/questions/Subarray%20Sort")