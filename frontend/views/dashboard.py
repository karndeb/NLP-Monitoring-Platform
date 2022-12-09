import streamlit as st
import numpy as np
import pandas as pd


class Dashboard:
    class Model:
        pageTitle = "Dashboard"

        documentsTitle = "Documents"
        documentsCount = "10.5K"
        documentsDelta = "125"

        patientsTitle = "Patients"
        patientsCount = "510"
        patientsDelta = "40"

        BatchTitle = "Jobs"
        BatchCount = "87.9%"
        BatchDelta = "0.1%"

        PurgeTitle = "Purge Count"
        PurgeCount = "100"
        PurgeDelta = "10"

        TumorTypeTitle = "Tumor Types"
        TumorTypeCount = "17"
        TumorTypeDelta = "3"

        titleBatchMonitoring = "## Batch Job Monitoring"
        titleCPUMonitoring = "## CPU Monitoring"
        titleMemoryMonitoring = "## Memory Monitoring"

    def view(self, model):
        st.title(model.pageTitle)

        with st.container():
            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                st.metric(label=model.documentsTitle, value=model.documentsCount, delta=model.documentsDelta)

            with col2:
                st.metric(label=model.patientsTitle, value=model.patientsCount, delta=model.patientsDelta)

            with col3:
                st.metric(label=model.BatchTitle, value=model.BatchCount, delta=model.BatchDelta)

            with col4:
                st.metric(label=model.PurgeTitle, value=model.PurgeCount, delta=model.PurgeDelta,
                          delta_color="inverse")

            with col5:
                st.metric(label=model.TumorTypeTitle, value=model.TumorTypeCount, delta=model.TumorTypeDelta,
                          delta_color="inverse")

            st.markdown("---")

        with st.container():
            st.write(model.titleBatchMonitoring)
            chart_data = pd.DataFrame(
                np.random.randn(20, 3),
                columns=['Transformation', 'Inference', 'Analytics'])

            st.line_chart(chart_data)

        st.markdown("---")

        with st.container():
            col1, col2 = st.columns(2)

            with col1:
                with st.container():
                    st.write(model.titleCPUMonitoring)

                    # You can call any Streamlit command, including custom components:
                    st.bar_chart(np.random.randn(50, 3))

            with col2:
                with st.container():
                    st.write(model.titleMemoryMonitoring)

                    chart_data = pd.DataFrame(
                        np.random.randn(20, 3),
                        columns=['a', 'b', 'c'])

                    st.area_chart(chart_data)

