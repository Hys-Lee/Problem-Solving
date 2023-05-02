# print("!!")
# array=[5,9,7,8,6,1,4,3,2]

# def quicksort(array, start, end):
#   # pivot은 subarray[0]
#   if start>=end: return

#   pivot = start
#   left = start
#   right = start+1

#   while right<=end:
#     if array[right]<array[pivot]:
#       left +=1
#       array[left], array[right] = array[right], array[left]
#     right+=1

#   array[left], array[pivot] = array[pivot], array[left]
#   quicksort(array, start, left)
#   quicksort(array, pivot+1, right-1)

# quicksort(array, 0, len(array)-1)
# for ele in (array):
#   print(ele)
