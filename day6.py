#Question 1(Recursion using Parameters(x,N times))
def func(x,N):
  if N==0:
    return
  print(x)
  func(x,n-1)

func(15,4)

#Question 2(print 1 to N using Head Recursion)
def func(i,N):
  if i>N:
    return
  print(i)
  func(i+1,N)

func(1,4)

#Question 3(Print N to 1 using Tail Recursion(Backtracking))
def func(i,N):
  if i>N:
    return
  func(i+1,N)
  print(i)

func(1,4)

#Question 4(Print N to 1 using Head Recursion)
def func(N):
  if N==0:
    return
  print(N)
  func(N-1)

func(4)

#question 5(Print 1 to N using Tail Recursion)
def func(N):
  if N==0:
    return
  func(N-1)
  print(N)

func(4)

#Question 6(Sum of 1 to N (Parameterized))
def func(sum,i,N):
  if i>N:
    print(sum)
    return
  func(sum+i,i+1,N)

func(0,1,4)

#Question 7(Sum of 1 to N(Functional))
def func(N):
  if N==1:
    return 1
  return N+func(N-1)

func(4)

#question 8(Find the Factorial of a Number using a Recursion)
def func(N):
  if N==0 or N==1:
    return 1
  return N*func(N-1)

func(5)

#Question 9(Reverse an Array using Recursion)
n = [5,7,3,2,6,1,5,9]
def func(n,left,right):
  if left>=right:
    return
  arr[left],arr[right]=arr[right],arr[left]
  func(arr,left+1,right=1)

func(n,1,7)
print(n)
