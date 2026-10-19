class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        max_volume = 0
        while right > left:
            volume = (right-left) * min(heights[left], heights[right])
            max_volume = max(max_volume, volume)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1
        return max_volume
