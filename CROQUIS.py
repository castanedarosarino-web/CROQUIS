import streamlit as st
import pandas as pd

st.set_page_config(page_title="S.I.V. - CROQUIS ESQUEMÁTICO", layout="wide")

st.title("📐 CONSTRUCTOR DE CROQUIS ESQUEMÁTICO")
st.sidebar.write("**Autoría:** Sub Comisario CASTAÑEDA Juan")

# --- 1. ENTRADA DE DATOS (LECTURA INTELIGENTE) ---
st.header("1. Análisis de la Inspección Ocular")
texto_acta = st.text_area("Pegue el texto de la Inspección Ocular aquí:", height=100, 
                          placeholder="Ej: Se observa una motocicleta sobre la vereda este...")

# Diccionario de búsqueda
catalogo = ["MOTO", "AUTO", "ARMA", "VAINA", "CUERPO", "DROGA", "BALANZA", "DINERO", "CELULAR"]
detectados = [obj for obj in catalogo if obj.lower() in texto_acta.lower()]

if st.button("🔍 Escanear Escena"):
    if detectados:
        st.session_state['evidencia'] = detectados
        st.success(f"Objetos listos para posicionar: {', '.join(detectados)}")
    else:
        st.warning("No se detectaron objetos clave. Puede posicionar manualmente.")

# --- 2. CONFIGURACIÓN DEL PLANO ---
st.divider()
st.header("2. Configuración del Escenario")

col_esc, col_orient = st.columns(2)
with col_esc:
    escenario = st.selectbox("Tipo de Escena:", 
                            ["Interior (Habitación)", "Calle Recta", "Intersección en T", "Cruce de Calles"])
with col_orient:
    calle_nombre = st.text_input("Nombre de la calle principal:", "Mendoza")

# --- 3. UBICACIÓN DE OBJETOS ---
st.divider()
st.header("3. Posicionamiento de Evidencia")

posiciones_finales = []
if 'evidencia' in st.session_state:
    for obj in st.session_state['evidencia']:
        st.write(f"📍 **{obj}**")
        c1, c2, c3 = st.columns(3)
        with c1:
            cuadrante = st.selectbox(f"Ubicación {obj}:", 
                                     ["NORTE / ARRIBA", "SUR / ABAJO", "ESTE / DERECHA", "OESTE / IZQUIERDA", "CENTRO"], 
                                     key=f"cuad_{obj}")
        with c2:
            distancia = st.text_input(f"Distancia (opcional) {obj}:", placeholder="Ej: a 2mts del cordón", key=f"dist_{obj}")
        with c3:
            estado = st.selectbox(f"Estado {obj}:", ["Posición Final", "Punto de Impacto", "Punto de Hallazgo"], key=f"est_{obj}")
        
        posiciones_finales.append({"Objeto": obj, "Ubicación": cuadrante, "Detalle": distancia, "Tipo": estado})
        st.divider()

# --- 4. GENERACIÓN DEL GRÁFICO TÉCNICO ---
if st.button("🏁 GENERAR ESQUEMA PARA PDF"):
    st.subheader("Vista Previa del Anexo Planimétrico")
    
    # Renderizado del esquema usando HTML/CSS puro (liviano y seguro)
    items_html = ""
    for item in posiciones_finales:
        # Lógica de color según tipo
        color = "red" if "Impacto" in item['Tipo'] else "blue"
        items_html += f"""
        <div style="border: 2px solid {color}; padding: 10px; margin: 5px; border-radius: 5px; background-color: white;">
            <b>{item['Objeto']}</b><br>
            <small>{item['Ubicación']} - {item['Detalle']}</small><br>
            <span style="font-size: 10px; color: {color};">{item['Tipo']}</span>
        </div>
        """

    st.markdown(f"""
    <div style="border: 4px double black; padding: 25px; background-color: #fcfcfc; font-family: sans-serif;">
        <h3 style="text-align: center; text-decoration: underline;">ANEXO: ESQUEMA ILUSTRATIVO DE POSICIONES</h3>
        <p style="text-align: center; font-size: 14px;">Escenario: {escenario} - Calle: {calle_nombre}</p>
        <hr>
        <div style="display: flex; flex-wrap: wrap; justify-content: center; min-height: 200px; border: 1px dashed #ccc; padding: 15px;">
            {items_html}
        </div>
        <hr>
        <div style="font-size: 12px; line-height: 1.4;">
            <b>REFERENCIAS TÉCNICAS:</b><br>
            El presente diagrama es una representación esquemática no a escala, basada estrictamente en lo 
            consignado en el Acta de Inspección Ocular. Los puntos cardinales se establecen de acuerdo 
            a la orientación declarada por el personal actuante.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 Este bloque se adjunta como imagen técnica al final del Sumario Digital.")
