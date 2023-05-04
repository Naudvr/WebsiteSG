# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 10:28:53 2021

@author: jeroe
"""


import streamlit as st
from PIL import Image
import base64


img = Image.open(r"C:\Users\jeroe\OneDrive - TU Eindhoven\Vakken\Digital Twin 2\Matlab EDES python\Final version logo.png")
img_us = Image.open(r"C:\Users\jeroe\OneDrive - TU Eindhoven\Vakken\Digital Twin 2\Matlab EDES python\us.jpg")
img_cyc = Image.open(r"C:\Users\jeroe\OneDrive - TU Eindhoven\Vakken\Digital Twin 2\Matlab EDES python\Cycling.jpg")
img_sugar = Image.open(r"C:\Users\jeroe\OneDrive - TU Eindhoven\Vakken\Digital Twin 2\Matlab EDES python\Sugar_1.png")
img_dia = Image.open(r"C:\Users\jeroe\OneDrive - TU Eindhoven\Vakken\Digital Twin 2\Matlab EDES python\diabetes.jpg")
st.set_page_config(page_title='MySugarFlow', page_icon=img, layout="wide")
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

file_ = open("C:/Users/jeroe/OneDrive - TU Eindhoven/Vakken/Digital Twin 2/Matlab EDES python/04de2e31234507.564a1d23645bf.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

amount_of_peoples = 1

st.sidebar.image(img)

st.sidebar.title("MySugarFlow")

choice = st.sidebar.selectbox('login/signup',['Login','Sign up'])

email = st.sidebar.text_input('Please enter your email address')
handle = st.sidebar.text_input('Please input your app username')
password = st.sidebar.text_input('Please enter your password (at least 6 characters)', type = 'password')


email_dict = {}
email_dict["exists"] = email

password_dict = {}
password_dict["exists"] = password

email_list = []
handle_list = []


dict_boi_1 = db.child('Password_List').get().val()
dict_boi = db.child('Email_List').get().val()
handle_list = dict_boi.keys()

st.markdown("""
             <style>
             .big-font {
                 font-size:40px !important;
                 }
             </style>
             """, unsafe_allow_html=True)

for i in handle_list:
    email_list.append(dict_boi[i]["exists"])
    
if choice == 'Sign up':
    st.header("Welcome to MySugarFlow")
    st.write(""" This dashboard is designed for people with Prediabetes, people with Diabetes Type 1 and 2, or for people who want to keep their blood sugar concentration within a healthy range. Regular blood sugar concentrations are extremely important for people with type 1 or type 2-diabetes, or people with prediabetes who want to stop the further development of this disease.  
With this dashboard, you can keep track of your current blood sugar concentrations, and your blood sugar concentrations. The main purpose of this dashboard is to check whether it is advisable to eat a certain food item, taking into account the blood glucose levels of the user. """)
    st.image(img, width = 500)
    st.write("""© 2022 Pentabetes""")
    password_verify = st.sidebar.text_input('Please verify your password (at least 6 characters)', type = 'password')
    submit = st.sidebar.button('Create my account')
    if submit and email != "" and email not in email_list and password != "" and password == password_verify and handle != "" and handle not in handle_list and len(password) >= 6:
        db.child('Email_List').child(handle).set(email_dict)
        db.child('Password_List').child(handle).set(password_dict)
        user = auth.create_user_with_email_and_password(email,password)
        st.success('Your account has been created successfully')
        st.balloons()
        user = auth.sign_in_with_email_and_password(email,password)
        db.child(user['localId']).child("Handle").set(handle)
        db.child(user['localId']).child("ID").set(user['localId'])
        db.child(user['localId']).child("Food").child("Banana").set(food_1)
        db.child(user['localId']).child("Food").child("Apple").set(food_2)
        db.child(user['localId']).child("Food").child("Tagliatelle").set(food_3)
        db.child(user['localId']).child("Food").child("Cucumber").set(food_4)
        db.child(user['localId']).child("Food").child("White bread").set(food_5)
        db.child(user['localId']).child("Food").child("Milk chocolate").set(food_6)
        db.child(user['localId']).child("Food").child("Egg").set(food_7)
        db.child(user['localId']).child("Food").child("Cheese").set(food_8)
        st.title('Welcome '+handle)
        st.info('Login via the login option')
    elif submit and email in email_list:
        st.error("Email already exits, please enter a different email or log in with your existing account")
    elif submit and email == "":
        st.error("Please enter an email adress")
    elif submit and password == "":
        st.error("Please enter a password")
    elif submit and password != password_verify:
        st.error("Your password and password verification don't match")
    elif submit and len(password) < 6:
        st.error("Password needs to be longer than 6 characters")
    elif submit and handle == "":
        st.error("Please enter a username")
    elif submit and handle in handle_list:
        st.error("Username already exists")           


data_pd = {}
weight_var = 0
logout_1 = 0
variable_log_1 = st.empty()
variable_log_2 = st.empty()
variable_log_3 = st.empty()
variable_log_4 = st.empty()





if choice == 'Login':
    variable_log_1.header("Welcome to MySugarFlow")
    variable_log_2.write(""" This dashboard is designed for people with Prediabetes, people with Diabetes Type 1 and 2, or for people who want to keep their blood sugar concentration within a healthy range. Regular blood sugar concentrations are extremely important for people with type 1 or type 2-diabetes, or people with prediabetes who want to stop the further development of this disease.  
