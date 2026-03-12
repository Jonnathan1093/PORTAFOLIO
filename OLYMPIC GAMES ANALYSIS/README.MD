# 🏅 Olympic Games Data Analysis (SQL + Python)

## 📊 Descripción del Proyecto

Este proyecto realiza un **análisis exploratorio de datos de los Juegos Olímpicos** utilizando **Python, SQL y DuckDB**.

El dataset utilizado es un archivo **CSV** que contiene información histórica de atletas olímpicos, incluyendo:

- Nombre del atleta
- País
- Deporte
- Evento
- Año de participación
- Tipo de medalla

El objetivo del proyecto es responder diferentes **preguntas analíticas utilizando consultas SQL**, ejecutadas directamente sobre el dataset desde Python.

---

# 🎯 Propósito del Proyecto

En muchos proyectos de análisis de datos, la información no se encuentra en una base de datos relacional, sino en archivos planos como:

- CSV
- Excel
- JSON

El propósito de este proyecto fue **analizar un archivo CSV como si fuera una tabla dentro de una base de datos SQL**.

Para lograr esto se utilizó **DuckDB**, que permite ejecutar consultas SQL directamente sobre **DataFrames de Pandas**.

De esta manera:

- El archivo CSV se carga en **Pandas**
- Luego se realizan **consultas SQL directamente sobre el dataset**
- Simulando un **entorno de análisis basado en bases de datos**

Este enfoque permite combinar:

- **Python** para la manipulación de datos
- **SQL** para consultas analíticas complejas

---

# ⚙️ Tecnologías Utilizadas

- Python
- Pandas
- DuckDB
- SQL
- Jupyter Notebook

---


# 📥 Carga de Datos

Primero se carga el dataset utilizando **Pandas**.

```python
import pandas as pd
import duckdb

athletes = pd.read_csv('./Data/athlete_events.csv')

# Información del dataset
athletes.info()
```

También se puede visualizar el dataset mediante SQL:

```python
duckdb.query("""
select *
from athletes
""").to_df()
```

---

# 🔎 Preguntas Analíticas

A continuación se muestran algunas de las consultas utilizadas para analizar el dataset.

---

## 1️⃣ ¿Cuántos Juegos Olímpicos se han realizado?

```python
duckdb.query("""
select count(distinct year)
as Total_juegos
from athletes
""").to_df()
```

---

## 2️⃣ Enumerar todos los Juegos Olímpicos realizados

```python
duckdb.query("""
select distinct games
from athletes
order by games
""").to_df()
```

---

## 3️⃣ Número total de naciones que participaron en cada Juego Olímpico

```python
duckdb.query("""
select Games, count(distinct noc)
as Num_Naciones
from athletes
group by Games
""").to_df()
```

---

## 4️⃣ Año con mayor y menor número de países participantes

```python
duckdb.query("""
(select 'Maximo' as tipo, year, count(distinct noc) as numero_paises
from athletes
group by year
order by numero_paises desc
limit 1
)
union
(select 'Minimo' as tipo, year, count(distinct noc) as numero_paises
from athletes
group by year
order by numero_paises asc
limit 1
)
""").to_df()
```

---

## 5️⃣ Nación que participó en todos los Juegos Olímpicos

```python
duckdb.query("""
select noc, count(distinct year) as Num_Participaciones
from athletes
group by noc
having Num_Participaciones =
(select count (distinct year)
from athletes)
""").to_df()
```

---

## 6️⃣ Deporte jugado en todas las olimpiadas de verano

```python
duckdb.query("""
SELECT sport, COUNT(DISTINCT games) AS Num_juegos
FROM athletes
WHERE season = 'Summer'
GROUP BY sport
HAVING COUNT(DISTINCT games) = (
    SELECT COUNT(DISTINCT games)
    FROM athletes
    WHERE season = 'Summer'
)
""").to_df()
```

---

## 7️⃣ Número total de deportes jugados en cada Juego Olímpico

```python
duckdb.query("""
SELECT games, COUNT(DISTINCT sport) AS Total_Juegos
FROM athletes
GROUP BY games
""").to_df()
```

---

## 8️⃣ Proporción de atletas masculinos y femeninos por año

```python
duckdb.query("""
SELECT year,
round( MaleCount/TotalCount, 2) AS Male_Proporcion,
round(FemaleCount/TotalCount, 2) AS Female_Proporcion
From(
SELECT year,
COUNT(*) AS TotalCount,
sum(case when sex = 'M' then 1 else 0 end) *100 as MaleCount,
sum(case when sex = 'F' then 1 else 0 end) *100 as FemaleCount
from athletes
group by year) AS sq1
order by year
""").to_df()
```

---

## 9️⃣ Top 5 atletas con más medallas de oro

```python
duckdb.query("""
SELECT Name, COUNT(*) AS Total_medallas_oro
FROM athletes
WHERE Medal = 'Gold'
GROUP BY Name
ORDER BY Total_medallas_oro DESC
LIMIT 5
""").to_df()
```

---

## 🔝 Países más exitosos en los Juegos Olímpicos

```python
duckdb.query("""
SELECT team AS Country,
sum(case when Medal = 'Gold' then 1 else 0 end) AS Medallas_oro,
sum(case when Medal = 'Silver' then 1 else 0 end) AS Medallas_plata,
sum(case when Medal = 'Bronze' then 1 else 0 end) AS Medallas_bronce,
COUNT(*) AS Total_medallas
FROM athletes
WHERE Medal IN ('Gold', 'Silver', 'Bronze')
GROUP BY team
ORDER BY Total_medallas DESC
LIMIT 5
""").to_df()
```

---

# 🧠 Técnicas SQL Utilizadas

Durante el análisis se aplicaron diferentes técnicas de SQL utilizadas comúnmente en proyectos de **Data Analysis**:

- SELECT
- GROUP BY
- COUNT
- DISTINCT
- ORDER BY
- LIMIT
- CASE WHEN
- HAVING
- SUBQUERIES
- UNION
- WINDOW FUNCTIONS

---

# 🚀 Posibles Mejoras

Este proyecto puede ampliarse con:

- Visualizaciones con **Matplotlib o Seaborn**
- Dashboards con **Power BI o Tableau**
- Limpieza y preparación avanzada de datos
- Análisis estadístico más profundo
---
