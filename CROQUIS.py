import streamlit as st
import json
from fpdf import FPDF
import io

# 1. Función para armar el PDF "CROQUIS DEMOSTRATIVO"
def generar_pdf_croquis(imagen_bytes):
    pdf = FPDF()
    pdf.add_page()
    
    # Encabezado Oficial
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "POLICIA DE LA PROVINCIA DE SANTA FE", ln=True, align='C')
    pdf.ln(10)
    
    # Título
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "CROQUIS DEMOSTRATIVO", ln=True, align='C')
    pdf.ln(10)
    
    # Insertar la imagen
    if imagen_bytes:
        img_temp = io.BytesIO(imagen_bytes.getvalue())
        # fpdf2 maneja BytesIO directamente
        pdf.image(img_temp, x=10, w=190)
    
    # Pie de autoría
    pdf.set_y(-30)
    pdf.set_font("Arial", 'I', 10)
    pdf.cell(0, 10, "Documento generado por Sub-Comisario Castañeda Juan", align='R')
    
    # LA CORRECCIÓN ESTÁ ACÁ: fpdf2 en modo 'S' ya devuelve bytes
    return pdf.output() 

# --- INTERFAZ ---
st.title("📐 Módulo Croquis S.I.V.")

img_file = st.file_uploader("🖼️ Pegar o subir imagen del croquis:", type=['jpg', 'png', 'jpeg'])

if img_file:
    st.image(img_file, caption="Imagen cargada", use_container_width=True)
    st.write("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📤 Enviar JSON al Actante"):
            datos_json = {
                "titulo": "CROQUIS DEMOSTRATIVO",
                "autor": "Sub-Comisario Castañeda Juan",
                "fecha": "2026"
            }
            st.json(datos_json)
            st.success("✅ Datos vinculados")

    with col2:
        # Generar PDF con la corrección
        pdf_bytes = generar_pdf_croquis(img_file)
        st.download_button(
            label="📥 Descargar PDF (CROQUIS DEMOSTRATIVO)",
            data=pdf_bytes, # Ahora pdf_bytes tiene el formato correcto
            file_name="Croquis_Demostrativo.pdf",
            mime="application/pdf"
        )
