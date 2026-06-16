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


  
