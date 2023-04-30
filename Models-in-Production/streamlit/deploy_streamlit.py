import pickle
import streamlit as st

st.header('Aplicação')
st.subheader('Construído em Python')
st.markdown('Insira as informações para efetuar as previsões')

# Slider 
tamanho = st.slider('Informe o tamanho da casa:',min_value = 10.0, max_value = 600.0)
st.write(tamanho)

ano = st.text_input('Informe o ano da casa: ', max_chars=4)
st.write(ano)

garagem = st.slider('Informe a quantidade de garagens da casa: ',min_value = 0, max_value = 5)
st.write(garagem)

# Seleção dentre uma lista de opções pré-definida
modelos_opcoes = ['Regressão Linear','Regressão Ridge', 'Regressão Lasso']
opcao = st.selectbox('Escolha o modelo de Machine Learning a ser utilizado:', options = modelos_opcoes)
st.write(opcao)

if opcao == 'Regressão Linear':
    modelo = pickle.load(open('modelo_rl.pkl','rb'))
if opcao == 'Regressão Ridge':
    modelo = pickle.load(open('modelo_ridge.pkl','rb'))
if opcao == 'Regressão Lasso':
    modelo = pickle.load(open('modelo_lasso.pkl','rb'))

botao = st.button('Fazer previsão')
if(botao):
    st.write(modelo.predict([[tamanho, ano, garagem]])[0])
