# ============================
# IMPORTACIONES Y CONFIGURACIÓN INICIAL
# ============================

import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from texto_a_voz import TextoAVoz  # Importa la clase principal del programa

voz = TextoAVoz()  # Instancia del conversor de texto a voz

# Diccionario con los idiomas disponibles para traducir
idiomas_disponibles = {
    "Español": "es",
    "Inglés": "en",
    "Francés": "fr",
    "Italiano": "it",
    "Alemán": "de",
    "Turco": "tr",
    "Chino (simplificado)": "zh-cn"
}


# ============================
# FUNCIONES DE UTILIDAD PRINCIPALES
# ============================

# Resume el texto actual y actualiza el contenido de la caja de texto
def resumir_texto_gui(caja):
    voz.texto = caja.get("1.0", tk.END).strip()
    resultado = voz.resumir_texto()
    if not resultado:
        messagebox.showwarning("Advertencia", "El texto es demasiado corto para resumir.")
        return
    caja.delete("1.0", tk.END)
    caja.tag_configure("espaciado", lmargin1=20, lmargin2=10, rmargin=60)
    caja.insert("1.0", voz.texto, "espaciado")

# Traduce el texto actual al idioma elegido y lo actualiza en pantalla
def traducir_texto_gui(caja, idioma="en"):
    voz.texto = caja.get("1.0", tk.END).strip()
    voz.traducir_texto(idioma)
    caja.delete("1.0", tk.END)
    caja.tag_configure("espaciado", lmargin1=20, lmargin2=10, rmargin=60)
    caja.insert("1.0", voz.texto, "espaciado")

# Vuelve al menú principal
def volver_menu():
    mostrar_menu_principal()

# Cierra la aplicación
def salir_app():
    ventana.destroy()

# Convierte el contenido actual de la caja a voz y muestra botones adicionales
def convertir_a_voz_desde(caja_texto, tipo_entrada=None):
    texto = caja_texto.get("1.0", tk.END).strip()
    if texto:
        voz.texto = texto
        print(f"[DEBUG] Texto recibido: '{texto}'")
        voz.reproducir()
        if tipo_entrada:
            mostrar_opciones_extras(caja_texto, tipo_entrada)
    else:
        messagebox.showwarning("Advertencia", "Por favor, escribe algo de texto.")


# ============================
# FUNCIONES PARA TRADUCCIÓN CON MENÚ DESPLEGABLE
# ============================        

# Muestra el menú desplegable con idiomas disponibles para traducir
def mostrar_menu_idiomas(caja_texto):
    idioma_var = tk.StringVar(ventana)
    idioma_var.set("Selecciona un idioma")

    opciones = list(idiomas_disponibles.keys())

    menu_idiomas = tk.OptionMenu(
        ventana,
        idioma_var,
        *opciones,
        command=lambda seleccion: traducir_desde_menu(seleccion, idiomas_disponibles, caja_texto, menu_idiomas)
    )
    menu_idiomas.config(bg="#dddddd", width=20)
    menu_idiomas.grid(row=1, column=0, sticky="n", pady=(220, 5))

# Traduce según idioma elegido y oculta el menú una vez traducido
def traducir_desde_menu(seleccion, diccionario_idiomas, caja_texto, menu_widget):
    codigo = diccionario_idiomas.get(seleccion)
    if codigo:
        traducir_texto_gui(caja_texto, codigo)
        menu_widget.destroy()  # oculta el menú de idiomas después de seleccionar


# ============================
# BOTONES EXTRAS TRAS CONVERTIR TEXTO A VOZ
# ============================        

# Variable global para el frame de botones extra
frame_opciones_extras = None
# Muestra botones adicionales: resumir, traducir, volver
def mostrar_opciones_extras(caja_texto, tipo_entrada):
    # Contenedor para todos los botones extra
    frame_botones = tk.Frame(ventana, bg="#222222")
    frame_botones.grid(row=1, column=0, pady=(10, 10))

    # PRIMER GRUPO: Botones principales en orden
    opciones = [
        ("Convertir a Voz", lambda: convertir_a_voz_desde(caja_texto, tipo_entrada), "#000000", "#f1b42f"),
        ("Resumir Texto", lambda: resumir_texto_gui(caja_texto), "#000000", "#ffb84d"),
        ("Traducir a:", lambda: mostrar_menu_idiomas(caja_texto), "#000000", "#66ccff"),
        ("Volver al Menú Principal", volver_menu, "#3A3939", "white")
    ]

    for texto, comando, bg, fg in opciones:
        tk.Button(
            frame_botones,
            text=texto,
            command=comando,
            bg=bg,
            fg=fg,
            activebackground="#222222",
            activeforeground=fg,
            font=("Segoe UI", 10, "bold"),
            relief="raised",
            bd=2,
            width=30
        ).pack(pady=3)

    # SEPARADOR VISUAL
    tk.Label(frame_botones, text=" ", bg="#222222").pack(pady=5)

    # SEGUNDO GRUPO: Reiniciar y Cerrar en la misma línea
    frame_fila_final = tk.Frame(frame_botones, bg="#222222")
    frame_fila_final.pack(pady=10)

    tk.Button(
        frame_fila_final,
        text="Reiniciar entrada actual",
        command=lambda: iniciar_con_entrada(tipo_entrada),
        bg="#ff9900",
        fg="#000000",
        activebackground="#222222",
        activeforeground="#000000",
        font=("Segoe UI", 10, "bold"),
        relief="raised",
        bd=2,
        width=25
    ).grid(row=0, column=0, padx=5)

    tk.Button(
        frame_fila_final,
        text="Cerrar programa",
        command=voz.cerrar_aplicacion,
        bg="#cc4444",
        fg="#000000",
        activebackground="#222222",
        activeforeground="#000000",
        font=("Segoe UI", 10, "bold"),
        relief="raised",
        bd=2,
        width=25
    ).grid(row=0, column=1, padx=5)



