################ Librerias ################

import streamlit as st
import numpy as np
import pandas as pd
################ Funciones #################


############################################

def tech_app():
    st.title(body="Applica Tech")

    st.subheader(body="Inicio")

    st.write("Bienvenidos a la web donde podrás explorar el mercado laboral tech español.")

    st.markdown("""The data for this project comes from the following website: 
                    [Open Canada](https://open.canada.ca/data/en/dataset/98f1a129-f628-4ce4-b24d-6f16bf24dd64).""")

    # Cuando pongo las comillas se pone el texto en verde
    st.write("""To use this app just go to the `Exploratory Data Analysis` section to know more about the data that we used to build
                the Machine Learning models.""")

    st.write(
        """To use the `Machine Learning Model` section you can either use the sliders in the sidebar or upload you own CSV file.""")

    #df = read_data()

    st.warning(""" CARGAR LOS DATOS PARA HACER UN MAPA DE RELIEVE """)

    st.write(
        """poner mapa y explicación""")


if __name__ == "__tech_app__":
    tech_app()
