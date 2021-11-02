ns=input()
n=int(ns)
j=0
for i in ns:
    for k in range(2,n//2):
        if n%k==0:
            j+=1
    ns=ns[1:]+ns[0]
    n=int(ns)
if j==0:
    print('prime')
else:
    print('not prime')