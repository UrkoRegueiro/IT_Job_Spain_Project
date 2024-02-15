
################ Funciones #################

from funciones.funciones_eda import *

############################################


def tech_app():

    ################ DATOS #########################
    geo_spain, _, _, _, _, _, _ = load_data()
    ################################################

    ################ TITULO ########################
    st.markdown("<h1 style='text-align: center; font-size: 3em;'>Applica Tech</h1>", unsafe_allow_html=True)
    ################################################

    ################ GRÁFICO #######################

    layer = pdk.Layer(
        "HexagonLayer",
        geo_spain,
        get_position=["lng", "lat"],
        auto_highlight=True,
        elevation_scale=5000,
        pickable=True,
        elevation_range=[0, 1000],
        extruded=True,
        coverage=1,
        radius=3000,
    )

    # Configurar la vista del mapa
    view_state = pdk.ViewState(
        longitude=-1.979444,
        latitude=40.223611,
        zoom=1,
        min_zoom=5,
        max_zoom=7,
        pitch=40,
        bearing=-10)

    st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))
    ################################################

    ########## INTRODUCCIÓN ########################
    st.subheader(body="Inicio")

    st.write("Bienvenidos a la web donde podrás explorar el mercado laboral tech español.")

    st.markdown("""The data for this project comes from the following website: 
                    [Open Canada](https://open.canada.ca/data/en/dataset/98f1a129-f628-4ce4-b24d-6f16bf24dd64).""")

    # Cuando pongo las comillas se pone el texto en verde
    st.write("""To use this app just go to the `Exploratory Data Analysis` section to know more about the data that we used to build
                the Machine Learning models.""")

    st.write(
        """To use the `Machine Learning Model` section you can either use the sliders in the sidebar or upload you own CSV file.""")

    st.warning(""" CARGAR LOS DATOS PARA HACER UN MAPA DE RELIEVE """)

    st.write("""poner mapa y explicación""")
    ################################################




if __name__ == "__tech_app__":
    tech_app()
