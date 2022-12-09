import streamlit as st
import json
import pandas as pd
from tools.utilities import getFromDict
from collections import ChainMap


class RunMonitoring:
    class Model:
        pageTitle = "Run Monitoring"
        titleRunMonitoring = "## Run Monitoring"

    def view(self, model, ui_width):
        with st.sidebar:
            st.markdown("---")
        with st.container():
            option = st.selectbox(
                'Please select the tumor type to get its relevant run information',
                ('', 'Liver', 'Bladder', 'Headandneck', 'Glioblastoma', 'gastroesophageal', 'endometrial',
                 'colorectal', 'Cervical', 'breast', 'Lung', 'Melanoma', 'Ovarian', 'Pancreas', 'Prostate',
                 'Renal', 'Renalpelvis', 'Thyroid'), format_func=lambda x: 'Select an option' if x == '' else x)
            if option:
                st.write('Yay! 🎉 You selected:', option)
                with st.container():
                    f = open('../sample-data/test.json')
                    res = json.load(f)
                    dataDict = dict(ChainMap(*res))
                    # print(dataDict)
                    # print('<--------------->')
                    for key in dataDict.keys():
                        # print(key)
                        # print('<--------------->')
                        map_list_fields = [key, "NON_BIOMARKER", "INFERENCE", "TUMOR_TYPE"]
                        each_wf_tumor = getFromDict(dataDict, map_list_fields)
                        # print(each_wf_tumor)
                        # print('<--------------->')
                        if each_wf_tumor == option.lower():
                            map_list2 = [key, "NON_BIOMARKER", "INFERENCE"]
                            each_wf = getFromDict(dataDict, map_list2)
                            # print(each_wf)
                            # print('<--------------->')
                            for k, v in each_wf.items():
                                st.write(k, ':', v)
                                # print('<--------------->')
            else:
                st.warning('No option is selected')

