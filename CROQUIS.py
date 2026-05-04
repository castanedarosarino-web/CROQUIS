import streamlit as st

def bloque_croquis():
    st.header("📐 BLOQUE 7 CROQUIS DEMOSTRATIVO")
    
    st.info("""
    **PROCEDIMIENTO OPERATIVO:**
    1. Realice el croquis a mano alzada o mediante el módulo externo.
    2. Capture la fotografía del diseño.
    3. Cargue el archivo final en este apartado para su anexado al acta.
    """)

    # --- 1. ENLACE AL SATÉLITE ---
    st.subheader("1. Herramientas Externas")
    col1, col2 = st.columns(2)
    with col1:
        # Reemplaza con la URL que te dé Render para el anexo_fotos.py
        url_fotos = "https://tu-app-de-fotos.render.com" 
        st.link_button("🚀 ABRIR GENERADOR DE ANEXOS", url_fotos, use_container_width=True)
    with col2:
        st.caption("Use el módulo externo si necesita procesar imágenes pesadas o fotos de alta resolución.")

    st.divider()

    # --- 2. CARGA DEL RESULTADO FINAL ---
    st.subheader("2. Incorporación al Sumario")
    archivo_croquis = st.file_uploader("Suba el Croquis Finalizado (JPG o PNG):", type=['jpg', 'png', 'jpeg'])

    if archivo_croquis:
        st.image(archivo_croquis, caption="Vista previa del croquis a anexar", width=400)
        st.success("✅ Archivo listo para la impresión del PDF final.")
        
        # Guardamos en el estado del programa principal para el cierre del acta
        st.session_state['croquis_final'] = archivo_croquis

    # --- 3. REFERENCIA TÉCNICA ---
    st.divider()
    observaciones_croquis = st.text_area("Observaciones del croquis (opcional):", 
                                        placeholder="Ej: Se deja constancia que las medidas son aproximadas...")
