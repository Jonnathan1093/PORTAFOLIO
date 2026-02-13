#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Proyecto: Tienda Aurelion — Código integrado (Sprint 1, Sprint 2 y Sprint 3)
Autor original: Jonnathan Heras
Integración y ajustes: Assistant
"""

import os
import glob
import re
import unicodedata

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# =========================
# CONFIGURACIÓN GENERAL
# =========================
RUTA_DATA = "Data_Aurelion"  # carpeta que contiene los .xlsx

# =========================
# UTILIDADES
# =========================
def limpiar_pantalla():
    """Limpia la pantalla de la terminal (Windows / macOS / Linux)."""
    os.system('cls' if os.name == 'nt' else 'clear')


def semaforo(valor, bajo=5, alto=20):
    """Devuelve emoji tipo semáforo según valor."""
    return "🟢" if valor == 0 else "🟡" if valor <= bajo else "🔴"


# =========================
# TEXTOS DE DOCUMENTACIÓN (Sprint 1 y Sprint 2)
# =========================
tema_problema_solucion = """
１ Tema, problema y solución

📋 Tema:
Tienda Aurelion estudiará el comportamiento de compra y las preferencias de los clientes en un supermercado de Córdoba a partir de datos simulados, buscando generar una visión completa del entorno comercial.

📉 Problema:
La Tienda Aurelion enfrenta dificultades para comprender y aprovechar la información que genera día a día.  
Los datos de clientes, productos, ventas y detalle de ventas se encuentran distribuidos en diferentes archivos, lo que hace difícil relacionarlos y obtener conclusiones útiles para el negocio.

Esta forma de gestionar la información complica tareas importantes como:
- 📊 Saber cuáles son los productos más vendidos o las categorías con mayor demanda.  
- 💳 Analizar los medios de pago preferidos por los clientes.  
- 🧍‍♂️ Conocer cómo ha crecido la base de clientes según la ciudad o la fecha de registro.  
- 📈 Utilizar los datos históricos para proyectar resultados o detectar tendencias.  

Por esta razón, la tienda no logra tener una comprensión completa de su actividad comercial ni aprovechar los datos que ya posee para tomar decisiones informadas. Además, se ha notado que algunos clientes han dejado de comprar o han reducido su frecuencia de compra, mientras que ciertos productos muestran bajas ventas, afectando el rendimiento general del negocio y su posibilidad de crecimiento.

💡 Solución:
Para enfrentar las dificultades que presenta la Tienda Aurelion, se propone desarrollar un sistema que integre la información proveniente de los distintos archivos de clientes, productos y ventas, permitiendo analizarla de forma ordenada y comprensible.

El proyecto busca:
- 🔍 ¿Qué productos y categorías tienen mayor demanda?  
- 💳 ¿Cuáles son los medios de pago más utilizados?  
- 📆 ¿Cómo evolucionan las ventas y los clientes a lo largo del tiempo?  
- 📊 ¿Qué tendencias pueden observarse para planificar estrategias futuras?  

Con esta solución, la tienda podrá comprender mejor su actividad comercial, detectar oportunidades de mejora y aprovechar la información disponible para tomar decisiones basadas en datos, fortaleciendo su competitividad y crecimiento a largo plazo.
"""

dataset_referencia = """
２ Dataset de referencia

Fuente:
Datos ficticios proporcionados con fines educativos, orientados a representar las operaciones generales de una tienda.

Definición:
Los archivos proporcionados una simulación del entorno de ventas, donde se gestionan productos, clientes, ventas y los detalles de cada transacción.
"""

estructura_tablas = """
３ Estructura por tabla
...
(Se mantiene igual, no modificado)
"""

escalas_medicion = """
４ Escalas de medición
...
"""

sugerencias_copilot = """
５ Sugerencias y mejoras aplicadas con Copilot
...
"""

# Sprint 2 textos
sprint2_contexto = """
1. CONTEXTO DEL PROYECTO
-----------------------------------------
La Tienda Aurelion dispone de datos separados en:
- clientes.xlsx
- productos.xlsx
- ventas.xlsx
- detalle_ventas.xlsx

Problemas detectados:
- Archivos desconectados
- Tipos inconsistentes
- Calidad de datos desconocida
- Categorías poco explotables

