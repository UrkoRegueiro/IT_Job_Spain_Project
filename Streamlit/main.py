################ Librerias ################

import streamlit as st
import pandas as pd
import os

################ Funciones #################
from funciones.config import PAGE_CONFIG

from tech_job_app import tech_app
from eda import eda
from modelo import modelo

############################################
st.set_page_config(**PAGE_CONFIG)
def main():

    menu = ["Inicio", "Explora el mercado", "Predictor Salarial", "Acerca de"]

    # Mostrar el menú en la barra lateral
    st.sidebar.markdown("<h1 style='text-align: center; font-size: 2em;'>Menu</h1>", unsafe_allow_html=True)

    page = st.sidebar.selectbox(label="", options= menu)

    if page == "Inicio":

        tech_app()

        pass

    elif page == "Explora el mercado":

        eda()

        pass

    elif page == "Predictor Salarial":

        modelo()

        pass

    else:

        #info()

        pass


if __name__ == "__main__":
    main()