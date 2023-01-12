import streamlit as st
import json
import hydralit_components as hc


# can apply customisation to almost all the properties of the card, including the progress bar
theme_bad = {'bgcolor': '#FFF0F0','title_color': 'red','content_color': 'red','icon_color': 'red', 'icon': 'fa fa-times-circle'}
theme_neutral = {'bgcolor': '#f9f9f9','title_color': 'orange','content_color': 'orange','icon_color': 'orange', 'icon': 'fa fa-question-circle'}
theme_good = {'bgcolor': '#EFF8F7','title_color': 'green','content_color': 'green','icon_color': 'green', 'icon': 'fa fa-check-circle'}


class BatchMonitoring:
    class Model:
        pageTitle = "Batch Monitoring"
        titleBatchMonitoring = "## Batch Monitoring"

    def view(self, model, ui_width):
        with st.sidebar:
            st.markdown("---")
        with st.container():
            st.write(model.titleBatchMonitoring)
        f = open('./sample-data/monitoring-api-response-sample.json')
        res = json.load(f)
        c1 = st.columns(1)
        c2 = st.columns(1)
        c3 = st.columns(1)

        with st.container():
            with c1[0]:
                # can just use 'good', 'bad', 'neutral' sentiment to auto color the card
                hc.info_card(title='Jobs in Runnable/Starting', title_text_size='1.4rem',
                             bar_value=str(int(res["runnable"]) + int((res["starting"]))), theme_override=theme_good)
        with st.container():
            with c2[0]:
                hc.info_card(title='Jobs in Running/Succeeded', title_text_size='1.4rem',
                             bar_value=str(int(res["running"]) + int((res["succeeded"]))),
                             theme_override=theme_neutral)
        with st.container():
            with c3[0]:
                hc.info_card(title='Jobs in Failed', title_text_size='1.4rem',
                             bar_value=str(int(res["failed"])),
                             theme_override=theme_bad)

