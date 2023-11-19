import streamlit as st


#Apps
st.set_page_config(page_title="App Previsão de Câncer de Próstata", page_icon= ":bar_chart:") 
st.header("🎗Analytics Câncer de Próstata🩺", divider='blue')

st.sidebar.image("img/01.jpg", width=300)

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

#Texto na página
st.markdown("""<h6 style='text-align: justify;'> Contribuindo com a campanha de concientização do Novembro Azul, essa aplicação demonstra uma análise exploratória dos dados de previsão de pacientes com câncer de próstata num conjunto de dados disponível no [www.kaggle.com], utilizando Machine Learning (IA) tem o intuito de demonstrar graficamente as correlações e previsões de pacientes que possam a sobreviver ao tratamento da doença, de acordo com exames clínicos do paciente se o câncer de próstata é Benigno ou Maligno. </h6""", unsafe_allow_html=True) 

st.markdown("""<h6 style='text-align: justify;'> A utilização de Machine Learning para a detecção do câncer de próstata vem crescendo cada vez mais e contribuindo para diagnósticos mais rápidos e precisos. Muitos centros de pesquisas têm utilizado a técnica de machine learning para treinar inteligência artificial na detecção de lesões suspeitas de câncer de próstata e os dados são promissores.
Um estudo publicado em novembro de 2020 comparou inteligência artificial e um radiologista experiente na avaliação de 1034 lesões suspeitas de câncer de próstata identificadas em exames de ressonância, com resultados bastante semelhantes, sobretudo em pacientes submetidos a biópsia de próstata guiada por ressonância . </h6""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🌍Fonte: [https://www.takanourologia.com.br/blog/inteligencia-artificial-melhora-a-precisao-da-de-ressonancia-magnetica-da-prostata]. </h6""", unsafe_allow_html=True) 
    

st.subheader("📋 Informações sobre o Câncer de Próstata:", divider='blue')
st.image("img/04.png", width= 400, use_column_width=True)
st.markdown("""<h6 style='text-align: justify;'> O câncer de próstata é o segundo tipo de câncer mais incidente na população masculina em todas as regiões do país, atrás apenas dos tumores de pele não melanoma. No Brasil, estimam-se 71.730 novos casos de câncer de próstata por ano para o triênio 2023-2025. Atualmente, é a segunda causa de óbito por câncer na população masculina, reafirmando sua importância epidemiológica no país.</h6""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> A idade é o principal fator de risco para o câncer de próstata, sendo mais incidente em homens a partir da sexta década de vida, bem como, histórico familiar de câncer de próstata antes dos 60 anos e obesidade para tipos histológicos avançados. Destaca-se também a exposição a agentes químicos relacionados ao trabalho, sendo responsável por 1% dos casos de câncer de próstata. </h6""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> O INCA recomenda que os homens estejam alertas a qualquer anormalidade no corpo e procurem o serviço de saúde o mais breve possível para realizar o diagnóstico precoce do câncer de próstata. Não há recomendação para rastreamento (exames de rotina) do câncer de próstata, uma vez que as evidências atualmente disponíveis apontam para balanço desfavorável entre os riscos e benefícios para a saúde dos homens. Caso o homem deseje realizar esses exames, deve-se realizar a decisão compartilhada, após o profissional de saúde conversar sobre todos os possíveis riscos do rastreamento.</h6""", unsafe_allow_html=True)

st.markdown("""<h4 style='text-align: justify;'> Diagnóstico do câncer de próstata: </h4""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> Os exames utilizados para a investigação diagnóstica do câncer de próstata são o PSA e o toque retal. O exame de PSA tem a finalidade de medir no sangue o antígeno prostático específico, que é uma proteína produzida pela próstata e está disponível na corrente sanguínea e no sêmen. Níveis alterados dessa proteína podem indicar alterações na próstata. O toque retal possui a finalidade de avaliar o tamanho, o volume, a textura e a forma da próstata. Destaca-se que esses exames são recomendados para a investigação, mediante suspeita de câncer de próstata.</h6""", unsafe_allow_html=True)