# ============================
# FUNCIÓN AUXILIAR PARA VOLVER AL MENÚ PRINCIPAL
# ============================

def resetear_y_volver_menu():
    for widget in ventana.winfo_children():
        widget.destroy()
    mostrar_menu_principal()



# ============================
# FUNCIÓN PRINCIPAL PARA CARGAR DIFERENTES TIPOS DE TEXTO
# ============================

# Carga texto desde entrada manual, archivo o URL según el modo seleccionado
def iniciar_con_entrada(tipo_entrada):
    # Limpia todos los elementos anteriores de la ventana
    for widget in ventana.winfo_children():
        widget.destroy()

# Configura el layout de la ventana principal
    ventana.columnconfigure(0, weight=1)
    ventana.rowconfigure(0, weight=7)
    ventana.rowconfigure(1, weight=3)

    etiquetas = {
        "manual": "Introduce el texto:",
        "archivo": "Texto cargado desde archivo Local:",
        "url": "Texto extraído de URL:"
    }

# Crea el frame contenedor del texto
    frame_texto = tk.LabelFrame(
        ventana,
        text=etiquetas.get(tipo_entrada, "Texto:"),
        bg="#222222",
        fg="#cc9955",
        font=("Segoe UI", 10, "bold"),
        labelanchor="nw",
        bd=1,
        relief="groove"
    )
    frame_texto.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    frame_texto.columnconfigure(0, weight=1)
    frame_texto.rowconfigure(0, weight=1)


# Crea la caja de texto donde se mostrará el contenido
    caja_texto = tk.Text(
        frame_texto,
        height=10,
        width=50,
        bg="#2b2b2b",
        fg="white",
        insertbackground="white",
        borderwidth=0,
        highlightthickness=1,
        highlightbackground="#555555",
        wrap="word",
        font=("Segoe UI", 10, "bold")
    )
    caja_texto.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    caja_texto.tag_configure("espaciado", lmargin1=20, lmargin2=10, rmargin=60)
    caja_texto.bind("<KeyRelease>", lambda event: caja_texto.tag_add("espaciado", "1.0", "end"))


# Entrada manual de texto
    if tipo_entrada == "manual":
       caja_texto.delete("1.0", tk.END)  # Limpia el contenido anterior
       caja_texto.tag_configure("espaciado", lmargin1=20, lmargin2=10, rmargin=60)
       mostrar_opciones_extras(caja_texto, tipo_entrada)

# Carga desde archivo local
    elif tipo_entrada == "archivo":
        archivo = filedialog.askopenfilename(
            title="Seleccionar archivo de texto",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if not archivo or archivo.strip() == "":
            messagebox.showinfo("Cancelado", "No se seleccionó ningún archivo.")
            resetear_y_volver_menu()
            ventana.update()
            return

        voz.leer_archivo(archivo)
        caja_texto.tag_configure("espaciado", lmargin1=20, lmargin2=10, rmargin=60)
        caja_texto.insert("1.0", voz.texto, "espaciado")
        mostrar_opciones_extras(caja_texto, tipo_entrada)

# Carga desde URL
    elif tipo_entrada == "url":
        url = simpledialog.askstring("Introducir URL", "Introduce la URL del artículo:")

    # Verifica si el usuario cerró la ventana o dejó el campo vacío
        if url is None or url.strip() == "":
            messagebox.showinfo("Cancelado", "No se ingresó ninguna URL.")
            resetear_y_volver_menu()
            ventana.update()
            return

        # Si hay URL válida, continuar
        voz.leer_url(url)
        caja_texto.tag_configure("espaciado", lmargin1=20, lmargin2=10, rmargin=60)
        caja_texto.insert("1.0", voz.texto, "espaciado")
        mostrar_opciones_extras(caja_texto, tipo_entrada)


   

# ============================
# MENÚ PRINCIPAL DE LA APLICACIÓN
# ============================

# Carga la pantalla principal con opciones para introducir texto
def mostrar_menu_principal():
    for widget in ventana.winfo_children():
        widget.destroy()

    tk.Label(
        ventana,
        text="Texto a Voz Inteligente: Convertidor + Traductor",
        font=("Segoe UI", 14, "bold"),
        bg="#222222",
        fg="#cc9955",
        pady=20
    ).pack()

    menu_frame = tk.Frame(ventana, bg="#222222")
    menu_frame.pack(pady=20)

    opciones = [
        ("Introducir texto manual", "manual"),
        ("Cargar texto desde archivo Local", "archivo"),
        ("Obtener texto desde URL", "url")
    ]

    for texto, tipo in opciones:
        tk.Button(
            menu_frame,
            text=texto,
            width=30,
            bg="#3c3c3c",
            fg="white",
            relief="flat",
            font=("Segoe UI", 9, "bold"),
            command=lambda t=tipo: iniciar_con_entrada(t)
        ).pack(pady=5)

    tk.Button(
        menu_frame,
        text="Salir",
        command=voz.cerrar_aplicacion,
        width=30,
        bg="#cc4444",
        fg="white",
        relief="flat",
        font=("Segoe UI", 9, "bold"),
    ).pack(pady=(20, 5))


# ============================
# INICIO DE LA APLICACIÓN
# ============================    
if __name__ == "__main__":
# Crea y lanza la ventana principal
    ventana = tk.Tk()
    ventana.title("Texto a Voz Inteligente: Convertidor + Traductor")
    ventana.geometry("650x650")
    ventana.minsize(650, 650)
    ventana.config(bg="#222222")
    mostrar_menu_principal()
    ventana.mainloop()
