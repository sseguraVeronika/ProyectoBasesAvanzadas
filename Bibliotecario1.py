import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymongo import MongoClient 


# Conectar a MongoDB (Antares)
client_antares = MongoClient("mongodb://localhost:27017/")
db_antares = client_antares["biblioteca"]
collection_libros = db_antares["libros"]
collection_usuarios = db_antares["usuarios"]



def agregar_libro():
    titulo = titulo_entry.get() #Nombre de libro
    autor = autor_entry.get()
    genero = genero_entry.get()
    userRating= userRating_entry.get()
    reviews= reviews_entry.get()
    precio= precio_entry.get()
    ano= anno_entry.get()


    libro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "userRating": userRating,
        "reviews": reviews,
        "price": precio,
        "year": ano

    }

    libros_collection.insert_one(libro)
    resultado_label.config(text="Libro agregado con éxito.")

def registroLibro():
        ventana_RegistroLibro = tk.Tk()
        ventana_RegistroLibro.title("Bibliotecario Nivel 1 - Sistema de Biblioteca")
        # Etiquetas y campos de entrada
        titulo_label = tk.Label(ventana_RegistroLibro, text="Título del Libro:")
        titulo_label.pack()
        titulo_entry = tk.Entry(ventana_RegistroLibro)
        titulo_entry.pack()

        autor_label = tk.Label(ventana_RegistroLibro, text="Autor del Libro:")
        autor_label.pack()
        autor_entry = tk.Entry(ventana_RegistroLibro)
        autor_entry.pack()

        genero_label = tk.Label(ventana_RegistroLibro, text="Género del Libro:")
        genero_label.pack()
        genero_entry = tk.Entry(ventana_RegistroLibro)
        genero_entry.pack()

        userRating_label = tk.Label(ventana_RegistroLibro, text="User rating del Libro:")
        userRating_label.pack()
        userRating_entry = tk.Entry(ventana_RegistroLibro)
        userRating_entry.pack()

        reviews_label = tk.Label(ventana_RegistroLibro, text="Reviews del Libro:")
        reviews_label.pack()
        reviews_entry = tk.Entry(ventana_RegistroLibro)
        reviews_entry.pack()

        precio_label = tk.Label(ventana_RegistroLibro, text="Precio del Libro:")
        precio_label.pack()
        precio_entry = tk.Entry(ventana_RegistroLibro)
        precio_entry.pack()

        anno_label = tk.Label(ventana_RegistroLibro, text="Año de publicación del Libro:")
        anno_label.pack()
        anno_entry = tk.Entry(ventana_RegistroLibro)
        anno_entry.pack()

        # Botón para agregar libro
        agregar_button = tk.Button(ventana_RegistroLibro, text="Agregar Libro", command=agregar_libro)
        agregar_button.pack()

        #Etiqueta para mostrar el resultado
        resultado_label = tk.Label(ventana_RegistroLibro, text="")
        resultado_label.pack()
#Buscar Libro
def buscar_libro():
    titulo = titulo_busqueda_entry.get()
    libro = libros_collection.find_one({"titulo": titulo})

    if libro:
        resultado_label.config(text=f"Título: {libro['titulo']}, Autor: {libro['autor']}, Género: {libro['genero']}")
    else:
        messagebox.showerror("Error", "Libro no encontrado")

def ventanaBusquedaLibro(): 
    ventana_busquedaLibro = tk.Tk()
    ventana_busquedaLibro.title("Bibliotecario Nivel 1 - Sistema de Biblioteca- Buscar Libro")

    # Etiquetas y campos de entrada
    titulo_label = tk.Label(ventana_busquedaLibro, text="Título del Libro:")
    titulo_label.pack()
    titulo_entry = tk.Entry(ventana_busquedaLibro)
    titulo_entry.pack()

    # Botón para buscar libro
    buscar_button = tk.Button(ventana_busquedaLibro, text="Buscar Libro", command=buscar_libro)
    buscar_button.pack()

    #Etiqueta para mostrar el resultado
    resultado_label = tk.Label(ventana_busquedaLibro, text="")
    resultado_label.pack() 

