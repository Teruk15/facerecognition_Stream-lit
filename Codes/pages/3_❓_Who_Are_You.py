import streamlit as st
import os

st.set_page_config(
    page_title= "Who Are You?",
    page_icon= "❓"
)

st.title("First... Let me know you!!!")
path = 'Train_Images'

with st.form(key = "first or not"):
    name = st.text_input('What is your name?')
    img = st.camera_input("Take a picture")
    if img:
        if not os.path.isdir("Train_Images"):
            os.makedirs("Train_Images")
            with open (os.path.join(path,name+'_train.jpg'),'wb') as file:
                file.write(img.getbuffer())
        else:
            with open (os.path.join(path,name+'_train.jpg'),'wb') as file:
                file.write(img.getbuffer())

    submit = st.form_submit_button('Submit')

    if submit:
        st.markdown("Picture successfully taken!!")
    
with st.form(key='upload'):
    image_file = st.file_uploader("Or... Upload Images", type=["jpg"])
    name = st.text_input('What is your name?')
    upload = st.form_submit_button('Upload')
    
    if upload:
        with open (os.path.join(path,name+'_train.jpg'),'wb') as file:
            file.write(image_file.getbuffer())
            st.markdown("File upload successfully!")


