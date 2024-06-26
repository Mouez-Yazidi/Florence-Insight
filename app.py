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

st.markdown("""
    <style>
    .option-buttons {
        display: flex;
        flex-direction: column;
    }
    .option-button {
        margin: 5px 0;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 4px;
        cursor: pointer;
    }
    .option-button:hover {
        background-color: #f0f0f0;
    }
    </style>
    <div class="option-buttons">
        <div class="option-button" onclick="document.getElementById('radio-upload').checked=true; alert('Upload an image selected');">Upload an image</div>
        <div class="option-button" onclick="document.getElementById('radio-url').checked=true; alert('Enter an image URL selected');">Enter an image URL</div>
    </div>
""", unsafe_allow_html=True)

# This will not actually change the state in Streamlit, just for display purposes
st.radio("Select an option:", ('Upload an image', 'Enter an image URL'))
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



