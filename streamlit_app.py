import os
import streamlit as st

from converter import convert_docx


def delete_edit():
    os.remove('converted.docx')


st.title(".docx Latin <-> Cyrillic (Serbian) converter")
st.write("This is a transliterator that can convert between Latin and Cyrillic scripts of Serbian language.")
st.write("It doesn't convert the text that is inside tables.")
uploaded_file = st.file_uploader(label="Upload .docx file")

choice = st.radio(
    "Choose direction of transliteration: ",
    ('Latin -> Cyrillic', 'Cyrillic -> Latin'))


if choice == 'Latin -> Cyrillic':
    direction = 'lc'
else:
    direction = 'cl'

if uploaded_file is not None:
    convert_docx(uploaded_file, direction)

if os.path.exists('converted.docx'):
    with open('converted.docx', 'rb') as f:
        st.download_button(label="Download converted file", data=f, file_name="converted.docx")
        delete_edit()
