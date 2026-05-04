import streamlit as st
import json
from fpdf import FPDF

st.title("Módulo de Recepción e Impresión - SVI")

# 1. RECEPCIÓN DEL JSON (Lo que envía el policía de calle)
archivo_json = st.file_uploader("Cargar JSON del hecho", type=['json'])

if archivo_json:
    # El actante abre el bloque de datos
    datos = json.load(archivo_json)
    st.success(f"Datos recibidos: {datos.get('archivo_origen', 'Sin nombre')}")
    
    # 2. CARGA DEL CROQUIS COMPLEMENTARIO
    foto_croquis = st.file_uploader("Cargar Imagen del Croquis para el Acta", type=['jpg', 'png', 'jpeg'])
    
    if foto_croquis:
        st.image(foto_croquis, caption="Vista previa para impresión")
        
        # 3. IMPRESIÓN DEL PDF (El actante genera el documento final)
        if st.button("Generar PDF para el Sumario"):
            pdf = FPDF()
            pdf.add_page()
            
            # Encabezado técnico automático
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, f"ANEXO: CROQUIS POLICIAL - {datos.get('modulo', 'SVI')}", ln=True, align='C')
            
            # Insertar la imagen del croquis
            pdf.image(foto_croquis, x=10, y=30, w=180)
            
            # Output binario directo (Corrección AttributeError)
            pdf_bytes = pdf.output()
            
            st.download_button(
                label="📥 Descargar PDF Final",
                data=pdf_bytes,
                file_name="acta_inspeccion_ocular.pdf",
                mime="application/pdf"
            )
