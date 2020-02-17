n=int(input("enter first value"))
a=int(input("enter second value"))
m=int(input("choose 1.add,2.sub,3.multiple,4.divide"))
while(True):
  if(m==1):
    print(n+a)
  elif(m==2):
    print(n-a)
  elif(m==3):
    print(n*a)
  elif(m==4):
    print(n//a)
  else:
    print("please choose 1,2,3,4 for your operations")
    print("do you need to do it again:::(Y/N)")
    c=input()
  if(c=="Y"or c=="y"):
  break
     
