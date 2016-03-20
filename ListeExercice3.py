t2 = [32,5,12,8,3,75,2,15]
liste_paires = []
liste_impaires = []
i = 0
while i < len(t2):
    if t2[i] % 2 == 0 :
        liste_paires.append(t2[i])
    else:
        liste_impaires.append(t2[i])
    i+=1
print('Liste des nombres paires : ' , liste_paires)
print('Liste des nombres impaires : ' , liste_impaires)
