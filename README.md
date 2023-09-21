# Store Sales Time Series Forecasting

Este proyecto se basa en la competición [Store Sales Time Series Forecasting](https://www.kaggle.com/competitions/store-sales-time-series-forecasting/overview) de Kaggle, que desafía a los participantes a predecir las ventas futuras de tiendas minoristas en función de datos históricos. El objetivo es desarrollar modelos de series temporales precisos que puedan proporcionar predicciones útiles para la gestión de inventario y la planificación de recursos.

## Contexto

En el mundo del comercio minorista, la capacidad de prever las ventas futuras es esencial para la toma de decisiones efectiva. Las ventas pueden variar significativamente debido a factores estacionales, promociones, eventos especiales y otros factores. Por lo tanto, contar con modelos de pronóstico precisos es fundamental para garantizar que las tiendas tengan el inventario adecuado en el momento adecuado y para optimizar la planificación de recursos.

## Objetivo

El objetivo principal de este proyecto es desarrollar modelos de machine learning precisos que puedan anticipar las ventas futuras de las tiendas en función de las tendencias históricas y otros factores relevantes. Estos modelos pueden tener un impacto significativo en la eficiencia operativa y la toma de decisiones estratégicas en el ámbito del comercio minorista.

## Contenido del Repositorio

En este repositorio, encontrarás los siguientes archivos:

- Codigo_Desarrollo: Archivo `.ipynb` que contiene el código de todo el desarrollo de los modelos, incluyendo la limpieza de datos, la creacion, transformación y preselección de variables y las predicciones que se envían a Kaggle para ser calificadas.

- Codigo_Produccion: Archivo `.ipynb` que contiene el código de puesta en producción, es decir, es el código que se usa a la hora de predecir, mucho mas comprimido y eficaz.

- App_forecast: Archivo '.py' que desarrolla una aplicación en streamlit donde un usuario puede hacer las predicciones. Al app no se puede subir a streamlit debido al gran peso de los modelos. Sin embargo, mas adelante mostrare imagenes de su funcionamiento.

## Resumen del proyecto

1. Unificar datasets: Kaggle nos proporciona distintos datasets (historico de ventas, información sobre cada tienda, fechas de fiestas o eventos nacionales y el precio del aceitea lo largo del tiempo). Todos estos datasets hay que unificarlos en uno solo para poder trabajar sobre él.
2. Limpieza de datos: trabajar con los nulos, los duplicados, los valores atípicos, etc.
3. Creación de variables: crear nuevas variables que nos puedan aportar valor adicional o crearlas a partir de otras variables ya existentes.
4. Transformación de los datos: transformar las variables para que queden todas en formato numérico para poder trabajar con sklearn.
5. Preselección de variables: al tener muchas variables es necesario elegir unicamente las variables que sean predictoras, para que, de esta forma desarrollar y aplicar los modelos no se muy costoso computacionalmente.
6. Desarrollar los modelos: en este proyecto he desarrollado 33 modelos, uno por cada familia de productos, por lo que he escogido LightGBM, un algoritmo muy eficiente.
7. Creación del codigo de producción: recopilar todo el codigo ya creado y hacerlo mas compacto poniendo unicamente lo necesario para que pueda predecir. Este es el código que se usara a la hora de pronosticar las ventas. Además, ya no crearemos los modelos, sino que solamente ejecutamos los que ya creamos.
8. Creación de una app: para poner en marcha nuestros modelos tenemos que entregarselo a los usuarios y para ello he creado una app con streamlit que te permite hacer el pronostico.

## Aplicación

![Captura App](Captura_app.png)

