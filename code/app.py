import streamlit as st
from galaxy_catalog import main

st.set_page_config(
    layout="wide",
    page_title='Galaxy Spotter',
    page_icon='gz_icon.jpeg'
)

if __name__ == '__main__':
    main()
