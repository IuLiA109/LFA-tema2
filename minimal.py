# f=open("input1.txt","r")
f=open("input2.txt","r")
L=[x.strip() for x in f.readlines()]
M=[x.split() for x in L]    #lista cu muchi
F=M[len(M)-1]   #stari finale
del M[len(M)-1]

lit=[M[i][1] for i in range(len(M))]
lit=list(set(lit))
lit.sort()  #lista literelor din alfabet (a,b / 0,1)

s=[M[i][0] for i in range(len(M))]
s1=[M[i][2] for i in range(len(M))]
s.extend(s1)
stari=[]
for st in s:
    if st not in stari:
        stari.append(st)
stari.sort()    #multimea starilor

tabel=[['aux' for j in range(len(lit)+1)]for i in range(len(stari))]

for i in range(len(stari)):
    tabel[i][0]=stari[i]
    for linie in M:
        if linie[0]==stari[i]:
            ind=lit.index(linie[1])
            tabel[i][ind+1]=linie[2]


tabel_aux=[[0 for j in range(len(lit)+1)]for i in range(len(stari))]

for i in range(len(stari)):
    tabel_aux[i][0]=stari[i]

litera=ord('A')
for i in range(len(stari)):
    for j in range(len(lit)):
        if tabel[i][j+1] not in F:
            tabel_aux[i][j+1]=chr(litera)
        else:
            tabel_aux[i][j+1]=chr(litera+1)

# # AFISARI
# for l in tabel:
#     print(*l,end='\n')

# print('\n')

# for l in tabel_aux:
#     print(*l,end='\n')

schimbari=True
izolat=[]
izolat.extend(F)
dct=dict()
litera=ord('A')
dct[chr(litera)]=[stari.index(stari[i]) for i in range(len(stari)) if stari[i] not in F]
dct[chr(litera+1)]=[stari.index(F[i]) for i in range(len(F))]
# print(dct)

nef=[stari[i] for i in range(len(stari)) if stari[i] not in F]
# print(nef)

while schimbari==True:

    schimbari=False
    dct1=dct
    dct=dict()
    dctn=dict() #dictionar de nefinale
    dctf=dict() #dictionar de finale
    litera=ord('A')
    dctn[chr(litera)]=[stari.index(nef[0])] #indexul primei stari nefinale

    for i in range(1,len(nef)):
        for key in dctn:
            if (tabel_aux[stari.index(nef[i])][1] , tabel_aux[stari.index(nef[i])][2])==(tabel_aux[dctn[key][0]][1] , tabel_aux[dctn[key][0]][2]):
                dctn[key].append(stari.index(nef[i]))
                break
        else:
                litera+=1
                dctn[chr(litera)]=[stari.index(nef[i])]

    for i in range(0,len(F)):
        for key in dctf:
            if (tabel_aux[stari.index(F[i])][1] , tabel_aux[stari.index(F[i])][2])==(tabel_aux[dctf[key][0]][1] , tabel_aux[dctf[key][0]][2]):
                dctf[key].append(stari.index(F[i]))
                break
        else:
                litera+=1
                dctf[chr(litera)]=[stari.index(F[i])]

    dct=dctn | dctf
    # print(dct)

    if dct1!=dct:
        schimbari=True

    for i in range(len(stari)):
        for j in range(len(lit)):
                for key in dct:
                    if stari.index(tabel[i][j+1]) in dct[key]:
                        tabel_aux[i][j+1]=key

    # for l in tabel_aux:
    #     print(*l,end='\n')


# print(dct)
# print(stari)
# print(M)

# for l in M:
#     print(*l,end='\n')

for key in dct:
    for ind in dct[key]:
        for l in range(len(M)):
            if M[l][0]==stari[ind]:
                 M[l][0]=stari[dct[key][0]]
            if  M[l][2]==stari[ind]:
                 M[l][2]=stari[dct[key][0]]

# print(M)

stari=[dct[a][0] for a in dct]
# print(stari)

N=[]
for l in M:
    if l not in N:
        N.append(l)

# print('\n')

for l in N:
    print(*l,end='\n')
    