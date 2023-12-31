import base64
import numpy as np
import pickle
import streamlit as st

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] > .main{
background-image: url("https://images.unsplash.com/photo-1520322082799-20c1288346e3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=772&q=80");
background-size: cover;
background-repeat: no-repeat;
background-attachment: local;
color: white;
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

st.set_page_config(page_title="Panic Disorder Diagnosis: Home", page_icon="🛡️", layout="wide")
st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown(hide_menu_style, unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center; color: white;'>Panic Disorder</h1>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""<h5 style='color: white;'>What Is Panic Disorder?</h5> 
            <p style='text-align: justify; color: white;'>Panic disorder is described as “a fear of fear” because people 
            with the condition develop a deep fear and anxiety of future panic attacks and avoid certain situations 
            they believe may trigger anxiety and a panic attack. While avoidance works to decrease anxiety in the moment,
            it reinforces the “false alarms,” increasing anxiety in the long run. Over time, this reinforcement increases 
            anxiety and avoidance to the point where it begins to interfere with a person’s normal routine and functioning,
            signaling the development of panic disorder.</p>""", unsafe_allow_html=True)
st.image("https://www.bridgestorecovery.com/wp-content/uploads/2018/09/Panic-Disorder-Symptoms.png")
st.markdown("""<p style='text-align: right;'><a href='https://www.bridgestorecovery.com/panic-disorder/' 
            style='color: yellow;'>Source</a></p>""", unsafe_allow_html=True)
st.markdown(""" A panic disorder causes sudden and unexpected attacks of severe anxiety, accompanied by an array of 
            disabling, uncontrollable physical symptoms. These attacks peak quickly, are highly intense, and may not 
            subside until the sufferer is able to return home or to another familiar environment.
            <h5 style='color: white;'>Panic Disorder in Children</h5> 
            <p style='text-align: justify;'>It is less common for children to be diagnosed with panic disorder, 
            but when they are, their symptoms can present differently than in adults. Children with panic disorder may 
            display more dramatic or emotional symptoms by having an outburst, crying, or screaming. Children who are 
            diagnosed with the disorder might not have the language or ability to describe their experiences and may 
            complain instead of a headache or stomach ache. Other times, children might appear irritable and on-edge 
            instead of anxious or scared, making it more difficult to detect the underlying issue.
            <a href='https://www.choosingtherapy.com/panic-disorder/' style='color: yellow;'>Click here</a> to know more </p>""",
            unsafe_allow_html=True)
st.markdown(""" <h4 style='color: white;'><u><i>Some proven Strategies to stop Panic Attack and Calm Yourself</u></i>
            </h4>""",unsafe_allow_html=True)
st.image("https://www.fabhow.com/wp-content/uploads/2017/08/how-to-stop-a-panic-attack.jpg")
st.markdown("""<p style='text-align: right;'>
            <a href='https://www.fabhow.com/self-improvement/how-to-stop-a-panic-attack' style='color: yellow;'>For details click here
            </a></p>""", unsafe_allow_html=True)
st.markdown("""<h4 style='color: white;'><u>Rationality of this web-application</u>: - </h4>
<p style='text-align: justify; color: white;'>
The prevalence of panic disorders and their significant impact on personal well-being and daily functioning 
underscore the importance of early detection and intervention. However, diagnosing panic disorders can be intricate due to the spontaneous 
nature of panic attacks and the absence of clear triggers. Moreover, accessing mental health professionals for timely diagnosis can be 
challenging due to various factors such as availability, stigma, and personal reluctance.
</p>
<p style='text-align: justify; color: white;'>
In response to these challenges, this predictive-panic-disorder-ml-web-app aims to bridge the gap between mental health assessment and 
treatment. By harnessing the power of machine learning algorithms, the application can analyse user-input data and potentially identify 
subtle patterns that might not be immediately evident to the users themselves. This data-driven approach can provide valuable insights to 
users and empower them to seek appropriate help.
</p>
<p style='text-align: justify; color: white;'>
Privacy and accessibility are key considerations in this endeavour. The application will prioritize user privacy by employing robust data 
security measures to ensure that personal information remains confidential. Additionally, the application's user-friendly interface and the 
convenience of conducting self-assessments remotely address the barriers that often hinder individuals from seeking professional help.
</p>
<p style='text-align: justify; color: white;'>
This Application seeks to leverage technology to offer users a means of self-assessment for panic disorders.
By proactively addressing the diagnostic challenges associated with panic disorders and promoting user-friendly accessibility, the 
application aims to contribute to early intervention, improved mental health outcomes, and a more informed approach to seeking professional
treatment.
</p>
<p style='text-align: justify; color: white;'>
It's important to acknowledge that while the application aims to provide valuable insights and support, it is not a substitute for 
professional medical advice. The application should be seen as a tool to assist users in self-assessment and early intervention, but 
individuals experiencing severe symptoms should still seek guidance from mental health professionals.
</p>
""", unsafe_allow_html=True)
st.markdown(
        "<p style='position:relative; bottom:-250px; color: white;'>&hearts; Special thanks to the online content creators </p>",
        unsafe_allow_html=True)
with st.sidebar:
    st.header("ABOUT")
    st.markdown("""<p>Developed by : <a href='https://www.linkedin.com/in/ranadeb-mallick-66a4b9222/' style='color: red;'>
<i>Ranadeb Mallick</i></a> </p>
               <p>USN : 211VMTR01111</p>
               <p>University : Jain University</p>
               <p>Project Mentor : Prof.Ruhiat Sultana</p>
               <p style='position:relative; bottom:-250px;'>copyright <b>&copy;</b> 2023 </p>""", unsafe_allow_html=True)
