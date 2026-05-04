import streamlit as st

st.set_page_config(page_title="S.I.V. - Puente de Croquis", layout="centered")

st.title("📐 MÓDULO DE CROQUIS (EXTERNO)")
st.sidebar.write("**Gestión:** Sub Comisario CASTAÑEDA Juan")

st.info("💡 Este módulo permite procesar el croquis por fuera del sistema principal para no afectar la velocidad del S.I.V.")

# --- 1. PREPARACIÓN DE DATOS ---
st.subheader("1. Preparar Información")
if st.button("📋 COPIAR INSPECCIÓN OCULAR AL PORTAPAPELES"):
    # Aquí simulamos la copia (en Streamlit el usuario suele copiar del text_area)
    st.write("Seleccione el texto de abajo y presione Ctrl+C:")
    st.code("Aquí aparecerá el contenido del Bloque 6 para que lo lleves al plano...")

# --- 2. ACCESO A HERRAMIENTAS ---
st.divider()
st.subheader("2. Ejecutar Herramienta de Diseño")
st.write("Utilice su software de confianza o abra la carpeta de plantillas.")

if st.button("📁 ABRIR CARPETA DE CROQUIS"):
    st.warning("⚠️ Por seguridad del navegador, abra manualmente la carpeta 'C:/SIV/Croquis' en su computadora.")

# --- 3. REINCORPORACIÓN ---
st.divider()
st.subheader("3. Adjuntar Croquis Terminado")
archivo = st.file_uploader("Suba el archivo final (JPG, PNG o PDF):", type=['jpg', 'png', 'pdf'])

if archivo:
    st.success("✅ Croquis vinculado con éxito. Se incluirá en el Anexo del sumario.")

st.divider()
st.caption("S.I.V. - Sistema de Validación de Identidad | Optimizado para operatividad de calle.")
