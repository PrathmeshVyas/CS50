a=7
b=10
if a<b:
    print("a is less")
elif a>b:
    print("b is big")
else:
    print("equal")


s = input()

if s.lower() in ["y", "yes"] or s.upper() in ["Y", "YES"]:
    print("agreed")


m=int(input())

def meow():
    print("meow")
    
for i in range(m):
    meow()