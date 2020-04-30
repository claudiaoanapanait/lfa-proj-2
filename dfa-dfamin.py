def dfa_dfamin(automat, alf, st, st_fin, q0):
    global q, r
    Mat = []
    for i in range( len(st)):
        l = []
        for j in range(len(st)):
            l.extend('T')
        Mat.append(l)
    for i in st_fin:
        for j in st:
            if i != j:
                Mat[i][j] = 'F'
                Mat[j][i] = 'F'
    # mai adaugam false
    for i in st:
        for j in st:
            if i > j:
                if Mat[i][j] == 'T':
                    q = automat[i][0]
                    r = automat[j][0]
                    if 'F' == Mat[q][r]:
                        Mat[i][j] = 'F'
    ste = []
    for i in st:
        for j in st:
            if i >= j and Mat[i][j] == 'T':
                l=[j, i]
                ste.append(l)

    ok = 0
    while ok == 0:
        ok = 1
        for i in range(len(ste)-1):
            x=ste[i][len(ste[i])-1]
            if x in ste[i+1]:
                ok = 0
                ste[i] = list(dict.fromkeys(ste[i]))
                ste[i] += ste[i + 1]
                ste = ste[:i + 1] + ste[i + 2:]
    automat = automat[:len(ste)] + automat[len(st) + 1:]
    for i in range(len(ste)):
        for j in range(len(ste)):
            for k in range(len(alf)):
                if automat[j][k] in ste[i]:
                    automat[j][k] = i
    for i in ste:
        if q0 in i:
            q0 = i
    stf = []
    for i in st_fin:
        for j in st:
            if i in j:
                stf.append(j)
    for i in range(len(st)):
        if stf not in automat[i]:
            automat = automat[i:] + automat[:i + 1]
    return automat, ste, stf


len_st = int(input("len_st= "))
len_alf = int(input("len_alf= "))
len_stf = int(input("len_ stf= "))
st = []
alf = []
stf = []
q0 = int(input("q0= "))
for i in range(len_st):
    st.append(i)
for i in range(len_alf):
    x = input("x= ")
    alf.append(x)
for i in range(len_stf):
    y = int(input("y= "))
    stf.append(y)
automat = []
for i in range(len_st):
    l=[-1]*len_alf
    for j in range(len_alf):
        z = int(input("z= "))
        l[j]=z
    automat.append(l)
automat, stf, alf = dfa_dfamin(automat, alf, st, stf, q0)
print(automat)