class Solution:
    # dutch national flag algorithm

    """ the value of low = mid = 1 and high = N.
     If the ith element is 0 then swap the element to the low range, thus shrinking the unknown range.
     Similarly, if the element is 1 then keep it as it is but shrink the unknown range.
    If the element is 2 then swap it with an element in high range. """

    def sort_colors(self, nums):
        low = 0
        mid = 0
        high = len(nums) - 1

        while(mid <= high):

            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                mid += 1
                low += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
