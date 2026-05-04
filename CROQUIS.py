import streamlit as st
from fpdf import FPDF
from PIL import Image

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="S.I.V. - Módulo de Inspección", layout="wide")

# 2. FUNCIÓN DE GENERACIÓN DE PDF (La que hace el trabajo sucio)
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'POLICÍA DE LA PROVINCIA DE SANTA FE', ln=True, align='C')
        self.ln(5)

def generar_acta_pdf(relato, imagen):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "ACTA DE INSPECCIÓN OCULAR Y CROQUIS", ln=True, align='C')
    pdf.ln(10)
    
    # Insertar Relato
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"RELATO DE LO OBSERVADO:\n{relato}")
    pdf.ln(10)
    
    # Insertar Imagen del Croquis
    if imagen:
        img = Image.open(imagen)
        img_path = "temp_croquis.png"
        img.save(img_path)
        pdf.image(img_path, x=10, w=180)
    
    return pdf.output(dest='S').encode('latin-1', errors='replace')

# 3. INTERFAZ DEL PROGRAMA (Lo que ve el oficial)
st.title("📐 SISTEMA DE INSPECCIÓN Y PLANIMETRÍA")
st.write("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("✍️ Redacción de la Inspección")
    relato_input = st.text_area("Describa detalladamente la escena:", height=300, placeholder="Siendo la hora...")

with col2:
    st.subheader("📸 Registro Visual")
    foto_input = st.file_uploader("Subir foto del Croquis o Escena:", type=['jpg', 'png', 'jpeg'])
    if foto_input:
        st.image(foto_input, caption="Vista previa del croquis", use_container_width=True)

st.write("---")

# 4. BOTÓN DE CIERRE Y DESCARGA
if st.button("💾 GENERAR Y DESCARGAR ACTA INTEGRADA"):
    if relato_input and foto_input:
        pdf_bytes = generar_acta_pdf(relato_input, foto_input)
        st.download_button(
            label="📥 DESCARGAR PDF AHORA",
            data=pdf_bytes,
            file_name="Acta_Inspeccion_Ocular.pdf",
            mime="application/pdf"
        )
        st.success("✅ Acta generada correctamente.")
        st.balloons()
    else:
        st.error("⚠️ Error: Debe completar el relato y subir la foto para generar el acta.")
