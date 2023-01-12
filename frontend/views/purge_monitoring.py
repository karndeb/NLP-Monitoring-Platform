import streamlit as st
import pandas as pd


class PurgeMonitoring:
    class Model:
        pageTitle = "Purge Monitoring"
        titlePurgeMonitoring = "## Purge Monitoring Report"

    def view(self, model, ui_width):
        with st.sidebar:
            st.markdown("---")
        with st.container():
            st.write(model.titlePurgeMonitoring)
        with st.container():
            df = pd.read_csv("./sample-data/Pre-Post-Purge-Artifact-Count.csv", nrows=17)
            st.table(df)


