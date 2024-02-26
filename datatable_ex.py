import pandas as pd
import json
import streamlit as st
import time
from snowflake.snowpark import Session

import pandas as pd
import json
import streamlit as st
from snowflake.snowpark import Session
import time

conn = st.connection("snowflake")
st.write("connected to snowflake")

st.set_page_config(layout="centered", page_title="Data Editor", page_icon="🧮")
st.title("Snowflake Table Editor ❄️")
st.caption("This is a demo of the `st.experimental_data_editor`.")