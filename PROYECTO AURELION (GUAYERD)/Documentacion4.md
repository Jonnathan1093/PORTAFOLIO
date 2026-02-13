# 🧠 Proyecto: Tienda Aurelion  
## Sprint 4 — Analítica Avanzada y Machine Learning  
**Versión:** 1.0  
**Fecha:** Diciembre 2025  
**Equipo:** Grupo 10  
**Archivo:** `Documentacion.md`

---

## 🖥️ Documentación

## 1. Contexto del Sprint

El **Sprint 4** representa la evolución del proyecto Tienda Aurelion desde el análisis descriptivo y exploratorio hacia un enfoque de **analítica avanzada**, incorporando técnicas de **Machine Learning** y su integración en dashboards ejecutivos en Power BI.

Este sprint consolida el trabajo previo de:
- comprensión del negocio (Sprint 1),
- limpieza, integración y categorización de datos (Sprint 2),
- y modelado inicial en Python (Sprint 3).

---

## 2. Objetivo del Sprint

El objetivo principal del Sprint 4 es:

- Implementar modelos de Machine Learning con fines **analíticos y exploratorios**.
- Integrar los resultados en Power BI para consumo ejecutivo.
- Establecer una **base metodológica sólida y trazable** para futuras mejoras analíticas.

El sprint no busca optimizar modelos finales, sino **construir una línea base confiable y explicable**.

---

## 3. Alcance

El alcance del sprint incluye dos componentes:

1. **Segmentación de clientes** mediante un modelo no supervisado.
2. **Predicción de ventas** mediante un modelo supervisado de referencia (baseline).

Ambos modelos fueron desarrollados en **Python**, exportados a Excel y consumidos en **Power BI**.

---

## 4. Modelo 1 — Segmentación de Clientes

### 4.1 Objetivo

Identificar **segmentos de clientes con patrones de consumo similares**, permitiendo comprender la heterogeneidad de la base de clientes y habilitar análisis estratégicos por grupo.

---

### 4.2 Tipo de modelo

- Tipo: **Aprendizaje no supervisado**
- Algoritmo: **K-Means**
- Variable objetivo: No aplica

---

### 4.3 Variables utilizadas

La segmentación se construyó a partir de indicadores de comportamiento de compra, entre ellos:

- Gasto total
- Frecuencia de compras
- Ticket promedio
- Cantidad de productos adquiridos
- Diversidad de categorías
- Recencia del cliente
- Antigüedad del cliente

Las variables fueron normalizadas para asegurar una contribución equilibrada al modelo.

---

### 4.4 Resultados

- Se identificaron **4 segmentos de clientes**.
- Cada segmento presenta comportamientos diferenciados en términos de gasto y ticket promedio.
- La segmentación permite analizar la base de clientes más allá de métricas agregadas.

Los resultados fueron integrados al dashboard mediante filtros y tooltips para análisis interactivo.

---

## 5. Modelo 2 — Predicción de Ventas (Baseline)

### 5.1 Objetivo

Estimar las ventas diarias utilizando un modelo simple que sirva como **línea base de comparación** para futuros modelos predictivos.

---

### 5.2 Tipo de modelo

- Tipo: **Aprendizaje supervisado**
- Algoritmo: **Regresión Lineal**
- Enfoque: Modelo baseline (referencial)

---

### 5.3 Variables del modelo

**Variable objetivo:**
- Ventas totales diarias

**Variables explicativas:**
- Variables temporales (año, mes, día de la semana)
- Indicador de fin de semana
- Clientes activos diarios

---

### 5.4 Evaluación

Se calcularon métricas estándar de evaluación:

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² (Coeficiente de determinación)

El comportamiento del modelo muestra una alta alineación entre valores reales y predichos, resultado coherente con su propósito como **modelo de referencia**, no como modelo optimizado.

---

## 6. Integración en Power BI

Los resultados de ambos modelos se integraron en un **dashboard de Analítica Avanzada** que permite:

- Visualizar la distribución de clientes por segmento.
- Analizar perfiles de consumo promedio por segmento.
- Explorar resultados mediante filtros por ciudad y fecha.
- Comparar ventas reales versus ventas predichas.
- Consultar métricas clave mediante tooltips contextuales.

El diseño prioriza claridad, coherencia visual y lectura ejecutiva.

---

## 7. Conclusiones

1. La segmentación de clientes evidencia que la base de clientes presenta **comportamientos de consumo diferenciados**, relevantes para la toma de decisiones.
2. El análisis por segmentos permite distinguir entre volumen de clientes y aporte económico.
3. El modelo predictivo baseline establece una **referencia objetiva** para evaluar futuras mejoras.
4. La integración de Machine Learning y BI fortalece la trazabilidad del análisis.
5. El sprint sienta bases sólidas para evolucionar hacia analítica predictiva más avanzada.

---

## 8. Limitaciones

- El modelo predictivo corresponde a un enfoque inicial y no incorpora variables externas.
- La segmentación se basa en comportamiento histórico y debe revisarse periódicamente.
- No se busca inferencia causal ni optimización en esta etapa.

---

## 9. Próximos Pasos

- Evaluar modelos predictivos alternativos y compararlos contra el baseline.
- Incorporar nuevas variables al análisis.
- Usar la segmentación como insumo para estrategias comerciales.
- Evolucionar el dashboard hacia escenarios de seguimiento y simulación.

---

📄 **Fin del documento**  
Este archivo forma parte del entregable oficial del  
**Sprint 4 — Proyecto Tienda Aurelion**
