import streamlit as st
from PIL import Image
import os

st.set_page_config(
    page_title= "Hello!",
    page_icon= "😄"
)

st.title("Hello!")

st.subheader("I will show you how to use this program!")

col1,col2 = st.columns(2,gap='large')

with col1:
    st.subheader("-Option1: If this is the first time")
    st.markdown('''1. Select "❓ Who Are You page" at the right side of the page''')
    image1 = Image.open("Codes/manual/1.png")
    st.image(image1)

    st.markdown('''2. Click "Allow" if page asks''')
    st.markdown('''3. Type your name''')
    image2 = Image.open("Codes/manual/2.png")
    st.image(image2)

    st.markdown('''4. Take a picture of yourself''')
    st.markdown('''5. Click "Submit" ''')
    image3 = Image.open("Codes/manual/3.png")
    st.image(image3)

    st.markdown('''6. Move to "Option2" ''')

with col2:
    st.subheader("-Option2: If this is NOT the first time")

    st.markdown('''1. Select "❗Guess Your Name" at the right side of the page''')
    image4 = Image.open("Codes/manual/4.png")
    st.image(image4)

    st.markdown('''2. Click "Allow" if page asks''')
    image5 = Image.open("Codes/manual/5.png")
    st.image(image5)

    st.markdown('''3. Take a picture of yourself''')
    st.markdown('''4. Click "See The Result" ''')
    image6 = Image.open("Codes/manual/6.png")
    st.image(image6)

#Make user name 
#->Hello! My name is... nice to meet you!
#Write the discription of how to use
#->Now let me guess your name!