import heapq

def calculateTikTokShoppingCost(vouchersCount, prices):
    # Write your code here
    n = vouchersCount
    heap = [] 
    prices.sort()
    for price in prices:
        heapq.heappush(heap, (-price, price))
    sum = 0
    print(heap)
    while n > 0:
        curr = heapq.heappop(heap)[1]
        curr = curr // 2
        heapq.heappush(heap, (-curr, curr))
        n -= 1
    for price in heap:
        sum += price[1]
    print(sum)
    return sum

if __name__ == '__main__':
    calculateTikTokShoppingCost(12, [11,21,31,41,51])
