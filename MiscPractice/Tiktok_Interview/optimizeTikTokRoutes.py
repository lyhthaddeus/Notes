def optimizeTikTokRoutes(numServers, disconnectedPairs):
    # Write your code here
    serverDict = {}
    lst = []
    for pair in disconnectedPairs:
        if abs(pair[0] - pair[1]) == 1:
            serverDict[pair[0]] = pair[1]
    for i in range(1,numServers+1):
        if i not in serverDict:
            lst.append([i])
    lenth = len(lst)
    return sumTill(lenth) - lenth + numServers  

def sumTill(num):
    sum = 0
    for i in range(1, num+1):
        sum += i
    return sum

if __name__ == '__main__':
    optimizeTikTokRoutes(4, [[1,2],[2,3]])
