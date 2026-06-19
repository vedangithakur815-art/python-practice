#Question 1(Find the Fibonacci Number)
class Solution:
  def func(self, num):
    if num==0 or num==1:
      return num
    return self.func(num-1)+self.func(num-2)
  def fib(self, n:int)->int:
    answer = self.func(n)
    return answer
obj = Solution()
print(obj.fib(5))

#Question 2(Arrange in Ascending Order) SELECTION SORT
nums = [5,7,8,4,1,6,9,2]

for i in range(len(nums)):
  min_index = i
  for j in range(i+1,len(nums)):
    if nums[j]<nums[min_index]:
      min_index = j
  nums[i],nums[min_index] = nums[min_index],nums[i]

print("Ascending Order",nums)

#Question 2(Arrange in Ascending Order) SELECTION SORT
nums = [5,7,8,4,1,6,9,2]

for i in range(len(nums)):
  max_index = i
  for j in range(i+1,len(nums)):
    if nums[j]>nums[max_index]:
      max_index = j
  nums[i],nums[max_index] = nums[max_index],nums[i]

print("Descending Order",nums)

#Quesion 3(Arrange in Ascending Order) BUBBLE SORT
nums = [5,7,8,4,1,6,9,2]
n = len(nums)
for i in range(n-2,-1,-1):
  for j in range(0,i+1):
    if nums[j]>nums[j+1]:
      nums[j],nums[j+1] = nums[j+1],nums[j]

print("Ascending order:",nums)

#Quesion 4(Arrange in Descending Order) BUBBLE SORT
nums = [5,7,8,4,1,6,9,2]
n = len(nums)
for i in range(n):
  for j in range(0,n-i-1):
    if nums[j]<nums[j+1]:
      nums[j],nums[j+1] = nums[j+1],nums[j]

print("Descending order:",nums)

#Question 5(Arrange in Descending Order)INSERTION SORT
nums = [3,5,6,4,8,9,10,7,1]
n = len(nums)
for i in range(1,n):
  key = nums[i]
  j = i-1
  while j>=0 and nums[j]>key:
    j-=1
  nums[j+1] = nums[j]

print("ascending order:"nums)

#Question 6 MERGE SORT
def merge_array(left,right):
  sorted_arr = []
  i = j = 0
  while i<len(left) and j<len(right):
    if left[i] < right[j]:
      sorted_arr.append(left[i])
      i+=1
    else:
      sorted_arr.append(right[j])
      j+=1
  sorted_arr.extend(left[i:])
  sorted_arr.extend(right[j:])
  return sorted_arr

def merge_sort(arr):
  if len(arr)<=1:
    return arr
  mid = len(arr)//2
  left_half = arr[:mid]
  right_half = arr[mid:]
  left_half = merge_sort(left_half)
  right_half = merge_sort(right_half)
  return merge_array(left_half,right_half)

nums = [3,1,2,4,1,5,2,6,4]
sorted_nums = merge_sort(nums)
print(sorted_nums)

#Question 7(Merge Two Sorted Array)
def merge_array(left,right):
  sorted_arr = []
  i = j = 0
  while i<len(left) and j<len(right):
    if left[i]<right[j]:
      sorted_arr.append(left[i])
      i+=1

    else:
      sorted+arr.append(right[j])
      j+=1

sorted_arr.extend(left[i:])
sorted_arr.extend(right[j:])

arr1 = [1,2,3,4]
arr2 = [1,1,1,3,4,5,6,7]
print(merge_array(arr1,arr2))

#question 8(QUICK SORT)
def partition(nums,low,high):
    pivot = nums[low]
    i = low
    j = high
    while i<j:
        while nums[i]<= pivot and i<=high-1:
            i+=1
        while nums[j]>pivot and j>= low+1:
            j-=1
        if i<=j:
            nums[i],nums[j] = nums[j],nums[i]
    nums[low],nums[j] = nums[j],nums[low]
    return j

def quick_sort(nums,low,high):
    if low<high:
        p_ind = partition(nums,low,high)
        quick_sort(nums,low,p_ind-1)
        quick_sort(nums,p_ind+1,high)

nums = [3,1,2,4,6,7,8]
quick_sort(nums,0,len(nums)-1)
print(nums)






  
