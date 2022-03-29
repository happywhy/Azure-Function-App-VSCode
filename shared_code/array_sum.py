# sum all the elements in array arr
def sumall(arr: list)->int:
    if len(arr)==0:
        return 0
    idx = 0

    total_sum = arr.pop(idx)
    if len(arr)==0:
        return total_sum
    else:
        return total_sum+sumall(arr)

    # return sum(new_arr)

    # totalsum = 0
    # for num in len(arr):
    #     totalsum+=arr[num]
    # return totalsum