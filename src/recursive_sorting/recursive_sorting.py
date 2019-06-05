# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements =  len(arrA)  +  len(arrB) 
    merged_arr = [] 
    # TO-DO
    i = j = 0
    
    while i < len(arrA) and j < len(arrB):
        if arrA[i] >= arrB[j]:
            merged_arr.append(arrB[j])
            j += 1
        else:
            merged_arr.append(arrA[i])
            i += 1
    
    merged_arr += (arrA[i:] + arrB[j:]) 
    
    return merged_arr
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    mid_point = int(len(arr) / 2)
    beginning = merge_sort(arr[:mid_point])
    end = merge_sort(arr[mid_point:])
    arr = merge(beginning, end)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
