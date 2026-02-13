# 🖥️ **Documentación — Proyecto Aurelion**

## Sprint 3 — Implementación de Modelos de Machine Learning  
**Grupo 10**

En este sprint se añaden dos componentes de Machine Learning al pipeline del proyecto:

1. **Segmentación de clientes** mediante *clustering* (KMeans).  
2. **Predicción de ventas diarias** mediante regresión lineal.

Ambos modelos trabajan sobre las tablas depuradas en el Sprint 2 y se integran manteniendo la estructura de carpetas y el uso del diccionario `tablas`.

---

## 1. Modelo ML 1 — Segmentación de Clientes (Clustering KMeans)

### 1.1. Objetivo del modelo

- Agrupar a los clientes de la Tienda Aurelion en **segmentos de comportamiento** basados en sus patrones de compra.  
- Permite identificar:
  - Clientes de alto valor.
  - Clientes frecuentes vs. esporádicos.
  - Perfiles con distinta diversidad de productos y categorías.

En términos de Machine Learning, se trata de un problema **no supervisado de clustering**.

---

### 1.2. Algoritmo elegido y justificación

- Algoritmo: **KMeans** (`sklearn.cluster.KMeans`).
- Motivos de selección:
  - Es un algoritmo estándar, interpretable y práctico para segmentación inicial.
  - Funciona bien con KPIs numéricos previamente escalados.
  - El hiperparámetro `k` puede analizarse mediante el **método del codo** usando la inercia.

---

### 1.3. Entradas (X) y salida (y)

Este modelo **no tiene variable objetivo (`y`)**.  
Las entradas (`X`) son KPIs derivados de ventas y detalle de ventas:

- `total_gastado`
- `frecuencia_ventas`
- `total_items`
- `ticket_promedio`
- `diversidad_productos`
- `categorias_distintas`
- `categoria_favorita_code`
- `recencia_dias`
- `antiguedad_dias`

Código:

```python
features = [
    "total_gastado",
    "frecuencia_ventas",
    "total_items",
    "ticket_promedio",
    "diversidad_productos",
    "categorias_distintas",
    "categoria_favorita_code",
    "recencia_dias",
    "antiguedad_dias"
]

df_model = df_kpis[["id_cliente"] + features].fillna(0)
```

---

### 1.4. Métricas de evaluación

Para KMeans se utiliza:

- **Inercia**: suma de distancias intracluster.  
- Se calcula para distintos valores de `k` (2–7):

```python
inertias = []
K = range(2, 8)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init="auto")
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)

df_elbow = pd.DataFrame({"k": list(K), "inertia": inertias})
```

También se revisa:

- Distribución de clientes por segmento.
- Promedios de KPIs por segmento (análisis recomendado).

---

### 1.5. Modelo ML implementado

Pasos principales:

1. **Lectura de tablas** desde `tablas`:  
   `clientes`, `ventas`, `detalle_ventas`, `productos`, `categorias`, etc.

2. **Enriquecimiento de productos y categorías**:
   - Unión por `id_categoria`.
   - Unión con `detalle_ventas`.

3. **Cálculo de KPIs por cliente**:
   - Totales, diversidad, primera/última compra, categoría favorita.

4. **Cálculo de recencia y antigüedad**:
   - `recencia_dias`
   - `antiguedad_dias`

5. **Codificación de categoría favorita**:
   - Conversión a numérico: `categoria_favorita_code`.

6. **Escalado y clustering**:
   - Escalado con `StandardScaler`.
   - Clustering con `k = 4`:

   ```python
   kmeans_final = KMeans(n_clusters=4, random_state=42, n_init="auto")
   df_model["segmento"] = kmeans_final.fit_predict(X_scaled)
   ```

7. **Unión con tabla de clientes y exportación**:
   - Se genera el archivo `clientes_segmentados.xlsx`.

---

### 1.6. División train/test

- Para clustering **no se realiza partición train/test**.
- El modelo se entrena con el total de clientes.

---

### 1.7. Predicciones y métricas calculadas

- La predicción es la **asignación de un segmento**:

