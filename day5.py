#question 1(Hashin in Python)METHOD 1
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

for num in m:
  count = 0
  for x in n:
    if x==num:
      count+=1

print(count)

#Question 1(Hashing in Pyhton)METHOD 2
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]
hash_list = [0]*11
for num in n:
  hash_list[num+=1]

for num in n:
  if num<1 or num>10:
    print(0)
  else:
    print(hash_list[num])

#Question 18(Hashing in Pyhton)METHOD 3
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]
freq = {}
for num in n:
  freq[num] = freq.get(num,0)+1

for num in m:
  print(freq.get(num,0))

#Question 19(Character Hashing)METHOD 1
s = "azyxxyyzaaaa"
q = ["d","a","y","x"]
for ch in q:
    count = 0
    for c in s:
        if c==ch:
            count+=1

    print(count)

#Question 19(Character Hashing)METHOD 2
s = "azyxxyyzaaaa"
q = ["d","a","y","x"]
hash_dict = {}
for ch in s:
    hash_dict[ch] = hash_dict.get(ch,0)+1

for ch in q:
    print(hash_dict.get(ch,0))

#Question 19(Character Hashing)METHOD 3
s = "azyxxyyzaaaa"
q = ["d","a","y","x"]
hash_list = [0]*26
for ch in s:
    index = ord(ch)-ord('a')
    hash_list[index]+=1

for ch in q:
    index = ord(ch)-ord('a')
    print(hash_list[index])
