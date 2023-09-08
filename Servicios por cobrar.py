from pymongo import MongoClient
from datetime import datetime, timedelta
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Conectar a MongoDB (Sargas)
client_sargas = MongoClient("mongodb://localhost:27017/")
db_sargas = client_sargas["sargas"]
collection_alquileres = db_sargas["alquileres"]
collection_libros = db_sargas["libros"]

# Función para generar el reporte de morosos
def generar_reporte_morosos():
    morosos = []
    hoy = datetime.now()
    
    for alquiler in collection_alquileres.find():
        fecha_alquiler = alquiler["fecha_alquiler"]
        fecha_devolucion = alquiler["fecha_devolucion"]
        estudiante_id = alquiler["estudiante_id"]
        libros_alquilados = alquiler["libros_alquilados"]
        
        # Verificar si el alquiler está vencido
        if fecha_devolucion < hoy:
            dias_vencidos = (hoy - fecha_devolucion).days
            monto_cobrar = 2000 * dias_vencidos  # Cobro por semana de retraso
            
            # Verificar si hay libros con calificación de 4 o más
            for libro in libros_alquilados:
                if libro["user_rating"] >= 4:
                    monto_cobrar += 3500  # Cobro adicional por libros de alta demanda
            
            morosos.append({
                "estudiante_id": estudiante_id,
                "monto_cobrar": monto_cobrar
            })
    
    # Aquí debes implementar la generación del reporte de morosos en formato PDF
    generar_pdf("reporte_morosos.pdf", pagesize=letter)
    # Mostrar un mensaje de éxito
    messagebox.showinfo("Generar Reporte Morosos", "Reporte de morosos generado")

# Función para generar el reporte de libros extraviados
def generar_reporte_extraviados():
    extraviados = []
    hoy = datetime.now()
    un_mes_atras = hoy - timedelta(days=30)
    
    for alquiler in collection_alquileres.find():
        fecha_devolucion = alquiler["fecha_devolucion"]
        libros_alquilados = alquiler["libros_alquilados"]
        
        # Verificar si la fecha de devolución es anterior a un mes atrás
        if fecha_devolucion < un_mes_atras:
            for libro in libros_alquilados:
                extraviados.append({
                    "libro_id": libro["libro_id"],
                    "cantidad_disponible": libro["cantidad_disponible"],
                    "cantidad_extraviada": libro["cantidad_alquilada"],
                    "campus": alquiler["campus"]
                })
    
    generar_pdf("reporte_extraviados.pdf", pagesize=letter)
    messagebox.showinfo("Generar Reporte Extraviados", "Reporte de libros extraviados generado")

# Función para exportar el reporte en formato PDF
def generar_pdf(nombre_archivo, contenido):
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    
    if(nombre_archivo == "reporte_morosos.pdf"):
        # Configuración del título
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, 750, "Reporte de Morosos")
        
        # Contenido del PDF (debes proporcionar el contenido)
        c.setFont("Helvetica", 12)
        y = 700
        for moroso in morosos:
            estudiante_id = moroso["estudiante_id"]
            monto_cobrar = moroso["monto_cobrar"]
            c.drawString(100, y, f"Estudiante ID: {estudiante_id}, Monto a Cobrar: {monto_cobrar} colones")
            y -= 20
        c.showPage()
        c.save()
    else: 
        #Titulo
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, 750, "Reporte de Libros Extraviados")
        #texto 
        c.setFont("Helvetica", 12)
        y = 700

        for extraviado in extraviados:
        libro_id = extraviado["libro_id"]
        cantidad_disponible = extraviado["cantidad_disponible"]
        cantidad_extraviada = extraviado["cantidad_extraviada"]
        campus = extraviado["campus"]
        c.drawString(100, y, f"Libro ID: {libro_id}, Cantidad Disponible: {cantidad_disponible}, Cantidad Extraviada: {cantidad_extraviada}, Campus: {campus}")
        y -= 20
    c.showPage()
    c.save()

# Interfaz para el Servicio de Cobros
ventana_cobros = tk.Tk()
ventana_cobros.title("Servicio de Cobros")

# Botones para generar los reportes y exportar en PDF
btn_reporte_morosos = tk.Button(ventana_cobros, text="Generar Reporte Morosos", command=generar_reporte_morosos)
btn_reporte_extraviados = tk.Button(ventana_cobros, text="Generar Reporte Extraviados", command=generar_reporte_extraviados)
btn_exportar_pdf = tk.Button(ventana_cobros, text="Exportar PDF", command=exportar_pdf)

# Posicionamiento de widgets
btn_reporte_morosos.pack()
btn_reporte_extraviados.pack()
btn_exportar_pdf.pack()

# Iniciar la interfaz
ventana_cobros.mainloop()
