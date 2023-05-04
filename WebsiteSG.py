import streamlit as st
from PIL import Image

img_logo = Image.open(r"C:\Users\jeroe\OneDrive - TU Eindhoven\Website_SG.()\SG_logo.png")
img_us_theme = Image.open(r"C:\Users\jeroe\OneDrive - TU Eindhoven\Website_SG.()\SG_Iedereen.jpg")
img_bar_sep = Image.open(r"C:\Users\jeroe\OneDrive - TU Eindhoven\Website_SG.()\SG_bar.png")


st.set_page_config(page_title='Studie.Gezelligheid()', page_icon=img_logo, layout="wide")
col1b, col2b, col3b, col4b, col5b = st.columns(5, gap="large")
with(col1b):
    st.title("Studie.Gezelligheid()")
with(col5b):
    st.image(img_logo, width=80)

bio = st.radio('Choose an option:',['Home','Activiteiten','Afgehuurde Lokalen','Fotos'],horizontal=True)
st.image(img_bar_sep, use_column_width="always")

if bio == 'Home':
    col1, col2, col3 = st.columns(3,gap="small")
    with col2:
        st.markdown("""
                 ## Welkom gezellige studiemensen!
                 """)
    col1l, col2l, col3l, col4l, col5l = st.columns(5, gap="large")
    with col2l:
        st.image(img_us_theme, width=1000)
    with st.container():
        st.image(img_bar_sep, use_column_width="always")
    st.markdown("""
             ### Hallo Studie.Gezelligheid() mensen op onze volledige eigen website!!\n
             Op deze website kunnen we al onze activiteiten zien zodat iedereen precies weet waar en wanneer we wat kunnen doen!\n 
             Want heel eerlijk, ik houd al die shit niet meer bij.\n
             Ook zijn op deze website al onze mooie kiekjes te vinden zodat we altijd kunnen genieten van onze prachtige snoetjes :)
             """)
elif bio == 'Activiteiten':
    ol1, col2, col3, col4, col5 = st.columns(5, gap="small")
    with col3:
        st.markdown("""
                     ## Activiteiten
                     """)
    st.write("### Pannenkoeken avond")
    st.image(Image.open(r"C:\Users\jeroe\OneDrive - TU Eindhoven\Website_SG.()\SG_pannenkoek.jpg"),width=200)
    st.write("""
             **Datum is 11-05-2023**\n
             **Locatie: Joep thuis**\n
             De grote Studiegezelligheid pannenkoeken avond!\n
             Vol met pannenkoeken en gezelligheid!!
             """)