With this dashboard, you can keep track of your current blood sugar concentrations, and your blood sugar concentrations. The main purpose of this dashboard is to check whether it is advisable to eat a certain food item, taking into account the blood glucose levels of the user. """)
    variable_log_3.image(img, width = 500)
    variable_log_4.write("""© 2022 Pentabetes""")
    login = st.sidebar.checkbox('Login')
    if login and email != '' and password !='' and email in email_list  and handle in handle_list and str(password) == str(dict_boi_1[handle]["exists"]) and dict_boi[handle]["exists"] == email:
        variable_log_1.empty()
        variable_log_2.empty()
        variable_log_3.empty()
        variable_log_4.empty()
        user = auth.sign_in_with_email_and_password(email,password)
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    
        bio = st.radio('Choose an option:',['Home','Add food','Pick food','Base settings', 'Help', 'Info about diabetes','About us'])
        
        if bio == 'Base settings':
            if db.child(user['localId']).child("Weight").get().val() is not None:
                st.write("Your last weight input was "+str(db.child(user['localId']).child("Weight").get().val())+" kg")
            if db.child(user['localId']).child("Weight").get().val() is not None:
                weight_var = db.child(user['localId']).child("Weight").get().val()
            weight = st.number_input('Please enter your bodyweight (in kg)', min_value=0.0, max_value=None, value=0.0, step = 1.0)
            weight_button = st.button('Submit!')
            if weight_button and weight != 0:
                if weight_var>weight:
                    st.success("Great job!")
                db.child(user['localId']).child("Weight").set(weight)
                st.success('Your weight has been added successfully')
            st.markdown('<p class="big-font">"The greatest wealth is health"</p>', unsafe_allow_html=True)
            st.image(img, width = 500)
            st.write("""© 2022 Pentabetes""")
        elif bio == 'Home':
            st.header("Blood sugar concentrations")
            st.write("""This is graph of your blood sugar concentration of the last two hours: your sugar flow!   \n  
