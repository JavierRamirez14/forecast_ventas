# 📈 Forecasting de Ventas
**Modelo LightGBM para predecir ventas en 54 tiendas (Top 15% en Kaggle)**  
[![Kaggle Competition](https://img.shields.io/badge/Kaggle-Competition-blue)](https://www.kaggle.com/competitions/store-sales-time-series-forecasting/)

---

## 📌 Objetivo
Desarrollar un sistema de forecasting para predecir ventas de **33 familias de productos** en **54 tiendas** de Ecuador, utilizando datos históricos (2013-2017) de la competencia Kaggle *"Store Sales - Time Series Forecasting"*.

---

## 🔍 Datos
**Variables clave:**
- `sales`: Ventas diarias por producto/tienda  
- `onpromotion`: Productos en promoción  
- `dcoilwtico`: Precio del petróleo (variable externa)  
- Festivos y eventos locales  

**Esquema de datos:**  
![Esquema de datos](https://prod-files-secure.s3.us-west-2.amazonaws.com/c0e5d5fd-3f6e-4f4a-a107-e858e7ea878f/esquema_datos.drawio.png)

---

## 🛠️ Metodología
### 1. Preprocesamiento
- **Limpieza:** Interpolación de valores faltantes en `transactions` y `dcoilwtico`  
- **Feature Engineering:**  
  - Variables temporales (mes, día, año)  
  - Indicadores de festivos (Navidad, Carnaval)  
  - Lags y medias móviles de ventas  
  - Efecto del terremoto de abril 2016  

### 2. Modelado
- **Algoritmo:** LightGBM (33 modelos, uno por familia de producto)  
- **Hiperparámetros:** Optimizados con Optuna  
- **Validación:** Métrica RMSLE (Raíz del Error Logarítmico Cuadrático Medio)  

### 3. Resultados
- **RMSLE:** 0.45 (**Top 13%** en Kaggle, puesto 89/679)  
- **Otras métricas:**  
  - RMSE: 295.26  
  - MAE: 87.38  

**Comparativa real vs. predicciones:**  
![Gráfico de resultados](https://prod-files-secure.s3.us-west-2.amazonaws.com/b72612b4-de86-445f-9e73-f18665b87a31/grafica_resultados.png)

---

## 📂 Estructura del Proyecto
