# cook your dish here
a,b,c = map(int, input().split())
if a*c>b*c:
    print(a*c)
elif a*c<b*c:
    print(b*c)
elif a*c == b*c:
    print(a*c)
