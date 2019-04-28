print ('whatsapp')

def selectionsort(arr):
    for i in range(len(arr)-1):
        unordered = arr[i:] ##back of list
        val = min(unordered) ##find min
        arr[arr.index(val)] = arr[i]
        arr[i] = val


        print(arr)

    return arr

def bubblesort(arr):
    for v in range(len(arr)-1):
        flag = 0
        for i in range(len(arr) - 1):
            
            if arr[i] > arr[i+1]:
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
                flag = 1
            
        if not flag:
            print(v)            
            break
            

    
    print(arr)


def insertionsort(arr):
    '''like taking the right most card, sliding all the sorted
    cards in the left until its in the right place'''
    for i in range(len(arr) - 1):
        val = arr[i+1]
        j = i+1

        while arr[j-1] >  val and j>0:
            arr[j] = arr[j-1]
            arr[j-1] = val
            j -= 1
            print(arr)
    return arr

def mergesort(arr):
    n = len(arr)
    if n == 1: ##base condition
        return arr 
    
    mid = int(n/2)

    left = arr[:mid]
    right = arr[mid:]

    mergesort(left)
    mergesort(right)

    print(left, right)
    mergefix(left, right, arr)

    return arr


def mergefix(left, right, arr):
    l, r, a = len(left), len(right), len(arr)
    i, j, k, = 0 , 0 , 0
    while i < l and j < r:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1 
        k += 1

    while i < l:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < r:
        arr[k] = right[j]
        j += 1
        k += 1
    ##all the work happens in the merge part
    return arr

def quicksort(arr):
    piv = arr[-1]

    ##put pivot in the right position

def twoSum(nums, target):
    if len(nums) <= 1:
        return False
    buff_dict = {}
    for i in range(len(nums)):
        if nums[i] in buff_dict:
            ##if nums[i] is a key
            return [buff_dict[nums[i]], i]
        else:
            ### dict[key'] = value (stored as index)
            buff_dict[target - nums[i]] = i
            print (buff_dict)

print(twoSum([1,2,4,5,6] , 4) )

# nums = [2,1,3,4,0,7,9,8,2,14,9,11,7]

# # selectionsort(nums)
# ans = mergesort(nums)
# print(ans)