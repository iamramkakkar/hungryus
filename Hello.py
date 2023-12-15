# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import pandas as pd
import time
import os 
import datetime as dt

LOGGER = get_logger(__name__)


def run():
    
    st.set_page_config(
        page_title="HungryUs",
        page_icon="😋",
    )

    st.write("# Welcome to Streamlit! 👋")
    
    # df = pd.DataFrame({
    #     'first column': [1, 2, 3, 4],
    #     'second column': [10, 20, 30, 40]
    #     })

    # option = st.selectbox(
    #     'Which number do you like best?',
    #     df['first column'])

    # 'You selected: ', option
    # #st.sidebar.success("Select a demo above.")
    # # Add a selectbox to the sidebar:
    # add_selectbox = st.sidebar.selectbox(
    #     'How would you like to be contacted?',
    #     ('Email', 'Home phone', 'Mobile phone')
    # )

    # # Add a slider to the sidebar:
    # add_slider = st.sidebar.slider(
    #     'Select a range of values',
    #     0.0, 100.0, (25.0, 75.0)
        
    # )

    # 'Starting a long computation...'

    # # # Add a placeholder
    # # latest_iteration = st.empty()
    # # bar = st.progress(0)

    # # for i in range(100):
    # #   # Update the progress bar with each iteration.
    # #   latest_iteration.text(f'Iteration {i+1}')
    # #   bar.progress(i + 1)
    # #   time.sleep(0.1)



    l0 = os.listdir("data/")
    # st.write(os.listdir("data/"))

    df = pd.DataFrame(l0,columns =["FileName"] )
    # st.dataframe(df)

    df['Date1'] = df['FileName'].str.split("__").str[1]
    df['Year'] = df['Date1'].str[:4]
    df['Month'] = df['Date1'].str[4:6]
    df['Day'] = df['Date1'].str[6:8]
    df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']]).dt.date
    df.drop(['Date1', 'Year', 'Month', 'Day'],axis=1,inplace=True)
    df.sort_values(by='Date',ascending=False, inplace=True, ignore_index=True)
    # st.dataframe(df)

    range_selected = st.slider("Select a range of date",
              dt.date(2019, 7, 6),
              dt.date(2024, 12, 12),
              (dt.date(2022, 7, 6),dt.date(2022, 12, 12)))

    st.markdown(range_selected[0])
    st.markdown(range_selected[1])
    
    col1, col2, col3 = st.columns(3)

    df2 = df.loc[(df['Date']>range_selected[0]) & (df['Date']<range_selected[1])]
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

if __name__ == "__main__":
    run()
