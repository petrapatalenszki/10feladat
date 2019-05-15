import matplotlib.pyplot as plt
def pascalharomszog(n):
    if n==0:
        return [1]
    else:
        X = pascalharomszog(n-1)
    return [1] + [X[i] +X[i+1] for i in range(n-1)] + [1]
def kiir(n):
    for i in range(n+1):
        print(pascalharomszog(i))


n1,n2=(input('ket szamot vesszovel elvalasztva, n1 legyen nagyobb mint n2')).split(',')
n1,n2=int(n1),int(n2)
while n1<n2 or n1==n2:
    n1, n2 = (input('ket szamot vesszovel elvalasztva, n1 legyen nagyobb mint n2')).split(',')
    n1, n2 = int(n1), int(n2)

kiir(n1)
plt.plot(pascalharomszog(n2),'g.')
plt.show()
