import streamlit as st

def tell_me_more():
    st.title('About the Model')

    st.markdown(
        """
        Built using Bayesian CNNs for morphology classification as developed 
        [here](https://arxiv.org/abs/1905.07424). This model utilizes a novel generative 
        model from the volunteer responses of [Galaxy Zoo](https://www.zooniverse.org/projects/zookeeper/galaxy-zoo/about/results) 
        at Zooniverse.org to infer posteriors for the visual morphology of galaxies.
        """
    )

    st.button('Back to galaxies', key='back_again')  # This button will change state and trigger a rerun to reset the 'tell_me_more' view
