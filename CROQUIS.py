import streamlit as st
import json
from fpdf import FPDF
import base64

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="S.I.V. - Generador de Actas", layout="wide")

def crear_pdf(texto, imagen_bytes):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "ACTA DE INSPECCIÓN OCULAR Y CROQUIS", ln=True, align='C')
    pdf.set_font("Arial", 'I', 10)
    pdf.cell(0, 10, "Creado por Sub Comisario Castañeda Juan", ln=True, align='R')
    pdf.ln(10)
    
    # Texto de la inspección
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"INSPECCIÓN OCULAR:\n{texto}")
    pdf.ln(10)
    
    # Imagen del croquis generado
    if imagen_bytes:
        with open("temp_croquis.png", "wb") as f:
            f.write(imagen_bytes.getbuffer())
        pdf.image("temp_croquis.png", x=10, w=180)
    
    return pdf.output(dest='S').encode('latin-1', errors='replace')

# --- INTERFAZ ---
st.title("🚓 S.I.V. - Finalización de Bloque")
st.write("Pegue el resultado obtenido de la IA para generar los archivos oficiales.")

col1, col2 = st.columns(2)

with col1:
    texto_final = st.text_area("Relato Final de la Inspección:", height=300)

with col2:
    foto_croquis = st.file_uploader("Subir el Croquis generado por la IA:", type=['jpg', 'png', 'jpeg'])
    if foto_croquis:
        st.image(foto_croquis, caption="Croquis listo para acta")

st.write("---")

if st.button("🚀 GENERAR ARCHIVOS (JSON Y PDF)"):
    if texto_final and foto_croquis:
        # 1. GENERAR JSON
        datos_json = {
            "autor": "Sub Comisario Castañeda Juan",
            "inspeccion": texto_final,
            "estado": "Validado"
        }
        json_str = json.dumps(datos_json, indent=4)
        
        # 2. GENERAR PDF
        pdf_data = crear_pdf(texto_final, foto_croquis)
        
        # 3. DESCARGAS
        st.success("✅ Archivos generados con éxito.")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.download_button("📥 Descargar PDF Oficial", data=pdf_data, file_name="Acta_Final.pdf", mime="application/pdf")
        with col_b:
            st.download_button("📥 Descargar Datos JSON", data=json_str, file_name="datos_inspeccion.json", mime="application/json")
        st.balloons()
    else:
        st.error("⚠️ Falta el texto o la imagen del croquis.")
