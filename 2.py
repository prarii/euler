i=0
j=1
fib=0
sum=0
while(fib>=0):
 fib=i+j
 i=j
 j=fib
 if(fib%2==0 and fib<4000000):
  print(fib)
  sum=sum+fib
  print("the sum is:",sum)