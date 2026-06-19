#Question 1(FIND THE LARGEST ELEMENT IN AN ARRAY)METHOD 1
nums = [55,32,-97,99,3,67]
largest nums[0]
n = len(nums)
for i in range(0,n):
  largest = max(largest,nums[i])

print(largest)

#Question 2(FIND THE LARGEST ELEMENT IN AN ARRAY)METHOD 2
nums = [55,32,-97,99,3,67]
largest = ("-inf")
for i in range(0,n):
  largest = max(largest,nums[i])

print(largest)

#Question 3(FIND THE SECOND LARGEST ELEMENT IN AN ARRAY)BRUTE FORCE 
nums = [55,32,97,-55,45,32,88,21]
nums.sort()
n = len(nums)
print(nums[-2])

#Question 3(FIND THE SECOND LARGEST ELEMENT IN AN ARRAY)BETTER SOLUTION
nums = [55,32,97,-55,45,32,88,21]
largest = float("-inf")
S_largest = float("-inf")
n = len(nums)
for i in range(0,n):
  largest = max(largest,nums[i])

for i in range(0,n):
  if nums[i]>S_largest and nums[i]!=largest:
    S_largest = nums[i]

print(S_largest)

#Question 4(FIND THE SECOND LARGEST ELEMENT IN AN ARRAY)OPTIMAL SOLUTION
nums = [55,32,97,-55,45,32,88,21]
largest = float("-inf")
S_largest = float("-inf")
n = len(nums)
for i in range(0,n):
  if nums[i]>largest:
    S_largest = largest
    largest = nums[i]
  elif nums[i]>S_largest and nums[i]!=largest:
    S_largest = nums[i]

print(S_largest)

#Question 5(CHECK IF ARRAY IS SORTED OR NOT)
class Solution:
    def isSorted(self, arr) -> bool:
        # code here
      n = len(arr)
      for i in range(0,n-1):
        if arr[i]>arr[i+1]:
          return False
      return True


arr1 = [3,5,6,8,9,10,20]
print(Solution().isSorted(arr1))
arr2 = [3,5,2,8,9]
print(Solution().isSorted(arr2))