#ActualizarLibro 
def actualizarLibro():
    titulo = titulo_entry.get() #Nombre de libro
    autor = autor_entry.get()
    genero = genero_entry.get()
    userRating= userRating_entry.get()
    reviews= reviews_entry.get()
    precio= precio_entry.get()
    ano= anno_entry.get()
    
    nuevo_valor = {
        "$set": {
            "titulo": titulo,
            "autor": autor,
            "genero": genero,
            "userRating": userRating,
            "reviews": reviews,
            "price": precio,
            "year": ano
        }
    }
    collection.update_one({"titulo": titulo}, {"$set": nuevo_valor})

def ventanaActualizarLibro():
    ventana_actualizarLibro = tk.Tk()
    ventana_actualizarLibro.title("Bibliotecario Nivel 1 - Sistema de Biblioteca")
        # Etiquetas y campos de entrada
    titulo_label = tk.Label(ventana_actualizarLibro, text="Título del Libro:")
    titulo_label.pack()
    titulo_entry = tk.Entry(ventana_actualizarLibro)
    titulo_entry.pack()

    autor_label = tk.Label(ventana_actualizarLibro, text="Autor del Libro:")
    autor_label.pack()
    autor_entry = tk.Entry(ventana_actualizarLibro)
    autor_entry.pack()

    genero_label = tk.Label(ventana_actualizarLibro, text="Género del Libro:")
    genero_label.pack()
    genero_entry = tk.Entry(ventana_actualizarLibro)
    genero_entry.pack()

    userRating_label = tk.Label(ventana_actualizarLibro, text="User rating del Libro:")
    userRating_label.pack()
    userRating_entry = tk.Entry(ventana_actualizarLibro)
    userRating_entry.pack()

    reviews_label = tk.Label(ventana_actualizarLibro, text="Reviews del Libro:")
    reviews_label.pack()
    reviews_entry = tk.Entry(ventana_actualizarLibro)
    reviews_entry.pack()

    precio_label = tk.Label(ventana_actualizarLibro, text="Precio del Libro:")
    precio_label.pack()
    precio_entry = tk.Entry(ventana_actualizarLibro)
    precio_entry.pack()

    anno_label = tk.Label(ventana_actualizarLibro, text="Año de publicación del Libro:")
    anno_label.pack()
    anno_entry = tk.Entry(ventana_actualizarLibro)
    anno_entry.pack()

        # Botón para agregar libro
    agregar_button = tk.Button(ventana_actualizarLibro, text="Agregar Libro", command=actualizarLibro)
    agregar_button.pack()

        #Etiqueta para mostrar el resultado
    resultado_label = tk.Label(ventana_actualizarLibro, text="")
    resultado_label.pack()

#Eliminar Libro
def eliminarLibro(): 
    titulo = titulo_entry.get()
    collection.delete_one({"titulo": titulo})

    if result.deleted_count > 0:
        messagebox.showinfo("Éxito", "Libro eliminado correctamente")
    else:
        messagebox.showerror("Error", "Libro no encontrado")
    #limpiar_campos()

def ventanaEliminarLibro():
    ventana_eliminarLibro = tk.Tk()
    ventana_eliminarLibro.title("Bibliotecario Nivel 1 - Sistema de Biblioteca")
        # Etiquetas y campos de entrada
    titulo_label = tk.Label(ventana_eliminarLibro, text="Título del Libro a eliminar:")
    titulo_label.pack()
    titulo_entry = tk.Entry(ventana_eliminarLibro)
    titulo_entry.pack()

    agregar_button = tk.Button(ventana_eliminarLibro, text="Eliminar Libro", command=eliminarLibro)
    agregar_button.pack()

        #Etiqueta para mostrar el resultado
    resultado_label = tk.Label(ventana_eliminarLibro, text="")
    resultado_label.pack()
