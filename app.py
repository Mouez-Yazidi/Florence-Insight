import streamlit as st 
from transformers import AutoProcessor, AutoModelForCausalLM 
from PIL import Image
import requests
from PIL import Image
from io import BytesIO
# Set the app title 
st.title('My First Streamlit App') 
# Add a welcome message 
st.write('Welcome to my Streamlit app!') 

# This will not actually change the state in Streamlit, just for display purposes
st.radio("Select an option:", ('Upload an image', 'Enter an image URL'),index=None)
# Add a sidebar
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ['Caption','Segmentation','Object Detection'])

if option == 'Upload an image':
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    # Open the uploaded image
    image = Image.open(uploaded_file)
    
    # Display the uploaded image
    st.image(image, caption='Uploaded Image', use_column_width=True)
elif option == 'Enter an image URL':
    url = st.text_input("Enter the URL of the image:")
    if url:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        st.image(img, caption='Downloaded Image', use_column_width=True)



