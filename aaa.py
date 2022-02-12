a,b,c=map(int,input(),split())

if a<b:
    d=b
else:
    d=a

if d<c:
    d=c

if d>a:
    e=a
elif d>b:
    e=b
elif d>c:
    e=c

if e>a:
    f=a
elif e>b:
    f=b
elif e>c:
    f=c

print(d)