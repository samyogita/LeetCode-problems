class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def solve(index):
            i = index
            if index == len(days):
                return 0
            day_cost = costs[0] + solve(index+1)

            while i < len(days) and days[index] + 7 > days[i]:
                i += 1
            week_cost = costs[1] + solve(i) 

            while i < len(days) and days[index] + 30 > days[i]:
                i += 1
            month_cost = costs[2] + solve(i)

            return min(day_cost,week_cost,month_cost)
        return solve(0)
