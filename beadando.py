#10.
def _10fv (x):
    lista=x.split(',')
    for szamsor in lista:
        forditott_string=szamsor[::-1]
        sum = 0
        for i in range(0,len(szamsor)):
            if forditott_string[i]=='1':
                sum+=2**i
        print(szamsor+'!!'+str(sum))

_10fv(x=input('szamokat vesszovel elvalasztva'))