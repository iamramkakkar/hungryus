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

import inspect
import textwrap
import pandas as pd
import os
import streamlit as st

def show_code(demo):
    """Showing the code of the demo."""
    show_code = st.sidebar.checkbox("Show code", True)
    if show_code:
        # Showing the code of the demo.
        st.markdown("## Code")
        sourcelines, _ = inspect.getsourcelines(demo)
        st.code(textwrap.dedent("".join(sourcelines[1:])))

def get_df():
    l0 = os.listdir("data/")

    df = pd.DataFrame(l0,columns =["FileName"] )

    df['Date1'] = df['FileName'].str.split("__").str[1]
    df['Year'] = df['Date1'].str[:4]
    df['Month'] = df['Date1'].str[4:6]
    df['Day'] = df['Date1'].str[6:8]
    df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']]).dt.date
    df.drop(['Date1', 'Year', 'Month', 'Day'],axis=1,inplace=True)
    df.sort_values(by='Date',ascending=False, inplace=True, ignore_index=True)
    df['City'] = df['FileName'].str.split("__").str[0]
    
    return(df)