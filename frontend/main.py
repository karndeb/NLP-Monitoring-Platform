import streamlit as st
import yaml
from streamlit_option_menu import option_menu
from tools.utilities import load_css

from views.dashboard import Dashboard
from views.batch_monitoring import BatchMonitoring
from views.log_search import LogSearch
from views.purge_monitoring import PurgeMonitoring
from views.run_monitoring import RunMonitoring

import streamlit_javascript as st_js
import streamlit_authenticator as stauth

st.set_page_config(
    page_title="Oncology-Monitoring-Platform",
    page_icon="assets/favicon_io/favicon.ico",
    layout="wide"
)

load_css()

# User Auth
with open('credentials.yaml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
name, authentication_status, username = authenticator.login("Login", "main")

# if not st.session_state["authentication_status"]:
#     st.error("Username/password is incorrect")
#
# if st.session_state["authentication_status"] is None:
#     st.warning("Please enter your username and password")

if st.session_state["authentication_status"]:

    class Model:
        menuTitle = "Oncology-Monitoring-Platform"
        option1 = "Dashboard"
        option2 = "Batch Monitoring"
        option3 = "Log Search"
        option4 = "Purge Monitoring"
        option5 = "Run Monitoring"

        menuIcon = "menu-up"
        icon1 = "speedometer"
        icon2 = "activity"
        icon3 = "clipboard-data"
        icon4 = "clipboard-data"
        icon5 = "clipboard-data"


    def view(model):
        with st.sidebar:
            menuItem = option_menu(model.menuTitle,
                                   [model.option1, model.option2, model.option3, model.option4, model.option5],
                                   icons=[model.icon1, model.icon2, model.icon3, model.icon4, model.icon5],
                                   menu_icon=model.menuIcon,
                                   default_index=0,
                                   styles={
                                       "container": {"padding": "5!important", "background-color": "#fafafa"},
                                       "icon": {"color": "black", "font-size": "25px"},
                                       "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px",
                                                    "--hover-color": "#eee"},
                                       "nav-link-selected": {"background-color": "#037ffc"},
                                   })

        if menuItem == model.option1:
            Dashboard().view(Dashboard.Model())
            ui_width = st_js.st_javascript("window.innerWidth")
            ui_width = round(ui_width + (18 * ui_width / 100))

            st.session_state['ui_width'] = ui_width
            logout_widget()

        if menuItem == model.option2:
            BatchMonitoring().view(BatchMonitoring.Model(), st.session_state['ui_width'])
            logout_widget()

        if menuItem == model.option3:
            LogSearch().view(LogSearch.Model(), st.session_state['ui_width'])
            logout_widget()

        if menuItem == model.option4:
            PurgeMonitoring().view(PurgeMonitoring.Model(), st.session_state['ui_width'])
            logout_widget()

        if menuItem == model.option5:
            RunMonitoring().view(RunMonitoring.Model(), st.session_state['ui_width'])
            logout_widget()


    def logout_widget():
        with st.sidebar:
            st.markdown("---")
            st.text("User: Karn Deb")
            st.text("Version: 0.0.1")
            st.button("Logout")
            st.markdown("---")


    view(Model())
