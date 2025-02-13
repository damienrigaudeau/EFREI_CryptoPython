from cryptography.fernet import Fernet
from flask import Flask, render_template
                                                                                                                                       
app = Flask(__name__)

key = Fernet.generate_key()
f = Fernet(key)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/exercice1')
def exo1():
     return render_template('exercice1.html')

@app.route('/exercice2')
def exo2():
     return render_template('exercice2.html')

@app.route('/exercice3')
def exo3():
     return render_template('exercice3.html')

@app.route('/exercice4')
def exo4():
     return render_template('exercice4.html')

@app.route('/svg')
def exo_svg():
     return render_template('svg.html')

@app.route('/maison_version_chatgpt')
def exo_maisonv1():
     return render_template('maison_version_chatgpt.html')
    
@app.route('/maison_v2')
def exo_maisonv2():
     return render_template('maison_v2.html')

@app.route('/valet')
def exo_valet():
     return render_template('valet.svg')

@app.route('/chenille')
def exo_chenille():
     return render_template('chenille.html')

@app.route('/Jeu_de6')
def exo_Jeu_de6():
     return render_template('Jeu_de6.html')
    
@app.route('/imageJS')
def exo_imageJS():
     return render_template('imageJS.html')
    
@app.route('/russe')
def exo_russe():
     return render_template('russe.html')

@app.route('/russeexo1')
def exo_russe1():
     return render_template('russeexo1.html')

@app.route('/russeexo2')
def exo_russe2():
     return render_template('russeexo2.html')

@app.route('/russeexo3')
def exo_russe3():
     return render_template('russeexo3.html')

@app.route('/russeexo4')
def exo_russe4():
     return render_template('russeexo4.html')

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytess
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str
                                                                                                                                                     
if __name__ == "__main__":
  app.run(debug=True)
