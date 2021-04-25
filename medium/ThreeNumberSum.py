


# First Version complexity O(n^3)
def threeNumberSum1(array, targetSum):
    # Write your code here.
    array.sort()
    result=[]
    for i in range(0 ,len(array)):
        for j in range( i +1 ,len(array)):
            for k in range( j +1 ,len(array)):
                first = array[i]
                second = array[j]
                third = array[k]
                if first+second+third == targetSum:
                    arr = [first, second, third];
                    result.extend([arr])
    return result





# o(n^2)
def threeNumberSum(array, targetSum):
    array.sort()
    result=[]
    for i in range(0,len(array)):
        first = array[i]
        j = i+1
        k = j+1
        while (j<k):
            second = array[j]
            third = array[k]
            sum = first + second + third
            if sum==targetSum:
                result.extend([[first,second,third]])
                j+=1
                k-=1
            elif sum < targetSum:
                j+=1
            else:
                k-=1
    return result


def fourNumberSum(array, targetSum):
    # Write your code here.
    array.sort()


    result = []
    for a in range(0, len(array)):
        for i in range(a + 1, len(array)):
            first = array[a]
            second =array[i]
            j = i + 1
            k = len(array) - 1
            while j < k:
                third = array[j]
                fourth = array[k]
                sum = first + second + third + fourth
                if sum == targetSum:
                    result.extend([[first, second, third, fourth]])
                    j += 1
                    k -= 1
                elif sum < targetSum:
                    j += 1
                else:
                    k -= 1

    return result
pass

array=[12,3,1,2,-6,5,-8,6]
array2=[7,6,4,-1,1,2]
targetSum=16
# print(threeNumberSum1(array,targetSum))

print(fourNumberSum(array2,targetSum))

if __name__ == '__main__':
    print('PyCharm')