import streamlit as st
import json
from fpdf import FPDF
import base64

def crear_pdf_final(imagen_croquis):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "ANEXO: CROQUIS DE INSPECCIÓN OCULAR", ln=True, align='C')
    
    # Insertar el croquis generado por la IA
    # Usamos la imagen que ya está en memoria
    pdf.image(imagen_croquis, x=10, y=30, w=180)
    
    # Retorno binario directo para evitar AttributeError en Python 3.14
    return pdf.output()

st.title("Módulo de Recepción e Impresión - SVI")

# 1. CARGA DEL ARCHIVO JSON (Generado por la IA)
archivo_json = st.file_uploader("Cargar JSON del hecho", type=['json'])

if archivo_json:
    # Leer el contenido del JSON
    datos_hecho = json.load(archivo_json)
    st.success("✅ Datos del hecho cargados correctamente.")
    
    # Mostramos un resumen rápido para el actante
    st.info(f"Procedimiento: {datos_hecho.get('tipo', 'N/A')} | Origen: {archivo_json.name}")

    # Necesitamos la imagen del croquis para el PDF
    # (Asumiendo que se carga o se referencia aquí)
    archivo_imagen = st.file_uploader("Cargar imagen del croquis (AI)", type=['png', 'jpg', 'jpeg'])

    if archivo_imagen:
        st.image(archivo_imagen, caption="Croquis listo para procesar")

        st.markdown("---")
        col1, col2 = st.columns(2)

        # BOTÓN 1: VIAJAR AL ACTANTE (Lógica de integración SVI)
        with col1:
            if st.button("🚀 Enviar datos al Actante"):
                # Aquí iría tu lógica de st.session_state o base de datos
                st.session_state['datos_listos'] = True
                st.toast("Datos enviados al bloque del actante")

        # BOTÓN 2: DESCARGA PDF PARA IMPRESIÓN
        with col2:
            pdf_bytes = crear_pdf_final(archivo_imagen)
            st.download_button(
                label="📥 Descargar PDF para Impresión",
                data=pdf_bytes,
                file_name=f"Croquis_{archivo_json.name}.pdf",
                mime="application/pdf"
            )
