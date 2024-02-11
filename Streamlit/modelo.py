################ Librerias ################
import os
import streamlit as st
import numpy as np
import pandas as pd
from st_aggrid import AgGrid
import json

################ Funciones #################

from funciones.funciones_modelo import load_model, load_listas, data_transformer

############################################

def modelo():
    ############################################ CUERPO ############################################
    st.markdown("<h2 style='text-align: center; font-size: 50px;color: red; '>Predictor Salarial</h2>", unsafe_allow_html=True)


    st.markdown("En esta sección podrás tener una referencia de tu ``rango salarial`` seleccionando tus ``preferecias geográficas`` y ``experiencia profesional``.")
    st.markdown(body=""" EXPLICAR EL MODELO Y CON QUE DATOS SE HA CONSTRUIDO""")


    #################################################################################################


    # Rutas de acceso:
    ruta_listas = os.getcwd().replace("Streamlit", "Modelo_predictivo\listas\listas.json")
    ruta_encoders = os.getcwd().replace("Streamlit", "Modelo_predictivo\encoders\\")
    ruta_modelos = os.getcwd().replace("Streamlit", "Modelo_predictivo\\trained_models")

    # Cargo los datos:
    listas = load_listas(ruta_listas)

    comunidad = listas["comunidades"]
    categoria = listas["categorias"]
    experiencia = listas["experiencia"]
    herramientas = listas["herramientas"]
    jornada = listas["jornada"]
    contrato = listas["contrato"]
    beneficios = listas["beneficios"]

    # Selección de datos por el usuario:

    col1, col2 = st.columns([1, 1])
    comunidad_selected = None
    categoria_selected = None
    jornada_selected = None
    contrato_selected = None


    comunidad_selected = col1.selectbox(label   = "Comunidad autónoma",
                                        options = comunidad,
                                        index   = None)

    categoria_selected = col2.selectbox(label   = "Categoría",
                                        options = categoria,
                                        index   = None)

    jornada_selected = col1.selectbox(label   = "Tipo de jornada",
                                      options = jornada,
                                      index   = None)

    contrato_selected = col2.selectbox(label   = "Tipo de contrato",
                                       options = contrato,
                                       index   = None)

    experiencia_selected = st.slider(label     = "Experiencia laboral",
                                     min_value = int(min(experiencia)),
                                     max_value = int(max(experiencia)),
                                     step      = 1)

    herramientas_selected = st.multiselect(label   = "Herramientas",
                                           options = herramientas,
                                           default = None)



    beneficios_selected = st.slider(label= "Beneficios",
                                            min_value= min(beneficios),
                                            max_value= max(beneficios),
                                            step= 1)
    if (contrato_selected and comunidad_selected and categoria_selected and jornada) is not None:
        # Datos del usuario:
        X_datos = {"herramientas": [herramientas_selected],
                   "jornada": [jornada_selected],
                   "experiencia": [experiencia_selected],
                   "tipo_contrato": [contrato_selected],
                   "beneficios": [beneficios_selected],
                   "comunidad": [comunidad_selected],
                   "categoria_empleo": [categoria_selected]}
        df = pd.DataFrame(X_datos)
        X = df.copy()

        # Modelo:
        min_model, max_model = load_model(ruta_modelos)

        # Transformación de los datos:
        X_min, X_max = data_transformer(X, ruta_encoders, ruta_modelos)

        # Predicción

        if st.button("Predecir salario", type="primary"):

            salario_minimo_predicho = np.exp(min_model.predict(X_min))
            salario_maximo_predicho = np.exp(max_model.predict(X_max))

            # Muestra el mensaje de éxito centrado y con un tamaño de texto más grande
            st.success(f"El rango salarial con estas características es de {round(int(salario_minimo_predicho), -2)} a {round(int(salario_maximo_predicho), -2)} € brutos anuales.")



if __name__ == "__modelo__":
    modelo()



