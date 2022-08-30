a=int(input("Enter a a number--"))
b=int(input("Enter a b number--"))
c=int(input("Enter a c number--"))
d=b**2-4*a*c
if d>0:
    print("Real and distinct roots")
elif d==0:
    print("Real and equal roots ")
else:
    print("Imaginary roots")