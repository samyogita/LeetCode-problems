import math
N = int(input())
quantity = list(map(int, input().split()))
queries = int(input())

def vegetables(N, quantity, k):
    l, r = 1, max(quantity)
    while l < r:
        if sum(quantity) < k:
            return -1
        mid = l + (r - l) // 2
        minimum = 0
        for i in quantity:
          minimum += min(mid, i)  
        if minimum >= k:
            r = mid
        else:
            l = mid + 1
    
    return l


for i in range(queries):
   k = int(input())
   print(vegetables(N, quantity, k) )





