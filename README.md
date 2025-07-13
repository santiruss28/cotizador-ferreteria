# 🤖 Cotizador IA para Ferretería vía WhatsApp

Este proyecto es un sistema de cotización automática que permite a una ferretería responder consultas de productos desde WhatsApp utilizando inteligencia artificial, procesamiento de lenguaje natural y búsqueda inteligente en un catálogo de más de 22.000 productos.

## 🧱 Tecnologías utilizadas

- [Dify](https://dify.ai/): Plataforma de creación de asistentes de IA.
- [Replit](https://replit.com/): Plataforma gratuita para alojar y ejecutar webhooks.
- [Flask](https://flask.palletsprojects.com/): Framework liviano de Python para la creación del webhook.
- [RapidFuzz](https://maxbachmann.github.io/RapidFuzz/): Librería para búsqueda por similitud (fuzzy search).
- [Pandas](https://pandas.pydata.org/): Manejo eficiente del listado de productos.
- [OpenAI GPT / LLM]: Para interpretar las consultas de los clientes.
- Formato `CSV` o `Google Sheets`: como base de conocimiento para precios.

---

## 🚀 ¿Qué hace este proyecto?

1. El cliente escribe un mensaje por WhatsApp con una consulta de productos.
2. Dify interpreta el mensaje y extrae:
   - Los ítems consultados.
   - El segmento al que podrían pertenecer (opcional).
3. Se envía una solicitud HTTP a un webhook alojado en Replit.
4. El webhook busca coincidencias por similitud en un archivo `listado.csv`.
5. Devuelve la cotización completa (precio contado y precio tarjeta) para cada ítem encontrado.
6. La IA formatea y responde por WhatsApp al cliente.

---

## 🧠 Estructura esperada del archivo `listado.csv`

```csv
ID Producto,SEGMENTO,Descripcion,Precio Contado,Precio Tarjeta
1234,TERMOTANQUE,TERMOTANQUE ELECTRICO 50L MARCA X,100000,120000
1235,GAS,ANODO MAGNESIO TERMOTANQUE PEISA,5000,6000
...
