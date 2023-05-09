import streamlit as st
from PIL import Image
from google.cloud import firestore
import time

db_Website = firestore.Client.from_service_account_json("Firestore_key.json")


img_logo = Image.open("SG_logo.png")
img_us_theme = Image.open("SG_Iedereen.jpg")
img_bar_sep = Image.open("SG_bar.png")

Doc_Pass_ref = db_Website.collection("Activiteiten").document("Key")
Doc_Pass = Doc_Pass_ref.get()
Pass_Dict = Doc_Pass.to_dict()
Pass_list = list(Pass_Dict.values())

st.set_page_config(page_title='Studie.Gezelligheid()', page_icon=img_logo, layout="wide")

if "load_state" not in st.session_state:
    st.session_state.load_state = False

st.sidebar.title("Studie.Gezelligheid()")
Password = st.sidebar.text_input("Typ hier het wachtwoord", type="password")
Login = st.sidebar.checkbox("Vink aan om in te loggen")
if Password == Pass_list[0] and Login:
    st.session_state.load_state = True
    col1b, col2b, col3b, col4b, col5b = st.columns(5, gap="large")
    with(col1b):
        st.title("Studie.Gezelligheid()")
    with(col5b):
        st.image(img_logo, width=80)
    
    bio = st.radio('Choose an option:', ['Home', 'Activiteiten', 'Gereserveerde Lokalen', 'Quotes', 'Vriendenweekend Planning'], horizontal=True)
    st.image(img_bar_sep, use_column_width="always")
    
    if bio == 'Home':
        Doc_af_ref = db_Website.collection("Lokalen").document("Afgehuurd")
        doc_af = Doc_af_ref.get()
        if not doc_af.exists:
            Doc_af_ref.set({" ": " "})
        doc_af = Doc_af_ref.get()
        if doc_af.exists:
            Tijd_Locatie_Dict = doc_af.to_dict()
            Tijd_list = list(Tijd_Locatie_Dict.keys())
            Locatie_list = list(Tijd_Locatie_Dict.values())
            List_length = len(Tijd_list)
            time_list = time.localtime()
            Today_mon = time_list[1]
            Today_day = time_list[2]
            Today_year = int(str(time_list[0])[3])
            for i in range(List_length):
                if Tijd_list[i][0] == "0":
                    day = int(Tijd_list[i][1])
                elif Tijd_list[i][0] != "0":
                    day = int(Tijd_list[i][0] + Tijd_list[i][1])
                if Tijd_list[i][3] == "0":
                    month = int(Tijd_list[i][4])
                elif Tijd_list[i][3] != "0":
                    month = int(Tijd_list[i][3] + Tijd_list[i][4])
                year = int(Tijd_list[i][7])
                if day < Today_day:
                    Doc_af_ref.update({Tijd_list[i]: firestore.DELETE_FIELD})
                if day > Today_day and month < Today_mon:
                    Doc_af_ref.update({Tijd_list[i]: firestore.DELETE_FIELD})
                if day > Today_day and month > Today_mon and year < Today_year:
                    Doc_af_ref.update({Tijd_list[i]: firestore.DELETE_FIELD})
        col1, col2, col3 = st.columns([1.7, 3, 1])
        col2.write("""
                     ## Welkom gezellige studiemensen!
                     """)
        col1l, col2l, col3l, col4l, col5l, col6l, col7l = st.columns(7, gap="large")
        with col2l:
            st.image(img_us_theme, width=1000)
        with st.container():
            st.image(img_bar_sep, use_column_width="always")
        st.markdown("""
                 ### Hallo Studie.Gezelligheid() mensen op onze volledig eigen website!!\n
                 Op deze website kunnen we al onze activiteiten zien zodat iedereen precies weet waar en wanneer we wat kunnen doen!\n 
                 Want heel eerlijk, ik houd al die shit niet meer bij.\n
                 Ook zijn op deze website al onze mooie kiekjes te vinden zodat we altijd kunnen genieten van onze prachtige snoetjes :)
                 """)
    elif bio == 'Gereserveerde Lokalen':
        col1, col2, col3 = st.columns(3, gap="small")
        with col2:
            st.markdown("""
                             ## Gereserveerde Lokalen
                             """)
        Doc_af_ref = db_Website.collection("Lokalen").document("Afgehuurd")
        doc_af = Doc_af_ref.get()
        if not doc_af.exists:
            Doc_af_ref.set({" ": " "})
        doc_af = Doc_af_ref.get()
        if doc_af.exists:
            Tijd_Locatie_Dict = doc_af.to_dict()
            Tijd_list = list(Tijd_Locatie_Dict.keys())
            Locatie_list = list(Tijd_Locatie_Dict.values())
            List_length = len(Tijd_list)
            col1p, col2p, col3p, col4p, col5p = st.columns(5, gap="small")
            with col1p:
                st.write("""### Tijden""")
                for i in range(List_length):
                    if Tijd_list[i] != " ":
                        st.write(Tijd_list[i])
            with col2p:
                st.write("""### Locatie""")
                for i in range(List_length):
                    if Locatie_list[i] != " ":
                        st.write(Locatie_list[i])
        Locatie = st.text_input("Typ hier alsjeblieft de locatie van het lokaal")
        Tijd = st.text_input("Typ hier alsjeblieft de datum en tijd wanneer je het lokaal hebt afgehuurd",
                             placeholder="DD/MM/YYYY HH:MM-HH:MM")
        Toevoegen = st.button("Voeg mijn lokaal toe")
        if Toevoegen and Locatie != "" and Tijd != "" and Tijd[1] == "/" and Tijd[3] == "/":
            st.error("Gebruik alsjeblieft de juiste notatie voor de datum")
        elif Toevoegen and Locatie != "" and Tijd != "" and Tijd[1] == "/":
            st.error("Gebruik alsjeblieft de juiste notatie voor de datum")
        elif Toevoegen and Locatie != "" and Tijd != "" and Tijd[4] == "/":
            st.error("Gebruik alsjeblieft de juiste notatie voor de datum")
        elif Toevoegen and Locatie != "" and Tijd != "":
            Doc_af_ref.update({Tijd: Locatie})
            st.success("Lokaal is toegevoegd!")
        elif Toevoegen and Locatie == "" and Tijd != "":
            st.error("Vul alsjeblieft een locatie in")
        elif Toevoegen and Locatie != "" and Tijd == "":
            st.error("Vul alsjeblieft een tijd in")
        elif Toevoegen and Locatie == "" and Tijd == "":
            st.error("Vul alsjeblieft een locatie en tijd in")
    
    elif bio == 'Quotes':
        ol1, col2, col3, col4, col5 = st.columns(5, gap="small")
        with col3:
            st.markdown("""
                         ## Quotes
                         """)
        doc_ref_q = db_Website.collection("Quotes").document("Ingevulde quotes")
        doc_q = doc_ref_q.get()
        if doc_q.exists:
            Quote_Dict = doc_q.to_dict()
            Quote_list = list(Quote_Dict.values())
            Quote_length = len(Quote_list)
            for i in range(Quote_length):
                if Quote_list[i] != " ":
                    st.write(str(Quote_list[i]))
        Quote = st.text_input("Typ hier alsjeblieft je geweldige quote", placeholder="Naam: Quote")
        Toevoegen = st.button("Voeg de quote toe!")
        if Toevoegen and Quote != "":
            Quote_Dict = doc_q.to_dict()
            Quote_list = list(Quote_Dict.values())
            Quote_length = len(Quote_list)
            doc_ref_q.update({str(Quote_length): Quote})
            st.success("Je hebt je quote geplaatst!")
        elif Toevoegen and Quote == "":
            st.error("Vul alsjeblieft een quote in")
    
    elif bio == 'Vriendenweekend Planning':
        st.markdown("""
                  # Planning Vriendenweekend:\n
                  \n
                  \n
                  ## Vrijdag:\n
                  \n
                  \n
                  ### Vrijdag avond:\n
                  **Avond eten**\n
                  **Quiz night** \n
                  **Spelletjes avond**\n
                  **Film Kijken**\n
                  \n
                  \n
                  ## Zaterdag:
        
        """)
    
    elif bio == 'Activiteiten':
        ol1, col2, col3, col4, col5 = st.columns(5, gap="small")
        with col3:
            st.markdown("""
                         ## Activiteiten
                         """)
        st.write("### Pannenkoeken avond")
        # st.image(Image.open("SG_pannenkoek.jpg"),width=200)
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
                doc_ref.set({"Inschrijvingen": " "})
            doc = doc_ref.get()
            if doc.exists:
                Name_Dict = doc.to_dict()
                Name_list = list(Name_Dict.values())
                Name_length = len(Name_list)
                for i in range(Name_length):
                    if Name_list[i] != " ":
                        st.write(str(Name_list[i]))
            Name = st.text_input("Typ hier alsjeblieft je naam :)")
            Submit = st.button("Schrijf me in!")
            if Submit and Name != "":
                Name_Dict = doc.to_dict()
                Name_list = list(Name_Dict.values())
                Name_length = len(Name_list)
                doc_ref.update({str(Name_length): Name})
                st.success("Je bent ingeschreven!")
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
        # st.image(Image.open(r"C:\Users\jeroe\OneDrive - TU Eindhoven\Website_SG.()\SG_pannenkoek.jpg"), width=200)
        st.write("""
                     **Datum is 21-05-2023, Tijd: 13:00**\n
                     **Locatie: Naast de Dommel op campus, meeten appie station**\n
                     Tijd om in de natuur lekker te genieten van een stukje púúr natuur, moeder aarde der ultieme gift, zaza!\n
                     Een heerlijk middagje muziek, munchies en lachkickjes. Zoals Snoop Dogg zei: 'Smoke weed every day!'\n
                     Neem ook een picnic kleed of een lekkere camping stoel mee!
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
                        st.write(str(Name_list[i]))
            Name1 = st.text_input("Typ hier alsjeblieft je naam :) ")
            Submit1 = st.button("Schrijf me in! ")
            if Submit1 and Name1 != "":
                Name_Dict = doc1.to_dict()
                Name_list = list(Name_Dict.values())
                Name_length = len(Name_list)
                doc_ref1.update({str(Name_length): Name1})
                st.success("Je bent ingeschreven!")
            elif Submit1 and Name1 == "":
                st.error("Vul alstublieft eerst een naam in")
        st.write("      ")
        st.write("      ")
        st.write("      ")
        st.write("      ")
        st.write("      ")
        st.write("      ")
        st.write("      ")
        st.write("### Borrel Protagoras")
        # st.image(Image.open(r"C:\Users\jeroe\OneDrive - TU Eindhoven\Website_SG.()\SG_pannenkoek.jpg"), width=200)
        st.write("""
                         **Datum is 25-05-2023 Tijd: 16:00**\n
                         **Locatie: In Vivo**\n
                         Weer donderdag, dus tijd om te borrelen!\n
                         """)
        with st.expander("Inschrijven"):
            doc_ref4 = db_Website.collection("Activiteiten").document("Borrel_25")
            doc4 = doc_ref4.get()
            if not doc4.exists:
                doc_ref4.set({"Inschrijvingen": " "})
            doc4 = doc_ref4.get()
            if doc4.exists:
                Name_Dict = doc4.to_dict()
                Name_list = list(Name_Dict.values())
                Name_length = len(Name_list)
                for i in range(Name_length):
                    if Name_list[i] != " ":
                        st.write(str(Name_list[i]))
            Name4 = st.text_input("Typ hier alsjeblieft je naam :)    ")
            Submit4 = st.button("Schrijf me in!    ")
            if Submit4 and Name4 != "":
                Name_Dict = doc4.to_dict()
                Name_list = list(Name_Dict.values())
                Name_length = len(Name_list)
                doc_ref4.update({str(Name_length): Name4})
                st.success("Je bent ingeschreven!")
            elif Submit4 and Name4 == "":
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
                         Weekendje Eindhoven en omgeving onveilig te maken ft. deze stichting van hele gezellige idioten ;).\n
                         08/05 12:45 MEETING OM PROGRAMMA TE BEDENKEN.
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
                        st.write(str(Name_list[i]))
            Name2 = st.text_input("Typ hier alsjeblieft je naam :)  ")
            Submit2 = st.button("Schrijf me in!  ")
            if Submit2 and Name2 != "":
                Name_Dict = doc2.to_dict()
                Name_list = list(Name_Dict.values())
                Name_length = len(Name_list)
                doc_ref2.update({str(Name_length): Name2})
                st.success("Je bent ingeschreven!")
            elif Submit2 and Name2 == "":
                st.error("Vul alstublieft eerst een naam in")
        st.write("      ")
        st.write("      ")
        st.write("      ")
        st.write("      ")
        st.write("      ")
        st.write("      ")
        st.write("      ")
        st.write("### Borrel Protagoras")
        # st.image(Image.open(r"C:\Users\jeroe\OneDrive - TU Eindhoven\Website_SG.()\SG_pannenkoek.jpg"), width=200)
        st.write("""
                         **Datum is 01-06-2023 Tijd: 16:00**\n
                         **Locatie: In Vivo**\n
                         Weer donderdag, dus tijd om te borrelen!\n
                         """)
        with st.expander("Inschrijven"):
            doc_ref5 = db_Website.collection("Activiteiten").document("Borrel_01")
            doc5 = doc_ref5.get()
            if not doc5.exists:
                doc_ref5.set({"Inschrijvingen": " "})
            doc5 = doc_ref5.get()
            if doc5.exists:
                Name_Dict = doc5.to_dict()
                Name_list = list(Name_Dict.values())
                Name_length = len(Name_list)
                for i in range(Name_length):
                    if Name_list[i] != " ":
                        st.write(str(Name_list[i]))
            Name5 = st.text_input("Typ hier alsjeblieft je naam :)     ")
            Submit5 = st.button("Schrijf me in!     ")
            if Submit5 and Name5 != "":
                Name_Dict = doc5.to_dict()
                Name_list = list(Name_Dict.values())
                Name_length = len(Name_list)
                doc_ref5.update({str(Name_length): Name5})
                st.success("Je bent ingeschreven!")
            elif Submit5 and Name5 == "":
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
                                         Zoals Snoop Dogg zei 'Smoke weed every day'. Nog meer munchies en nog meer lachkikjes.\n
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
                        st.write(str(Name_list[i]))
            Name3 = st.text_input("Typ hier alsjeblieft je naam :)   ")
            Submit3 = st.button("Schrijf me in!   ")
            if Submit3 and Name3 != "":
                Name_Dict = doc3.to_dict()
                Name_list = list(Name_Dict.values())
                Name_length = len(Name_list)
                doc_ref3.update({str(Name_length): Name3})
                st.success("Je bent ingeschreven!")
            elif Submit3 and Name3 == "":
                st.error("Vul alstublieft eerst een naam in")
