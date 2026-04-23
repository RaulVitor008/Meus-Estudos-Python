import streamlit as st

st.title('cadastro de clientes')

nome =st.text_input('digite o nome do cliente')
endereco=st.text_input('digite o endereço')
data_nascimento=st.date_input('escolha a data de nascimento')
tipo_cliente = st.selectbox('Tipo de cliente',['pessoa fisica','pessoa juridica'])

cadastrar = st.button('cadastrar cliente')

if cadastrar:
    with open('clientes.csv', 'a', encoding='utf8') as arquivo:
        arquivo.write(f'{nome},{endereco},{data_nascimento},{tipo_cliente}. \n')
        st.success('cadastro salvo com sucesso!') 