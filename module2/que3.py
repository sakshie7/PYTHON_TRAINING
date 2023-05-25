num=int(input("enter any number:"))
n1=0
n2=1
sum=0

if num<=0:
    print("number is negative")
else: 
    for i in range(0,num):
         print(sum,end=" ")
         n1=n2
         n2=sum
         sum=n1+n2
   