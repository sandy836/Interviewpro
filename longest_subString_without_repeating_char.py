class Solution:
    #Approch 1 Time :- O(n^2) Space :- O(n)
    def lengthOfLongestSubstring_1(self, s):
        _max_len = ptr1 = ptr2 = 0
        loopup = ''
        while ptr1<len(s):
            if s[ptr1] in loopup:
                while ptr2<=ptr1 and s[ptr2]!=s[ptr1]:
                    ptr2 += 1
                ptr2 += 1 
                loopup = s[ptr2:ptr1+1]
            loopup += s[ptr1]
            _max_len = max(_max_len, ptr1 - ptr2 + 1)
            ptr1 += 1
        return _max_len
    
    #Approch 2 Time :- O(n) Space :- O(n) using dict
    def lengthOfLongestSubstring_2(self, s):
        _max_len = ptr1 = ptr2 = 0
        loopup = dict()
        while ptr1<len(s):
            if s[ptr1] in loopup and loopup[s[ptr1]]>=ptr2:
                ptr2 = loopup[s[ptr1]]+1
            loopup[s[ptr1]] = ptr1
            _max_len = max(_max_len, ptr1 - ptr2 + 1)
            ptr1 += 1
        return _max_len

print(Solution().lengthOfLongestSubstring_1('abrkaabcdefghijjxxx'))
print(Solution().lengthOfLongestSubstring_2('abrkaabcdefghijjxxx'))