
################ Funciones #################
import streamlit

from funciones.funciones_modelo import *

############################################

def modelo():
    ############################################ CUERPO ############################################
    st.markdown("<h2 style='text-align: center; font-size: 60px;color: orange; '>Predictor Salarial</h2>", unsafe_allow_html=True)

    st.markdown("""
    <style>
    .big-font {
        font-size:20px;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown("""
        <style>
        .center-font {
            font-size:25px;
            color: orange;
            text-align: center;
        }
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">Una de las preguntas más frecuentes que podemos hacernos a la hora de aplicar a una oferta laboral es la siguiente:</p>', unsafe_allow_html=True)
    st.markdown('<p class="center-font">¿Cuál es el rango salarial que puedo negociar?</p>', unsafe_allow_html=True)
    st.markdown('<p class="big-font">Es por ello que ponemos a tu disposición una herramienta que ofrece una estimación del rango salarial bruto anual en base a tus habilidades y preferencias. Esta herramienta está construida sobre dos modelo de machine learning entrenados con nuestra base de datos de empleos en España, más en concreto se trata de dos SVR(Suport Vector Regressor), cada uno entrenado para predecir el salario mínimo y máximo respectivamente.</p>', unsafe_allow_html=True)
    st.markdown('<p class="big-font">Presentados a los protagonistas, pongámoslos a trabajar.</p>', unsafe_allow_html=True)
    st.markdown('<p class="big-font">A continuación deberás elegir las opciones que se presentan y presionar el botón de predicción, obteniendo tu rango salarial estimado.</p>', unsafe_allow_html=True)

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

    col1, col2 = st.columns([1, 1], gap="large")
    comunidad_selected = None
    categoria_selected = None
    jornada_selected = None
    contrato_selected = None
    beneficios_selected = 0


    comunidad_selected = col1.selectbox(label   = "Comunidad autónoma",
                                        options = comunidad,
                                        index   = None)

    st.markdown("")
    st.markdown("")

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

    st.markdown("")
    st.markdown("")

    col_1, col_2 = st.columns((3.2,1), gap="large")

    herramientas_selected = col_1.multiselect(label   = "Herramientas",
                                           options = herramientas,
                                           default = None,
                                           max_selections=5)

    st.markdown("")
    st.markdown("")
    col_2.markdown("")
    col_2.markdown("")
    if col_2.toggle(label="Con beneficios"):

        beneficios_selected = 1

    #beneficios_selected = (st.selectbox("Beneficios", options=["Sin beneficios", "Con beneficios"], key= "botton_bool"))

    if (contrato_selected and comunidad_selected and categoria_selected and jornada and beneficios_selected) is not None:
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
        min_model, max_model = load_model()

        # Transformación de los datos:
        X_min, X_max = data_transformer(X, ruta_encoders, ruta_modelos)

        st.markdown("")
        st.markdown("")
        st.markdown("")

        col_1, col_2, col_3, col_4, col_5 = st.columns(5)

        with col_1:
            pass
        with col_2:
            pass
        with col_4:
            pass
        with col_5:
            pass
        with col_3:
            boton_predecir = st.button("Predecir salario", type="primary")

        # Predicción

        if boton_predecir:
            salario_minimo_predicho = np.exp(min_model.predict(X_min))
            salario_maximo_predicho = np.exp(max_model.predict(X_max))

            st.markdown("""
                    <style>
                    .resultado {
                        font-size:25px;
                        color: #FAFAFA;
                        text-align: center;
                        background-color: #00bde0;
                        padding: 10px;
                        border-radius: 10px;
                    }
                    </style>
                    """, unsafe_allow_html=True)
            st.markdown(f'<p class="resultado">El rango salarial con estas características es de {round(int(salario_minimo_predicho), -2)} a {round(int(salario_maximo_predicho), -2)} € brutos anuales.</p>', unsafe_allow_html=True)

            st.link_button("Aqui tienes una lista de empleos en ese rango salarial.", "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")

if __name__ == "__modelo__":
    modelo()


