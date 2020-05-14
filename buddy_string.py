class Solution:
  def buddyStrings(self, A, B):
        if len(A) != len(B):
            return False
        if A==B:
            seen = set()
            for a in A:
                if a in seen:
                    return True
                seen.add(a)
            return False
        else:
            swap_count = 0
            index = []
            for i in range(0, len(A)):
                if swap_count>2:
                    return False
                if A[i] != B[i]:
                    index.append(i)
                    swap_count += 1
            if index and A[index[0]] == B[index[1]] and A[index[1]] == B[index[0]]:
                return True
            return False

print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))