
#encoding in utf-8
"""
Spyder Editor

This is a temporary script file.
"""
from math import sqrt
def jointure_tab():
    '''
    Cette fonction permet de joindre la table Caracteristiques_des_persos
    à la table Characters dans une nouvelle table appelé poudlard_characters.
    
    entrer : deux table (Caracteristiques_des_persos et Characters)
    sortie : une nouvelle table (poudlard_characters)
    '''
    import csv
    
    #ouverture de la table characters_tab
    with open("Characters.csv", mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        characters_tab = [{key : value for key, value in element.items()} for element in reader]
    
    #ouverture de la table characteristic_perso
    with open("Caracteristiques_des_persos.csv", mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        characteristics_tab = [{key : value for key, value in element.items()} for element in reader]
    
    #jointure des deux table grace à l'element 'Name'
    poudlard_characters = []
    for poudlard_character in characteristics_tab:
        for kaggle_character in characters_tab:
            if poudlard_character['Name'] == kaggle_character['Name']:
                poudlard_character.update(kaggle_character)
                poudlard_characters.append(poudlard_character)
                
    return poudlard_characters
def house(table):
    '''
    Cette fonction permet de déterminer avec quelle maison
    notre personnage a le plus d'affiniter,
    pour ensuite choisir sa maison grace a la table
    en parametre
    
    entrer : liste de liste
    sortie : string (maison du personnage) et liste des 5
    plus proche voisin
    '''
    #on crée une table final
    table_final = []
    
    #on crée une variable pour chaque maison
    Ravenclaw = 0
    Gryffindor = 0
    Hufflepuff = 0
    Slytherin = 0
    
    # on crée une un boucle qui va donner 1 point a la maison d'affiniter
    #pour chacune de ses caracteristique (donc la boucle va se repeter 4 fois)
    for d in range(5):
        if table[d][1] == 'Ravenclaw':
            Ravenclaw = Ravenclaw + 1
        elif table[d][1] == 'Gryffindor':
            Gryffindor = Gryffindor + 1
        elif table[d][1] == 'Hufflepuff':
            Hufflepuff = Hufflepuff + 1
        elif table[d][1] == 'Slytherin':
            Slytherin = Slytherin + 1
        mini_table = []
        mini_table.append(table[d][0])
        mini_table.append(table[d][1])
        table_final.append(mini_table)
    
    #la maison qui aura le plus de point a la fin de cette iteration
    #sera la maison de prédilection du personnage
    if Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw > Slytherin:
        maison = "Ravenclaw"
        return(maison, table_final)
    elif Gryffindor > Ravenclaw and Gryffindor > Hufflepuff and Gryffindor > Slytherin:
        maison = "Gryffindor"
        return(maison, table_final)
    elif Hufflepuff > Ravenclaw and Hufflepuff > Gryffindor and Hufflepuff > Slytherin:
        maison = "Hufflepuff"
        return(maison, table_final)
    elif Slytherin > Ravenclaw and Slytherin > Gryffindor and Slytherin > Hufflepuff:
        maison = "Slytherin"
        return(maison, table_final)

table = jointure_tab()

for index in range(len(table)) :
    table[index]['Courage'] = int(table[index]['Courage'])
    table[index]['Ambition'] = int(table[index]['Ambition'])
    table[index]['Intelligence'] = int(table[index]['Intelligence'])
    table[index]['Good'] = int(table[index]['Good'])
characteristic = {'Courage' : 5, 'Ambition' : 7, 'Intelligence' : 6, 'Good' : 3}

table_CAIG = []
for j in range(len(table)) :
    table_CAIG_small = []
    table_CAIG_small.append(table[j]['Name'])
    table_CAIG_small.append(table[j]['House'])
    table_CAIG_small.append(table[j]['Courage'])
    table_CAIG_small.append(table[j]['Ambition'])
    table_CAIG_small.append(table[j]['Intelligence'])
    table_CAIG_small.append(table[j]['Good'])
    table_CAIG.append(table_CAIG_small)
i = 0
for i in range(len(table_CAIG)) :
    perso = sqrt(sqrt((((characteristic['Courage']) ** 2 - int(table_CAIG[i][2]) ** 2
    + int(characteristic['Ambition']) ** 2 - int(table_CAIG[i][3]) ** 2
    + int(characteristic['Intelligence']) ** 2 - int(table_CAIG[i][4]) ** 2
    + int(characteristic['Good']) ** 2 - int(table_CAIG[i][5]) ** 2)**2)))
    table_CAIG[i].append(perso)
for i in range (0, len(table_CAIG)):
        while table_CAIG[i][6] < table_CAIG[i - 1][6] and i > 0:
            table_CAIG[i], table_CAIG[i - 1] = table_CAIG[i - 1], table_CAIG[i]
            i = i - 1
house , tab_maison = house(table_CAIG)
for i in range(5):
    print(f'Vous avez des aptitude voisine à {tab_maison[i][0]} qui est {tab_maison[i][1]}')
print(f'Apres reflexion vous serez ... \n{house}!')
 