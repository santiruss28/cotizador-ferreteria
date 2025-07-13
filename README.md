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

##🧪 Ejemplo de solicitud desde Dify al webhook
```js
{
  "consultas": [
    {"consulta": "termotanque eléctrico", "segmento": "TERMOTANQUE"},
    {"consulta": "roscas con tuercas", "segmento": "GAS, IPS, VALVULA, LLAVE"}
  ]
}
```


##🧩 Prompt del LLM
Tu único objetivo es identificar los ítems que el cliente solicita en la query y transformarlos a un determinado formato.

Deberás crear un listado de todos los productos que identificaste en la consulta del cliente y el segmento en cual cae la consulta y entregarlos en formato JSON con la siguiente forma:

```js
{
  "consultas": [
    {"consulta": "mouse", "segmento": "Periféricos"},
    {"consulta": "laptop", "segmento": "Computadoras"},
    {"consulta": "cable", "segmento": ""}
  ]
}
```

IMPORTANTE:
- El campo `segmento` lo deberás detectar automáticamente utilizando la base de conocimientos. 
- Si no está claro, dejalo vacío.
- La salida debe ser solo el JSON sin markdown ni texto adicional.
🧪 Endpoint del webhook

POST /cotizar
Host: https://<tu-url-de-replit>.replit.app
Content-Type: application/json
Body esperado:

```js
{
  "consultas": [
    {"consulta": "bomba de vacío", "segmento": ""},
    {"consulta": "roscas con tuercas", "segmento": "GAS, IPS, VALVULA, LLAVE"}
  ]
}
```

📄 JSON Schema utilizado
```js
{
  "name": "producto_consulta_segmento",
  "description": "Identifica productos mencionados en la consulta del cliente y asigna segmentos si es posible.",
  "strict": true,
  "schema": {
    "type": "object",
    "properties": {
      "consultas": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "consulta": { "type": "string" },
            "segmento": { "type": "string" }
          },
          "required": ["consulta", "segmento"],
          "additionalProperties": false
        }
      }
    },
    "required": ["consultas"],
    "additionalProperties": false
  }
}
```
🛠 ¿Qué sigue?
 Mejorar el reconocimiento de ítems compuestos o consultas múltiples.

 Agregar lógica de descuento o promociones personalizadas.

 Integrar lógica para sumar totales de múltiples ítems.

 Incorporar otras fuentes de datos (como stock en tiempo real o imágenes).

📬 Contacto
Este proyecto fue desarrollado por Santiago. Para consultas o mejoras, podés abrir un issue o un pull request.

```csv
ID Producto,SEGMENTO,Descripcion,Precio Contado,Precio Tarjeta
1234,TERMOTANQUE,TERMOTANQUE ELECTRICO 50L MARCA X,100000,120000
1235,GAS,ANODO MAGNESIO TERMOTANQUE PEISA,5000,6000
...
