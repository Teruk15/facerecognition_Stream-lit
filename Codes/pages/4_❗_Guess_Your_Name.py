import streamlit as st
import os
import face_recognition
import cv2
from PIL import Image

st.set_page_config(
    page_title= "Guess Your Name!",
    page_icon= "❗"
)

st.title("Now... Let me guess your name!!!")

path = 'Test_Images'
folder_dir = 'Train_Images'
train_images_list = os.listdir(folder_dir)
smallest_distance = 1

if not os.path.isdir("Test_Images"):
            os.makedirs("Test_Images")

with st.form(key = "take test"):
    img = st.camera_input("Take a picture...")
    st.text("Click 'See The Result' button to view my guess!")
    submit = st.form_submit_button("See The Result")       

    if img:
        with open (os.path.join(path,'test.jpg'),'wb') as file:
            file.write(img.getbuffer())

            test_image = face_recognition.load_image_file('Test_Images/test.jpg') 
            test_image = cv2.cvtColor(test_image,cv2.COLOR_BGR2RGB)
            encode_test_image = face_recognition.face_encodings(test_image)[0]

            for i in train_images_list:
                train_image = face_recognition.load_image_file('Train_Images/' + i) 
                train_image = cv2.cvtColor(train_image,cv2.COLOR_BGR2RGB)
                encode_train_image = face_recognition.face_encodings(train_image)[0]

                distance = face_recognition.face_distance([encode_train_image],encode_test_image)
                print(i)
                print(distance)

                if smallest_distance > distance:
                    smallest_distance = distance
                    guess_pic = i
    
            guess_name = guess_pic.split('_train.jpg')[0]
        

            if submit:
                st.text("I guess your name as...")
                st.text(guess_name + " !!!")
        
with st.form(key = 'faces'):
    see = st.form_submit_button("Look all the faces I know")
    for i in train_images_list:
        img = Image.open('Train_Images/' + i)
        if see:
            st.image(img,caption = i.split('_train.jpg')[0])
        


# face_location_test = face_recognition.face_locations(test_image)[0]
# cv2.rectangle(test_image,(face_location_test[3],face_location_test[0]),(face_location_test[1],face_location_test[2]),(255,0,0),2)
# cv2.imshow('tes_images',test_image)
# cv2.waitKey(0) 
    

