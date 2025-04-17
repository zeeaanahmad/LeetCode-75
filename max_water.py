class Solution:
    def maxArea(self, height: List[int]) -> int:
        results = []
        for i in range(len(height)):
            for j in range(i):
                add = (min([height[i],height[j]]))
                sub = (i-j)
                results.append(add*sub)


            

        # print(max(results))
        return max(results)
        
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the current area
            width = right - left
            current_height = min(height[left], height[right])
            area = width * current_height

            # Update max area if current is larger
            max_area = max(max_area, area)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
