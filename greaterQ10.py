a=int(input("Enter a a number--"))
b=int(input("Enter a b number--"))
c=int(input("Enter a c number--"))
print((a if a>c else c) if a>b else ( b if b>c else c))