import easyocr as ocr
import streamlit as st
from PIL import Image
import numpy as np

st.title("Medical Prescription Recognition")

st.markdown("Extract text from the prescription")

st.markdown("")
image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])


@st.cache_resource
def load_model():
    reader = ocr.Reader(['en'])
    return reader

reader = load_model()

if image is not None:

    input_image = Image.open(image)
    st.image(input_image)

    with st.spinner("Recognizing Text"):
        result = reader.readtext(np.array(input_image))
        result_text = []
        for text in result:
            result_text.append(text[1])

        st.write(result_text)
    st.success("Here you go!", icon="✅")
else:
    st.write("Upload an Image")