#Listar Libros 
def obtenerListaLibros():
    for libro in collection.find():
        resultado_listado.insert(tk.END, f"Titulo: {libro['Tittle']}\n")
        resultado_listado.insert(tk.END, f"Autor: {libro['Author']}\n")
        resultado_listado.insert(tk.END, f"Autor: {libro['UserRating']}\n")
        resultado_listado.insert(tk.END, f"Autor: {libro['Reviews']}\n")
        resultado_listado.insert(tk.END, f"Autor: {libro['Price']}\n")
        resultado_listado.insert(tk.END, f"Autor: {libro['anno']}\n")
        resultado_listado.insert(tk.END, f"Autor: {libro['Genre']}\n")
        resultado_listado.insert(tk.END, "\n")

def ventanaListaLibros(): 
    ventana_listaLibro = tk.Tk()
    ventana_listaLibro.title("Lista de Libros")

    command= obtenerListaLibros

    #Etiqueta para mostrar el resultado
    resultado_label = tk.Label(ventana_listaLibro, text="")
    resultado_label.pack()


#Ventana Bibliotecario1
def mostrar_campos(opcion):
    #limpiar_campos()
    if opcion == "Agregar Libro":
        registroLibro()
    elif opcion == "Buscar Libro":
        ventanaBusquedaLibro()
    elif opcion == "Actualizar Libro":
        ventanaActualizarLibro()
    elif opcion == "Eliminar Libro":
        ventanaEliminarLibro()
    elif opcion == "Listar Libros":
        ventanaListaLibros()


# Interfaz para Bibliotecario1
def biblotecario1():

    ventana_bibliotecario1 = tk.Tk()
    ventana_bibliotecario1.title("Bibliotecario1")

    # Etiqueta de selección de operación
    label_operacion = tk.Label(ventana_bibliotecario1, text="Selecciona una operación:")

    # Combobox para seleccionar la operación
    opciones_operacion = ["Selecciona una opción", "Agregar Libro", "Buscar Libro", "Actualizar Libro", "Eliminar Libro", "Listar Libros"]
    combo_operacion = ttk.Combobox(ventana_bibliotecario1, values=opciones_operacion, state="readonly")

    # Botón de operación (se configura con la función correspondiente cuando se elige una opción)
    btn_operacion = tk.Button(ventana_bibliotecario1, text="Realizar Operación", state=tk.DISABLED)

    # Posicionamiento de widgets
    label_operacion.grid(row=0, column=0, columnspan=2)
    combo_operacion.grid(row=1, column=0, columnspan=2)
    btn_operacion.grid(row=4, column=0, columnspan=2)

    # Asignar la función mostrar_campos cuando se seleccione una opción
    combo_operacion.bind("<<ComboboxSelected>>", lambda event: mostrar_campos(combo_operacion.get()))

    # Iniciar la interfaz
    ventana_bibliotecario1.mainloop()

# Función para validar el inicio de sesión del usuario
def validar_sesion():
    usuario = usuario_entry.get()
    contraseña = contraseña_entry.get()

    usuario_encontrado = usuarios_collection.find_one({"username": usuario, "password": contraseña})

    if usuario_encontrado:
        rol = usuario_encontrado["role"]
        if rol == "Bibliotecario1":
            biblotecario1()
        elif rol == "Bibliotecario2":
            #abrir_interfaz_bibliotecario2()
            pass
        elif rol == "Servicios de Cobros":
            #abrir_interfaz_servicios_cobros()
            pass
    else:
        messagebox.showerror("Error de inicio de sesión", "Usuario o contraseña incorrectos.")   

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Sistema de Biblioteca")

# Etiquetas y campos de entrada para usuario y contraseña
usuario_label = tk.Label(ventana_principal, text="Usuario:")
usuario_label.pack()
usuario_entry = tk.Entry(ventana_principal)
usuario_entry.pack()

contraseña_label = tk.Label(ventana_principal, text="Contraseña:")
contraseña_label.pack()
contraseña_entry = tk.Entry(ventana_principal, show="*")  # Para ocultar la contraseña
contraseña_entry.pack()

# Botón para iniciar sesión
iniciar_sesion_button = tk.Button(ventana_principal, text="Iniciar Sesión", command=validar_sesion)
iniciar_sesion_button.pack()

ventana_principal.mainloop()