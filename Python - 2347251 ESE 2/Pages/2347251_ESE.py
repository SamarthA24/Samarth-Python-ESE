import streamlit as st 
import matplotlib.pyplot as plt 
import plotly.express as px 
import pandas as pd

def load_data():
    return pd.read_csv("WomensClothingE-CommerceReviews.csv")  
data = load_data()

st.title("Women Clothing Analysis DashBorad")
gender_count = data.groupby(['Age', 'Rating']).size().reset_index(name='Count')
fig = px.scatter_3d(gender_count, x='Age', y='Rating', z='Count', color='Age',
                    labels={'Age': 'Age', 'Rating': 'Rating', 'Count': 'Count'},
                    title='Customer Demographics')
st.plotly_chart(fig)

gender_count = data.groupby(['Rating', 'Positive Feedback Count']).values_count.reset_index(name='Count')
fig = px.scatter_3d(gender_count, x='Rating', y='Positive Feedback Count', z='Count', color='Age',
                    labels={'Rating': 'Rating', 'Positive Feedback Count': 'Positive Feedback Count', 'Count': 'Count'},
                    title='Scatter Plot for Rating and Positive Feedback Count')
st.plotly_chart(fig)


