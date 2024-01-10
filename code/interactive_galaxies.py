import logging
import streamlit as st
import numpy as np
import pandas as pd
def interactive_galaxies():
    questions = {
        'bar': ['strong', 'weak', 'no'],
        'has-spiral-arms': ['yes', 'no'],
        'spiral-arm-count': ['1', '2', '3', '4'],
        'spiral-winding': ['tight', 'medium', 'loose'],
        'merging': ['merger', 'major-disturbance', 'minor-disturbance', 'none']
    }
    
    st.sidebar.markdown('# Choose Your Galaxies')
    current_selection = {}
    for question, answers in questions.items():
        valid_to_select = True
        st.sidebar.markdown("# " + question.replace('-', ' ').capitalize() + '?')

        if question.startswith('spiral-'):
            has_spiral_answer, has_spiral_mean = current_selection.get('has-spiral-arms', [None, None])
            if has_spiral_answer == 'yes':
                valid_to_select = np.min(has_spiral_mean) > 0.5
            else:
                valid_to_select = np.min(has_spiral_mean) < 0.5

        if valid_to_select:
            selected_answer = st.sidebar.selectbox('Answer', answers, format_func=lambda x: x.replace('-',' ').capitalize(), key=question+'_select')
            selected_mean = st.sidebar.slider(
                label='Posterior Mean',
                value=[.0, 1.],
                key=question+'_mean')
            current_selection[question] = (selected_answer, selected_mean)
        else:
            st.sidebar.markdown('*To use this filter, set "Has Spiral Arms = Yes" to > 0.5'.format(question))
            current_selection[question] = None, None

    galaxies = load_data() # You need to implement the load_data function here

    logging.info('Total galaxies: {}'.format(len(galaxies)))
    valid = np.ones(len(galaxies)).astype(bool)
    for question, answers in questions.items():
        answer, mean = current_selection.get(question, [None, None])
        if mean is None:
            mean = (None, None)
        if len(mean) == 1:
            mean = (0., mean[0])

        if (answer is not None) and (mean is not None):
            this_answer = galaxies[question + '_' + answer + '_fraction']
            all_answers = galaxies[[question + '_' + a + '_fraction' for a in answers]].sum(axis=1)
            prob = this_answer / all_answers
            within_limits = (np.min(mean) <= prob) & (prob <= np.max(mean))

            preceding = True
            if mean != (0., 1.):
                preceding = galaxies[question + '_proportion_volunteers_asked'] >= 0.5

            valid = valid & within_limits & preceding

    logging.info('Valid galaxies: {}'.format(valid.sum()))
    st.markdown('{:,} of {:,} galaxies match your criteria.'.format(valid.sum(), len(valid)))

    selected = galaxies[valid][:40]
    image_urls = selected['url']

    opening_html = '<div style="display: flex; flex-wrap: wrap; justify-content: center;">'
    closing_html = '</div>'
    child_html = ['<img src="{}" style="margin: 10px; width: 200px; height: 200px; object-fit: cover;"></img>'.format(url) for url in image_urls]
    gallery_html = opening_html
    for child in child_html:
        gallery_html += child
    gallery_html += closing_html
    st.markdown(gallery_html, unsafe_allow_html=True)

