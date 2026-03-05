# 🧠 Proyecto Data Analytics — Tienda Aurelion

## 📊 Descripción del Proyecto

El proyecto **Tienda Aurelion** tiene como objetivo analizar el comportamiento de compra de los clientes de un supermercado utilizando técnicas de **análisis de datos y machine learning**.

A partir de múltiples archivos de datos (clientes, productos, ventas y detalle de ventas), se construyó un pipeline completo de análisis que incluye:

- Limpieza y estandarización de datos  
- Creación de un sistema de categorías de productos  
- Análisis exploratorio de datos  
- Segmentación de clientes mediante clustering  
- Predicción de ventas diarias  
- Visualización de resultados en Power BI  

El proyecto sigue un enfoque progresivo de **Data Analytics → Machine Learning → Business Intelligence**.

---

# 🎯 Problema de Negocio

La tienda dispone de información valiosa sobre sus clientes y ventas, pero los datos se encontraban:

- Distribuidos en **múltiples archivos desconectados**
- Con **estructuras inconsistentes**
- Sin una categorización clara de productos
- Sin análisis que permitan comprender el comportamiento de compra

Esto dificultaba responder preguntas clave como:

- ¿Qué **categorías de productos** tienen mayor demanda?
- ¿Qué **clientes generan mayor valor**?
- ¿Cómo evolucionan las **ventas a lo largo del tiempo**?
- ¿Cuántas **ventas se pueden esperar en el futuro cercano**?

---

# 🗂️ Dataset

El proyecto utiliza los siguientes archivos:

- `clientes.xlsx`
- `productos.xlsx`
- `ventas.xlsx`
- `detalle_ventas.xlsx`

Estos datos contienen información sobre:

- clientes registrados
- productos del catálogo
- transacciones de ventas
- detalle de productos vendidos por transacción

---

# ⚙️ Pipeline del Proyecto

## 1️⃣ Preparación y Limpieza de Datos

Se realizó un proceso de **data cleaning y normalización**:

- estandarización de nombres de columnas
- corrección de tipos de datos
- eliminación de duplicados
- análisis de valores nulos

También se generó un **reporte de calidad de datos** para evaluar la confiabilidad de la información.

---

## 2️⃣ Sistema de Categorías de Productos

Se diseñó un sistema jerárquico de categorías utilizando:


Esto permitió analizar los productos a diferentes niveles y mejorar la capacidad de segmentación del catálogo.

---

## 3️⃣ Análisis Exploratorio de Datos (EDA)

Se realizaron análisis descriptivos para entender la estructura del catálogo y el comportamiento de los productos:

- distribución de precios por categoría
- cantidad de productos por categoría
- identificación de productos más caros
- matriz de correlación de variables numéricas

---

# 🤖 Machine Learning

## 1️⃣ Segmentación de Clientes

Se aplicó **K-Means Clustering** para identificar segmentos de clientes basados en su comportamiento de compra.

### Variables utilizadas

- total gastado
- frecuencia de compras
- ticket promedio
- diversidad de productos
- diversidad de categorías
- recencia
- antigüedad del cliente

### Resultado

El modelo identificó **4 segmentos de clientes** con comportamientos de consumo diferenciados.

Esto permite analizar perfiles como:

- clientes de alto valor
- clientes frecuentes
- clientes ocasionales

---

## 2️⃣ Predicción de Ventas Diarias

Se implementó un modelo de **Regresión Lineal** para estimar el número de ventas diarias.

### Variable objetivo

### Variables predictoras

- año
- mes
- día de la semana
- indicador de fin de semana
- clientes activos diarios

### Métricas de evaluación

- MAE
- RMSE
- R²

El modelo funciona como **baseline predictivo**, útil para comparar con modelos más avanzados en el futuro.

---

# 📈 Visualización en Power BI

Los resultados del análisis y los modelos fueron integrados en un **dashboard interactivo en Power BI** que permite:

- analizar segmentos de clientes
- visualizar perfiles de consumo por segmento
- comparar ventas reales vs ventas predichas
- explorar resultados por ciudad y fecha

---

# 🛠️ Tecnologías Utilizadas

### Lenguajes
- Python

### Librerías
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn

### Herramientas
- Power BI
- Excel
- Jupyter Notebook

---

# 📊 Resultados del Proyecto

El proyecto permitió:

- transformar datos dispersos en un **modelo de datos analizable**
- identificar **segmentos de clientes con comportamientos distintos**
- crear un **modelo predictivo inicial de ventas**
- construir dashboards que facilitan la **toma de decisiones basada en datos**

---

# 🚀 Posibles Mejoras

- Implementar modelos predictivos más avanzados (Random Forest, XGBoost)
- Incorporar variables externas como promociones o estacionalidad
- Analizar **venta cruzada entre categorías**
- Desarrollar modelos de **predicción de churn de clientes**

---

# 👨‍💻 Autor

**Jonnathan Heras**  
Ingeniero en Tecnologías de la Información  

📧 jonnathan1093@gmail.com  
💼 LinkedIn: https://linkedin.com/in/Jonnathan1093  
💻 GitHub: https://github.com/Jonnathan1093