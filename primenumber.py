n=input("Enter the number")
count=0
for i in range(1,n+1):
    if int(n)%i==0:
      count=count+1
if count==2:
  print"prime number"
else:
  print"not prime number"
