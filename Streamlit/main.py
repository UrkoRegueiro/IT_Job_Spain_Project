
################ Librerias ################

from streamlit_option_menu import option_menu

################ Funciones #################
from funciones.config import PAGE_CONFIG
from tech_job_app import *
from eda import eda
from modelo import modelo
from comparador import compara
from acercade import info

############################################
st.set_page_config(**PAGE_CONFIG)

page_gb_img = """
<style>
[data-testid="stSidebar"] {
background-image: url("https://evelazco.com/wp-content/uploads/2024/02/bg45-jpg.webp");
background-size: cover;
}

[data-testid="stAppViewBlockContainer"] {
background-color: #111111;
}

[data-testid="stHeader"] {
background-color: #202020;
}




</style>


"""
st.markdown(page_gb_img, unsafe_allow_html=True)



def main():


    menu = ["Inicio", "Una visión general", "Explora el mercado", "Predictor Salarial", "Acerca de"]
    default_index = 0

    # Crea el menú
    with st.sidebar:
        selected_option = option_menu("Menu", menu,
    icons=['rocket-takeoff', 'bar-chart-line-fill', "search-heart","robot", 'heart-fill'],
    menu_icon="house", default_index=0, orientation="vertical",
    styles={
        "menu": {"background": "transparent!important"},
        "container": {"padding": "0!important", "background-color": "#39393D", "border-radius":"20px"},
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "rgba(110,110,110,1.00)"},
        "nav-link-selected": {"background-color": "rgba(110,110,110,1.00)"},
        "menu-title": {"padding-top": ".5rem !important"}
    })



    if selected_option == "Inicio":

        tech_app()

        pass

    elif selected_option == "Una visión general":

        eda()

        pass

    elif selected_option == "Explora el mercado":

        compara()

        pass

    elif selected_option == "Predictor Salarial":

        modelo()

        pass

    else:

        info()

        pass


if __name__ == "__main__":
    main()
