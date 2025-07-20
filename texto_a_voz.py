import os
import platform
import subprocess
import trafilatura
import jieba
import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
from langdetect import detect
from googletrans import Translator
from summa.summarizer import summarize


class TextoAVoz:
    """
    Objeto que gestiona la conversión de texto a voz a partir de diferentes fuentes:
    texto fijo, entrada por teclado, archivos locales y artículos web.
    """

    def __init__(self):
        self.texto = "" #Atributo donde se guarda el texto a leer
        self.ruta_ffmpeg = "D:\\ffmpeg-7.1.1-essentials_build\\bin\\ffmpeg.exe"


    #Método texto entrada por teclado
    def leer_input(self):
        self.texto = input("De Texto a Voz, introduce el texto: ") 
       

    #Método texto archivos locales
    def leer_archivo(self, ruta):
        try:
           with open(ruta, "r", encoding="utf-8") as archivo:
               self.texto = archivo.read()              
        except FileNotFoundError:
            print("archivo no encontrado.")

    #Método texto artículos web
    def leer_url(self, url):
        try:
            downloaded = trafilatura.fetch_url(url)
            if downloaded:
                self.texto = trafilatura.extract(downloaded, include_comments = False)
                return "Texto extraído correctamente de la URL."
            else:    
                self.texto = ""
                return "No se pudo descargar el contenido de la URL."
        except Exception as e:
            print(f"Error al procesar la URL: {e}")

    #Método texto pasado a audio
    def reproducir(self):
        try:
            print("\n🎙️ INICIANDO CONVERSIÓN DE TEXTO A VOZ...")

            # Detección de idioma
            idioma_detectado = detect(self.texto)
            idioma_tag = idioma_detectado[:2].upper()
            print(f"🌍 Idioma detectado: {idioma_tag}")

            # Generar audio original
            self.audio = gTTS(text=self.texto, lang=idioma_detectado)
            nombre_base = f"Audio_{idioma_tag}.mp3"
            self.audio.save(nombre_base)
            print(f"✅ Audio generado como '{nombre_base}'. Reproduciendo ahora...\n")

            # Definir rutas
            ruta_completa_original = os.path.abspath(nombre_base)
            nombre_acelerado = f"Idioma detectado - {idioma_tag}.mp3"
            ruta_completa_acelerado = os.path.abspath(nombre_acelerado)


            # Ejecutar FFmpeg con subprocess
            print(f"[DEBUG] Ejecutando FFmpeg para acelerar audio...")
            subprocess.run([
                self.ruta_ffmpeg,
                "-y",
                "-i", ruta_completa_original,
                "-filter:a", "atempo=1.25",
                "-id3v2_version", "3",
                "-metadata", f"title=Idioma detectado: {idioma_tag}",
                "-metadata", f"artist=Texto a Voz Inteligente",
                "-metadata", f"album=Conversión Rápida",
                "-metadata", f"genre=Voz Sintética",
                "-metadata", f"track=1",
                ruta_completa_acelerado
            ], check=True)

            # Verificar que se generó el archivo
            if os.path.exists(ruta_completa_acelerado):
                print(f"⚡ Audio acelerado generado correctamente como: {ruta_completa_acelerado}")
                self.ruta_audio = ruta_completa_acelerado
            else:
                raise FileNotFoundError(f"No se encontró el archivo generado: {ruta_completa_acelerado}")

            # Ventana emergente para preguntar si eliminar el archivo original
            tk.Tk().withdraw()  # Oculta la ventana principal
            respuesta = messagebox.askyesno("Eliminar archivo original", f"¿Deseas eliminar el archivo '{nombre_base} despues de ser reproducido'?")

            if respuesta:
                os.remove(ruta_completa_original)
                print(f"🧹 Archivo original '{nombre_base}' eliminado.")
            else:
                print("✅ Archivo original conservado.")

            # Reproducción automática
            print("🎯 Intentando reproducir el audio...")
            sistema = platform.system()
            print(f"🖥️ Sistema operativo detectado: {sistema}")
            if sistema == "Windows":
                ruta_reproducible = os.path.normpath(self.ruta_audio)
                os.startfile(ruta_reproducible)
            elif sistema == "Darwin":  # macOS
                subprocess.call(["afplay", self.ruta_audio])
            elif sistema == "Linux":
                subprocess.call(["xdg-open", self.ruta_audio])
            else:
                print("❌ Reproducción automática no soportada en este sistema.")

        except Exception as e:
            print(f"❌ Error al generar o reproducir el audio: {e}")


    #Método para resumir el texto >= 100 palabras
    def resumir_texto(self, min_palabras=100, num_oraciones=5):
        idioma_actual = detect(self.texto)#Si el idioma es chino, segmentamos con jieba

        if idioma_actual.startswith("zh"):
            print("🔍 Segmentando texto en chino con jieba...")
            palabras_chinas = list(jieba.cut(self.texto))
            texto_segmentado = " ".join(palabras_chinas)
        else:
             texto_segmentado = self.texto
        
        if len(texto_segmentado.split()) < min_palabras:    #Ya podemos comprobar la cantidad de palabras correctamente
            print(f"\n⚠️ El texto tiene menos de {min_palabras} palabras. No se puede resumir.")
            return False

        print(f"\n🧠 Generando resumen...")
        resumen = summarize(self.texto, split = True)
        if resumen:
            resumen_texto = " ".join(resumen[:num_oraciones])
            self.texto = resumen_texto
            idioma_actual = detect(self.texto).upper()
            print(f"\n🔽🔽🔽 RESUMEN EN {idioma_actual} 🔽🔽🔽\n" + "-"*30)
            print(self.texto)
            return idioma_actual

   

    #Método para traducir el texto a otro idioma
    def traducir_texto(self, idioma_destino="en"):
        idioma_detectado = detect(self.texto)
        print(f"\n🌐 Traduciendo del idioma {idioma_detectado.upper()} a {idioma_destino.upper()}...")

        try:
            traductor = Translator()
            traduccion = traductor.translate(self.texto, src=idioma_detectado, dest=idioma_destino)
            self.texto = traduccion.text  # Sobrescribimos el texto con el traducido
            print("✅ Traducción completada.")  
            return idioma_detectado          
        except Exception as e:
            print(f"❌ Error al traducir el texto: {e}")
       
    #Método para contar palabras para determinar si hacer o no el resumen.
    def contar_palabras(self):
        idioma = detect(self.texto)
        if idioma.startswith("zh"):
            palabras = list(jieba.cut(self.texto))
            return len(palabras)
        else:
            return len(self.texto.split())
        








# -------------------------------------------------------------------------------------
# Descripción del programa:
# Este script permite ingresar texto desde diferentes fuentes (fijo, manual, archivo o URL),
# detecta su idioma automáticamente, da la opción de traducirlo a varios idiomas soportados
# (es, en, fr, it, de), puede generar un resumen si el texto tiene más de 100 palabras,
# y convierte el texto final (original, resumido o traducido) en audio utilizando gTTS.
# -------------------------------------------------------------------------------------




"""
---------------------------------------------------------------
Este script permite convertir texto a voz desde distintas fuentes:
- Texto fijo
- Entrada manual
- Archivos locales
- Artículos extraídos desde una URL

Funcionalidades adicionales:
- Resume automáticamente textos largos (más de 100 palabras)
- Traduce el texto a diferentes idiomas (es, en, fr, it, de)
- Reproduce el texto con voz usando gTTS

El flujo se adapta según las decisiones del usuario:
- Puede elegir si quiere un resumen del texto.
- Puede traducir el contenido antes o después del resumen.
- Ofrece una experiencia fluida con mensajes claros y voz generada.

Autor: José Cabello Romero
Fecha: 19/07/2025
---------------------------------------------------------------
"""

