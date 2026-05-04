import streamlit as st
import pandas as pd

st.set_page_config(page_title="S.I.V. - CROQUIS OPERATIVO", layout="wide")

st.sidebar.title("S.I.V. CONTROL")
st.sidebar.write("**Sub Comisario CASTAÑEDA Juan**")

st.title("📐 GENERADOR DE CROQUIS PLANIMÉTRICO")

# --- PASO 1: EL ESCÁNER DE SIEMPRE ---
st.header("1. Carga de Datos")
texto_inspeccion = st.text_area("Pegue la Inspección Ocular aquí:", height=100)

# Diccionario operativo rápido
palabras_clave = ["MOTO", "AUTO", "ARMA", "DROGA", "BALANZA", "CUERPO", "VAINA", "CELULAR"]
objetos_encontrados = [p for p in palabras_clave if p.lower() in texto_inspeccion.lower()]

if st.button("🔍 Escanear Escena"):
    st.session_state['lista_objetos'] = objetos_encontrados
    st.success(f"Objetos listos para ubicar: {', '.join(objetos_encontrados)}")

# --- PASO 2: CONSTRUCCIÓN POR TABLA (LO PRÁCTICO) ---
st.divider()
st.header("2. Dimensiones y Ubicación")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🏠 Estructura (Habitaciones)")
    if 'habitaciones' not in st.session_state:
        st.session_state['habitaciones'] = []
    
    with st.form("form_ambientes"):
        nom_amb = st.selectbox("Ambiente:", ["Dormitorio", "Cocina", "Living", "Patio", "Local", "Vereda"])
        largo = st.number_input("Largo (mts):", value=4.0)
        ancho = st.number_input("Ancho (mts):", value=3.0)
        if st.form_submit_button("Agregar al Plano"):
            st.session_state['habitaciones'].append({"Ambiente": nom_amb, "Medidas": f"{largo}x{ancho}m"})

    st.table(pd.DataFrame(st.session_state['habitaciones']))

with col2:
    st.subheader("📍 Evidencia (Ubicación)")
    if 'evidencia_plano' not in st.session_state:
        st.session_state['evidencia_plano'] = []
    
    with st.form("form_evidencia"):
        obj_sel = st.selectbox("Objeto:", st.session_state.get('lista_objetos', ["ESCANEE PRIMERO"]))
        ref = st.text_input("Referencia (Ej: A 1m de pared Norte):")
        if st.form_submit_button("Ubicar Objeto"):
            st.session_state['evidencia_plano'].append({"Objeto": obj_sel, "Ubicación": ref})

    st.table(pd.DataFrame(st.session_state['evidencia_plano']))

# --- PASO 3: EL RESULTADO ---
st.divider()
st.header("3. Vista Previa del Croquis")

# Aquí, en lugar de un dibujo que falle, generamos una representación esquemática limpia
if st.session_state['habitaciones']:
    for hab in st.session_state['habitaciones']:
        st.markdown(f"""
            <div style="border: 2px solid black; width: {float(hab['Medidas'].split('x')[0])*40}px; 
            height: {float(hab['Medidas'].split('x')[1].replace('m',''))*40}px; 
            background-color: #f0f0f0; margin: 10px; display: inline-block; text-align: center;">
            <br><b>{hab['Ambiente']}</b><br>{hab['Medidas']}
            </div>
        """, unsafe_allow_html=True)

st.divider()
if st.button("🏁 GENERAR ANEXO PLANIMÉTRICO PDF"):
    st.info("Generando documento con tablas de medidas y esquema técnico...")
    # Aquí llamaríamos a la función de PDF que ya tenemos blindada
