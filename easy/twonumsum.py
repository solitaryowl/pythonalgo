# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def twoNumberSum(array, targetSum):
    lst = set()
    res = []
    for i in array:
        lst.add(i)
    for i in array:
        if ((targetSum - i) in lst) & (targetSum != 2 * i):
            res.append(i)
    res.sort(reverse=False)
    return res


def twoNumberSumN(array, targetSum):
    # Write your code here.
    lst = set()
    for i in range(len(array)):
        num = array[i]
        if (targetSum - num) in lst:
            res = [num, targetSum - num]
            return res
        else:
            lst.add(num)
    return []



def isSubseq(array,sequence):
    i=0
    j=0
    sub=True
    while (i<len(sequence)) :
        found = False
        seq = sequence[i]
        for k in range(j,len(array)):
            if array[k] == seq:
                i+=1
                j+=1
                found=True
                break
            else:
                j+=1
        if found == False:
            return False
    return sub

print(isSubseq([1,2,3,5,4],[1,2,4,5]))













# print(twoNumberSumN([3, 5, -4, 8, 11, 1, -1, 6], 10))


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
