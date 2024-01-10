import streamlit as st
from interactive_galaxies import interactive_galaxies
from tell_me_more import tell_me_more
from data_loader import load_data

def main():
    st.title('Galaxy Zoo Catalog')
    st.markdown(
    """
    Galaxy Zoo is a Bayesian Deep Learning Model to classify galaxies. It can provide massive and detailed morphology catalogues to support research into various types of galaxies.
    Explore the predictions using the filters on the left.
    To read more about how the model works, click below.
    """
    , unsafe_allow_html=True)
    should_tell_me_more = st.button('Tell me more')
    if should_tell_me_more:
        tell_me_more()
        st.markdown('---')
    else:
        st.markdown('---')
        interactive_galaxies()
