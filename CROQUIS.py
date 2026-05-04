import streamlit as st

st.set_page_config(page_title="S.I.V. - Croquis Profesional", layout="wide")

st.title("🚓 GENERADOR DE PLANO TÉCNICO (S.I.V.)")
st.sidebar.write("**Sub Comisario CASTAÑEDA Juan**")import streamlit as st

st.set_page_config(page_title="S.I.V. Croquis Rápido", layout="centered")

st.title("🚓 CROQUIS RÁPIDO S.I.V.")
st.subheader("Sub Comisario CASTAÑEDA Juan")

# --- 1. SELECCIÓN DE ESCENARIO ---
escenario = st.selectbox("1. ¿Dónde es el hecho?", ["Calle Recta", "Intersección", "Habitación/Interior"])

# --- 2. CAJA DE HERRAMIENTAS (SELLOS) ---
st.write("### 2. Toque un elemento para activarlo:")
col1, col2, col3, col4 = st.columns(4)
with col1: st.button("🏍️ MOTO")
with col2: st.button("🔫 ARMA")
with col3: st.button("🩸 RASTRO")
with col4: st.button("👤 CUERPO")

# --- 3. EL TABLERO OPERATIVO ---
st.write("### 3. Ubique en la cuadrícula:")

# Creamos una grilla de 5x5 botones (pueden ser más)
# Esto simula el lugar del hecho.
for i in range(5):
    cols = st.columns(5)
    for j in range(5):
        with cols[j]:
            # Cada cuadro es un botón. Al tocarlo, se "marca" el lugar.
            if st.button("➕", key=f"btn_{i}_{j}"):
                st.session_state[f"mark_{i}_{j}"] = "📍"
            
            # Si el cuadro ya fue tocado, muestra la marca
            if f"mark_{i}_{j}" in st.session_state:
                st.write(st.session_state[f"mark_{i}_{j}"])

# --- 4. CIERRE ---
st.divider()
if st.button("💾 FINALIZAR Y PEGAR EN EL ACTA"):
    st.success("✅ Croquis generado. Se exportará como una tabla de posiciones técnica.")

# --- 1. SELECCIÓN DE PLANTILLA (ESTÁNDAR POLICIAL) ---
st.header("1. Seleccione la Escena Tipo")
escena = st.radio("Plantilla Base:", 
                 ["Vivienda: Dormitorio", "Vivienda: Cocina/Baño", "Vía Pública: Calle Recta", "Vía Pública: Intersección"],
                 horizontal=True)

# --- 2. CARGA DE EVIDENCIA (SIMBOLOGÍA) ---
st.divider()
st.header("2. Registro de Indicios")
st.info("Asigne un número de indicio a cada elemento detectado en la inspección.")

if 'indicios' not in st.session_state:
    st.session_state.indicios = []

with st.form("agregar_indicio"):
    c1, c2, c3 = st.columns([2,2,1])
    with c1:
        obj = st.text_input("Elemento (ej: Vaina, Arma, Mancha):")
    with c2:
        loc = st.selectbox("Ubicación Relativa:", ["Cerca de puerta", "Sobre la cama", "Bajo ventana", "Centro calzada", "Cordón Este"])
    with c3:
        nro = st.number_input("ID #", min_value=1, value=len(st.session_state.indicios)+1)
    
    if st.form_submit_button("Añadir Indicio"):
        st.session_state.indicios.append({"id": nro, "obj": obj, "loc": loc})

# --- 3. EL CROQUIS FINAL (REPRESENTACIÓN TÉCNICA) ---
st.divider()
if st.session_state.indicios:
    st.subheader("🖼️ Representación para el Acta")
    
    # Simulación de Plano Técnico
    col_plano, col_tabla = st.columns([3, 2])
    
    with col_plano:
        # Aquí generamos el cuadro técnico
        dibujo_html = f"""
        <div style="border: 2px solid #333; height: 400px; background-color: #fff; position: relative; background-image: radial-gradient(#d7d7d7 1px, transparent 1px); background-size: 20px 20px;">
            <div style="position: absolute; top: 10px; right: 10px;"><b>N ↑</b></div>
            <div style="text-align: center; color: #999; margin-top: 150px;">
                <h4>ESCENARIO: {escena.upper()}</h4>
                <div style="display: flex; justify-content: center; gap: 15px; flex-wrap: wrap;">
                    {" ".join([f'<div style="border: 2px solid black; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; background: yellow; font-weight: bold;">{i["id"]}</div>' for i in st.session_state.indicios])}
                </div>
            </div>
        </div>
        """
        st.markdown(dibujo_html, unsafe_allow_html=True)
    
    with col_tabla:
        st.write("**TABLA DE REFERENCIAS**")
        st.table(pd.DataFrame(st.session_state.indicios))

# --- 4. EXPORTACIÓN ---
if st.button("💾 Finalizar Anexo Planimétrico"):
    st.success("Plano generado siguiendo normativa de planimetría pericial.")
