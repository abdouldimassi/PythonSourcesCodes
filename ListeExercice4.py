liste_mots = ['Jean','Maximilien','Brigitte','Sonia','Jean-Pierre','Sandra']
liste_mots_plus_six = []
liste_mots_moins_six = []
for i in range(len(liste_mots)):
    if len(liste_mots[i]) >= 6 :
        liste_mots_plus_six.append(liste_mots[i])
    else:
        liste_mots_moins_six.append(liste_mots[i])
print('Liste des noms contenant plus de 6 caracteres : ', liste_mots_plus_six)
print('Liste des noms contenant moins de 6 caracteres : ', liste_mots_moins_six)
       
