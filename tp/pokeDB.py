import json

def pokeyolo():
    fichier_json = open('pokemon.json', 'r', encoding="utf-8")
    Imc_value = 22
    data = []
    with fichier_json as fichier:
       for line in fichier:
           data.append(json.loads(line))

    Pokedata = None

    for datum in data[1:]:
        if(abs(datum['weight']/(datum['height'])*(datum['height'])-Imc_value)<2):
            Pokedata = datum['name']

    if (Pokedata == None):
        print("I'm sorry but you don't exist in the pokemon world")
        return "I'm sorry but you don't exist in the pokemon world"
    else:
        print("your pokemon match is : " + Pokedata)
        return "your pokemon match is : " + Pokedata

pokeyolo()
