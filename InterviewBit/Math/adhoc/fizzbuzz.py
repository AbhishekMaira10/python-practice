class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        res = []
        for i in range(1, A+1):
            val = "Fizz"*(i % 3 == 0) + "Buzz"*(i % 5 == 0)
            res += [val] if val else [i]
        return res
