#Time complexity O(n^2)
class Solution: 
    def longestPalindrome(self, s):
        left = right = global_longest = 0
        for i in range(0, len(s)):
            #Substring that start at current character as middle
            #Substring of odd length
            len_1 = self.getlongestPalindromeSubString(i, i, s)
            #Substring of even length
            len_2 = self.getlongestPalindromeSubString(i, i+1, s)
            largest_len = max(len_1, len_2)
            
            if largest_len>global_longest:
                left = i-((largest_len-1)//2)
                right = i+(largest_len//2)
                global_longest = largest_len
        
        return s[left:right+1]

    def getlongestPalindromeSubString(self, left, right, s):
        while 0<=left and right<len(s) and s[left]==s[right]:
            left -= 1
            right += 1
        return (right-left-1)

s = "tracecars"
print(str(Solution().longestPalindrome(s)))