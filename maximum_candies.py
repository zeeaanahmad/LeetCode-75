class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        result = []
        for i in range(len(candies)):
            withExtraCandies = candies[i] + extraCandies
            if withExtraCandies >= maximum:
                result.append(True)
            else:
                result.append(False)
        return result

#After optimise the code 
class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maximum = max(candies)
        return [candy + extraCandies >= maximum for candy in candies]