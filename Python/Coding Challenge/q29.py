class Solution:
    def find(self, arr, n, x):
        # first occurance 
        def first(arr, x,low = 0,high = len(arr) - 1):
            if high >= low:
                mid = low + (high - low) // 2
                if arr[mid] > x:
                    return first(arr, x ,low , mid-1)
                elif arr[mid] < x:
                    return first(arr, x,  mid+1 , high)
                else:
                    if arr[mid] == x and arr[mid-1] != arr[mid]:
                        return mid
                    else:
                        return first(arr, x , low, mid-1)
            return -1
            
        # last occurance
        def last(arr,x,low = 0,high = len(arr) - 1):
            if high >= low:
                mid = low + (high - low) // 2
                if arr[mid] > x:
                    return last(arr, x ,low , mid-1)
                elif arr[mid] < x:
                    return last(arr, x,  mid+1 , high)
                else:
                    if arr[mid] == len(arr) - 1 or arr[mid + 1] != arr[mid]:
                        return mid
                    else:
                        return last(arr, x,  mid+1 , high)   
            return -1
                
        first_occurrence = first(arr, x)
        last_occurrence = last(arr, x)
        return first_occurrence, last_occurrence

