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
import utils

LOGGER = get_logger(__name__)


def run():
    
    st.set_page_config(
        page_title="HungryUS",
        page_icon="😋",
    )

    st.write("# Welcome to Hungry US! 👋")
    df = utils.get_df()

    range_selected = st.sidebar.slider("Select a range of date",
              dt.date(2019, 1, 1),
              dt.date(2024, 12, 12),
              (dt.date(2022, 7, 1),dt.date(2022, 12, 1)))
    
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
