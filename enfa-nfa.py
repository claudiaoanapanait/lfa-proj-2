def enfa_to_nfa(automat, alfabet, stari, stari_fin):
    l_alf = len(alfabet)
    l_stari = len(stari)
    epsilon = [-1] * l_stari

    for i in range(l_stari):
        l1 = [-1] * l_stari
        l1 = back(i, l_alf - 2, 0)
        epsilon[i] = l1
        for z in range(len(l1)):
            if epsilon[i][z] == -1 and len(l1) > 1:
                epsilon[i] = epsilon[i][:z] + epsilon[i][z + 1:]
    for i in range(0, l_alf - 2):
        l2 = [-1] * l_stari
        nou = [-1] * l_stari
        for j in range(l_stari):
            l2 = back(j, i, 0)
            nou[j] = l2
            for z in range(len(l2)):
                if nou[j][z] == -1 and len(l2) > 1:
                    nou[j] = nou[j][:z] + nou[j][z + 1:]
        automat[i] = tranzitie(nou, l_stari)
    automat = automat[:l_stari] + automat[l_stari + 1:]
    l_stari_fin = len(stari_fin)
    fin = [-1] * l_stari
    i = 0
    for j in range(l_stari):
        for k in range(l_stari_fin):
            if stari_fin[k] in epsilon[0][j]:
                fin[i] = j
                i += 1
    stari_fin = fin
    automat = identice(automat, l_alf, l_stari)
    return automat, stari_fin, alf


def tranzitie(nou, l_stari):
    new = [-1] * l_stari
    li = []
    l = [-1] * l_stari
    for j in range(l_stari):
        for i in nou[j]:
            l = back(j, i, 0)
            li.extend(l)
        li.sort()
        li = list(dict.fromkeys(li))
        for i in range(len(li)):
            if li[i] == -1 and len(li[i]) > 1:
                li = li[:i] + li[i + 1:]
        new[j] = li
    return new


def back(poz, e, k):  #calculeaza lambda inchidere + reuniune a
    global automat, stari, l
    if l[0] == -1:
        l[0] = poz
        back(poz, e, k + 1)
    else:
        for i in automat[e][poz]:
            if i not in l[:k]:
                l[k] = i
                if automat[e][i] != -1:
                    back(i, e, k + 1)
                else:
                    return l


def identice(automat, alf, st):
    for j in range(st):
        ok = 0
        for i in range(st):
            if automat[0][i] == automat[0][j]:
                ok += 1
                if ok == 2:
                    ok1 = 1
                    for k in range(1, alf):
                        ok1 = 1
                        if automat[k][i] != automat[k][j]:
                            ok1 = 0
                    if ok1 == 1:
                        for k in range(alf):
                            automat[k] = automat[k][i:] + automat[k][:i + 1]
                        st = len(automat[0])
                ok = 1
    return automat




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
        z = input("z= ")
        z.split()
        l2=[]
        for k in z:
            l2.extend(int(k))
        l.append(l2)
    automat.append(l)
automat, stf, alf = enfa_to_nfa(automat, alf, st, stf)
print(automat)