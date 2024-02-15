################ Funciones #################
import streamlit

from funciones.funciones_eda import *

############################################
def compara():
    ################ DATOS #########################

    _, df, _, _, _, df_spider, df_spider_sin_ingles = load_data()

    ################################################
    st.title("Explora cada rincón del mercado Tech español")

    ################################################
    ############## HERRAMIENTAS ##################
    col1, col2 = st.columns((3,2))

    ###################### COLUMNA 2 ############### EXPLICACION
    col2.markdown(" PONER EXPLICACION")

    ###################### COLUMNA 1 ############### GRAFICO SPIDER
    if col1.toggle(label="Sin inglés"):
        df_spider = df_spider_sin_ingles

    eleccion = col1.multiselect(label="Herramientas",
                               options=df_spider["herramienta"],
                               default=None,
                               max_selections=3)



    # number of variables
    df_spider.columns = ['Administracion', 'Ciberseguridad', 'Data Driven', 'ML Engineer', 'Programador', 'Sistemas', "herramienta"]
    categories = df_spider.columns[:-1]
    N = len(categories)

    # Calculate angles
    angles = [(n / float(N) * 2 * pi) for n in range(N)]
    angles += angles[:1]

    # Create figure and axes (using Figure and add_subplot instead)
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'}, facecolor='#111111')

    # Set axis properties
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    plt.xticks(angles[:-1], categories, color="#FF7300", size= 20, ha="center")
    ax.set_xticks(angles[:-1])

    # Set y-axis labels and limits
    ax.set_rlabel_position(30)
    plt.yticks([0, 0.25, 0.5, 0.75, 1], ["0%","25%", "50%", "75%", "100%"], color="white", size=13)
    ax.grid(color="white")
    ax.set_facecolor("#111111")
    for spine in ax.spines.values():
        spine.set_edgecolor('white')
    plt.ylim(0, 1)

    # Loop through selected tools and plot
    for herramienta in eleccion:
        values = df_spider[df_spider["herramienta"] == herramienta].drop(['herramienta'], axis=1).values.flatten().tolist()
        values += values[:1]  # Close the plot
        label = herramienta  # Use ferramenta directly for label
        ax.plot(angles, values, linewidth=4, linestyle='solid')
        ax.fill(angles, values, alpha=0.3, label=label)  # Use viridis colormap for better distinction

    # Add legend
    plt.legend(bbox_to_anchor=(1.4, 1.08), fontsize= 16, facecolor= "#111111", edgecolor= "white", labelcolor="#FF7300")
    # Show the graph with fig instead of ax
    col1.pyplot(fig)