st.markdown("""<h5 style='text-align: justify;'> 1️⃣ Fatores de risco: </h5""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔵 Idade: o risco aumenta com o avançar da idade. No Brasil, a cada dez homens diagnosticados com câncer de próstata, nove têm mais de 55 anos. </h6""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔵 Histórico de câncer na família: homens cujo o pai, avô ou irmão tiveram câncer de próstata antes dos 60 anos, fazem parte do grupo de risco. </h6""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔵 Sobrepeso e obesidade: estudos recentes mostram maior risco de câncer de próstata em homens com peso corporal mais elevado. </h6""", unsafe_allow_html=True)
st.markdown("")

st.markdown("""<h5 style='text-align: justify;'> 2️⃣ Sinais e sintomas: </h5""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔵 Dificuldade de urinar; </h6""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔵 Demora em começar e terminar de urinar; </h6""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔵 Sangue na urina; </h6""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔵 Diminuição do jato de urina; </h6""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔵 Necessidade de urinar mais vezes durante o dia ou à noite. </h6""", unsafe_allow_html=True)
st.markdown("")

st.markdown("""<h5 style='text-align: justify;'> 3️⃣ Estratégias para investigar o câncer de próstata: </h5""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔵 Exame de toque retal: o médico avalia tamanho, forma e textura da próstata, introduzindo o dedo protegido por uma luva lubrificada no reto. Este exame permite palpar as partes posterior e lateral da próstata; </h6""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔵 Exame de PSA: é um exame de sangue que mede a quantidade de uma proteína produzida pela próstata – Antígeno Prostático Específico (PSA). Níveis altos dessa proteína podem significar câncer, mas também doenças benignas da próstata. </h6""", unsafe_allow_html=True)
st.markdown("")
st.markdown("""<h5 style='text-align: justify;'> 4️⃣ Confirmação do diagnóstico: </h5""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔵 Para confirmar o câncer de próstata é preciso fazer uma biópsia. Nesse exame são retirados pedaços muito pequenos da próstata para serem analisados no laboratório. A biópsia é indicada caso seja encontrada alguma alteração no exame de PSA ou no toque retal. </h6""", unsafe_allow_html=True)
st.markdown("")
st.markdown("""<h5 style='text-align: justify;'> 5️⃣ Tratamento do câncer de próstata: </h5""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔵 O tratamento do câncer de próstata é feito por meio de uma ou de várias modalidades/técnicas de tratamento, que podem ser combinadas ou não. A principal delas é a cirurgia, que pode ser aplicada junto com radioterapia e tratamento hormonal, conforme cada caso. </h6""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔵 Quando localizado apenas na próstata, o câncer de próstata pode ser tratado com cirurgia oncológica, radioterapia e até mesmo observação vigilante, em alguns casos especiais. No caso de metástase, ou seja, se o câncer da próstata tiver se espalhado para outros órgãos, a radioterapia é utilizada junto com tratamento hormonal, além de tratamentos paliativos.</h6""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🔵 A escolha do melhor tratamento é feita individualmente, por médico especializado, caso a caso, após definir quais os riscos, benefícios e melhores resultados para cada paciente, conforme estágio da doença e condições clínicas do paciente. Todas as modalidades de tratamento são oferecidas, de forma integral e gratuita, por meio do Sistema Único de Saúde (SUS).</h6""", unsafe_allow_html=True)

st.markdown("")
st.markdown("""<h6 style='text-align: justify;'> 🌍 Fonte: [https://www.saude.ba.gov.br/novembroazul/]</h6""", unsafe_allow_html=True)
st.markdown("""<h6 style='text-align: justify;'> 🌍 Fonte: [https://www.gov.br/inca/pt-br/assuntos/campanhas/2023/novembro-azul]</h6""", unsafe_allow_html=True)

st.toast("Página atualizada!", icon='✅')



