def merge(intervals):
    intervals = sorted(intervals)
    ans = []
    for start, end in intervals:
        if ans and ans[-1][1]>=start:
            pop_element = ans.pop()
            ans.append((pop_element[0], max(pop_element[1], end)))
        else:
            ans.append((start, end))
    return ans 
  
print(merge([(1, 3), (5, 8), (4, 10), (20, 25)]))
print(merge([(1, 3),(2, 6),(5, 10),(15,18)]))