
import streamlit as st
from streamlit.logger import get_logger
import pandas as pd
import time
import os 
import datetime as dt
import utils

def jaipur():
    st.set_page_config(
        page_title="Jaipur",
        page_icon="🏰",
    )
    df = utils.get_df()
    df2 = df.loc[df['City']=='Jaipur']
    col1, col2, col3 = st.columns(3)

    l_filenames = list(df2['FileName'])
    for i in range(0,len(l_filenames),3):
        try:
            with col1:
                st.image("data/"+l_filenames[i])
            with col2:
                st.image("data/"+l_filenames[i+1])
            with col3:
                st.image("data/"+l_filenames[i+2])
        except Exception as e:
            print()
jaipur()