Sprint 2 se enfoca en preparar y estandarizar los datos.
"""

sprint2_rol = """
2. ROL DEL SPRINT 2 EN LA SOLUCIÓN
-----------------------------------------
Este sprint normaliza, limpia y estandariza los archivos.

Aporta:
- Esquema unificado
- Sistema de categorías jerárquicas
- Visualizaciones preliminares
- Bases listas para análisis posteriores
"""

sprint2_objetivos = """
3. OBJETIVOS ESPECÍFICOS DEL SPRINT 2
-----------------------------------------
1. Unificación del esquema de tablas
2. Evaluación y mejora de calidad de datos
3. Diseño de un sistema jerárquico de categorías
4. Generación de vistas descriptivas
5. Base lista para sprints futuros
"""

sprint2_datos = """
4. DATOS Y ARTEFACTOS GENERADOS
-----------------------------------------
Entradas:
- clientes.xlsx
- productos.xlsx
- ventas.xlsx
- detalle_ventas.xlsx

Salidas:
- Reportes de calidad
- categorias_ref.xlsx (archivo maestro)
- productos_actualizado.xlsx
- Gráficos y tablas descriptivas
"""

sprint2_analisis = """
5. ANÁLISIS REALIZADOS EN SPRINT 2
-----------------------------------------
Incluye:
- Normalización de nombres
- Corrección de tipos
- Eliminación de duplicados
- Reportes con semáforo
- Sistema de categorías jerárquicas
- Visualizaciones descriptivas
"""

sprint2_resultados = """
6. RESULTADOS CLAVE DEL SPRINT 2
-----------------------------------------
- Modelo de datos unificado
- Visibilidad sobre calidad
- Sistema escalable de categorías
- Catálogo de productos enriquecido
- Base alineada con necesidades de negocio
"""

sprint2_recomendaciones = """
7. RECOMENDACIONES Y SIGUIENTES PASOS
-----------------------------------------
1. Validar categorías con negocio
2. Integrar análisis de medios de pago
3. Profundizar análisis de clientes
4. Construir dashboards ejecutivos
"""

sprint2_completo = (
    sprint2_contexto
    + "\n"
    + sprint2_rol
    + "\n"
    + sprint2_objetivos
    + "\n"
    + sprint2_datos
    + "\n"
    + sprint2_analisis
    + "\n"
    + sprint2_resultados
    + "\n"
    + sprint2_recomendaciones
)

# =========================
# SUBMENÚS DOCUMENTACIÓN
# =========================
def submenu_sprint2():
    while True:
        limpiar_pantalla()
        print('--- Submenú Sprint 2 ---')
        print('1 - Contexto del proyecto')
        print('2 - Rol del Sprint 2')
        print('3 - Objetivos específicos')
        print('4 - Datos y artefactos generados')
        print('5 - Análisis realizados')
        print('6 - Resultados clave')
        print('7 - Recomendaciones y siguientes pasos')
        print('8 - Ver todo junto')
        print('9 - Volver al menú principal')

        opcion = input('\nSeleccione una opción: ').strip()

        if opcion == '1':
            limpiar_pantalla()
            print(sprint2_contexto)
        elif opcion == '2':
            limpiar_pantalla()
            print(sprint2_rol)
        elif opcion == '3':
            limpiar_pantalla()
            print(sprint2_objetivos)
        elif opcion == '4':
            limpiar_pantalla()
            print(sprint2_datos)
        elif opcion == '5':
            limpiar_pantalla()
            print(sprint2_analisis)
        elif opcion == '6':
            limpiar_pantalla()
            print(sprint2_resultados)
        elif opcion == '7':
            limpiar_pantalla()
            print(sprint2_recomendaciones)
        elif opcion == '8':
            limpiar_pantalla()
            print(sprint2_completo)
        elif opcion == '9':
            break
        else:
            print('\nOpción no válida.')

        input('\nPresione Enter para continuar...')


def submenu_tema_problema_solucion():
    texto = tema_problema_solucion

    partes = re.split(r'📋 Tema:|📉 Problema:|💡 Solución:', texto)
    if len(partes) >= 4:
        encabezado = partes[0].strip()
        tema = partes[1].strip()
        problema = partes[2].strip()
        solucion = partes[3].strip()
    else:
        print(texto)
        input('\nPresione Enter para volver...')
        return

    while True:
        limpiar_pantalla()
        print('--- Submenú: Tema, Problema y Solución ---')
        print('1 - Ver solo el Tema')
        print('2 - Ver solo el Problema')
        print('3 - Ver solo la Solución')
        print('4 - Ver todo junto')
        print('5 - Volver al menú principal')

        opcion = input('\nSeleccione una opción: ').strip()

        if opcion == '1':
            limpiar_pantalla()
            print('📋 Tema:\n')
            print(tema)
        elif opcion == '2':
            limpiar_pantalla()
            print('📉 Problema:\n')
            print(problema)
        elif opcion == '3':
            limpiar_pantalla()
            print('💡 Solución:\n')
            print(solucion)
        elif opcion == '4':
            limpiar_pantalla()
            print(encabezado)
            print('\n📋 Tema:\n' + tema)
            print('\n📉 Problema:\n' + problema)
            print('\n💡 Solución:\n' + solucion)
        elif opcion == '5':
            break
        else:
            print('\nOpción no válida.')

        input('\nPresione Enter para continuar...')


# =========================
# FUNCIONES DE CARGA Y PREPARACIÓN (Sprint 2 util)
# =========================
def normalizar_columnas(df: pd.DataFrame) -> pd.DataFrame:
    """Normaliza nombres de columnas: minúsculas, sin espacios ni tildes."""
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.normalize('NFKD')
        .str.encode('ascii', errors='ignore')
        .str.decode('utf-8')
        .str.replace(r'[^0-9a-zA-Z_]', '_', regex=True)
    )
    return df


def corregir_tipos(df: pd.DataFrame, estructura: dict) -> pd.DataFrame:
    """Corrige tipos de columnas según estructura dada."""
    conv = {
        "int": lambda s: pd.to_numeric(s, errors="coerce").astype("Int64"),
        "float": lambda s: pd.to_numeric(s, errors="coerce"),
        "str": lambda s: s.astype("string").str.strip(),
        "date": lambda s: pd.to_datetime(s, errors="coerce")
    }
    for col, tipo in estructura.items():
        if col in df.columns:
            df[col] = conv.get(tipo, lambda s: s)(df[col])
    return df


def reporte_calidad(df: pd.DataFrame, nombre: str):
    """Genera resumen y detalle de calidad de una tabla (retorna resumen y detalle)."""
    nulos = df.isnull().sum().sum()
    porc_nulos = round(nulos / df.size * 100, 2) if df.size > 0 else 0
    duplicados = df.duplicated().sum()

    resumen = {
        "Tabla": nombre,
        "Filas": len(df),
        "Columnas": df.shape[1],
        "Nulos Totales": int(nulos),
        "No Nulos Totales": int(df.notnull().sum().sum()),
        "Duplicados": int(duplicados),
        "Calidad Nulos": semaforo(porc_nulos),
        "Calidad Duplicados": semaforo(duplicados)
    }

    detalle = pd.DataFrame({
        "Tabla": nombre,
        "Columna": df.columns,
        "Tipo": df.dtypes.values,
        "Nulos": df.isnull().sum().values,
        "No Nulos": df.notnull().sum().values,
        "Total Filas": len(df),
        "Semaforo Nulos": [semaforo(int(v)) for v in df.isnull().sum().values]
    })
    return resumen, detalle


def cargar_y_preparar_datos(ruta_base: str):
    """
    Carga los .xlsx de Data_Aurelion, normaliza columnas, corrige tipos,
    elimina duplicados y devuelve el diccionario 'tablas'.
    """
    ruta = ruta_base
    archivos = glob.glob(os.path.join(ruta, "*.xlsx"))

    if not archivos:
        raise FileNotFoundError(f"No se encontraron archivos .xlsx en la ruta: {ruta}")

    dataframes = {
        os.path.basename(archivo).replace(".xlsx", ""): pd.read_excel(archivo)
        for archivo in archivos
    }

    estructuras = {
        "productos": {
            "id_producto": "int", "nombre_producto": "str",
            "categoria": "str", "precio_unitario": "float"
        },
        "clientes": {
            "id_cliente": "int", "nombre_cliente": "str",
            "email": "str", "ciudad": "str", "fecha_alta": "date"
        },
        "ventas": {
            "id_venta": "int", "fecha": "date", "id_cliente": "int",
            "nombre_cliente": "str", "email": "str", "medio_pago": "str"
        },
        "detalle_ventas": {
            "id_venta": "int", "id_producto": "int",
            "nombre_producto": "str", "cantidad": "int",
            "precio_unitario": "float", "importe": "float"
        }
    }

    tablas = {}
    for nombre_tabla in ["productos", "clientes", "ventas", "detalle_ventas"]:
        if nombre_tabla not in dataframes:
            raise FileNotFoundError(f"Falta el archivo requerido: {nombre_tabla}.xlsx")
        tablas[nombre_tabla] = dataframes[nombre_tabla]

    # Limpieza básica y normalización
    for nombre, df in tablas.items():
        df = normalizar_columnas(df)
        df = corregir_tipos(df, estructuras[nombre])
        df = df.drop_duplicates(ignore_index=True)
        tablas[nombre] = df

    return tablas


# =========================
# UTILIDADES DE ACCESO A TABLAS (SEGURAS)
# =========================
def get_tabla(tablas: dict, nombre: str):
    """Recuperación segura de tabla desde el diccionario."""
    if tablas is None:
        print("⚠️ El diccionario 'tablas' es None.")
        return None
    if nombre not in tablas:
        print(f"⚠️ La tabla '{nombre}' no existe en el diccionario 'tablas'.")
        return None
    return tablas[nombre].copy()


# =========================
# FASE 7 — SEGMENTACIÓN DE CLIENTES (KMEANS)
# =========================
def fase7_segmentacion_clientes(tablas: dict, ruta_base: str):
    """Ejecuta la Fase 7 de segmentación de clientes (KMeans)."""

    print("\n🚀 Iniciando Fase 7 — Segmentación de Clientes (Clustering KMeans)...\n")

    df_clientes = get_tabla(tablas, "clientes")
    df_ventas = get_tabla(tablas, "ventas")
    df_detalle = get_tabla(tablas, "detalle_ventas")
    df_productos = get_tabla(tablas, "productos")

    if df_clientes is None or df_ventas is None or df_detalle is None or df_productos is None:
        print("❌ No se pudieron cargar todas las tablas necesarias para la segmentación.")
        return

    # Preparar nombres de categoría
    df_prod_final = df_productos.copy()
    if "categoria" in df_prod_final.columns and "categoria_nombre" not in df_prod_final.columns:
        df_prod_final["categoria_nombre"] = df_prod_final["categoria"]
    elif "categoria_nombre" not in df_prod_final.columns:
        df_prod_final["categoria_nombre"] = "Sin categoría"

    # Integrar productos en detalle ventas
    cols_merge = [c for c in ["id_producto", "precio_unitario", "categoria_nombre"] if c in df_prod_final.columns]
    df_detalle_full = df_detalle.merge(df_prod_final[cols_merge], on="id_producto", how="left")

    # Unir detalle ventas con ventas (cliente + fecha)
    df_full = df_detalle_full.merge(df_ventas, on="id_venta", how="left")

    # KPIs por cliente
    print("\n📊 Calculando KPIs avanzados por cliente...")

    # Asegurarse de que las columnas necesarias existan
    for col in ["importe", "id_venta", "cantidad", "id_producto", "categoria_nombre", "fecha", "id_cliente"]:
        if col not in df_full.columns:
            df_full[col] = np.nan

    df_kpis = df_full.groupby("id_cliente").agg(
        total_gastado=("importe", "sum"),
        frecuencia_ventas=("id_venta", "nunique"),
        total_items=("cantidad", "sum"),
        ticket_promedio=("importe", "mean"),
        diversidad_productos=("id_producto", "nunique"),
        categorias_distintas=("categoria_nombre", "nunique"),
        primera_compra=("fecha", "min"),
        ultima_compra=("fecha", "max")
    ).reset_index()

    # Categoría favorita
    df_cat_top = (
        df_full.groupby(["id_cliente", "categoria_nombre"])
        .agg(total=("cantidad", "sum"))
        .reset_index()
    )
    if not df_cat_top.empty:
        df_cat_top = df_cat_top.sort_values(["id_cliente", "total"], ascending=[True, False])
        df_cat_top = df_cat_top.groupby("id_cliente").first().reset_index()
        df_cat_top.rename(columns={"categoria_nombre": "categoria_favorita"}, inplace=True)
        df_kpis = df_kpis.merge(df_cat_top[["id_cliente", "categoria_favorita"]], on="id_cliente", how="left")
    else:
        df_kpis["categoria_favorita"] = np.nan

    # Antigüedad y recencia
    if df_clientes is not None and "fecha_alta" in df_clientes.columns:
        df_kpis = df_kpis.merge(df_clientes[["id_cliente", "fecha_alta"]], on="id_cliente", how="left")
        try:
            df_kpis["antiguedad_dias"] = (df_kpis["ultima_compra"] - df_kpis["fecha_alta"]).dt.days
        except Exception:
            df_kpis["antiguedad_dias"] = 0
    else:
        df_kpis["antiguedad_dias"] = 0

    if "ultima_compra" in df_kpis.columns and pd.api.types.is_datetime64_any_dtype(df_kpis["ultima_compra"]):
        df_kpis["recencia_dias"] = (df_kpis["ultima_compra"].max() - df_kpis["ultima_compra"]).dt.days
    else:
        df_kpis["recencia_dias"] = 0

    # Codificación categoría favorita
    df_kpis["categoria_favorita"] = df_kpis["categoria_favorita"].fillna("Sin dato")
    df_kpis["categoria_favorita_code"] = df_kpis["categoria_favorita"].astype("category").cat.codes

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
    features = [f for f in features if f in df_kpis.columns]
    df_model = df_kpis[["id_cliente"] + features].fillna(0)

    print("\n📌 Features utilizados para clustering:")
    try:
        print(df_model[features].describe())
    except Exception:
        print("  (No hay suficientes datos para describir las features.)")

    # Escalado
    print("\n📏 Normalizando variables...")
    scaler = StandardScaler()
    try:
        X_scaled = scaler.fit_transform(df_model[features])
    except Exception as e:
        print(f"❌ Error al escalar features: {e}")
        return

    # Método del codo
    print("\n📉 Método del Codo para validar número de clusters...")
    inertias = []
    K = range(2, 8)
    for k in K:
        try:
            kmeans = KMeans(n_clusters=k, random_state=42, n_init="auto")
            kmeans.fit(X_scaled)
            inertias.append(kmeans.inertia_)
        except Exception as e:
            print(f"  ❌ Error entrenando KMeans con k={k}: {e}")
            inertias.append(np.nan)

    df_elbow = pd.DataFrame({"k": list(K), "inertia": inertias})
    print(df_elbow)

    # Entrenamiento final
    k_chosen = 4
    print(f"\n🤖 Entrenando modelo final de segmentación con K = {k_chosen}...")
    try:
        kmeans_final = KMeans(n_clusters=k_chosen, random_state=42, n_init="auto")
        df_model["segmento"] = kmeans_final.fit_predict(X_scaled)
    except Exception as e:
        print(f"❌ Error al entrenar KMeans final: {e}")
        return

    print("✔️ Segmentación completada:")
    print(df_model["segmento"].value_counts())

    # Unión con clientes y exportación
    df_segmentado = df_clientes.merge(df_model, on="id_cliente", how="left")
    ruta_seg = os.path.join(ruta_base, "clientes_segmentados.xlsx")
    try:
        df_segmentado.to_excel(ruta_seg, index=False)
        print(f"\n📁 Archivo generado: {ruta_seg}")
    except Exception as e:
        print(f"❌ Error al exportar archivo segmentado: {e}")

    print("🎉 Fase 7 completada.\n")


# =========================
# FASE 8 — PREDICCIÓN DE VENTAS DIARIAS (REGRESIÓN)
# =========================
def fase8_prediccion_ventas(tablas: dict, ruta_base: str):
    """
    Ejecuta la Fase 8: agregación diaria, entrenamiento de regresión,
    métricas y exportación de ventas_diarias_predichas.xlsx.

    Retorna df_diario (para graficar).
    """
    print("\n🚀 Iniciando Fase 8 — Predicción de ventas diarias...\n")

    df_ventas = get_tabla(tablas, "ventas")
    if df_ventas is None:
        raise ValueError("❌ No se encontró la tabla 'ventas', no se puede continuar.")

    # Asegurar columna fecha y tipo
    if "fecha" not in df_ventas.columns:
        raise ValueError("❌ 'ventas' no contiene la columna 'fecha' necesaria.")
    df_ventas["fecha"] = pd.to_datetime(df_ventas["fecha"], errors="coerce")
    print("✔️ Tabla de ventas cargada y fecha convertida a datetime.")

    df_diario = (
        df_ventas.groupby("fecha")
        .agg(
            ventas_totales=("id_venta", "nunique"),
            clientes_activos=("id_cliente", "nunique")
        )
        .reset_index()
    )

    print("\n📌 Primeras filas del dataset diario:")
    print(df_diario.head())

    df_diario["año"] = df_diario["fecha"].dt.year
    df_diario["mes"] = df_diario["fecha"].dt.month
    df_diario["dia"] = df_diario["fecha"].dt.day
    df_diario["dia_semana"] = df_diario["fecha"].dt.weekday
    df_diario["es_fin_de_semana"] = df_diario["dia_semana"].isin([5, 6]).astype(int)
    df_diario["feriado"] = 0

    print("\n✔️ Variables de fecha agregadas al dataset diario.")

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

    print("\nVariables de entrada (X):", features_diarias)
    print("Variable objetivo (y): ventas_totales")

    # Comprobar que hay suficientes filas para dividir
    if len(df_diario) < 2:
        raise ValueError("❌ No hay suficientes registros diarios para entrenar el modelo.")

    X_train, X_test, y_train, y_test = train_test_split(
        X_ventas,
        y_ventas,
        test_size=0.2,
        random_state=42
    )

    print(f"\nTrain diario: {X_train.shape[0]} filas | Test diario: {X_test.shape[0]} filas")

    modelo_diario = LinearRegression()
    modelo_diario.fit(X_train, y_train)
    print("\n✔️ Modelo de regresión diaria entrenado correctamente.")

    y_pred = modelo_diario.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    print("\n📊 Resultados del modelo de ventas diarias:")
    print(f"MAE  diario : {mae:.2f}")
    print(f"RMSE diario : {rmse:.2f}")
    print(f"R²   diario : {r2:.3f}")

    df_diario["ventas_predichas"] = modelo_diario.predict(X_ventas)

    ruta_pred = os.path.join(ruta_base, "ventas_diarias_predichas.xlsx")
    try:
        df_diario.to_excel(ruta_pred, index=False)
        print(f"\n📁 Archivo diario con predicciones generado: {ruta_pred}")
    except Exception as e:
        print(f"❌ Error al exportar predicciones: {e}")

    print("🎉 Fase 8 completada.\n")

    return df_diario


# =========================
# GRÁFICAS FASE 8
# =========================
def graficas_fase8(df_diario: pd.DataFrame):
    """Genera las gráficas de la Fase 8: serie, dispersión y barras por día semana."""
    if df_diario is None or "ventas_predichas" not in df_diario.columns:
        print("⚠️ df_diario no contiene la columna 'ventas_predichas'. Ejecuta primero Fase 8.")
        return

    df_diario_plot = df_diario.sort_values("fecha")

    # Serie temporal
    plt.figure(figsize=(10, 5))
    plt.plot(df_diario_plot["fecha"], df_diario_plot["ventas_totales"], label="Ventas reales")
    plt.plot(df_diario_plot["fecha"], df_diario_plot["ventas_predichas"], linestyle="--", label="Ventas predichas")
    plt.xlabel("Fecha")
    plt.ylabel("Número de ventas")
    plt.title("Ventas diarias: reales vs predichas")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Dispersión clientes vs ventas
    plt.figure(figsize=(7, 5))
    plt.scatter(df_diario["clientes_activos"], df_diario["ventas_totales"])
    plt.xlabel("Clientes activos diarios")
    plt.ylabel("Ventas totales diarias")
    plt.title("Relación entre clientes activos y ventas")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # Dispersión con línea de tendencia
    x = df_diario["clientes_activos"]
    y = df_diario["ventas_totales"]
    if len(x.dropna()) > 1 and len(y.dropna()) > 1:
        coef = np.polyfit(x, y, 1)
        linea = np.poly1d(coef)

        plt.figure(figsize=(7, 5))
        plt.scatter(x, y)
        plt.plot(x, linea(x))
        plt.xlabel("Clientes activos diarios")
        plt.ylabel("Ventas totales diarias")
        plt.title("Relación entre clientes activos y ventas (con línea de tendencia)")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

    # Barras por día de la semana
    promedio_semana = (
        df_diario
        .groupby("dia_semana")["ventas_totales"]
        .mean()
        .reindex([0, 1, 2, 3, 4, 5, 6])
    )
    labels_dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]

    plt.figure(figsize=(7, 5))
    plt.bar(labels_dias, promedio_semana.values)
    plt.xlabel("Día de la semana")
    plt.ylabel("Ventas promedio")
    plt.title("Ventas promedio por día de la semana")
    plt.tight_layout()
    plt.show()


# =========================
# SUBMENÚ ML — Sprint 3 (integrado)
# =========================
def submenu_ml():
    df_diario_global = None  # persistente durante la sesión del submenu

    while True:
        limpiar_pantalla()
        print("=== Submódulo: Modelos ML (Sprint 3) ===")
        print("1. Segmentación de clientes (KMeans)")
        print("2. Predicción de ventas diarias (Regresión)")
        print("3. Gráficas (Regresión)")
        print("4. Volver al menú principal")
        print("========================================")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            limpiar_pantalla()
            try:
                tablas = cargar_y_preparar_datos(RUTA_DATA)
                fase7_segmentacion_clientes(tablas, RUTA_DATA)
            except Exception as e:
                print(f"❌ Error en Fase 7:\n{e}")
            input("\nPresione Enter para continuar...")

        elif opcion == "2":
            limpiar_pantalla()
            try:
                tablas = cargar_y_preparar_datos(RUTA_DATA)
                df_diario_global = fase8_prediccion_ventas(tablas, RUTA_DATA)
            except Exception as e:
                print(f"❌ Error en Fase 8:\n{e}")
            input("\nPresione Enter para continuar...")

        elif opcion == "3":
            limpiar_pantalla()
            try:
                if df_diario_global is None:
                    tablas = cargar_y_preparar_datos(RUTA_DATA)
                    df_diario_global = fase8_prediccion_ventas(tablas, RUTA_DATA)
                graficas_fase8(df_diario_global)
            except Exception as e:
                print(f"❌ Error al generar gráficas:\n{e}")
            input("\nPresione Enter para continuar...")

        elif opcion == "4":
            break
        else:
            print("\nOpción no válida.")
            input("\nPresione Enter para continuar...")


# =========================
# MENÚ PRINCIPAL — MAESTRO (Sprint 1, Sprint 2 y Sprint 3)
# =========================
def main():
    textos_documentacion = {
        '1': ('Tema, problema y solución', submenu_tema_problema_solucion),
        '2': ('Dataset de referencia', lambda: print(dataset_referencia)),
        '3': ('Estructura por tabla', lambda: print(estructura_tablas)),
        '4': ('Escalas de medición', lambda: print(escalas_medicion)),
        '5': ('Sugerencias y mejoras con Copilot', lambda: print(sugerencias_copilot)),
        '6': ('Sprint 2 - Resumen Ejecutivo', submenu_sprint2),
        '7': ('Sprint 3 - Modelos ML', submenu_ml)
    }

    while True:
        limpiar_pantalla()
        print('===========================================')
        print('  MENÚ DE DOCUMENTACIÓN Y HERRAMIENTAS AURELION')
        print('===========================================')
        print('Seleccione una opción para consultar o ejecutar:\n')
        for key, value in textos_documentacion.items():
            print(f'{key}. {value[0]}')
        print('8. Salir')
        print('===========================================')

        opcion_usuario = input('\nIngrese el número de la opción: ').strip()

        if opcion_usuario in textos_documentacion:
            limpiar_pantalla()
            accion = textos_documentacion[opcion_usuario][1]
            try:
                accion()
            except Exception as e:
                print(f"\n❌ Error ejecutando la acción: {e}")
            input('\nPresione Enter para volver al menú...')
        elif opcion_usuario == '8':
            print('\nSaliendo del programa.')
            break
        else:
            print('\nOpción no válida. Intente de nuevo.')
            input('\nPresione Enter para continuar...')


# =========================
# EJECUCIÓN
# =========================
if __name__ == '__main__':
    main()
