import streamlit as st
import pickle
import numpy as np
import pandas as pd

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] > .main{
background-image: url("https://images.unsplash.com/photo-1689590872712-28f3248f8c91?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw5OHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=600&q=60");
background-size: cover;
background-repeat: no-repeat;
background-attachment: local;
}

[data-testid="stHeader"]{
background-color: rgba(0,0,0,0);
}

[data-testid="stSidebar"]{
background-image: url("https://images.unsplash.com/photo-1590622783586-e5d3ee34cc85?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=774&q=80");
background-size: cover;
}

</style>
"""

hide_menu_style = """<style>
#MainMenu{visibility: hidden;}
header{visibility: hidden;}
footer{visibility: hidden;}
</style>"""

st.set_page_config(page_title="Panic Disorder Diagnosis: Diagnosis", page_icon="📌", layout="wide")
st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #02022d;'>Symptoms Diagnosis</h1>", unsafe_allow_html=True)
st.markdown("---")

tab1, tab2, tab3 = st.tabs(
    ['Panic Disorder Diagnosis', 'Yoga Poses to keep you Feeling Great', 'Soothing music to keep you calm'])

with tab1:
    st.header('Enter your details below to diagnosis Panic Disorder')

    # loading the saved model
    loaded_model = pickle.load(open('panic_disorder_dtc.sav', 'rb'))


    @st.cache_data
    def panic_predictor(input_data):
        # Changing the input_data to numpy array
        input_data_array = pd.DataFrame(np.array(input_data).reshape(1, -1),
                                        columns=['Age', 'Gender', 'Family History', 'Personal History',
                                                 'Current Stressors', 'Symptoms', 'Severity', 'Impact on Life',
                                                 'Demographics', 'Medical History', 'Psychiatric History',
                                                 'Substance Use', 'Coping Mechanisms', 'Social Support',
                                                 'Lifestyle Factors'])
        # Reshaping the array as we are predicting for one instance
        input_data_reshape = input_data_array
        predict = loaded_model.predict(input_data_reshape)
        print(predict)
        if predict[0] == 0:
            return "Diagnosis:  ✅ Panic Disorder NOT Detected ✅"
        else:
            return "Diagnosis: 🛑 Panic Disorder Detected 🛑"


    def main():
        Age = st.slider('**Select your Age from the slider:**', 10, 100)
        col1, col2 = st.columns(2)
        with col1:
            Gender = st.radio('**Specify your Gender :**', ['Male', 'Female'], index=0)
            Family_History = st.radio('**Whether you have any Family History on Psychiatry :**', ['Yes', 'No'], index=0)
            Personal_History = st.radio('**Whether you have any Personal History on Psychiatry :**', ['Yes', 'No'],
                                        index=0)
            Current_Stressors = st.radio('**what is your Current Stress Label :**', ['Low', 'Moderate', 'High'],
                                         index=0)
            Symptoms = st.radio('**Which Symptom you are facing right now :**',
                                ['Shortness of breath', 'Panic attacks', 'Chest pain', 'Dizziness',
                                 'Fear of losing control'],
                                index=4)
            Severity = st.radio('**How Sever your symptom is :**', ['Mild', 'Moderate', 'Severe'], index=1)
            Impact_on_Life = st.radio('**How it impact on  your life :**', ['Mild', 'Moderate', 'Significant'], index=0)
        with col2:
            Demographics = st.radio('**Demographics of your living place :**', ['Rural', 'Urban'], index=1)
            Medical_History = st.radio('**Any Medical Disease do you have?**',
                                       ['None', 'Asthma', 'Heart disease', 'Diabetes'],
                                       index=0)
            Psychiatric_History = st.radio('**Any Psychiatric Disease do you have?**',
                                           ['None', 'Anxiety disorder', 'Depressive disorder', 'Bipolar disorder'],
                                           index=0)
            Substance_Use = st.radio('**Any kind of Substance do you use? like:**', ['None', 'Alcohol', 'Drugs'],
                                     index=0)
            Coping_Mechanisms = st.radio('**What you do to clam yourself?**',
                                         ['Socializing', 'Exercise', 'Seeking therapy', 'Meditation'], index=0)
            Social_Support = st.radio('**What kind of Social Support do you have?**', ['Low', 'Moderate', 'High'],
                                      index=0)
            Lifestyle_Factors = st.radio('**What LifeStyle Factor affects the most?**',
                                         ['Sleep quality', 'Exercise', 'Diet'], index=0)

        # code for prediction
        diagnosis = ''

        # creating a button
        if st.button("Click to Diagnosis"):
            diagnosis = panic_predictor(
                [Age, Gender, Family_History, Personal_History, Current_Stressors, Symptoms, Severity,
                 Impact_on_Life, Demographics, Medical_History, Psychiatric_History, Substance_Use, Coping_Mechanisms,
                 Social_Support, Lifestyle_Factors])

        st.success(diagnosis)


    if __name__ == '__main__':
        main()

with tab2:
    st.header('Yoga Poses to keep you Feeling Great')
    st.subheader('Yoga')

    poses = st.radio('**Choose any of the yoga poses**',
                     ['Tadasana', 'Forward bend', 'Wide leg forward bend', 'Hastapadasana', 'Ardhakurmasan',
                      'Batilasana(Cat & Camel pose)', 'Setu Bandhasana(Bridging)', 'Leg up wall', 'Child pose',
                      'Plank'])

    if poses == 'Tadasana':
        images = [
            'https://www.yogicwayoflife.com/wp-content/uploads/2014/12/Tadasana_Palm_Tree_Pose_Yoga_Asana_Standing_Pose.jpg',
            'https://media.istockphoto.com/id/1441325551/photo/full-length-of-young-woman-wearing-sportswear-practicing-yoga-standing-in-mountain-exercise.jpg?s=1024x1024&w=is&k=20&c=Nq7_k-uvdHV083GY1TcXAXoLIhzmoWVHHw1QkCmWUPs=']
        st.image(images, caption=["Tadasana"] * len(images))
    elif poses == 'Forward bend':
        images = [
            'https://cdn.yogajournal.com/wp-content/uploads/2022/05/forward-bend-andrew-clark.jpg?crop=604:344&width=604',
            'https://www.yogapedia.com/images/uploads/a77e194874f34519b4811f796e887ebb.jpg?height=580&width=940&mode=crop']
        st.image(images, caption=["Forward Bend"] * len(images))
    elif poses == 'Wide leg forward bend':
        images = [
            'https://cdn.yogajournal.com/wp-content/uploads/2020/03/Wide-Legged-Standing-Forward-Bend_Andrew-Clark.jpg?crop=604:344&width=604',
            'https://101yogastudio.com/wp-content/uploads/2019/05/Wide-Legged-Forward-Bend.jpg']
        st.image(images, caption=["Wide Leg Forward Bend"] * len(images))
    elif poses == 'Hastapadasana':
        images = ['https://cdn.yogajournal.com/wp-content/uploads/2007/08/big-toe-pose-1.jpg?crop=604:344&width=604',
                  'https://i.pinimg.com/originals/5a/88/70/5a8870ddcd0892b645ba8a4a9927459c.jpg']
        st.image(images, use_column_width=True, caption=["Hastapadasana / Uttanasana"] * len(images))
    elif poses == 'Ardhakurmasan':
        image = [
            'https://cdn.yogajournal.com/wp-content/uploads/2021/10/Childs-Pose_Andrew-Clark_1.jpg?crop=604:344&width=604']
        st.image(image, use_column_width=True, caption=["Ardhakurmasan"] * len(image))
    elif poses == 'Batilasana(Cat & Camel pose)':
        images = ['https://i.pinimg.com/736x/d1/e9/67/d1e967e12e66cbcac3132e33fc6d64dc.jpg',
                  'https://i.pinimg.com/736x/25/fc/8a/25fc8a64f629f636707ae9feec2055eb.jpg']
        st.image(images, use_column_width=True, caption=["Batilasana(Cat & Camel pose)"] * len(images))
    elif poses == 'Setu Bandhasana(Bridging)':
        images = [
            'https://cdn.yogajournal.com/wp-content/uploads/2021/11/YJ_Bridge-Pose_Andrew-Clark_2400x1350.png?crop=604:344&width=604',
            'https://i.pinimg.com/originals/e1/90/2c/e1902c0edfaa8b91e08f879991fa1c80.jpg']
        st.image(images, use_column_width=True, caption=["Setu Bandhasana(Bridging Pose)"] * len(images))
    elif poses == 'Leg up wall':
        image = [
            'https://cdn.yogajournal.com/wp-content/uploads/2021/12/Legs-Up-the-Wall-Pose_Andrew-Clark_2400x1350.jpeg?crop=604:344&width=604']
        st.image(image, use_column_width=True, caption=["Leg Up Wall"] * len(image))
    elif poses == 'Child pose':
        image = [
            'https://cdn.yogajournal.com/wp-content/uploads/2022/04/42-yoga-journal-2022-C-andrew-clark-BC8I0032_1.jpg?crop=604:344&width=604']
        st.image(image, use_column_width=True, caption=["Child Pose"] * len(image))
    elif poses == 'Plank':
        image = [
            'https://cdn.yogajournal.com/wp-content/uploads/2022/01/Forearm-Plank_Andrew-Clark.jpg?crop=604:344&width=604']
        st.image(image, use_column_width=True, caption=["Plank Pose"] * len(image))
    st.markdown(
        "<p style='font-size:5; position:relative; bottom:-250px;'>&hearts; Special thanks to the online content creators </p>",
        unsafe_allow_html=True)

with tab3:
    st.header('Music which makes you calm')
    st.subheader('Soothing Music')
    st.video('https://youtu.be/O2K0ptoYpuc=8:15')
    st.markdown(
        "<p style='font-size:5; position:relative; bottom:-250px;'>&hearts; Special thanks to the online content creators </p>",
        unsafe_allow_html=True)
with st.sidebar:
    st.header("ABOUT")
    st.markdown("""<p>Developed by : <a href='https://www.linkedin.com/in/ranadeb-mallick-66a4b9222/' style='color: red;'>
<i>Ranadeb Mallick</i></a> </p>
               <p>USN : 211VMTR01111</p>
               <p>University : Jain University</p>
               <p>Project Mentor : Prof.Ruhiat Sultana</p>
               <p style='position:relative; bottom:-250px;'>copyright <b>&copy;</b> 2023 </p>""",
                unsafe_allow_html=True)
