#Question 1(Check if String is Palindrome using Loop)
S = "ANBCDDCBNA"
left = 0
right = n-1

isPalindrome = True

while left<right:
  if S[left]!=S[right]:
    isPalindrome = False
  
  left+=1
  right-=1

print(isPalindrome)

#Question 1(Check if String is Palindrome using Loop)
S = "ANBCDDCBNA"
def func(S,left,right):
  if left>=right:
    return True
  if S[left]!=S[right]:
    return False

return func(S,left+1,right-1)

func(S,0,len(S)-1)
