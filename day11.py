#Question 11(Move Zeroes to the End)BRUTE FORCE SOLUTION
def move_zeroes_brute_force(nums):
    n = len(nums)
    temp = []
    for i in range(0,n):
        if nums[i]!=0:
            temp.append(nums[i])
    nz = len(temp)
    
    for i in range(0,nz):
        nums[i] = temp[i]
    for i in range(nz,n):
        nums[i] = 0

    return nums

nums = [1,0,2,4,3,0,0,3,5,1]
print(move_zeroes_brute_force(nums))

#Question 2(Move Zeroes to the End)OPTIMAL SOLUTION
def move_zeroes(nums):
    if len(nums)==1:
        return

    i = 0
    while i<len(nums):
        if nums[i]==0:
            break
        i+=1
    if i == len(nums):
        return
    j = i+1
    while j<len(nums):
        if nums[j]!=0:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
        j+=1
    return nums

nums = [1,0,2,4,3,0,0,3,5,1]
print(move_zeroes(nums))

#Question 13(Linear Search)
def linear_search(nums,target):
  n = len(nums)
  for i in range(0,n):
    return i

  return -1

  nums = [5,3,9,8,1,6,4,-10,-100]
target = 4

result = linear_search(nums,target)
print(result)
    return
  
