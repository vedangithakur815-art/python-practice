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

#Question 4(count the Digits that divide a Number)
class Solution:
  def countDigits(self, num: int) -> int:
      temp = num
      ans = 0
      while temp>0:
          r = temp%10
          if r!=0 and num%r==0:
              ans+=1
          temp//=10  

      return ans

s = Solution()
print(s.countDigits(1212))
    
#Question 5(Palindrome number)
class Solution:
  def isPalindrome(self,x: int) -> bool:
      temp = x
      rev = 0
      
      while temp>0:
          r = temp%10
          temp//=10
          rev = rev*10+r

      return rev==x
s = Solution()
print(s.isPalindrome(121))

#Question 6(Subtract the Product and Sum of Digits of an Integer)
class Solution:
  def subtractProductAndSum(self, n: int) -> int:
      temp = n
      sum_ = 0
      product = 1

      while temp>0:
          r = temp%10
          product *= r
          temp//=10
          sum_+=r

      return product - sum_

s = Solution()
print(s.subtractProductAndSum(234))

#Question 7(Kids with Greatest Number of Candies)
from typing import List
class Solution:
  def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    maxCandies = max(candies)
    ans = []

    for i in candies:
        if (i+extraCandies)>=maxCandies:
            ans.append(True)
        else:
            ans.append(False)

    return ans   
s = Solution()
print(s.kidsWithCandies([2,3,5,1,3],3))

