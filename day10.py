#Question 1(Remove Dulpicate Elements from the Sorted Array)IN PLACE(BRUTE FORCE SOLUTION)
arr = [1,1,1,2,3,4,4,7,9,9,9,10]
n = len(arr)
freq_map = {}
for i in range(0,n):
  freq_map[arr[i]] = 0
  j = 0

for k in freq_map:
  arr[j] = k
  j+=1

print(freq_map)

#Question 2(Remove Dulpicate Elements from the Sorted Array)IN PLACE(OPTIMAL SOLUTION)
def removeDuplicates(arr):
  n = len(arr)
  if n == 1:
    return 1
  i = 0
  j = i+1
  while j<n:
    if arr[j]!=arr[i]:
      i+=1
      arr[i],arr[j] = arr[j],arr[i]
    j+=1
  return i+1
arr = [1,1,1,2,3,4,4,7,9,9,9,10]
unique_count = removeDuplicates(arr)
print("modified array",arr[:unique_count])

#Question 3(Right a List by one place)
arr = [5,-2,3,9,0,6,10,7]
n = len(arr)
temp = arr[n-1]
for i in range(n-2,-1,-1):
  arr[i+1] = arr[i]
arr[0] = temp
print(arr)

#Question 4(Right Rotate a List by k place)BRUTE FORCE SOLUTION
arr = [3,9,5,6,7,2]
k = 5
n = len(arr)
r = k%n
for _ in range(0,r):
  e = arr.pop()
  arr.insert(0,e)

print(arr)

#Question 5(Right Rotate a List by k place)BETTER SOLUTION
arr = [3,9,5,6,7,2]
arr[:] = arr[n-k:]+arr[:n-k]
print(arr)

#Question 9(Right Rotate a List by k place)OPTIMAL SOLUTION
def reverse(nums,left,right):
  while left<right:
    nums[left],nums[right] = nums[right],nums[left]
    left+=1
    right-=1
nums = [3,9,5,6,7,2,10,9]
k = 3
n = len(nums)
k = k%n
reverse(nums,n-k,n-1)
reverse(nums,0,n-k-1)
reverse(nums,0,n-1)

print(nums)






