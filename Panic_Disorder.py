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
background-image: url("https://images.unsplash.com/photo-1530903677198-7c9f3577a63e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8ODF8fHJhaW4lMjBkcm9wfGVufDB8fDB8fHww&auto=format&fit=crop&w=800&q=60");
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