```python
df_model["segmento"] = kmeans_final.fit_predict(X_scaled)
```

- Distribución de segmentos:

```python
df_model["segmento"].value_counts()
```

- Inercias reportadas en `df_elbow`.

---

### 1.8. Resultados y gráficos recomendados

- **Distribución de clientes por segmento** (barras).  
- **KPIs por segmento** (cajas o barras).  
- **Curva del método del codo** (`k` vs. `inertia`).

Estos gráficos permiten interpretar los segmentos y soportan decisiones comerciales.

---

## 2. Modelo ML 2 — Predicción de Ventas Diarias (Regresión)

### 2.1. Objetivo del modelo

- Estimar el **número de ventas diarias** (`ventas_totales`) usando:
  - variables de fecha,
  - número de clientes activos por día.

---

### 2.2. Algoritmo elegido y justificación

- Algoritmo: **Regresión Lineal** (`LinearRegression`).
- Motivos:
  - Modelo simple e interpretable.
  - Ideal como baseline para análisis temporal.
  - Fácil de comparar con modelos más complejos posteriormente.

---

### 2.3. Entradas (X) y salida (y)

**Variable objetivo:**

- `ventas_totales`

**Variables predictoras:**

- `año`
- `mes`
- `dia_semana`
- `es_fin_de_semana`
- `clientes_activos`
- `feriado`

Código:

```python
y_ventas = df_diario["ventas_totales"]

features_diarias = [
    "año",
    "mes",
    "dia_semana",
    "es_fin_de_semana",
    "clientes_activos",
    "feriado"
]

X_ventas = df_diario[features_diarias].copy()
```

---

### 2.4. Métricas de evaluación

- **MAE**
- **RMSE**
- **R²**

Código:

```python
y_pred = modelo_diario.predict(X_test)

mae  = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2   = r2_score(y_test, y_pred)

print(f"MAE  diario : {mae:.2f}")
print(f"RMSE diario : {rmse:.2f}")
print(f"R²   diario : {r2:.3f}")
```

---

### 2.5. Modelo ML implementado

Pasos:

1. **Dataset diario**:

```python
df_diario = (
    df_ventas.groupby("fecha")
    .agg(
        ventas_totales=("id_venta", "nunique"),
        clientes_activos=("id_cliente", "nunique")
    )
    .reset_index()
)
```

2. **Ingeniería de variables**:  
   año, mes, día de semana, fin de semana, feriado.

3. **Definición de X e y**.

4. **Train/Test split**.

5. **Entrenamiento Regresión Lineal**.

6. **Evaluación**.

7. **Predicción total**:

```python
df_diario["ventas_predichas"] = modelo_diario.predict(X_ventas)
```

8. **Exportación**:  
   `ventas_diarias_predichas.xlsx`.

---

### 2.6. División train/test y entrenamiento

- 80% entrenamiento  
- 20% prueba  

Código:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X_ventas,
    y_ventas,
    test_size=0.2,
    random_state=42
)

modelo_diario = LinearRegression()
modelo_diario.fit(X_train, y_train)
```

---

### 2.7. Predicciones y métricas calculadas

- Predicciones:

```python
y_pred = modelo_diario.predict(X_test)
```

- Predicciones sobre el histórico:

```python
df_diario["ventas_predichas"] = modelo_diario.predict(X_ventas)
```

---

### 2.8. Gráficos recomendados

- **Serie temporal**: ventas reales vs. predichas.  
- **Dispersión**: clientes activos vs. ventas totales.  
- **Barras por día de la semana**: promedio de ventas.

---

## 3. Conclusiones del Sprint 3

- Se integró un **modelo no supervisado** para segmentación de clientes utilizando KPIs de comportamiento.
- Se desarrolló un **modelo supervisado de regresión** para predecir ventas diarias.
- Ambos modelos generan **salidas exportables en Excel** compatibles con herramientas de BI.
- El proyecto Aurelion evoluciona desde análisis descriptivo hacia análisis **predictivo y segmentación** para la toma de decisiones.

