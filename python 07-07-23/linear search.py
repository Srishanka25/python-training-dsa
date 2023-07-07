def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
numbers=[5,9,2,7,1,8,3]
target=8
index=linear_search(numbers,target)
print(f"Target found at index:{index}")