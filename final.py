import fpformat
matriz=[[2.0, -1.0, 1.0,2.0], [3.0, 1.0, -2.0,9.0], [-1.0, 2.0, 5.0,-5.0]]
dimx=0
dimy=0
mini=0
def resolver(m,p):
    for i in range(p):
        flag = True
        if m[i][i] == 0:
           m, flag = False
        if flag:
            m[i] = multi(m[i], 1/float(m[i][i]))
        else:
            return m
        for j in range(i+1,len(m)):
            m[j] = suma_resta(m[j], multi(m[i], -1*float(m[j][i])))
    for k in range(p-1, -1, -1):
        for l in range(k-1, -1, -1):
            m[l] = suma_resta(m[l], multi(m[k], -1*float(m[l][k])))
    return m
def impri(m):
    print "\n"
    print "\t" + ("\t" * (len(m[0]) + 1)) + ""
    for i in range(len(m)):
        print "\t\t",
        for j in range(len(m[0])):
            print fpformat.fix(m[i][j],2),"\t",
        print ""
        print "\t" + ("\t" * (len(m[0]) + 1))  + ""
    print "\n"
def valida_matriz(a,b):  
    if a > b: return b
    elif a < b: return a
    else: return a
def suma_resta(l1, l2):
    ln = [0]*len(l1)
    for i in range(len(l1)):
        ln[i] = l1[i] + l2[i]
    return ln
def multi(l1, k):
    ln = [0]*len(l1)
    for i in range(len(l1)):
        ln[i] = k * l1[i]
    return ln

impri (matriz)
print "             _________________________________________"
mini= valida_matriz(4,3)
sol=resolver(matriz,mini)
impri (matriz)