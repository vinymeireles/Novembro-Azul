import streamlit as st

#Apps
st.set_page_config(page_title="App Previsão de Câncer de Próstata", page_icon= ":bar_chart:")
#st.header("🎗Analytics Câncer de Próstata📊", divider='blue')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

st.markdown("<h1 style='text-align: center; color: red;'>📨Contatos</h1>", unsafe_allow_html=True)
st.subheader("", divider='blue')
st.markdown("")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image("icons/whatsapp.png", caption="28 99918-3961", width=90)

with col2:
    st.image("icons/gmail.png", caption="viniciusmeireles@gmail.com", width=100)

with col3:
    st.image("icons/location.png", caption="Ibatiba/ES", width=90)    

with col4:
    st.image("icons/linkedin.png",caption= "/pviniciusmeireles", width=90)

st.markdown("")
st.subheader("", divider='blue')
st.markdown("**Para desenvolvimento de novos projetos - Dashboard utilizando Inteligência Articial: Machine Learning**")

st.markdown("")

col1, col2, col3 = st.columns(3)
with col1:
    pass
with col2:
    st.image("img/logo.png", width=310)
with col3:
    pass    

st.toast("Página atualizada!", icon='✅')

