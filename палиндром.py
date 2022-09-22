pr=1
sp=[]
def numbers(x):
    po=str(x)
    per_pol=int(po[::-1])
    if x==per_pol:
        return True
    else:
        return False
for i in range(100,1000):
    for j in range(100,1000):
        if numbers(i*j)==True:
            sp.append(i*j)
print(max(sp))


