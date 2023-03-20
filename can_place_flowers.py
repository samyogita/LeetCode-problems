class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            l = i-1
            r = i+1
            if (l < 0 or flowerbed[l] != 1) and (r >= len(flowerbed) or flowerbed[r] != 1):
                flowerbed[i] = 1
                cnt += 1
        return cnt >= n
