def reversestring(s):
          ## RC ##
        ## APPROACH : 2 POINTERS ##
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(N) ##
    left = 0
    right = len(s) - 1
    while(left <= right):
      s[left], s[right] = s[right], s[left]
      left += 1
      right -= 1