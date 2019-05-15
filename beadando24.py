#24.
def RszTo10esbe (szamrendszer,n1,n2):
    reversen1=str(n1)[::-1]
    reversen2=str(n2)[::-1]
    sumn1=0
    sumn2=0
    sum=0
    for i in range(0, len(reversen1)):
        if reversen1[i] != '0':
            sumn1 += int(reversen1[i]) * (szamrendszer**i)
    for i in range(0, len(reversen2)):
        if reversen2[i] != '0':
            sumn2 += int(reversen2[i]) * (szamrendszer**i)
    sum=sumn1+sumn2
    return sum,szamrendszer
    print(sumn1)
    print(sumn2)

x=RszTo10esbe(2,10110,1010)


def _10esToRsz(sum,szamrendszer):
    string=""
    while sum>0:
        string+=str(sum%szamrendszer)
        sum//=szamrendszer
    return string[::-1]

print(_10esToRsz(46,3))

#reversen visszafelé kell olvasni