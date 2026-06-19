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
