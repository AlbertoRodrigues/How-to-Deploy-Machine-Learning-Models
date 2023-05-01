import streamlit as st
from joblib import dump, load
import numpy as np
import os
import sklearn

# streamlit_app = nome do app

st.header('Aplicação')
st.subheader('Construído em Python')
st.markdown('Insira as informações para efetuar as previsões')

# Slider 
st.subheader('Isso é um slider, serve para as pessoas arrastarem para algum valor inteiro')
alturaSepala = st.slider('Informe a altura da sépala em cm',min_value = 0, max_value = 10)
st.write(alturaSepala)

st.subheader('Isso é um slider, serve para as pessoas arrastarem para algum valor real')
alturaSepala = st.slider('Informe a altura da sépala em cm',min_value = 0.0, max_value = 10.0)
st.write(alturaSepala)

st.subheader('Isso é um caixa de seleção, podemos selecionar umas das opções pré-definidas')
listaOpcoes = ['a','b','c']
opcao = st.selectbox('Escolha a opção', options = listaOpcoes)
st.write(opcao)

st.subheader('Isso é um caixa de seleção com o estilo "radio", muito parecido com a seleção de caixa. Selecionamos algumas das opções')
listOpcoes = ['a','b','c']
suportePlano = st.radio('Tem suporte ao plano internacional?',options = listOpcoes)
st.write('Opção de suporte escolhida: ',suportePlano)

st.subheader('Isso é um caixa de seleção múltipla. Selecionamos algumas das opções')
listOpcoes = ['a','b','c']
suportePlano = st.multiselect('Tem suporte ao plano internacional?',options = listOpcoes)
st.write('Opção de suporte escolhida: ',suportePlano)

st.subheader('Qualquer texto, é bem útil se queremos que o usuário digite um texto')
nome = st.number_input('Digite o valor: ')
st.write(nome)

st.subheader('Qualquer número, é bem útil se queremos que o usuário digite um valor específico')
nome = st.text_input('Nome: ', max_chars=30)
st.write(nome)

st.subheader('Botão, podemos fazer várias coisas úteis caso ele seja clicado')
botao = st.button('Clique aqui')
