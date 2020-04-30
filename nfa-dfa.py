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
                    l.append(tranzitie(0, litera, stare, 0))
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

def tranzitie(poz, litera, stare, k):
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
automat, stf= nfa_to_dfa(automat, alf, st,q0,  stf)
print(automat)