def longest_substring_with_k_distinct_characters(s, k):
    window_start = longest_max=0
    char_count = dict()
    for window_end in range(0, len(s)):
        char_count[s[window_end]] = char_count.get(s[window_end], 0) + 1 
        
        while len(char_count)>k:
            char_count[s[window_start]] -= 1
            if char_count[s[window_start]] == 0:
                del char_count[s[window_start]]
            window_start += 1 
        
        longest_max = max(longest_max, window_end - window_start + 1)
    return longest_max


print(longest_substring_with_k_distinct_characters('aaaabaaaaaab', 2))
