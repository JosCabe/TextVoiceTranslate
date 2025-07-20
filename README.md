![Banner](banner.png)

# 🗣️ Texto a Voz - Conversor Inteligente Multilenguaje

Este proyecto permite convertir texto en voz a partir de diferentes fuentes. Además, puede detectar automáticamente el idioma, traducir el texto a varios idiomas disponibles, generar un resumen (si el texto es largo, concretamente mayor a 99 palabras) y reproducirlo en voz alta usando Google Text-to-Speech (`gTTS`).

---

## 🚀 Características

- ✅ Soporta múltiples fuentes de texto:
  - Texto fijo de prueba
  - Entrada manual del usuario
  - Archivos `.txt` locales
  - Artículos web (URLs)

- 🌍 Detecta automáticamente el idioma del texto.
- 🔁 Traduce el texto a varios idiomas soportados:
  - Español (`es`)
  - Inglés (`en`)
  - Francés (`fr`)
  - Italiano (`it`)
  - Alemán (`de`)
  - Turco (`tr`)
  - Chino simplificado (`zh-cn` o `zh`)

- 🧠 Si el texto tiene más de 100 palabras, puede generar un resumen automático con 5 oraciones clave.
- 🔊 Convierte el texto final en audio (`.mp3`) y lo reproduce automáticamente.

---

## 🛠️ Tecnologías y Librerías Usadas

- **Python 3.7+**
- `gTTS` – Google Text-to-Speech.
- `langdetect` – Para detectar el idioma original.
- `googletrans==4.0.0-rc1` – Para traducir el texto.
- `summa` – Para generar resúmenes automáticos.
- `trafilatura` – Para extraer texto de páginas web.
- `jieba` – Para segmentar el texto en Chino.


---

## ▶️ Cómo usarlo

1. Asegúrate de tener Python 3 instalado.  
2. Descarga este repositorio y ubica tu consola en la carpeta del proyecto.  
3. Asegúrate de tener FFmpeg instalado y extraído.  
   Puedes descargarlo desde:  
   🔗 [**Descargar TextVoiceTranslate (.exe) desde Google Drive**](https://drive.google.com/file/d/1OUrM65n-6eo5ASkjdiC6IIVj5n9041Sk/view?usp=drive_link)

4. Instala las dependencias ejecutando:

   ```bash
   pip install -r requirements.txt

---

## 🖥️ Descargar la aplicación ejecutable (.exe)

¿Quieres probar la app sin instalar nada más?  
Puedes descargar directamente el archivo `.exe` para Windows desde el siguiente enlace:

📥 [Descargar ejecutable desde Google Drive](https://drive.google.com/file/d/1kKdr9-faE68NiQ7Y0KGqxx0NDlYBnZyu/view?usp=sharing)


> ⚠️ Recomendación: si Windows bloquea la ejecución, haz clic derecho en el archivo → Propiedades → Marca "Permitir" y luego ejecuta normalmente.



## 👨‍💻 Autor

Proyecto creado por José Cabello Romero como ejercicio práctico de programación con Python.  
¡Libre de usar, modificar y mejorar!

---

## 🎯 Objetivo del Proyecto

Este proyecto nació como un reto personal para integrar diferentes librerías de Python en una aplicación funcional y útil.  
La idea es que cualquier usuario, sin conocimientos técnicos, pueda introducir texto, traducirlo y escucharlo fácilmente.

## 🔮 Posibles mejoras futuras

- Añadir una interfaz gráfica con Tkinter o PyQt.
- Permitir guardar múltiples audios generados.
- Integrar APIs externas para voces más naturales.
- Exportar resúmenes a PDF o TXT automáticamente.

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT.  
Puedes usarlo libremente para fines personales o educativos.


