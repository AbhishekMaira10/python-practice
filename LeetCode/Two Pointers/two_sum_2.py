class SolutionTwoPointer:
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]


class SolutionHashTable:
    def twoSum(self, numbers, target):
        seen = {}
        for i, n in enumerate(numbers):
            if n in seen:
                return [seen[n] + 1, i + 1]
            seen[target - n] = i
