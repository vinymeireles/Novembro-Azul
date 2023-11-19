import numpy as np
import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
from plotly import graph_objs as go
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from streamlit_extras.metric_cards import style_metric_cards
from sklearn.metrics import accuracy_score
import pickle
from sklearn.preprocessing import StandardScaler

import warnings
warnings.filterwarnings("ignore")


#Apps
st.set_page_config(page_title="App Previsão de Câncer de Próstata", page_icon= ":bar_chart:")
st.header("🎗Analytics Câncer de Próstata🩺", divider='blue')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

#load data #### DataFrame 
@st.cache_data
def load_data():
    data = pd.read_csv("data/Prostate_Cancer.csv")
    return data

df = load_data()

#Sidebar de Opções
st.sidebar.markdown("▶ Selecione uma opção:")
st.sidebar.markdown("")
if st.sidebar.checkbox("🧾**Mostrar Informações**", True, key=0, help="Desmarque essa opção para visualizar outras opções"):
    #Layout da página
    st.subheader("🔎 Analisar previsão de índice em pacientes com câncer de próstata:")

    col1, col2 = st.columns(2)
    with col1:    
        st.markdown("""<h6 style='text-align: justify;'>Nessa seção iremos analisar dados exploratórios de 100 pacientes diagnosticado com câncer de próstata. Análise consiste em EAD dos dados e previsão utilizando algoritmos de machine learning e Dashboard dos dados.</h6""", unsafe_allow_html=True)
        st.markdown("""<h6 style='text-align: justify;'>As etapas seguintes consistem em: Preprocessamentos dos dados, treinamento e testes dos dados, submeter os dados em vários algoritmos de machine learning supervisionados e não supervisionados e por fim prever através dos resultados dos exames as dimensões da próstata do paciente se o nível de câncer é "Benigno" ou "Maligno."</h6""", unsafe_allow_html=True)
    with col2:
        st.image("img/03.png", width=350)

    
    st.divider()

################### Estudo Análise exploratórias dos dados #####################################

#tratamento dos dados nulos e ausentes
    df = df.dropna()

################# Criando um dicionário de dados para as colunas ####################3#
    dic = pd.DataFrame([
                {"id": "ID do paciente",
                "diagnosis_result": "Resultado do Diagnóstico: B ou M",
                "radius": "Raio",
                "texture": "Textura",
                "perimeter": "Perímetro",
                "area": "Área",
                "smoothness": "Suavidade",
                "compactness": "Compacidade",
                "symmetry": "Simetria",
                "fractal_dimension": "Dimensão fractal"},
        ])    

    ################## Mostrar DataFrame #######################################################################

    st.subheader("🎲**Dataset**", divider='blue')
    with st.expander("🗓 **Visualizar Dados**"):
        st.dataframe(df, use_container_width=True)
        st.markdown("")    
        st.markdown("Fonte Dataset: https://kaggle.com")

    with st.expander(" 📚 **Visualizar dicionários dos dados:**"):
            st.table(dic)
            

############### Mostrar dados estatisticos ################################################
if st.sidebar.checkbox("📝**Dados Estatísticos**", False, key=1):
    st.subheader("🔎 Análise estatísticas dos pacientes:", divider='blue')
    #Contagem por pacientes com cancer próstata B ou M

    count_b = df[df.diagnosis_result == "B"].diagnosis_result.count()
    count_m = df[df.diagnosis_result == "M"].diagnosis_result.count()

    st.markdown("👫🩸**Total de pacientes com câncer de próstata:**")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Benigno:", value= count_b)
    with col2:
       st.metric(label="Maligno:", value= count_m)
    with col3:
        st.metric(label="Total de Pacientes:", value = count_b + count_m)    
    st.divider()
    
    style_metric_cards(background_color="#63ace5",border_left_color="#2a4d69",border_color="#FFC0CB",box_shadow="#F71938")



############ Mostrar Gráficos ########################################################

    st.subheader("📊 Gráficos de análise estatísticas dos pacientes:", divider='blue')
    if not st.checkbox('Ocultar gráfico 1', False, key=3):    
        
        #Estágio de tumor dos pacientes
        stage = df["diagnosis_result"].value_counts()
        transactions = stage.index
        quantity = stage.values
       
        fig = px.pie(df, 
             title="Estágio de tumor dos pacientes",
             values=quantity, 
             names=transactions,hole = 0.5,
             template = 'gridon'   
            )
        fig.update_traces(pull=[0.1, 0, 0, 0])    
        st.plotly_chart(fig)
        st.info("📌 Foram diagnosticados **62%** dos pacientes possuem Câncer de Próstata **Maligno**.")
        st.divider()


