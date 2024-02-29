### Mobile Recognization App
from dotenv import load_dotenv

load_dotenv() ## load all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("AIzaSyDt9PK2goi-jk9hZW9SOF6JoNnAMg_SmeY"))

## Function to load Google Gemini Pro Vision API And get response

def get_gemini_repsonse(input,image,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
##initialize our streamlit app

st.set_page_config(page_title="Mobile details recognizer")

st.header("Mobile details recognizer")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me the details")

input_prompt="""
You are an expert in mobiles and electronics and you need to identify the mobile and its parts
and need to define the parts and explain about the parts like battery,camera ,sound system, display,
ram , processor, 4g or 5g .
out put should br like the below moentioned format 
                  FONT SHOULD TIMES NEW ROMAN
                   list its parts one by one like bulletin points
                   explain about its parts in seperatley with minimum 100 words
                   who manufactured that ,machine (200 WORDS)
                   say about that manufacturing company, THEIR AIM ETC ( 150 WORDS)
    the above given should be made properly , with good english

    ----
    ----



"""

## If submit button is clicked

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_repsonse(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)


