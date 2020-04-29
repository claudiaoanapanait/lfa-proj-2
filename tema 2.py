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
        li = li(dict.fromkeys(li))
        for i in range(len(li)):
            if li[i] == -1 and len(li[i]) > 1:
                li = li[:i] + li[i + 1:]
        new[j] = li
    return new


def back(poz, e, k):  # calculeaza lambda inchidere + reuniune a
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


def nfa_to_dfa(automat, alf, st, q0, stari_fin):
    Q = []
    Q.append(q0)
    automata = []
    automata.append(automat[0])
    ok = 1
    while ok == 1:
        j = 0
        ok = 0
        for stare in automata[j]:
            if stare not in Q:
                ok = 1
                Q.append(stare)
                lst = [-1] * len(st)
                l = []
                for litera in range(len(alf)):
                    l.append(tranzitie2(0, litera, stare, 0))
                automata.append(l)
        j += 1
    fin = [-1] * len(stari_fin)
    i = 0
    for j in range(len(st)):
        for k in range(len(stari_fin)):
            if stari_fin[k] in automata[0][j]:
                fin[i] = j
                i += 1
    stari_fin = fin
    for i in range(len(Q)):
        for j in range(len(Q)):
            for k in range(len(alf)):
                if Q[i] == automata[j][k]:
                    automata[j][k] = i
    return automata, stari_fin


def tranzitie2(poz, litera, stare, k):
    global lst, automat
    if lst[0] == -1:
        lst[0] = poz
    for i in range(len(stare)):
        for j in automat[litera][i]:
            if j not in lst[:k]:
                lst[k] = j
                if automat[litera][j] != -1 and automat[litera][j] != j:
                    tranzitie(j, litera, stare, k + 1)
                else:
                    return lst


def dfa_dfamin(automat, alf, st, st_fin, q0):
    Mat = [-1] * len(st)[-1] * len(st)
    for i in range(1, len(st)):
        for j in range(len(st)):
            if i > j:
                Mat[i][j] = True
    for i in st_fin:
        for j in st:
            if i != j:
                Mat[i][j] = False
                Mat[j][i] = False
    # mai adaugam false
    for i in st:
        for j in st:
            if i > j:
                if Mat[i][j] == True:
                    q = automat[i][0]
                    r = automat[j][0]
                if Mat[q][r] == False:
                    Mat[i][j] = False
    ste = []
    for i in st:
        for j in st:
            if i >= j and Mat[i][j] == True:
                ste.append([i, j])
    ok = 0
    while ok == 0:
        ok = 1
        for i in range(len(ste)):
            if ste[i + 1] in ste[i]:
                ok = 0
                ste[i] = ste[i](dict.fromkeys(ste[i]))
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


# PROGRAM PRINCIPAL

f = open("fisier.txt")
q0 = f.readline()
q0 = int(q0)
alf = f.readline()
st = f.readline()
stf = f.readline()
alf.split()
st.split()
for i in range(len(st)):
    st[i] = int(st[i])
stf.split()
for i in range(len(stf)):
    stf[i] = int(stf[i])
automat = [-1] * len(st)[-1] * len(alf)
for i in range(len(st)):
    for j in range(len(alf)):
        automat[i][j] = f.readline()
        automat[i][j].split()
        for k in range(len(automat[i][j])):
            automat[i][j][k] = int(automat[i][j][k])
automat, stf, alf = enfa_to_nfa(automat, alf, st, stf)
print(automat)
automat, stf = nfa_to_dfa(automat, alf, st, q0, stf)
print(automat)
automat, st, stf = dfa_dfamin(automat, alf, st, stf, q0)
print(automat)
f.close()
