################ Librerias ################
import os
import pandas as pd
import numpy as np
import pickle
import json
from joblib import dump, load
import sklearn
############################################################################################################
#################################### Función de carga de datos #############################################
def read_data(ruta):
    df = pd.read_csv(filepath_or_buffer=ruta)

    return df
############################################################################################################
#################################### Función de carga de modelos ###########################################
def load_model(ruta):

    min_model = load(ruta + '\min_model.pkl')
    max_model = load(ruta + '\max_model.pkl')

    return min_model, max_model
############################################################################################################
#################################### Función de carga de lista de datos ####################################
def load_listas(ruta):

    with open(ruta, 'r') as f:
        lista_datos = json.load(f)

    return lista_datos
############################################################################################################
#################################### Función de procesamiento de datos:#####################################
def data_transformer(X, ruta_encoders, ruta_modelos):

    # Cargo encoders
    encoders = [archivo for archivo in os.listdir(ruta_encoders) if archivo.endswith('.pickle')]

    encoders_cargados = {}
    for encoder in encoders:
        ruta_encoder = os.path.join(ruta_encoders, encoder)

        with open(ruta_encoder, 'rb') as file:
            encoders_cargados[encoder] = pickle.load(file)

    # Encoding a las columnas
    encoded_columns = ["jornada", "tipo_contrato", "comunidad", "categoria_empleo", "herramientas"]

    for columna, encoder in zip(encoded_columns, encoders_cargados.values()):

        if columna == "herramientas":
            data_encoded = encoder.transform(X[columna])
            df_encoded = pd.DataFrame(data_encoded, columns=encoder.classes_)
            X = pd.concat([X, df_encoded], axis=1).drop([columna], axis=1)

        else:
            data_encoded = encoder.transform(X[[columna]]).toarray()
            df_encoded = pd.DataFrame(data_encoded, columns=encoder.categories_)
            X = pd.concat([X, df_encoded], axis=1).drop([columna], axis=1)

    # Limpio nombre columnas
    X.columns = [str(columna).replace("('", "").replace("',)", "") for columna in X.columns]

    # Transformación PCA
    with open(ruta_modelos + "\\pca_min.pickle", 'rb') as file:
        pca_min = pickle.load(file)

    with open(ruta_modelos + "\\pca_max.pickle", 'rb') as file:
        pca_max = pickle.load(file)

    X_pca_min = pca_min.transform(X)
    X_pca_max = pca_max.transform(X)

    return X_pca_min, X_pca_max
############################################################################################################