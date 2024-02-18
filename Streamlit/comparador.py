################ Funciones #################
import streamlit

from funciones.funciones_eda import *

############################################

def compara():
    st.markdown("""
            <style>
            .big-font {
                font-size:20px;

            }
            .sub-font {
                font-size:22px;
                color: #FAA227;
                font-weight: bold;                    

            }
            .center-font {
                    font-size:25px;
                    color: #FAA227;
                    text-align: center;
                }
            </style>
            """, unsafe_allow_html=True)

                                    ##################### DATOS ####################

    _, df, _, df_herramientas, _, df_spider, df_spider_sin_ingles, df_salarios, df_salario_medio, df_stack, _ = load_data()

                                    ################################################

    ####################################################  INTRODUCCIÓN ##########################################################################

    st.markdown("<h2 style='text-align: center; font-size: 60px;color: orange; '>Investiga cada rincón del mercado Tech español</h2>", unsafe_allow_html=True)

    st.markdown(
        '<p class="sub-font">¿Te has preguntado cuál es la situación actual de los empleos en el sector tecnológico español?<br></p>'
        '<p class="big-font">Reconocemos que las carreras en tecnología están entre las mejor remuneradas y con mejor biestar laboral, pero surge la duda sobre qué salario esperar cuando buscamos un empleo, ya sea tras graduarse o por una transición laboral. Aún más desafiante puede ser determinar qué habilidades específicas se requieren para destacar en este sector, y no digamos encontrar en qué empresa pueden encajar nuestros ideales.</p>'
        '<p class="big-font">En nuestra búsqueda por despejar estas dudas, hemos recopilado información de los principales portales de empleo, analizándola para ayudarte a entender mejor el mercado tech en España. A continuación, te presentamos nuestros hallazgos para que estés un paso por delante en tu búsqueda de empleo.</p>',
        unsafe_allow_html=True)

    ################################################################## TABS ######################################################################

    tab1, tab2, tab3 = st.tabs([":orange[Un vistazo al Stack Tecnológico]", ":orange[Salario por comunidad]", ":orange[Rangos]"])

    ###################################################### APARTADO STACK TECNOLOGICO ######################################################
    with (tab1):

        columna_texto_1, columna_funnel_sun,  = st.columns((1, 2))

        with columna_texto_1:
            st.header(":orange[_Salario y Modalidad_]", divider="orange")
            st.markdown(
                '<p class="big-font">Lorem ipsum dolLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>',
                unsafe_allow_html=True)

        with columna_funnel_sun:
            ############################################################
            ###################### GRAFICO FUNNEL ######################
            color_funnel = {"Salario Minimo": "#66B78D", "Salario Maximo": "#FFBD45"}

            salarios_comp = px.funnel(df_salarios,
                                      x='salario',
                                      y='categoria_empleo',
                                      color="tipo",
                                      color_discrete_map=color_funnel)

            salarios_comp.update_traces(texttemplate="%{value:,d} €")
            salarios_comp.update_layout(paper_bgcolor='rgb(17,17,17)',
                                        plot_bgcolor='rgb(17,17,17)',
                                        yaxis_title="",
                                        font=dict(family="Courier New, monospace", size=42, color="#000000"),
                                        legend=dict(x=0.95, y= 0.5, font=dict(size=20)),
                                        width = 850,
                                        height = 340,
                                        margin = dict(l=0, r=0, t=80, b=0))
            st.plotly_chart(salarios_comp)

            ############################################################
            ###################### GRAFICO PRESENCIALIDAD ##############
            color_sunburst = {"presencial": '#C4E6C3', "hibrido": '#66B78D', "remoto": '#2A7271'}
            # "#C4E6C3" "#66B78D"  # 2A7271"

            mask_presencialidad = (df["presencialidad"] != "no especificado") & (df["categoria_empleo"] != "otros")
            df_presencialidad = df[mask_presencialidad].groupby(by="presencialidad")[
                "categoria_empleo"].value_counts().reset_index()

            grafico_presencialidad = px.sunburst(df_presencialidad,
                                                 path=['presencialidad', 'categoria_empleo'],
                                                 values='count',
                                                 color="presencialidad",
                                                 color_discrete_map=color_sunburst)
            grafico_presencialidad.update_layout(paper_bgcolor='rgb(17,17,17)',
                                                 plot_bgcolor='rgb(17,17,17)',
                                                 font=dict(family="Courier New, monospace", size=18, color="#000000"),
                                                 width = 550,
                                                 height = 300,
                                                 margin = dict(l=240, r=0, t=0, b=0))

            st.plotly_chart(grafico_presencialidad)

        ############################################################################################################
        st.divider()
        ############################################################################################################

        st.header(":orange[_Stack Tecnológico_]", divider="orange")
        st.markdown(
            '<p class="big-font">Lorem ipsum dolLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>',
            unsafe_allow_html=True)

        herr_1, herr_2, herr_3 = st.columns((0.1, 1, 4))
        herr_2.markdown(" ")
        boton_ingles = herr_2.toggle(label=":orange[Sin Inglés]", help="El filtrado se aplicará a toda la página.")
        herr_2.markdown(" ")
        herr_2.markdown(" ")
        herr_2.markdown(" ")
        herr_2.markdown(" ")

        categorias = df_stack.columns[1:]

        boton = herr_2.radio("Escoge la categoría", categorias)

        if boton:
            if boton_ingles:
                mask_ingles = (df_stack["herramienta"] != "ingles")
                df_stack = df_stack[mask_ingles]

            df_categoria = df_stack[[boton, "herramienta"]].sort_values(by=boton, ascending=False).head(20)

            grafico_stack = go.Figure(data=[go.Bar(
                x=df_categoria['herramienta'], y=df_categoria[boton],
                text=df_categoria['herramienta'],
                textposition='auto',
                marker={"color": list(range(0, len(df_categoria['herramienta']))), 'colorscale': 'blugrn'})])

            grafico_stack.update_layout(barmode='stack', xaxis_type='category', xaxis_tickvals=[0],
                                        xaxis_ticktext=[" "],
                                        #yaxis_ticklabel=
                                        title=f'<b></b><b>Stack tecnológico de {boton}</b>',
                                        paper_bgcolor='rgb(17,17,17)',
                                        plot_bgcolor='rgb(17,17,17)',
                                        font=dict(family="Courier New, monospace", size=40, color="#000000"),
                                        width=1000, height=400, margin=dict(l=0, r=0, t=70, b=0),
                                        autosize=True)
            herr_3.plotly_chart(grafico_stack)

        ################### GRAFICO SPIDER ##########################
        #############################################################
        columna_texto_2, columna_spider = st.columns((1, 2))
        with columna_texto_2:
            st.header(":orange[_Compara herramientas_]", divider="orange")
            st.markdown(
                '<p class="big-font">Lorem ipsum dolLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>',
                unsafe_allow_html=True)

        with columna_spider:



            if boton_ingles:
                df_spider = df_spider_sin_ingles

            eleccion = st.multiselect(label="",
                                       options=df_spider["herramienta"],
                                       default=None,
                                       max_selections=3)

            spider_izq, spider_drch = st.columns((1, 4))

            categories = df_spider.columns[:-1]
            N = len(categories)

            # Ángulos
            angles = [(n / float(N) * 2 * pi) for n in range(N)]
            angles += angles[:1]

            spider, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': 'polar'}, facecolor='#111111')

            ax.set_theta_offset(pi / 2)
            ax.set_theta_direction(-1)
            plt.xticks(angles[:-1], categories, color="#FF7300", size= 20, ha="center")
            ax.set_xticks(angles[:-1])

            ax.set_rlabel_position(-30)
            plt.yticks([0, 0.25, 0.5, 0.75, 1], ["0%","25%", "50%", "75%", "100%"], color="white", size=18, va="bottom", ha="right")
            ax.grid(color="white")
            ax.set_facecolor("#111111")
            for spine in ax.spines.values():
                spine.set_edgecolor('white')
            plt.ylim(0, 1)

            for herramienta in eleccion:
                values = df_spider[df_spider["herramienta"] == herramienta].drop(['herramienta'], axis=1).values.flatten().tolist()
                values += values[:1]  # Close the plot
                label = herramienta  # Use ferramenta directly for label
                ax.plot(angles, values, linewidth=4, linestyle='solid')
                ax.fill(angles, values, alpha=0.3, label=label)  # Use viridis colormap for better distinction

            plt.legend(bbox_to_anchor=(1.31, 1.05), fontsize= 15, facecolor= "#111111", edgecolor= "white", labelcolor="#FF7300")
            spider_drch.pyplot(spider)

    ###################################################### APARTADO GEOGRAFIA ######################################################
    with tab2:
        st.header(":orange[_Salarios_]", divider="orange")
        st.markdown(
            '<p class="big-font">Lorem ipsum dolLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>',
            unsafe_allow_html=True)


        ################### GRAFICO SALARIO MEDIO ###################
        #############################################################
        izq, centro, drcha = st.columns((2, 1.5, 2))
        st.info(":red[Notar:] En algunas comunidades la falta de datos provoca que la distribución de densidad no se ajuste correctamente.")
        columna_salario, columna_indicador = st.columns((4, 2))

        comunidades = ["", ""]
        valores = [0, 0]

        eleccion_comunidad = centro.multiselect(label="Comunidades Autónomas",
                                              options=df_salario_medio["comunidad"],
                                              default=["Cataluña", "Comunidad de Madrid"],
                                              max_selections=2)




        with columna_salario:

            ################### GRAFICO COMPARADOR ###################
            ##########################################################
            df_salario_comunidad = df[df["pais"] == "España"][["comunidad", "salario_min", "salario_max"]].dropna()
            df_salario_comunidad = metodo_tukey(df_salario_comunidad, "salario_min", 1.5)
            df_salario_comunidad = metodo_tukey(df_salario_comunidad, "salario_max", 1.5)
            df_salario_comunidad["salario_medio"] = (df_salario_comunidad["salario_min"] + df_salario_comunidad["salario_max"]) / 2
            max_salario = int(df_salario_comunidad["salario_medio"].max()) + 1000
            min_salario = int(df_salario_comunidad["salario_medio"].min()) - 900


            if len(eleccion_comunidad) >= 1:
                comunidades[0] = eleccion_comunidad[0]
                valores[0] = df_salario_medio[df_salario_medio["comunidad"] == comunidades[0]]["salario_medio"].values[0]
                if len(eleccion_comunidad) > 1:
                    comunidades[1] = eleccion_comunidad[1]
                    valores[1] = df_salario_medio[df_salario_medio["comunidad"] == comunidades[1]]["salario_medio"].values[0]


                mascara = df_salario_comunidad["comunidad"].isin(comunidades)
                grafico_comunidades, ax = plt.subplots(figsize=(12, 6), facecolor='#111111')
                sns.kdeplot(data=df_salario_comunidad[mascara],
                            x="salario_medio",
                            hue='comunidad',
                            fill=True,
                            common_norm=False,
                            palette="viridis",
                            cut= 0,
                            ax=ax)

                ax.set_xlabel('Salario Medio', color='orange', fontsize= 15)
                plt.xticks([i for i in range(min_salario, max_salario, 5000)], rotation=45)
                ax.set_ylabel('Densidad', color='orange', fontsize= 15)
                #ax.set_xlim(left= 0)
                plt.legend(comunidades, loc='best', fontsize=10, labelcolor="white", facecolor='#111111')
                grafico_comunidades.set_facecolor('#111111')
                ax.set_facecolor('#111111')
                ax.spines['bottom'].set_color('white')
                ax.spines['top'].set_color('white')
                ax.spines['right'].set_color('white')
                ax.spines['left'].set_color('white')
                ax.tick_params(axis='x', colors='white')
                ax.tick_params(axis='y', colors='#111111')
                st.pyplot(grafico_comunidades)


        with columna_indicador:

            trace1 = go.Indicator(mode="gauge+number",
                                  gauge={'axis': {'range': [0, 50000]}},
                                  value=valores[0],
                                  title={'text': f"Salario Medio {comunidades[0]}", "font":{"color":"orange"}})

            trace2 = go.Indicator(mode="gauge+number",
                                  gauge={'axis': {'range': [0, 50000]}},
                                  value=valores[1],
                                  title={'text': f"Salario Medio {comunidades[1]}", "font":{"color":"orange"}})

            comparacion_comunidades = make_subplots(rows=2,
                                                    cols=1,
                                                    specs=[[{'type': 'indicator'}], [{'type': 'indicator'}]],
                                                    vertical_spacing=0.2)

            comparacion_comunidades.append_trace(trace1, row=1, col=1)
            comparacion_comunidades.append_trace(trace2, row=2, col=1)
            comparacion_comunidades.update_layout(paper_bgcolor='rgb(17,17,17)',
                                                  plot_bgcolor='rgb(17,17,17)',
                                                  margin=dict(l=0, r=0, t=50, b=10),
                                                  width=480, height=440)

            st.plotly_chart(comparacion_comunidades)


    ###################################################### APARTADO RANK ######################################################
    with tab3:

        columna_texto_3, columna_salario_rango = st.columns((1, 2))

        with columna_texto_3:
            st.header(":orange[_Salario_]", divider="orange")
            st.markdown(
                '<p class="big-font">Lorem ipsum dolLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>',
                unsafe_allow_html=True)

        with columna_salario_rango:

            ############## GRAFICO SALARIO-RANGO #####################
            ##########################################################
            df["rango"] = df["experiencia"].apply(intervalo_experiencia)
            df_rango_salario = df.groupby(by="rango")[["salario_min", "salario_max"]].mean().reset_index()
            df_rango_salario["salario_medio"] = (df_rango_salario["salario_min"] + df_rango_salario["salario_max"]) / 2
            for col in df_rango_salario.columns[1:]:
                df_rango_salario[col] = df_rango_salario[col].apply(lambda x: int(x))

            rango_salario = go.Figure(
                go.Bar(x=df_rango_salario["rango"], y=df_rango_salario["salario_min"], name='Salario Mínimo', marker=dict(color="#66B78D")))
            rango_salario.add_trace(
                go.Bar(x=df_rango_salario["rango"], y=df_rango_salario["salario_medio"], name='Salario Medio', marker=dict(color="#B3BA68")))
            rango_salario.add_trace(
                go.Bar(x=df_rango_salario["rango"], y=df_rango_salario["salario_max"], name='Salario Máximo', marker=dict(color="#FFBD45")))
            rango_salario.update_layout(barmode='group',
                                        xaxis={'categoryorder': 'total ascending'},
                                        font=dict(family="Courier New, monospace", size=20, color="#000000"),
                                        legend=dict(x=0, y=1, font=dict(size=20)),
                                        width=770,
                                        height=470,
                                        margin=dict(l=200, r=0, t=80, b=0),
                                        paper_bgcolor='rgb(17,17,17)',
                                        plot_bgcolor='rgb(17,17,17)')

            st.plotly_chart(rango_salario)

        ############################################################################################################
        st.divider()
        ############################################################################################################

        columna_modalidad_rango, columna_texto_4  = st.columns((3, 2))

        with columna_texto_4:
            st.header(":orange[_Modalidad_]", divider="orange")
            st.markdown(
                '<p class="big-font">Lorem ipsum dolLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempur adipiscing elit, sed do eiusmod tempLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>',
                unsafe_allow_html=True)

        with columna_modalidad_rango:

            ############## GRAFICO PRESENCIALIDAD-RANGO ##############
            ##########################################################
            df_rango_presencialidad = df[df["presencialidad"] != "no especificado"].groupby(by="rango")["presencialidad"].value_counts(normalize=True).reset_index()
            df_rango_presencialidad = df_rango_presencialidad.pivot_table(index="rango", columns="presencialidad",values="proportion").reset_index()
            for col in df_rango_presencialidad.columns[1:]:
                df_rango_presencialidad[col] = round(df_rango_presencialidad[col] * 100)
            df_rango_presencialidad = df_rango_presencialidad.sort_values(by="remoto")

            presencialidad_rango = go.Figure(
                data=[go.Bar(x=df_rango_presencialidad.rango, y=df_rango_presencialidad.presencial, name="Presencial", text=df_rango_presencialidad.presencial, marker_color="#C4E6C3"),
                      go.Bar(x=df_rango_presencialidad.rango, y=df_rango_presencialidad.hibrido, name="Hibrido", text=df_rango_presencialidad.hibrido, marker_color="#66B78D"),
                      go.Bar(x=df_rango_presencialidad.rango, y=df_rango_presencialidad.remoto, name="Remoto", text=df_rango_presencialidad.remoto, marker_color="#2A7271")])

            presencialidad_rango.update_layout(xaxis_type='category',
                              paper_bgcolor='rgb(17,17,17)',
                              plot_bgcolor='rgb(17,17,17)',
                              legend=dict(x=0, y=1, font=dict(size=20)),
                              font=dict(family="Courier New, monospace", size=20, color="#000000"),
                              width=760,
                              height=490,
                              margin=dict(l=0, r=50, t=85, b=0),
                              autosize=True
                              )

            st.plotly_chart(presencialidad_rango)

            #width = st.sidebar.slider("plot width", 100, 1000, 10)
            #height = st.sidebar.slider("plot height", 100, 1000, 10)

