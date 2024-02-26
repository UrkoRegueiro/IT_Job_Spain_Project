<div align="center">

# Un viaje por el mercado Tech español.
  
</div>

<div align="center">

  <img src="https://github.com/UrkoRegueiro/IT_Job_Spain_Project/blob/main/Datos/Procesados/divider.png" alt="IT_Jobs" width="100%">
  
</div>

## Tecnologías usadas

**Lenguaje:** Python.

**Librerias:** numpy, regex, pandas, matplotlib, seaborn, plotly, tensorflow, sklearn, xgboost, streamlit

------------

## 1. **Introducción**

Este proyecto es el resultado del trabajo en equipo llevado a cabo por Adrián Moldes, Eduardo Velazco, Esteban Pérez y Urko Regueiro como proyecto final del bootcamp de Data Science e Inteligencia Artificial de la escuela HACKABOSS.
La idea de realizar un estudio pormenorizado del mercado laboral tecnólogico en España surge de nuestro propio interés en podernos incorporar a él, entendiendo al menos de forma general cuáles son las necesidades actuales y reales de las empresas que requieren este tipo de perfiles. Para conseguir nuestro objetivo, hemos llevado a cabo la tarea de extraer, transformar, cargar y analizar datos de los portales de empleo más utilizados con el objetivo de conseguir información valiosa y detallada, obteniendo una primera muestra de más de 18000 datos que seguiremos ampliando y actualizando.

Los resultados obtenidos se han presentado en la web [Applicatech](https://applicatech.streamlit.app/) donde organizamos nuestros hallazgos en tres secciones:

- <u>**Una visión general**</u>:<br> En esta sección hemos querido proporcionar una panorámica completa de la situación del mercado tecnológico español. Desde la demanda de empleos por sector hasta las habilidades más demandadas. Reconocemos la importancia de comprender las tendencias generales antes de sumergirse en detalles más específicos.
  
- <u>**Explora el mercado**</u>:<br> Aquí brindamos la posibilidad de personalizar tu exploración, pudiendo descubrir qué stack tecnológico se adapta mejor a cada sector o entender la distribución salarial por comunidad autónoma a través de gráficos interactivos. Creemos que esta personalización permitirá obtener información precisa y relevante para saciar tu curiosidad.
  
- <u>**Predictor Salarial**</u>:<br> En esta parte hemos diseñado una herramienta montada sobre dos modelos de Machine Learning que te permitirán, especificando ciertos parámetros, obtener un rango salarial estimado ajustado a tus características.

Queremos destacar que este proyecto no solo es una iniciativa informativa, sino también un testimonio de nuestro aprendizaje en el mundo de la ciencia de datos e inteligencia artificial. Este sitio web es el producto de un esfuerzo colaborativo de nuestro talentoso equipo, y queremos compartir contigo los frutos de nuestro trabajo. Podrás explorar más a fondo el proceso ETL y el código detrás de esta plataforma en las siguientes secciones.

## 2. **Extracción, Transformación y Carga de datos**<br>

El proceso de extracción puede encontrarse en la carpeta [Scrapers](https://github.com/UrkoRegueiro/IT_Job_Spain_Project/tree/main/Codigo/Scrapers). Aquí se pone a disposición el código que ha hecho posible la obtención de todos nuestros datos.

A su vez el código del proceso de transformación y limpieza de datos lo encontramos diponible en la carpeta [Limpieza](https://github.com/UrkoRegueiro/IT_Job_Spain_Project/tree/main/Codigo/Limpieza)

## 3. **Análisis Exploratorio de Datos**<br>

Este análisis puede encontrarse en la carpeta [EDA](https://github.com/UrkoRegueiro/IT_Job_Spain_Project/tree/main/Codigo/EDA). Aquí se podrá explorar más a fondo todas las relaciones encontradas en nuestros datos. Debido al gran tamaño del notebook es necesario su descarga para su visualización.

## 4. **Modelización**<br>

En esta sección ponemos a tu disposición el código implementado para los modelos de machine learning entrenados con nuestra base de datos de empleos en España. En concreto se trata de dos SVR(Suport Vector Regression), cada uno entrenado para predecir el salario mínimo y máximo respectivamente.

En la carpeta [Modelo_predictivo](https://github.com/UrkoRegueiro/IT_Job_Spain_Project/tree/main/Modelo_predictivo) encontrarás todo el proceso de construcción.

## 4. **Deploy**<br>

Para visualizar el código que ha hecho posible montar la web a traves de Streamlit pueden acceder al repositorio [Applicatech](https://github.com/UrkoRegueiro/applicatech).
