#Question 1(Fizz Buzz)
from typing import List
class Solution:
  def fizzBuzz(self, n: int) -> List[str]:
      ans = []
      for i in range(1, n+1):
          if i%3==0 and i%5==0:
              ans.append("FizzBuzz")
          elif i%3==0:
              ans.append("Fizz")
          elif i%5==0:
              ans.append("Buzz")
          else:
              ans.append(str(i))

      return ans

sol = Solution()
print(sol.fizzBuzz(15))
    
#Question 2(Count Odd Numbers in an Interaval Range)
class Solution:
  def countOdds(self, low: int, high: int) -> int:
    return (high+1)//2 - (low//2)

sol = Solution()
print(sol.countOdds(3,7))

#Question 3(How Many Numbers arw Smaller than the Current Number)
from typing import List
class Solution:
  def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    ans = []
    for i in nums:
      c = 0
      for j in nums:
        if j < i:
          c += 1
      ans.append(c)

    return ans

sol = Solution()
print(sol.smallerNumbersThanCurrent([8,1,2,2,3]))

#Question 4(Count the Digits that divide a Number)
from typing import List
class Solution:
  def countDigits(self, num: int) -> int:
    temp = num
    ans = 0
    while temp>0:
      r = temp>0:
      if num%r==0:
        ans+1
      temp//=10  

     return ans
    


