from flask import Flask, render_template, redirect, url_for, request
import json

app = Flask(__name__)

def pokeyolo(Imc_value):
    fichier_json = open('pokemon.json', 'r', encoding="utf-8")
    data = []
    with fichier_json as fichier:
       for line in fichier:
           data.append(json.loads(line))

    Pokedata = None

    for datum in data[1:]:
        if(abs((datum['weight']/((datum['height'])*(datum['height'])))-Imc_value)<0.1):
            Pokedata = datum['name']

    if (Pokedata == None):
        return "I'm sorry but you don't exist in the pokemon world"
    else:
        return "Your pokemon match is: " + Pokedata

@app.route('/', methods=["GET"])
def index():
    return render_template('test.html')

@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    IMC = float(weight/(height*height))
    rep = pokeyolo(IMC)
    return rep

if __name__=="__main__":
    app.run(host="0.0.0.0")
