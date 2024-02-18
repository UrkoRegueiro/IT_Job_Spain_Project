################ Librerias ################
import os
import pandas as pd
import numpy as np
import streamlit as st
import folium
import circlify
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pydeck as pdk
import plotly.figure_factory as ff
import geopandas as gpd
import re
from unidecode import unidecode
import json
from streamlit_folium import folium_static
import plotly.express as px
import plotly.graph_objs as go
import math
from math import pi
from plotly.subplots import make_subplots
import joypy
############################################################################################################
#################################### Función de carga de datos #############################################

@st.cache_data
def load_data():
    ruta_datos = os.getcwd().replace("Streamlit", "Datos\\Procesados\\")
    geo_spain = pd.read_csv(ruta_datos + 'coordenadas_empleos.csv')
    df = pd.read_csv(ruta_datos + "datos_jobs_finales.csv")
    df_comunidades = pd.read_csv(ruta_datos + 'comunidades_esp.csv')
    df_herramientas = pd.read_csv(ruta_datos + 'data_herramientas.csv')
    df_spider = pd.read_csv(ruta_datos + 'df_spider.csv')
    df_spider_sin_ingles = pd.read_csv(ruta_datos + 'df_spider_sin_ingles.csv')
    with open(ruta_datos + "provincias_esp_choro.geojson", 'r') as archivo:
        provincias_geojson = json.load(archivo)

    df_salarios = pd.read_csv(ruta_datos + 'salarios_comparacion.csv')
    df_salario_medio = pd.read_csv(ruta_datos + 'salario_medio_comunidades.csv')
    df_stack = pd.read_csv(ruta_datos + 'stack_tecnologico.csv')
    df_grafico = pd.read_csv(ruta_datos + 'df_grafico.csv')
    return geo_spain, df, df_comunidades, df_herramientas, provincias_geojson, df_spider, df_spider_sin_ingles, df_salarios, df_salario_medio, df_stack, df_grafico


############################################################################################################
def metodo_tukey(df, columna, alfa):
    q1 = df[columna].quantile(0.25)
    q3 = df[columna].quantile(0.75)
    riq = q3 - q1

    df = df[df[columna].between(q1 - alfa * riq, q3 + alfa * riq) | (df[columna].isna())]

    return df

def intervalo_experiencia(experiencia):
    if experiencia <= 1:
        return 'Junior'
    elif experiencia <= 4:
        return 'Mid'
    elif experiencia <= 7:
        return 'Senior'
    elif experiencia <= 10:
        return 'Lead'
    return np.nan