import streamlit as st
import google.generativeai as genai

# Configuração da sua chave (Você vai colar a chave que pegou no passo anterior aqui)
genai.configure(api_key="AIzaSyAhiF4ga6DtObnv4pzlA7_z0yIvg6bnNuY")

st.title("Agente Contábil IA - Nicholas")
st.subheader("Transforme meses de trabalho em segundos")

arquivo = st.file_uploader("Suba aqui o Excel ou PDF com os dados brutos", type=["csv", "xlsx", "pdf", "txt"])

if arquivo:
    st.info("Processando dados com inteligência artificial...")
    # Aqui o código envia para o Gemini com o prompt que treinamos
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(f"Atue como contador sênior. Transforme estes dados em uma tabela contábil e gere o código CSV de importação: {arquivo.name}")
    
    st.success("Processamento Concluído!")
    st.write(response.text)
    st.download_button("Baixar Arquivo de Importação (CSV)", response.text, "importacao_contabil.csv")
  
