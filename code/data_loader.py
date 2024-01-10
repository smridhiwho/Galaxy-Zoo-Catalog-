import pandas as pd
import streamlit as st

@st.cache
def load_data():
    # Load your data here
    # Example: Load CSV files into a DataFrame
    df_locs = ['decals_{}.csv'.format(n) for n in range(4)]
    df_locs.append('gz2_classification.csv')  # Add the new file here
    dfs = [pd.read_csv(df_loc) for df_loc in df_locs]
    return pd.concat(dfs)
