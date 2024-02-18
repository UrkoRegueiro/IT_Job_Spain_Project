
################ Funciones #################

from funciones.funciones_eda import *

############################################

def tech_app():
    st.markdown("""
        <style>
        .big-font {
            font-size:20px;
        }
        </style>
        """, unsafe_allow_html=True)
    ################ DATOS #########################
    geo_spain, _, _, _, _, _, _, _, _, _,_ = load_data()
    ################################################

    ################ TITULO ########################
    st.markdown("<h1 style='text-align: center;color: orange; font-size: 3em;'>Un viaje por el mercado Tech español</h1>", unsafe_allow_html=True)

    st.markdown('' '<p class="big-font">'
                'Bienvenidos a la web donde podrás descubrir y sumergirte en el mercado tech, partiendo desde lo general hasta sus particularidades.'
                ''
                '</p>''', unsafe_allow_html=True)


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
        coverage=2,
        radius=3000,
    )

    width = st.sidebar.slider("plot width", 100, 1000, 10)
    height = st.sidebar.slider("plot height", 100, 1000, 10)
    # Configurar la vista del mapa
    view_state = pdk.ViewState(
        longitude=-4,
        latitude=41,
        zoom=1,
        min_zoom=4,
        max_zoom=7,
        pitch=25,
        bearing=-10, height=420)

    st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))
    ################################################



if __name__ == "__tech_app__":
    tech_app()
