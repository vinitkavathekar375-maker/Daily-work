# cook your dish here
x,y,z = map(int, input().split())
a = (x*12)
b = (y*12)
if (a < b+z):
    print(a)
elif (a> b+z):
    print(b+z)
elif (a)==(b+z):
    print(a)
