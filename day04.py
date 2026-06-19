#question 1(Count the Number of Digits in an Integer)
n = 5478
num = n
count = 0

while num>0:
  count+=1
  num = num//10


print(count)

from math import*
n = 177715
digits = int(log10(n))+1
print(digits)

#question 2(Check if the Number is Palindrome or not)
n = 1234
num = n
result = 0

while num>0:
  ld = num%10
  result = (result*10)+ld
  num = num//10

print(result)

#question 3(Armstrong Number)
n = 153
num = n
total = 0
nod = len(str(n))

while num>0:
  ld = num%10
  total = total+(ld**nod)
  num = num//10

print(total)

#question 4(Print All Factors of the Given Number)
n = 20
num = n
result = []
for i in range(1, num+1):
  if num%i==0:
    result.append(i)

print(result)

#question 4(Print All Factors of the Given Number)BETTER SOLUTION
n = 10
num = n
result[]
for i in range(1, num+1):
  if num%i==0:
    result.append(i)

result.append(num)
print(result)

#question 4(Print All Factors of the Given Number)OPTIMAL SOLUTION
from math import sqrt
result = []
for i in range(1, int(sqrt(num))+1):
  if num%i==0:
    result.append(i)
    if num//i !=i:
      result.append(num)

result.sort()
print(result)

#question 5(Store Frequency in Dictionary)METHOD 1
num = [5,6,7,7,1,9,111,1,1,5,1,1]
freq_map = dict()
for i in range(0, len(num)):
    if num[i] in freq_map:
        freq_map[num[i]]+=1

    else:
        freq_map[num[i]]=1

print(freq_map)

#question 5(Store Frequency in Dictionary)METHOD 2
num = [5,6,7,7,1,9,111,1,1,5,1,1]
hash_map = dict()
n = len(num)
for i in range(0, n):
    hash_map[num[i]] = hash_map.get(num[i],0)+1
print(hash_map)    