So, 80% of your glucose values during the last two hours were within a healthy range. Good job!""")
            st.image(img_sugar,width = 300)
            st.header("Information about the graph")
            st.write("""The end of the blue line represents your blood glucose concentration at this moment. Healthy ranges are within 3.9 mmol/l and 6,1 mmol/l, so with monitoring your glucose the goal is to keep your blood glucose concentration within those limits. The red dots represent data points that were predicted automatically, but the blue line is of most importance. After you have connected the dashboard to your continuous glucose monitor, this graph updates itself automatically real-time.  """)
            
            st.header("Welcome to MySugarFlow")
            st.write("""This dashboard is designed for people with Prediabetes, people with Diabetes Type 1 and 2, or for people who want to keep their blood sugar concentration within a healthy range. Regular blood sugar concentrations are extremely important for people with type 1 or type 2-diabetes, or people with prediabetes who want to stop the further development of this disease.  
             """)
            st.write("""With this dashboard, you can keep track of your current blood sugar concentrations, and your blood sugar concentrations of the last few hours here at the home tab. The main purpose of this dashboard is to check whether it is advisable to eat a certain food item, taking into account the blood glucose levels of the user. This can be done via the “Pick food” menu; with this menu a food item can be chosen, and then it will be calculated whether your blood sugar concentrations stay within a healthy range and whether a food item can be eaten. This calculation is done with the eDES model containing your current blood sugar concentrations. If a food item is not yet available in the “Pick food” menu, it is possible to add it via the “Add food” menu.  """)
            st.markdown('<p class="big-font">"Life is sweet, but living it healthily is even sweeter!" </p>', unsafe_allow_html=True)
            st.image(img, width=300)
            st.write("""© 2022 Pentabetes""")
            
        elif bio == 'Add food':
            Food_addition = st.text_input("Type the name of what food you want to add")
            Carb_addition = st.number_input("Amount of carbohydrates per 100 grams of chosen food", min_value=0.0, max_value=None, value=0.0, step = 1.0)
            press_input = st.button("Add food")
            if press_input and Food_addition != "":
                data_pd[Food_addition] = Carb_addition
                db.child(user['localId']).child("Food").child(Food_addition).set(data_pd)
                st.success('Your food has been added successfully')
            elif press_input and Food_addition == "":
                st.error("Please enter the name of the food you want to add")
            st.image(img, width = 500)
            st.write("""© 2022 Pentabetes""")
        elif bio == 'Pick food':
            if db.child(user['localId']).child("Food").get().val() is not None and db.child(user['localId']).child("Weight").get().val() is not None:
                data_pd_1 = db.child(user['localId']).child("Food").get().val()
                weight_1 = db.child(user['localId']).child("Weight").get().val()
                Chosen_food = st.selectbox("Select food you want to eat",data_pd_1)
                Amount_food = st.number_input("grams of "+Chosen_food+" you want to eat", min_value=0.0, max_value=None, value=0.0, step = 1.0)
                time = st.number_input('Time until consumption (min)', min_value=0.0, max_value=None, value=0.0, step = 1.0)
                Select_food = st.button("Calculate food")
                Add_food = st.checkbox("Add second food item")
                placeholder = st.empty()
                if Select_food and weight_1 != None:
                    placeholder.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',unsafe_allow_html=True,)
                    carb_100 = db.child(user['localId']).child("Food").child(Chosen_food).get().val()
                    carbs = ((((carb_100[Chosen_food])/100)*1000)*Amount_food)
                    Test_1 = Matlab_Calc(amount_of_peoples, weight_1, carbs, time)
                    if Test_1 == 'YES GOOD YES EAT':
                        st.success("You can eat "+str(Amount_food)+" grams of "+Chosen_food)
                    else:
                        st.error("Eating "+str(Amount_food)+" grams of "+Chosen_food+" would spike your blood glucose too much, we advise you not to eat "+str(Amount_food)+" grams of "+Chosen_food)
                    placeholder.empty()
                if Add_food:
                    Chosen_food_1 = st.selectbox("Select second food you want to eat",data_pd_1)
                    Amount_food_1 = st.number_input("grams of "+Chosen_food_1+" you want to eat ", min_value=0.0, max_value=None, value=0.0, step = 1.0)
                    Select_food_1 = st.button("Calculate first and second food items")
                    Add_food_1 = st.checkbox("Add third food item")
                    placeholder_1 = st.empty()
                    if Select_food_1 and weight_1 != None:
                        placeholder_1.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',unsafe_allow_html=True,)
                        carb_100 = db.child(user['localId']).child("Food").child(Chosen_food).get().val()
                        carb_100_1 = db.child(user['localId']).child("Food").child(Chosen_food_1).get().val()
                        carbs_1 = (((((carb_100_1[Chosen_food_1])/100)*1000)*Amount_food_1)+((((carb_100[Chosen_food])/100)*1000)*Amount_food))
                        Test_1_1 = Matlab_Calc(amount_of_peoples, weight_1, carbs_1, time)
                        if Test_1_1 == 'YES GOOD YES EAT':
                            st.success("You can eat "+str(Amount_food)+" grams of "+Chosen_food+" and "+str(Amount_food_1)+" grams of "+Chosen_food_1)
                        else:
                            st.error("Eating "+str(Amount_food)+" grams of "+Chosen_food+" and "+str(Amount_food_1)+" grams of "+Chosen_food_1+" would spike your blood glucose too much, we advise you not to eat "+str(Amount_food)+" grams of "+Chosen_food+" and "+str(Amount_food_1)+" grams of "+Chosen_food_1)
                        placeholder_1.empty()
                    if Add_food_1:
                        Chosen_food_2 = st.selectbox("Select third food you want to eat",data_pd_1)
                        Amount_food_2 = st.number_input("grams of "+Chosen_food_2+" you want to eat  ", min_value=0.0, max_value=None, value=0.0, step = 1.0)
                        Select_food_2 = st.button("Calculate all three food items")
                        Add_food_2 = st.checkbox("Add fourth food item")
                        placeholder_2 = st.empty()
                        if Select_food_2 and weight_1 != None:
                            placeholder_2.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',unsafe_allow_html=True,)
                            carb_100 = db.child(user['localId']).child("Food").child(Chosen_food).get().val()
                            carb_100_1 = db.child(user['localId']).child("Food").child(Chosen_food_1).get().val()
                            carb_100_2 = db.child(user['localId']).child("Food").child(Chosen_food_2).get().val()
                            carbs_2 = (((((carb_100_1[Chosen_food_1])/100)*1000)*Amount_food_1)+((((carb_100[Chosen_food])/100)*1000)*Amount_food)+((((carb_100_2[Chosen_food_2])/100)*1000)*Amount_food_2))
                            Test_1_2 = Matlab_Calc(amount_of_peoples, weight_1, carbs_2, time)
                            if Test_1_2 == 'YES GOOD YES EAT':
                                st.success("You can eat "+str(Amount_food)+" grams of "+Chosen_food+" and "+str(Amount_food_1)+" grams of "+Chosen_food_1+" and "+str(Amount_food_2)+" grams of "+Chosen_food_2)
                            else:
                                st.error("Eating "+str(Amount_food)+" grams of "+Chosen_food+" and "+str(Amount_food_1)+" grams of "+Chosen_food_1+" and "+str(Amount_food_2)+" grams of "+Chosen_food_2+" would spike your blood glucose too much, we advise you not to eat "+str(Amount_food)+" grams of "+Chosen_food+" and "+str(Amount_food_1)+" grams of "+Chosen_food_1+" and "+str(Amount_food_2)+" grams of "+Chosen_food_2)
                            placeholder_2.empty()
                        if Add_food_2:
                            Chosen_food_3 = st.selectbox("Select fourth food you want to eat",data_pd_1)
                            Amount_food_3 = st.number_input("grams of "+Chosen_food_3+" you want to eat   ", min_value=0.0, max_value=None, value=0.0, step = 1.0)
                            Select_food_3 = st.button("Calculate all four food items")
                            placeholder_3 = st.empty()
                            if Select_food_3 and weight_1 != None:
                                placeholder_3.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',unsafe_allow_html=True,)
                                carb_100 = db.child(user['localId']).child("Food").child(Chosen_food).get().val()
                                carb_100_1 = db.child(user['localId']).child("Food").child(Chosen_food_1).get().val()
                                carb_100_2 = db.child(user['localId']).child("Food").child(Chosen_food_2).get().val()
                                carb_100_3 = db.child(user['localId']).child("Food").child(Chosen_food_3).get().val()
                                carbs_3 = (((((carb_100_1[Chosen_food_1])/100)*1000)*Amount_food_1)+((((carb_100[Chosen_food])/100)*1000)*Amount_food)+((((carb_100_2[Chosen_food_2])/100)*1000)*Amount_food_2)+((((carb_100_3[Chosen_food_3])/100)*1000)*Amount_food_3))
                                Test_1_3 = Matlab_Calc(amount_of_peoples, weight_1, carbs_3, time)
                                if Test_1_3 == 'YES GOOD YES EAT':
                                    st.success("You can eat "+str(Amount_food)+" grams of "+Chosen_food+" and "+str(Amount_food_1)+" grams of "+Chosen_food_1+" and "+str(Amount_food_2)+" grams of "+Chosen_food_2+" and "+str(Amount_food_3)+" grams of "+Chosen_food_3)
                                else:
                                    st.error("Eating "+str(Amount_food)+" grams of "+Chosen_food+" and "+str(Amount_food_1)+" grams of "+Chosen_food_1+" and "+str(Amount_food_2)+" grams of "+Chosen_food_2+" and "+str(Amount_food_3)+" grams of "+Chosen_food_3+" would spike your blood glucose too much, we advise you not to eat "+str(Amount_food)+" grams of "+Chosen_food+" and "+str(Amount_food_1)+" grams of "+Chosen_food_1+" and "+str(Amount_food_2)+" grams of "+Chosen_food_2+" and "+str(Amount_food_3)+" grams of "+Chosen_food_3)
                                placeholder_3.empty()
                st.image(img, width = 500)
                st.write("""© 2022 Pentabetes""")
            elif db.child(user['localId']).child("Food").get().val() is None and db.child(user['localId']).child("Weight").get().val() is not None:
                st.info('Please add food')
            elif db.child(user['localId']).child("Weight").get().val() is None and db.child(user['localId']).child("Food").get().val() is not None :
                st.info('Please add your weight in the base settings')
            elif db.child(user['localId']).child("Weight").get().val() is None and db.child(user['localId']).child("Food").get().val() is None:
                st.info('Please add your weight in the base settings')
                st.info('Please add food')
        elif bio == "Help":
            st.header("Frequently asked questions")
            st.write("""
                     1.	What is the purpose of My Sugar Flow?\n  
                     MySugarFlow is designed for people who have the goal of keeping their blood sugar concentration within a healthy range, for example, people with prediabetes, diabetes type 1 or 2, or people who are overweight. With MySugarFlow, the current blood glucose concentrations can be viewed and the concentration flow over the past two hours. Furthermore, advice about whether to eat a specific food item can be gained. This has the purpose of keeping the blood glucose concentrations within a healthy range, because when a food item would cause a too high peak with the current blood glucose concentration, it is advised that the food item should not be eaten. 
                     
                     2.	How do I connect my continuous glucose monitor (CGM) to My Sugar Flow?\n
                     Unfortunately, at this moment it is not yet possible to connect your CGM to the dashboard. The Pentabetes team is still working on this together with the research team of the Eindhoven University of Technology. Hopefully, this will be available soon. 
                     
                     3.	How can I see if a food item is advisable to eat?\n  
                     In the “Pick food” menu a food item can be chosen. Then, the information about how many grams of the food item will be eaten should be inserted. Next, the time of food consumption should be inserted; this is how many minutes after the current moment the food item will be eaten. The last step is to push the button “Calculate food”. It takes some time to calculate this; during the calculating process ‘Running’ is visible in the right upper corner, so as long that is visible you know it is active and there is no need to fill the information again. It should not take longer than 2 minutes so after this, it would be wise to load the website again. 
                     
                     4.	How can I change the base settings?\n  
                     Via the menu “Base setting” the weight can be changed. It shows what you entered previously. Furthermore, when you are new to MySugarFlow, your weight should also be inserted into this menu as this information is needed for the calculation of whether a food item is possible at that moment.
                     
                     5.	How can I add new food items?\n  
                     Via the menu item “Add food” it is possible to add new food items. These food items will be saved to your account and will be available every time you log in. To log a new item, it is necessary to add the carbohydrate content per 100 grams of the food item. 

                     6.	How does My Sugar Flow calculate whether it is advisable or not to eat something?\n   
                     MySugarFlow is connected to the Eindhoven Diabetes Education Simulator, also called eDES. EDES is a physiology-based mathematical model that can make a prediction about glucose and insulin concentrations over a set period of time after the intake of meals and insulin injections. The input parameters for eDES are glucose concentration, insulin concentration, bodyweight, carbohydrate content, and time of food intake. Insulin concentration can at this moment of time not be measured real-time, so, because of that, the data of multiple blood tests is needed, which the model uses in the future.  \n  
                     The dashboard has a connection with eDES that is implemented in Matlab, and the information that is inserted in the dashboard is the input for the model, which then calculate the blood glucose concentrations and then can give an advice whether a food item is healthy to eat at the specified time. 

                     7.	What is a healthy range for my blood sugar concentrations?\n   
                     Healthy ranges are within 3.9 mmol/l and 6,1 mmol/l. 

                     8.	Where can I get in contact about the website?\n   
                     We are available via pentabetes@gmail.com. You can reach out to us for questions, feedback, or information! 
                     """)
            st.image(img, width = 300)
            st.write("""© 2022 Pentabetes""")
        elif bio == 'Info about diabetes':
            st.header("Diabetes")
            st.write("""Diabetes is a disease where the body itself can no longer balance blood sugar. Insulin is a hormone that regulates blood sugar levels by lowering blood sugar levels. Due to the insulin shortage, there is too much sugar in the blood and high blood sugar levels for a long time causes damage to the heart, eyes, kidneys and feet.  \n  
