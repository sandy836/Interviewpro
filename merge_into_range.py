def merge_ranges(arr):
    if not arr:
        return None
    prev = arr[0]
    res = []
    curr_string = str(arr[0])
    for num in arr[1:]:
        if num==prev or prev+1 == num:
            curr_string += "->"+str(num) 
        else:
            if len(curr_string) == 1:
                curr_string += "->"+curr_string
            res.append(curr_string)
            prev = num 
            curr_string = str(num)
        prev = num 
    if len(curr_string) == 1:
        curr_string += "->"+curr_string
    res.append(curr_string)
    return res

print(merge_ranges([]))


