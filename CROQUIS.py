import streamlit as st
import re

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="S.I.V. - Generador de Croquis", layout="wide")

st.title("📐 CROQUIS PLANIMÉTRICO DINÁMICO")
st.sidebar.write("**Autoría:** Sub Comisario CASTAÑEDA Juan")

# --- MOTOR DE DETECCIÓN (EL CEREBRO) ---
CATALOGO = {
    "Ambientes": ["dormitorio", "habitación", "pieza", "cocina", "comedor", "living", "baño", "patio", "cochera"],
    "Accesos": ["puerta", "ventana", "reja", "portón", "persiana"],
    "Objetos de Interés": ["placard", "caja fuerte", "televisor", "cama", "cajón", "escritorio", "alacena"],
    "Indicios/Rastros": ["vaina", "mancha hemática", "vidrio", "huella", "frenada", "impacto"]
}

def escanear_texto(texto):
    detectados = {cat: [] for cat in CATALOGO.keys()}
    texto_limpio = texto.lower()
    for categoria, palabras in CATALOGO.items():
        for p in palabras:
            if re.search(rf"\b{p}s?\b", texto_limpio):
                detectados[categoria].append(p.upper())
    return detectados

# --- INTERFAZ DE ENTRADA ---
st.info("📋 PEGUE LA INSPECCIÓN OCULAR PARA ALIMENTAR EL CROQUIS")
texto_fuente = st.text_area("Contenido del Bloque 6:", height=150, 
                             placeholder="Ej: Se observa la puerta de ingreso violentada y en el dormitorio el placard revuelto...")

if st.button("🔍 PROCESAR ESCENA"):
    if texto_fuente:
        elementos = escanear_texto(texto_fuente)
        
        # Guardamos en el estado de la sesión para que no se borre
        st.session_state['elementos_croquis'] = elementos
        st.success("✅ Escena analizada. Objetos listos para el croquis.")
    else:
        st.error("El campo está vacío.")

# --- MOSTRAR CAJA DE HERRAMIENTAS SI HAY DATOS ---
if 'elementos_croquis' in st.session_state:
    st.divider()
    st.subheader("📦 Objetos Detectados (Haga clic para posicionar)")
    
    elementos = st.session_state['elementos_croquis']
    
    # Creamos columnas para organizar las herramientas
    cols = st.columns(len(elementos))
    
    for i, (categoria, items) in enumerate(elementos.items()):
        with cols[i]:
            st.markdown(f"**{categoria}**")
            if items:
                for item in items:
                    if st.button(f"➕ {item}", key=f"btn_{item}"):
                        st.write(f"Seleccionado: {item}") 
                        # Aquí se activará el objeto en el lienzo cuadriculado
            else:
                st.caption("Ninguno detectado")

# --- EL LIENZO (VISTA PREVIA) ---
st.divider()
st.subheader("🖼️ Lienzo de Reconstrucción")
st.markdown("""
    <div style="width:100%; height:300px; background-color:#f0f2f6; 
    border:2px dashed #999; display:flex; align-items:center; justify-content:center; color:#666;">
    [ ESPACIO PARA EL DIBUJO TÉCNICO ]
    </div>
    """, unsafe_allow_html=True)
