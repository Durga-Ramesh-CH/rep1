import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="Image Display App",
    page_icon="🖼️",
    layout="centered"
)

st.title("Image Display Application")

st.write("Click the button below to display three images.")

# Button
if st.button("Show Images"):

    col1, col2, col3 = st.columns(3)

    with col1:
        image1 = Image.open("images/image1.jpeg")
        st.image(image1, caption="Image 1", use_container_width=True)

    with col2:
        image2 = Image.open("images/image2.jpeg")
        st.image(image2, caption="Image 2", use_container_width=True)

    with col3:
        image3 = Image.open("images/image3.jpeg")
        st.image(image3, caption="Image 3", use_container_width=True)