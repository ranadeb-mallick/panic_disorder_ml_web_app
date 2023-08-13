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

contact_style = """<style> 
input[type="text"], input[type="email"], textarea[type="message"]{
width: 100%; 
padding: 12px;
border: 1px solid #ccc;
border-radius: 25px;
box-sizing: border-box;
margin-top: 6px;
margin-bottom: 16px;
resize: vertical; 
} 
button[type="submit"]{
background-color: yellow;
border-radius: 10px;
}
</style>"""

st.set_page_config(page_title="Panic Disorder Diagnosis: Contact", page_icon="📧", layout="wide")
st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown(hide_menu_style, unsafe_allow_html=True)
st.markdown(contact_style, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>Reach out to me</h1>", unsafe_allow_html=True)

st.markdown("---")
# st.markdown("Ranadeb Mallick <p>Contact: 7001171498</p> <p>Email address: ranadebm15@gmail.com</p>", unsafe_allow_html=True)
st.markdown("""<form action="https://formsubmit.co/ranadebm15@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your email address" required>
     <textarea type="message" name="message" placeholder="Please type your message here"></textarea>
     <button type="submit">Send ✉</button>
     </form>""", unsafe_allow_html=True)



with st.sidebar:
    st.header("ABOUT")
    st.markdown("""<p>Developed by : <a href='https://www.linkedin.com/in/ranadeb-mallick-66a4b9222/' style='color: red;'>
<i>Ranadeb Mallick</i></a> </p>
               <p>USN : 211VMTR01111</p>
               <p>University : Jain University</p>
               <p>Project Mentor : Prof.Ruhiat Sultana</p>
               <p style='position:relative; bottom:-250px;'>copyright <b>&copy;</b> 2023 </p>""", unsafe_allow_html=True)