#################### Mostrar Previsões ###################################################################

if st.sidebar.checkbox("🎯**Previsões**", False, key=4):
    st.subheader("🎯 Previsões utilizando IA:", divider='rainbow')
    st.error("📌**Com base no Dataset iremos prever e demonstrar os resultados abaixo:**")

    count_b = df[df.diagnosis_result == "B"].diagnosis_result.count()
    count_m = df[df.diagnosis_result == "M"].diagnosis_result.count()

    st.markdown("👫🩸**Total de pacientes com câncer de próstata:**")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Benigno:", value= count_b)
    with col2:
       st.metric(label="Maligno:", value= count_m)
    with col3:
        st.metric(label="Total de Pacientes:", value = count_b + count_m)    
    st.divider()
    
    style_metric_cards(background_color="#63ace5",border_left_color="#2a4d69",border_color="#FFC0CB",box_shadow="#F71938")
    

    ####### Previsões utilizando machine learning #########################################################################################
    
    #PREPARAÇÃO DOS DADOS
    def get_clean_data():
        data = pd.read_csv("data/Prostate_Cancer.csv")
        
        data = data.drop(['id'], axis=1)
        
        data['diagnosis_result'] = data['diagnosis_result'].map({ 'M': 1, 'B': 0 })
  
        return data

    def add_sidebar():
        st.sidebar.subheader("Selecionar medidas da próstata:", divider='blue')
        
        data = get_clean_data()
        
        slider_labels = [
                ("Raio:", "radius"),
                ("Textura:", "texture"),
                ("Perímetro:", "perimeter"),
                ("Area:", "area"),
                ("Suavidade:", "smoothness"),
                ("Compacidade:", "compactness"),
                ("Simetria:", "symmetry"),
                ("Dimensão fractal:", "fractal_dimension"),
        ]

        input_dict = {}

        for label, key in slider_labels:
            input_dict[key] = st.sidebar.slider(
            label,
            min_value=float(0),
            max_value=float(data[key].max()),
            value=float(data[key].mean())
            )
            
        return input_dict

    def get_scaled_values(input_dict):
        data = get_clean_data()
        X = data.drop(['diagnosis_result'],axis = 1)
        scaled_dict = {}

        for key, value in input_dict.items():
            max_value = X[key].max()
            min_value = X[key].min()
            scaled_value = (value - min_value)/(max_value - min_value)
            scaled_dict[key] = scaled_value
        return scaled_dict


    ########## Criando modelo de machine learning SVC ###############################3
    def add_prediction(input_data):
        model = pickle.load(open("model/model.pkl","rb"))
        scaler = pickle.load(open("model/scaler.pkl","rb"))

        input_np = np.array(list(input_data.values())).reshape(1,-1)
        input_scaled = scaler.transform(input_np)

        prediction = model.predict(input_scaled)
        
        st.write("🔬 **Resultado Diagnóstico:**")

        if prediction[0] == 0:
            st.write("<span class='diagnosis benign'>Benigno</span>",unsafe_allow_html = True)
        else:
            st.write("<span class='diagnosis malicious'>Maligno</span>",unsafe_allow_html = True)
        
        prob_b = (round(model.predict_proba(input_scaled)[0][0],3))
        prob_m = (round(model.predict_proba(input_scaled)[0][1],3))

        st.info(f'✅ **Probabilidade Benigno: {round(prob_b*100,2)} %**')
        st.info(f'❌ **Probabilidade Maligno: {round(prob_m*100,2)}%**')
       
       
                
    input_data = add_sidebar()

    #### Realizando Novas Previsões com base nos índices médicos dos exames antes da cirurgia ######################
    st.info("🎯**Novas Previsões do status do paciente Maligno ou Benigno de acordo com os índices médicos dos exames:**")
    add_prediction(input_data)
    
    with st.expander("🔬 **Visualizar dados dos resultados clínicos**"):
        st.dataframe(input_data, use_container_width=True)
  

    st.error("📌**Conclusão: Com base nos resultados apresentados nos índices dos exames antes de um procedimento cirúrgico, o médico pode tomar a decisão sobre realizar ou não o procedimento cirúrgico. Com base nos dados analisados e obtidos no [Kaggle.com], a inteligência Artificial contribui de forma a prever os riscos na saúde dos pacientes. A análise visa apenas aumentar a qualidade do diagnóstico e não pretende substituir o diagnóstico profissional.**")

 

#Mensagem de atualização da página web    
st.toast("Página atualizada!", icon='✅')