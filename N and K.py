N=input("Enter n value")
K=input("Enter k value")
a=[input() for i in range(N)]
sum=0
for i in range(K):
  sum=sum+a[i]
print sum
