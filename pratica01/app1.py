import streamlit as st
import datetime

st.title('Cadastro do alunos')
nome = st.text_input('nome do aluno')
altura = st.text_input('qual sua altura')
peso = st.text_input('qual o seu peso')
endereco = st.text_input('qual é o endereço e cep')
data = st.date_input ('data de nascimento',min_value=datetime.date(1950,1,1),max_value=datetime.date.today())
tipo_aluno = st.selectbox ('tipo do aluno', ['iniciante','intermediario','avançado'])

cadastrar = st.button('Cadastrar cliente')

if cadastrar:
    with open('base_alunos','a') as arquivo:
        arquivo.write(f'{nome},{data},{endereco},{data},{tipo_aluno}.\n')
        st.success('cadastro feito com sucesso, so aguarda o professor')

