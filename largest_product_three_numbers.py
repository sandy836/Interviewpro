def maximum_product_of_three(lst):
    lst.sort()
    product_1 = lst[-1]*lst[0]*lst[1]
    product_2 = lst[-1]*lst[-2]*lst[-3]
    if product_2>product_1:
        return product_2
    return product_1

print(maximum_product_of_three([-4, -4, 2, 8]))