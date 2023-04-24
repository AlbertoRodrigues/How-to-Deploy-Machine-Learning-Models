from flask import Flask, request, jsonify
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

df = pd.read_csv('casas.csv')
colunas = ['tamanho','preco']
df = df[colunas]

X = df.drop('preco', axis=1)
y = df['preco']

modelo = LinearRegression()
modelo.fit(X, y)

## Definindo a rota básica
@app.route('/')

def home():
    return "Minha primeira API"


@app.route('/cotacao/', methods=['POST'])
def cotacao():
    dados = request.get_json()
    dados_input = [dados[col] for col in colunas]
    preco = modelo.predict([dados_input])
    return jsonify(preco=preco[0])

app.run(debug=True)

