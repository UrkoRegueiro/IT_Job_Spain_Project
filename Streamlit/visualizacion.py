import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

def generate_map(df_filtered):
    mapa = folium.Map(location=[df_filtered['latitud'].mean(), df_filtered['longitud'].mean()], zoom_start=4)

    for i, row in df_filtered.iterrows():
        folium.Marker(location=[row['latitud'], row['longitud']], popup=row['titulo']).add_to(mapa)
    return mapa

def main():
    st.title("Mapa de Trabajos")

    df = pd.read_csv("C:/Users/Adri1/OneDrive/Documentos/Bootcamp/Proyects/Jobs/Limpieza/datos_trabajos_ubicaciones.csv")

    df = df.dropna(subset=['provincia'])
    # Crear widgets para filtrar
    provincia = df['provincia'].unique()


    selected_provincia = st.selectbox("Selecciona Provincia", provincia)

    # Filtrar el DataFrame
    df_filtered = df[(df['provincia'] == selected_provincia)]

    folium_map = generate_map(df_filtered)
    folium_static(folium_map)

if __name__ == "__main__":
    main()
