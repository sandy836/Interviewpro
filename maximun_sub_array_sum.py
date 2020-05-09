def max_subarray_sum(arr):
    global_sum = local_sum = arr[0]
    for num in arr[1:]:
        local_sum = max(num, local_sum+num)
        global_sum = max(global_sum, local_sum)
    return global_sum

print(max_subarray_sum([34, -50, 42, 14, -5, 86]))