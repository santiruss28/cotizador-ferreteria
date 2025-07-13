from fastapi import FastAPI, Request
import pandas as pd
from rapidfuzz import fuzz

app = FastAPI()

# Cargar listado de productos
csv_path = "listado.csv"
df = pd.read_csv(csv_path)


@app.post("/cotizar")
async def cotizar(request: Request):
    data = await request.json()
    productos = data.get("productos", [])

    resultados = []
    total_contado = 0
    total_tarjeta = 0

    for nombre in productos:
        mejor_match = None
        mejor_score = 0

        for _, row in df.iterrows():
            descripcion = str(row["Descripcion"])
            score = fuzz.partial_ratio(nombre.lower(), descripcion.lower())

            if score > mejor_score:
                mejor_score = score
                mejor_match = row

        if mejor_score > 70 and mejor_match is not None:  # UMBRAL AJUSTABLE
            resultados.append({
                "entrada_cliente": nombre,
                "descripcion_match": mejor_match["Descripcion"],
                "precio_contado": mejor_match["Precio Contado"],
                "precio_tarjeta": mejor_match["Precio Tarjeta"],
                "score": mejor_score
            })
            total_contado += float(
                str(mejor_match["Precio Contado"]).replace(",", "").replace(
                    ".", ""))
            total_tarjeta += float(
                str(mejor_match["Precio Tarjeta"]).replace(",", "").replace(
                    ".", ""))

    return {
        "productos_encontrados": resultados,
        "total_precio_contado": total_contado,
        "total_precio_tarjeta": total_tarjeta
    }
