A=[4,6,3,2,56,11,45,22,-10,87,90,345,234,421,978,1024,34,11,21,76,56,11,654,43,45,67,11,2,-56,11,45,-34]
B=[37,17,59,36,75,58,-4,36,46,46,68,81,57,61,34,-50,87,82,37,28,421,978,1024,34,11,21,76,56,11,654,43,45,-67,11]
C=[57,29,44,44,49,78,9,90,96,88,74,19,86,50,40,61,58,81,16,24,11,81,72,62,16,50,87,82,37,28,421,978,1024,34,11,2]
m=input("Liste à analyser: A,B ou C ? ")
def minmax(l):
    mini=l[0]
    maxi=l[0]
    for i in range(len(l)):
        if l[0]>l[i]:
            mini=i
            if l[0]<l[i]:
                maxi=i
    return mini,maxi

print("Les valeurs Mini et Maxi de la liste",m,"sont:",minmax(m))