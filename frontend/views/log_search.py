import streamlit as st
import requests
import pandas as pd
from tools.utilities import format_search, load, make_query
from tools.config import *

APP_URL = 'http://host.docker.internal:9292'


class LogSearch:
    class Model:
        pageTitle = "Log Search"
        titleLogSearch = "## Log Search"

    def view(self, model, ui_width):
        with st.sidebar:
            st.markdown("---")
        with st.container():
            res = load()
            if res['status'] == 'ok':
                st.write(model.titleLogSearch)
                # User search
                user_input = st.text_area("Search box")
                q = make_query(user_input, Fields)
                search_endpoint = "/search"
                api_res = requests.get(APP_URL + search_endpoint + "/" + str(q))
                print(api_res.json())
                lst = format_search(api_res.json())
                df = pd.DataFrame(lst)
                st.table(df)


