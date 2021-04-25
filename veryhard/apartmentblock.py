


def calcCostLeft(blks,i,j,costs):
    if blks[i][j]:
        return 0
    elif i==0:
        return len(blks)
    else:
        return costs[i-1][j]


def calcCostRight(blks,i,j,costs):
    if blks[i][j]:
        return 0
    elif i == len(blks)-1:
        return len(blks)
    else:
        return costs[i+1][j]



blocks = [{"gym": False, "school": True, "store": False},
          {"gym": True, "school": False, "store": False},
          {"gym": True, "school": True, "store": False},
          {"gym": False, "school": True, "store": False},
          {"gym": False, "school": True, "store": True}]


reqs=["gym","school","store"]


cache=[]
for i in range(0,len(blocks)):
    c=[]
    for j in range(0,len(reqs)):
        c.append(-1)
    cache.append(c)

def calcLeftCost(blks,i,reqs,j,cache):
    if i<0:
        return len(blks)
    if blks[i][reqs[j]]:
        cache[i][j]=0
        return 0
    else:
        return 1+calcLeftCost(blks,i-1,reqs,j,cache)


def calcRightCost(blks, i, reqs, j, cache):
    if i >= len(blks):
        return len(blks)
    if blks[i][reqs[j]]:
        return 0
    else:
        return 1 + calcRightCost(blks, i+1, reqs, j, cache)

def calcCost(blks,i,reqs,j,cache):
    if cache[i][j] != -1:
        return cache[i][j]
    if blks[i][reqs[j]]:
        cache[i][j] = 0
        return 0
    else:
        cc=min(calcRightCost(blks,i,reqs,j,cache),calcLeftCost(blks,i,reqs,j,cache))
        cache[i][j] = cc
        return cc



def apartmentHunting(blocks, reqs):
    cache=[]
    minCost=2*len(blocks)
    minCostInd=-1
    for i in range(0,len(blocks)):
        currentMax=0
        for j in range(0,len(reqs)):
            ccost=calcCost(blocks,i,reqs,j,cache)
            if ccost > currentMax:
                currentMax=ccost
        if currentMax < minCost:
            minCost = currentMax
            minCostInd=i
    return minCostInd

if __name__ == '__main__':
    print('hi')