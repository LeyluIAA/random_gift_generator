# coding: utf-8
from random import shuffle
import json

def main():
    family = get_family('family.json', 'family')
    family, initialFamilyList = shuffleTheFamily(family)
    printResult(family, initialFamilyList)

def get_family(file, key):
    family = []
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for entry in data:
            family = entry[key]

        f.close()

    return family

def shuffleTheFamily(family):
    initialFamilyList = family.copy()
    rulesValid = False

    while not (rulesValid):
        shuffle(family)
        rulesValid = checkRules(family, initialFamilyList)

    return family, initialFamilyList

def checkRules(shuffledList, initialList):
    
    for i in range(len(shuffledList)):
        
        same_giver_same_receiver = (shuffledList[i] == initialList[i])
        dad_offers_to_mum = (shuffledList[i] == 'Papa' and initialList[i] == 'Maman')
        mum_offers_to_dad = (shuffledList[i] == 'Maman' and initialList[i] == 'Papa')
        
        if same_giver_same_receiver or dad_offers_to_mum or mum_offers_to_dad:
            return False
                
        for j in range(len(shuffledList)):
            
            bilateral_giving = (shuffledList[j] == initialList[i] and initialList[j] == shuffledList[i])
            
            if bilateral_giving:
                return False

    return True

def printResult(family, initialFamilyList):
    
    file = open('random_gift_result', 'w', encoding='utf-8')
    file.write('Résultat du tirage au sort:\n\n\n')
    
    for i in range(len(family)):
        file.write(family[i] + ' offre à ' + initialFamilyList[i] + '\n\n')
    
    file.close()

main()
