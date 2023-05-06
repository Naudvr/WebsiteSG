import streamlit as st
from PIL import Image
from google.cloud import firestore

db_Website = firestore.Client.from_service_account_json("Firestore_key.json")


img_logo = Image.open("SG_logo.png")
img_us_theme = Image.open("SG_Iedereen.jpg")
img_bar_sep = Image.open("SG_bar.png")



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
    with st.expander("Inschrijven"):
        doc_ref = db_Website.collection("Activiteiten").document("Pannenkoeken")
        doc = doc_ref.get()
        if not doc.exists:
            doc_ref.set({"Inschrijvingen":"Inschrijvingen"})
        doc = doc_ref.get()
        if doc.exists:
            Name_Dict = doc.to_dict()
            Name_list = list(Name_Dict.values())
            Name_length = len(Name_list)
            for i in range(Name_length):
                if Name_list[i] != " ":
                    st.write(Name_list[i])
        Name = st.text_input("Typ hier alsjeblieft je naam :)")
        Submit = st.button("Schrijf me in!")
        if Submit and Name != "":
            doc_ref.update({Name:Name})
            st.write("Je bent ingeschreven!")
        elif Submit and Name == "":
            st.error("Vul alstublieft eerst een naam in")
    st.write("      ")
    st.write("      ")
    st.write("      ")
    st.write("      ")
    st.write("      ")
    st.write("      ")
    st.write("      ")
    st.write("### Graswandeling Picnic Editie")
    #st.image(Image.open(r"C:\Users\jeroe\OneDrive - TU Eindhoven\Website_SG.()\SG_pannenkoek.jpg"), width=200)
    st.write("""
                 **Datum is 17-05-2023**\n
                 **Locatie: Naast de Dommel op campus**\n
                 Tijd om lekker in de natuur te genieten van een stukje puur natuur, een dikke jonko!\n
                 Een heerlijk middagje muziek, munchies en lachkickjes. Het is weer ultiem chillen geblazen!
                 """)
    with st.expander("Inschrijven"):
        doc_ref1 = db_Website.collection("Activiteiten").document("GraswandelingPicnicEditie")
        doc1 = doc_ref1.get()
        if not doc1.exists:
            doc_ref1.set({"Inschrijvingen": " "})
        doc1 = doc_ref1.get()
        if doc1.exists:
            Name_Dict = doc1.to_dict()
            Name_list = list(Name_Dict.values())
            Name_length = len(Name_list)
            for i in range(Name_length):
                if Name_list[i] != " ":
                    st.write(Name_list[i])
        Name1 = st.text_input("Typ hier alsjeblieft je naam :) ")
        Submit1 = st.button("Schrijf me in! ")
        if Submit1 and Name1 != "":
            doc_ref1.update({Name1: Name1})
            st.write("Je bent ingeschreven!")
        elif Submit1 and Name1 == "":
            st.error("Vul alstublieft eerst een naam in")
    st.write("      ")
    st.write("      ")
    st.write("      ")
    st.write("      ")
    st.write("      ")
    st.write("      ")
    st.write("      ")
    st.write("### Vrienden Weekend")
    # st.image(Image.open(r"C:\Users\jeroe\OneDrive - TU Eindhoven\Website_SG.()\SG_pannenkoek.jpg"), width=200)
    st.write("""
                     **Datum is 27-05-2023 tot 29-05-2023**\n
                     **Locatie: Door heel Eindhoven**\n
                     -\n
                     """)
    with st.expander("Inschrijven"):
        doc_ref2 = db_Website.collection("Activiteiten").document("VriendenWeekend")
        doc2 = doc_ref2.get()
        if not doc2.exists:
            doc_ref2.set({"Inschrijvingen": " "})
        doc2 = doc_ref2.get()
        if doc2.exists:
            Name_Dict = doc2.to_dict()
            Name_list = list(Name_Dict.values())
            Name_length = len(Name_list)
            for i in range(Name_length):
                if Name_list[i] != " ":
                    st.write(Name_list[i])
        Name2 = st.text_input("Typ hier alsjeblieft je naam :)  ")
        Submit2 = st.button("Schrijf me in!  ")
        if Submit2 and Name2 != "":
            doc_ref1.update({Name2: Name2})
            st.write("Je bent ingeschreven!")
        elif Submit2 and Name2 == "":
            st.error("Vul alstublieft eerst een naam in")
    st.write("      ")
    st.write("      ")
    st.write("      ")
    st.write("      ")
    st.write("      ")
    st.write("      ")
    st.write("      ")
    st.write("### Graswandeling")
    # st.image(Image.open(r"C:\Users\jeroe\OneDrive - TU Eindhoven\Website_SG.()\SG_pannenkoek.jpg"), width=200)
    st.write("""
                                     **Datum is 11-06-2023**\n
                                     **Locatie: TBA**\n
                                     -\n
                                     """)
    with st.expander("Inschrijven"):
        doc_ref3 = db_Website.collection("Activiteiten").document("Graswandeling")
        doc3 = doc_ref3.get()
        if not doc3.exists:
            doc_ref3.set({"Inschrijvingen": " "})
        doc3 = doc_ref3.get()
        if doc3.exists:
            Name_Dict = doc3.to_dict()
            Name_list = list(Name_Dict.values())
            Name_length = len(Name_list)
            for i in range(Name_length):
                if Name_list[i] != " ":
                    st.write(Name_list[i])
        Name3 = st.text_input("Typ hier alsjeblieft je naam :)   ")
        Submit3 = st.button("Schrijf me in!   ")
        if Submit3 and Name3 != "":
            doc_ref1.update({Name3: Name3})
            st.write("Je bent ingeschreven!")
        elif Submit3 and Name3 == "":
            st.error("Vul alstublieft eerst een naam in")