When suffering from diabetes, the body either has too little insulin or it no longer makes insulin at all. Often the reaction that the body should have to insulin is also disturbed; cells in the body have become resistant to insulin. There are different types of diabetes. The most common form is diabetes type 2 in which there is too little insulin, and/or the body no longer responds properly to insulin. With diabetes type 1, the immune system attacks the cells that make insulin, namely the beta cells in the pancreas. As a result, these cells can no longer produce insulin. """)
            st.write("The following symptoms are common in diabetes type 2: ")
            st.write("· More urination than usual, especially at night ")
            st.write("· Constant thirst  ")
            st.write("· Being very tired  ")
            st.write("· Losing weight unexpectedly  ")
            st.write("· Wounds that take longer to heal  ")
            st.write("· Impaired vision, such as red and burning eyes, blurred vision, double vision or poor vision")
            st.write("· Shortness of breath or leg pain when walking")
            st.write("· Infections that come back, such as cystitis")
            st.write("Diabetes type 1 is unfortunately not yet curable; people with type 1 diabetes should measure their blood sugar, measure their food intake and inject insulin every single day.")
            st.write("The first step in treating type 2 diabetes is living healthily. This can be achieved by:  ")
            st.write("· Eating healthily ")
            st.write("· Moving a lot  ")
            st.write("· Losing weight in case of being overweight ")
            st.write("· Sufficient relaxation and sleeping enough ")
            st.write("· Quitting smoking  ")
            st.write("By living a healthy life, the average blood sugar level can go down to a healthier range and there is a chance that fewer or no medications for diabetes are needed. ")
            st.image(img_dia, width = 350)
            st.header("Prediabetes")
            st.write("Prediabetes is a major risk factor for developing diabetes type 2; about 70% of people with prediabetes eventually develop diabetes type 2. With prediabetes, the reaction to high blood sugar levels is already disturbed, but not so fiercely that the patient is diagnosed with diabetes. It is essential that blood sugar levels are kept within normal values to prevent the further development of diabetes. ")
            st.write("Diabetes type 2 is often asymptomatic in the initial stages and can go unnoticed for years. Early diagnosis of the disease is important, because careful management can prevent long-term conditions. Impaired glucose tolerance is an indication of prediabetes and by means of an oral glucose tolerance test (OGTT), in which fasting 75 grams of sugar is consumed, prediabetes or diabetes can be determined. ")
            st.header("Diagnosis of diabetes")
            st.write("The most commonly used tests to diagnose diabetes are the fasting plasma glucose test (FPG) and the oral glucose tolerance test (OGTT). These tests both use the measurement of blood-glucose concentrations. Patients must have fasted before the study, so they are not allowed to eat anything starting the night before the test, as nothing should be eaten at least 8 hours before the study. Another possibility is to use glycated hemoglobin (HbA1c) to check the average blood glucose levels over a longer period (2 to 3 months). The blood test measures what percentage of the total amount of hemoglobin (Hb) has changed to glycated hemoglobin (HbA1c). Because this glycated hemoglobin remains in the blood for an average of 6 to 8 weeks, it gives an impression of the average blood glucose level over that period of time. ")
            st.header("Movement recommendations")
            st.write("Exercise is important become and remain healthy. As a result of exercising, the insulin sensitivity improves for diabetics. In addition, exercising helps to become fit and stay fit, maintain a healthy weight and it aids in reducing stress. At least half an hour of exercise a day is essential and the more, the better.   ")
            st.write("It is, however, important to adjust medication or insulin to exercise. Due to the higher insulin sensitivity, there is a faster chance of low blood sugar (hypoglycemia). ")
            st.write("Ideas for movement: ")
            st.write(""" \n  
                            ·   Take a walk of 20 minutes or more\n  
                            ·   Cycle through your neighbourhood\n  
                            ·   Go for a run\n   
                            ·   Work in the garden\n   
                            ·   Clean the house\n   
                            ·   Go swimming\n    """)
            st.image(img_cyc)
            st.write("Small things can already help in sitting less, such as walking to the grocery shop, dressing yourself standing, standing during cooking, taking the stairs instead of the elevator. Trying to at least stand up every half hour. ")
            st.subheader("Other interesting facts: ")
            st.write("· Movement can reduce sleeping issues ")
            st.write("· Walking is good for your mood. Serotine, the happiness hormone, is released in the brain during movement, so try to move! ")
            st.image(img, width = 500)
            st.write("""Sources:  \n  
