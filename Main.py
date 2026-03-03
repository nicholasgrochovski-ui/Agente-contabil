import streamlit as st
import google.generativeai as genai

# Puxa a chave do cofre seguro que você configurou
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

st.title("Agente Contábil IA - Nicholas")
st.subheader("Transforme meses de trabalho em segundos")

arquivo = st.file_uploader("Suba aqui o Excel ou PDF com os dados brutos", type=["csv", "xlsx", "pdf", "txt"])

if arquivo:
    st.info("Processando dados com inteligência artificial...")
    
    # Lendo o conteúdo real do arquivo
    conteudo = arquivo.read().decode("utf-8", errors="ignore")
    
    # Usando a versão estável para evitar o erro "Permission Denied"
    model = genai.GenerativeModel('gemini-1.0-pro')
    
    # O comando com a "Memória de Contador Sênior" que discutimos
    prompt = f"Atue como contador sênior. Analise o conteúdo deste documento e transforme em uma tabela contábil organizada para Imposto de Renda. Gere também o código CSV para importação. Conteúdo: {conteudo}"
    
    response = model.generate_content(prompt)
    
    st.success("Processamento Concluído!")
    st.write(response.text)
    st.download_button("Baixar Arquivo de Importação (CSV)", response.text, "importacao_contabil.csv")
    
