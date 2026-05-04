import streamlit as st
from PIL import Image, ImageOps, ImageEnhance
import pandas as pd
import io

st.set_page_config(page_title="S.I.V. - ANEXO CROQUIS", layout="wide")

st.title("📐 MÓDULO DE CROQUIS PLANIMÉTRICO")
st.sidebar.write("**Responsable:** Sub Comisario CASTAÑEDA Juan")

# --- 1. GENERADOR DE LEYENDA AUTOMÁTICA ---
st.header("1. Referencias Técnicas")
st.info("El sistema detectará los objetos del acta para armar la leyenda del dibujo.")
texto_acta = st.text_area("Pegue el texto de la Inspección Ocular aquí:", height=100)

# Diccionario táctico
vocabulario = ["MOTO", "AUTO", "ARMA", "VAINA", "CUERPO", "DROGA", "BALANZA", "DINERO", "CELULAR", "BICICLETA"]
detectados = [obj for obj in vocabulario if obj.lower() in texto_acta.lower()]

if detectados:
    st.write("**TABLA DE REFERENCIAS (Para el Croquis):**")
    # Creamos la tabla que el oficial usará para numerar su dibujo (1, 2, 3...)
    df_leyenda = pd.DataFrame({
        "NRO": [i+1 for i in range(len(detectados))],
        "ELEMENTO": detectados
    })
    st.table(df_leyenda)
    st.caption("💡 Instrucción: En su dibujo a mano, numere los objetos según esta tabla.")

# --- 2. DIGITALIZACIÓN DEL DIBUJO A MANO ---
st.divider()
st.header("2. Captura de Croquis (Libreta/Papel)")
archivo_foto = st.file_uploader("📷 Suba la foto del croquis o use la cámara:", type=['jpg', 'png', 'jpeg'])

if archivo_foto:
    col1, col2 = st.columns(2)
    
    img_original = Image.open(archivo_foto)
    
    with col1:
        st.image(img_original, caption="Foto Original", use_container_width=True)
    
    with col2:
        # --- PROCESAMIENTO TÉCNICO ---
        # 1. Convertir a Gr escala de grises
        proc = ImageOps.grayscale(img_original)
        # 2. Aumentar contraste para limpiar el fondo y resaltar el trazo
        enhancer = ImageEnhance.Contrast(proc)
        proc = enhancer.enhance(2.5) 
        # 3. Ajustar brillo para blanquear el papel
        bright = ImageEnhance.Brightness(proc)
        proc = bright.enhance(1.2)
        
        st.image(proc, caption="Resultado Digitalizado (Filtro Judicial)", use_container_width=True)

    # --- 3. FINALIZACIÓN ---
    st.divider()
    if st.button("🏁 VALIDAR Y ADJUNTAR AL SUMARIO"):
        st.success("✅ Croquis procesado con éxito. Se ha vinculado a las referencias del Acta.")
        st.balloons()
