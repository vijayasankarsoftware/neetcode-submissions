class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        warm_days = []

        days = len(temperatures)

        for i in range(days):
            j = i + 1
            got = False
            while j < days:
                if temperatures[i] < temperatures[j]:
                    got = True
                    break
                j += 1
            if got:
                warm_days.append(j - i)
            else:
                warm_days.append(0)
        return warm_days