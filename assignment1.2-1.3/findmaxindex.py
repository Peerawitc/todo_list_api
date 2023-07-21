arr =   [1,2,6,3,5,2,4] 
def findmaxindex(arr):
    max_number = 0
    max_index = 0
    for i in range(len(arr)):
        if max_number<arr[i]:
            max_number=arr[i]
            max_index= i
    return max_index

       
print(findmaxindex(arr))