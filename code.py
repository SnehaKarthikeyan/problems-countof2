Coding:
  
x=int(input())
count=0
i=0
for j in range(1,x+1):
  i=j
  while i!=0:
    if i%10==2:
      count=count+1
    i=int(i/10)
print(count)    