https://www.diabetesfonds.nl/over-diabetes/diabetes-in-het-algemeen/wat-is-diabetes \n  
https://www.thuisarts.nl/diabetes-type-2/ik-wil-gezond-leven-met-diabetes-type-2 \n  
https://spreekuurthuis.nl/themas/diabetes_type_2/informatie/diagnose_en_onderzoek/hba1c_of_geglyceerd_hemoglobine  \n  """)
            st.write("""© 2022 Pentabetes""")
        elif bio == 'About us':
            st.header("About us")
            st.write("We are Charlie, Elena, Jeroen, Tessa and Sterre, together we form group 9 for the USE course Digital Twins in Healthcare at Eindhoven University of Technology. Together we have developed this User Interface to help people with prediabetes to inform them about their own disease and to be able to help with what is and is not wise to eat with the user's personal information.  ")
            st.write("The User Interface is still under development, but our vision is to be able to link the dashboard with a Continuous Glucose Monitor (CGM). The dashboard is connected to the Eindhoven Diabetes Education Simulator, eDEs, which is a physiologically-based mathematical model. Through the CGM, eDES can check whether the glucose value does not become too high by eating a certain food. Based on the information of the model, the dashboard advises the user.  ")
            st.subheader("Contact")
            st.write("Do you have a question, complaint or compliment? We are happy to help you! We are available at the following email address: ")
            st.write("pentabetes@gmail.com ")
            st.image(img_us)
            st.write("""© 2022 Pentabetes""")
            
    elif login and email not in email_list:
        st.error('This email does not exist')
    elif login and email == '':
        st.error("Please enter an email adress")
    elif login and password == '':
        st.error("Please enter a password")
    elif login and handle not in handle_list:
        st.error("This username does not exist")    
    elif login and str(password) != str(dict_boi_1[handle]["exists"]):
        st.error("Password and username do not match")
    elif login and dict_boi[handle]["exists"] != email:
        st.error("Username and email do not match")
    