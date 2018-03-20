n=input("Enter the number")
N=n
newno=0
while(n):
   rem=n%10
   newno=newno*10+rem
   n=n/10
if newno==N:
   print"palindrome"
else:
   print"not palindrome"
