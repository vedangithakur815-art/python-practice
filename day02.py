#Question 1
monday = 84
tuesday = 74
avg = (monday/tuesday)/2
print(avg)

#Question 2
age = 22
height = 5.11
print(age,type(age))
print(height,type(height))

#Question 3
a = input("Enter your First Name")
b = input("Enter your Last Name")
print(a,b)

#Question 4(take input of age on the basis of age print eligible or not eligible)
age = int(input("Enter your age"))

if(age>=18):
  test = input()
  if test=="PASS":
    print("Eligible for the Driving License")
  else:
    print("Not Eligible for the Driving License")

else:
  print("Not Eligible for the Driving License")

#Question 5(Marks)
marks = int(input("Enter your Marks"))

if marks>=90:
  print("Excellent")
elif marks>=70:
  print("Good")
elif marks>=40:
  print("Fair")
else:
  print("Bad")

#Question 6(Temperature)
temp = int(input("Enter the Temperature"))

if temp<=50 and Temp>=25:
  print("Hot")
elif 10<=temp<=24:
  print("Cold")
elif temp<10:
  print("Extremely Cold")
            
#Question 7(Ternary Operator)
age = int(input("enter your age"))
result = "Eligible" if age>=18 else "Not Eligible"
print(result)

#question 8
i = 0
while i<5:
  print(i,end=" ")
  i+=1

#Question 9
list1 = [1,2,3,4]

for i in list1:
  print(i,end=" ")

#Question 10
for i in range(1,11):
  print(i,end=" ")
print()  

for i in range(1,11,2):
  print(i,end=" ")
print()  

for i in range(20,0):
  print(i,end=" ")
print()  

#Question 11
def addtwonumbers(a,b):
  sum = a+b
  return sum

ans = addtwonumbers(15,3)
print(ans)

  
