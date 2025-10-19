sum=0
i=0
while(i<1000):
 if(i%3==0 & i%5==0):
  sum=sum+i
  i=i+1
 elif(i%3==0):
  sum=sum+i
  i=i+1
 elif(i%5==0):
  sum=sum+i
  i=i+1
 else:
  sum=sum+0
  i=i+1
print(i)
print(sum)