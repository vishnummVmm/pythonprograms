''' calculator using function'''


a=float(input( "enter first number "))
b=float(input("enter second number"))
def add(m,n):
    sum1=m+n
    return(sum1)
x=add(a,b)
print("sum is",x)
def sub(m,n):
    sub=m-n
    return(sub)
y=sub(a,b)
print("subtracted value is",y)
def mul(m,n):
    mul=m*n
    return(mul)
z=mul(a,b)
print("multiplied value is",z)
def div(m,n):
    div=m/n
    return(div)
k=div(a,b)
print("divided value is",k)
