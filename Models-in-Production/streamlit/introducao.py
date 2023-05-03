import streamlit as st
import time
import pandas as pd

data=pd.read_csv("../estudo-APIs/casas.csv")

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
suportePlano = st.radio('Tem suporte ao plano internacional?', options = listOpcoes)
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

agree = st.checkbox('I agree')
if agree:
    st.write('Great!')
    
#@st.cache
st.subheader('Botão para baixar qualquer arquivo')
st.download_button(
    label="Download data as CSV",
    data=data.to_csv().encode('utf-8'),
    file_name='large_df.csv',
    mime='text/csv'
)
    
st.subheader('Adicionando dois status, um de espera e o outro de sucesso')
with st.spinner('Processando...'):
    time.sleep(3)
st.success('Processo Finalizado!')

st.subheader('Acrescentando elementos em uma barra lateral á esquerda')
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)
st.sidebar.write(add_selectbox)


alturaSepala2 = st.sidebar.slider('Informe a altura', min_value = 0, max_value = 20)
st.sidebar.write(alturaSepala2)

