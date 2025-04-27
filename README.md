# Forecasting de Ventas
**Modelo LightGBM para predecir ventas en 54 tiendas (Top 15% en Kaggle)**  
[![Kaggle Competition](https://img.shields.io/badge/Kaggle-Competition-blue)](https://www.kaggle.com/competitions/store-sales-time-series-forecasting/)

---

## Objetivo
Desarrollar un sistema de forecasting para predecir ventas de **33 familias de productos** en **54 tiendas** de Ecuador, utilizando datos históricos (2013-2017) de la competencia Kaggle *"Store Sales - Time Series Forecasting"*.

---

## ¿Que problemas resuelve? Y, ¿qué ofrece?

- **Predicciones precisas de ventas:** Modelos de forecasting entrenados con datos históricos que ofrecen predicciones fiables para cada producto en cada tienda.
- **Optimización de inventario:** Evita el exceso o la falta de existencias al predecir con precisión las ventas futuras, reduciendo costos asociados.
- **Evitar la pérdida de ventas:** Al prever con precisión la demanda futura, las empresas pueden asegurarse de tener suficiente inventario disponible para satisfacer la demanda del mercado, evitando así la pérdida de ventas debido a productos agotados.
- **Toma de decisiones basada en datos:** Permite tomar decisiones estratégicas fundamentadas en análisis cuantitativos, en lugar de intuiciones subjetivas.

--- 

## Esquema de datos
![Esquema de datos](https://prod-files-secure.s3.us-west-2.amazonaws.com/c0e5d5fd-3f6e-4f4a-a107-e858e7ea878f/esquema_datos.drawio.png)

---

## Metodología
### 1. Preprocesamiento
- **Análisis exploratorio de datos**
- **Limpieza:** Interpolación de valores faltantes en `transactions` y `dcoilwtico`  
- **Feature Engineering:**  
  - Variables temporales (mes, día, año)  
  - Indicadores de festivos (Navidad, Carnaval)  
  - Lags y medias móviles de ventas  
  - Efecto del terremoto de abril 2016
- **Transformación de datos:** One Hot Encoding y Normalización

### 2. Modelado
- **Preselección de variables:** Mutual Info Regression
- **Algoritmo:** LightGBM (33 modelos, uno por familia de producto)  
- **Hiperparámetros:** Optimizados con Optuna  
- **Evaluación:** Métrica RMSLE (Raíz del Error Logarítmico Cuadrático Medio)  

### 3. Resultados
- **RMSLE:** 0.45 (**Top 13%** en Kaggle, puesto 89/679 a día 5/03/2024)  
- **Otras métricas:**  
  - RMSE: 295.26  
  - MAE: 87.38  

**Comparativa real vs. predicciones:**  
![Gráfico de resultados](https://prod-files-secure.s3.us-west-2.amazonaws.com/b72612b4-de86-445f-9e73-f18665b87a31/grafica_resultados.png)

---

## 📂 Estructura del Proyecto
- **Notebook_desarrollo:** Archivo `.ipynb` que contiene desde la extracción de datos hasta la transformación y preselección de variables. Contiene también las explicaciones de cada paso tomado.
- **Notebook_ejecución:** Archivo `.ipynb` que contiene la modelización e hiperparametrización de los modelos, así como, el entrenamiento de cada uno de ellos, sus predicciones y la evaluación de los modelos. Está diseñado específicamente para el entrenamiento y ejecución eficiente de modelos y la generación rápida de predicciones. Proporciona un código más compacto y orientado a la aplicación práctica.
