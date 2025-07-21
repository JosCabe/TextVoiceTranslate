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

- 🧠 Si el texto tiene más de 99 palabras, puede generar un resumen automático con oraciones clave.
- 🔊 Convierte el texto final en audio (`.mp3`) y lo reproduce automáticamente.

---

## 🛠️ Tecnologías y Librerías Usadas

- **Python 3.7+**
- `gTTS` – Google Text-to-Speech.
- `langdetect` – Para detectar el idioma original.
- `googletrans==4.0.0-rc1` – Para traducir el texto.
- `summa==1.2.0` – Para generar resúmenes automáticos.
- `trafilatura` – Para extraer texto de páginas web.
- `jieba` – Para segmentar el texto en Chino.


---

## ▶️ Cómo usarlo

1. Asegúrate de tener Python 3 instalado.  
2. Descarga este repositorio y ubica tu consola en la carpeta del proyecto.  
3. Asegúrate de tener FFmpeg instalado y extraído.  
   Puedes descargarlo desde:  
   🔗 [🔗 Descargar desde Google Drive](https://drive.google.com/file/d/12YH9ncFVZ3QSuckfAWTPDTzqd_26SMr9/view?usp=drive_link)

4. Instala las dependencias ejecutando:

   ```bash
   pip install -r requirements.txt

---

## 🖥️ Descargar la aplicación ejecutable (.exe)

¿Quieres probar la app sin instalar nada más?  
Puedes descargar directamente el archivo `.exe` para Windows desde el siguiente enlace:

📥[Descargar ejecutable de la app de Texto a Voz](https://drive.google.com/file/d/12YH9ncFVZ3QSuckfAWTPDTzqd_26SMr9/view?usp=sharing)


### 🔐 Aviso de seguridad al ejecutar la aplicación

Es posible que al ejecutar `interfaz_gui.exe`, **Windows muestre un mensaje de advertencia** como:  
_"Windows protegió su PC"_ o _"Esta aplicación no es de confianza"_.

Esto ocurre porque el ejecutable ha sido creado por un desarrollador independiente y **no está firmado digitalmente por Microsoft**.  
Es totalmente normal en proyectos personales o en desarrollo.

#### ✅ ¿Qué hacer si aparece este mensaje?

1. Haz clic en **"Más información"** (en azul).
2. Luego haz clic en **"Ejecutar de todas formas"**.

> ⚠ La aplicación **no contiene ningún virus ni realiza ninguna conexión externa**, y todos los procesos ocurren en local.  
> Solo genera y reproduce un archivo de audio en tu ordenador, sin subir nada a internet.

Puedes usarla con total confianza mientras sigo mejorando su funcionalidad.


### 🎧 Nota importante sobre la reproducción de audio:

- **Ubicación del archivo generado**:  
Al seleccionar la opción "Convertir a audio", el archivo `.mp3` se genera automáticamente en la **misma carpeta donde se encuentra el ejecutable. Para reproducirlo después de haber seleccionado que: no quiere eliminar el archivo.mp3, tiene que ir a la ruta comentada anteriormente (misma carpeta donde se encunetra el ejecutable)
`interfaz_gui.exe`**.

---

## 👨‍💻 Autor

Proyecto creado por José Cabello Romero como ejercicio práctico de programación con Python.  
¡Libre de usar, modificar y mejorar!

---

## 🎯 Objetivo del Proyecto

Este proyecto nació como un reto personal para integrar diferentes librerías de Python en una aplicación funcional y útil.  
La idea es que cualquier usuario, sin conocimientos técnicos, pueda introducir texto, traducirlo y escucharlo fácilmente.

## 🔮 Posibles mejoras futuras

- Permitir guardar múltiples audios generados.
- Integrar APIs externas para voces más naturales.
- Exportar resúmenes a PDF o TXT automáticamente.

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT.  
Puedes usarlo libremente para fines personales o educativos.


