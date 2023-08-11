import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

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

st.set_page_config(page_title="Panic Disorder Diagnosis: Visualization", page_icon="📊", layout="wide")
st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>Visualizing of Dataset</h1>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""<h3 style='color: white;'>Description of the Panic disorder diagnosis dataset: </h3> <p>This dataset 
contains total 120000 records about Panic disorder patients. Dataset contains two files. <ol>(1) Panic_Disorder_training 
dataset contains 100000 labeled records.</ol> <ol>(2) Panic_Disorder_testing dataset contains 20000 labeled records.</ol> 
We are going to use Panic_Disorder_testing dataset file for visualization purpose.</p>""", unsafe_allow_html=True)


@st.cache_data
def get_data(file_name):
    test_data = pd.read_csv(file_name)

    return test_data


test_data = get_data('D:/My_Projects/panic_disorder/pages/panic_disorder_dataset_testing.csv')
st.write(test_data.head(15))

parameter = ['Gender', 'Age', 'Demographics', 'Current Stressors', 'Symptoms', 'Medical History', 'Psychiatric History',
             'Coping Mechanisms', 'Social Support', 'Lifestyle Factors', 'Panic Disorder Diagnosis']
st.markdown("<h2 style='color: white;'><u>Select any of the one parameter to visualize: <u>: </h2>",
            unsafe_allow_html=True)
select_parameter = st.selectbox("**Choose a parameter:**", options=parameter)

if select_parameter == "Gender":
    fig1 = px.pie(test_data, names='Gender', template='none', title='Gender', color='Gender',
                  color_discrete_map={'Male': 'lightcyan', 'Female': 'cyan'})
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True, sharing="streamlit")

if select_parameter == "Age":
    plt.figure(figsize=(18, 8))
    fig1 = sns.countplot(x=test_data['Age'], hue='Gender', data=test_data, palette="mako")
    st.pyplot(plt.gcf())  # get current figure

if select_parameter == "Demographics":
    fig1 = px.pie(test_data, names='Demographics', template='none', title='Demographics', color='Demographics',
                  color_discrete_map={'Rural': 'aqua', 'Urban': 'darkblue'})
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True, sharing="streamlit")

if select_parameter == "Current Stressors":
    fig1 = px.pie(test_data, names='Current Stressors', template='none', title='Current Stressors',
                  color='Current Stressors',
                  color_discrete_map={'Low': 'lavender', 'High': 'darkblue', 'Moderate': 'cornflowerblue'})
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True, sharing="streamlit")

if select_parameter == "Symptoms":
    fig1 = px.pie(test_data, names='Symptoms', template='none', title='Symptoms', color='Symptoms',
                  color_discrete_map={'Dizziness': 'lavender', 'Fear of losing control': 'royalblue', 'Chest pain': 'cyan',
                                      'Shortness of breath': 'lightcyan', 'Panic attacks': 'darkblue'})
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True, sharing="streamlit")

if select_parameter == "Medical History":
    fig1 = px.pie(test_data, names='Medical History', template='none', title='Medical History', color='Medical History',
                  color_discrete_map={'None': 'aqua', 'Diabetes': 'darkblue', 'Heart disease': 'mediumslateblue',
                                      'Asthma': 'royalblue'})
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True, sharing="streamlit")

if select_parameter == "Psychiatric History":
    fig1 = px.pie(test_data, names='Psychiatric History', template='none', title='Psychiatric History',
                  color='Psychiatric History',
                  color_discrete_map={'Bipolar disorder': 'darkblue', 'Depressive disorder': 'royalblue',
                                      'Anxiety disorder': 'cyan',
                                      'None': 'lightcyan'})
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True, sharing="streamlit")

if select_parameter == "Coping Mechanisms":
    fig1 = px.pie(test_data, names='Coping Mechanisms', template='none', title='Coping Mechanisms',
                  color='Coping Mechanisms',
                  color_discrete_map={'Socializing': 'c', 'Meditation': 'cyan', 'Seeking therapy': 'royalblue',
                                      'Exercise': 'lavender'})
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True, sharing="streamlit")

if select_parameter == "Social Support":
    fig1 = px.pie(test_data, names='Social Support', template='none', title='Social Support', color='Social Support',
                  color_discrete_map={'High': 'darkblue', 'Moderate': 'mediumslateblue', 'Low': 'cyan', })
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True, sharing="streamlit")

if select_parameter == "Lifestyle Factors":
    fig1 = px.pie(test_data, names='Lifestyle Factors', template='none', title='Lifestyle Factors',
                  color='Lifestyle Factors',
                  color_discrete_map={'Exercise': 'royalblue', 'Diet': 'cyan', 'Sleep quality': 'darkblue'})
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True, sharing="streamlit")

if select_parameter == "Panic Disorder Diagnosis":
    fig1 = px.pie(test_data, names='Panic Disorder Diagnosis', template='none', title='Panic Disorder Diagnosis',
                  color='Panic Disorder Diagnosis', color_discrete_map={0: 'darkblue', 1: 'cyan'})
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True, sharing="streamlit")


with st.sidebar:
    st.header("ABOUT")
    st.markdown("""<p>Developed by : <a href='https://www.linkedin.com/in/ranadeb-mallick-66a4b9222/' style='color: red;'>
<i>Ranadeb Mallick</i></a> </p>
               <p>USN : 211VMTR01111</p>
               <p>University : Jain University</p>
               <p>Project Mentor : Prof.Ruhiat Sultana</p>
               <p style='position:relative; bottom:-250px;'>copyright <b>&copy;</b> 2023 </p>""", unsafe_allow_html=True)
