# fabonacci series in list

a=0
b=1
n=[a]
while b<1000:
    n.append(b)
    a,b=b,a+b
print(n)