num = int(input("Enter the number:"))
y=num
x=0
while num>0:
    s=num%10
    x+=s*s*s
    num=num//10
if(x==y):
    print("This number is a armstrong number")
else:
    print("this number is not an armstrong number")

