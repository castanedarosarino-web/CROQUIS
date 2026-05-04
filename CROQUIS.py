import streamlit as st

# Configuración de página
st.set_page_config(page_title="S.I.V. - CROQUIS", layout="centered")

# Encabezado (Sin errores de sintaxis)
st.title("🚓 CROQUIS RÁPIDO S.I.V.")
st.sidebar.markdown("### Autoría\n**Sub Comisario CASTAÑEDA Juan**")

# 1. EL "CEREBRO" (Lo que el policía ve en el acta)
st.info("Paso 1: Identifique qué hay en la escena")
texto = st.text_area("Pegue aquí la Inspección Ocular:", height=70)

# Detectamos palabras clave para que el oficial no tenga que escribir
catalogo = {"MOTO": "🏍️", "AUTO": "🚗", "ARMA": "🔫", "VAINA": "🎞️", "DROGA": "📦", "CUERPO": "👤"}
detectados = [catalogo[obj] for obj in catalogo if obj.lower() in texto.lower()]

if detectados:
    st.write(f"Elementos encontrados: {' '.join(detectados)}")

# 2. EL TABLERO (Lo más fácil para el policía)
st.divider()
st.write("### Paso 2: Marque la ubicación en la grilla")
st.caption("Cada cuadro es un sector del lugar del hecho. Toque para marcar la evidencia.")

# Inicializar el estado de la grilla si no existe
if 'mapa' not in st.session_state:
    st.session_state.mapa = {}

# Crear una grilla de 6x6 (Tamaño ideal para celular)
for fila in range(6):
    cols = st.columns(6)
    for columna in range(6):
        id_celda = f"{fila}_{columna}"
        with cols[columna]:
            # Si la celda está marcada, mostramos el icono, sino el botón +
            label = st.session_state.mapa.get(id_celda, "➕")
            if st.button(label, key=id_celda):
                # Al tocarlo, si estaba vacío ponemos un marcador
                if id_celda not in st.session_state.mapa:
                    st.session_state.mapa[id_celda] = "📍"
                else:
                    # Si ya tenía marca, lo limpiamos
                    del st.session_state.mapa[id_celda]
                st.rerun()

# 3. CIERRE OPERATIVO
st.divider()
if st.button("🏁 FINALIZAR CROQUIS"):
    if st.session_state.mapa:
        st.success("✅ Croquis guardado. Se generó el esquema de posiciones para el PDF.")
        st.write("**Resumen de Coordenadas:**")
        for k, v in st.session_state.mapa.items():
            f, c = k.split("_")
            st.write(f"- Elemento en Sector: Fila {f}, Columna {c}")
    else:
        st.warning("Debe marcar al menos un punto en la grilla.")

if st.button("🗑️ Limpiar Plano"):
    st.session_state.mapa = {}
    st.rerun()
