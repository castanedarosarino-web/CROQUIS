import streamlit as st
from fpdf import FPDF

# --- ESTA ES LA FUNCIÓN QUE TENÉS QUE PEGAR EN TU S.I.V. ---
def modulo_inspeccion_ocular_completo():
    st.header("📐 BLOQUE: INSPECCIÓN OCULAR Y PLANIMETRÍA")
    st.write("---")

    # 1. ENTRADA DE DATOS: Relato y Foto
    st.subheader("1. Carga de Información")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        relato = st.text_area(
            "✍️ Redacción de la Inspección Ocular:", 
            placeholder="Describa aquí lo observado (ej: rastro, daños, posición de elementos)...",
            height=300,
            key="input_relato"
        )
    
    with col2:
        img_file = st.file_uploader(
            "📸 Subir Croquis o Foto de la Escena:", 
            type=['jpg', 'png', 'jpeg'],
            key="input_foto"
        )
        if img_file:
            st.image(img_file, caption="Imagen seleccionada", use_container_width=True)

    # 2. LA FUSIÓN (La vista previa que viste en el chat)
    if relato and img_file:
        st.write("---")
        st.subheader("🔍 VISTA PREVIA DEL ACTA INTEGRADA")
        
        with st.container(border=True):
            st.markdown(f"**RELATO DE INSPECCIÓN:**")
            st.write(relato)
            st.write("---")
            st.image(img_file, caption="CROQUIS/RELEVAMIENTO ADJUNTO", use_container_width=True)

        # 3. EL BOTÓN DE GUARDADO DEFINITIVO
        if st.button("💾 CONFIRMAR E INTEGRAR AL SUMARIO FINAL"):
            # Guardamos todo en la memoria del programa (session_state)
            st.session_state['texto_inspeccion_final'] = relato
            st.session_state['imagen_croquis_final'] = img_file
            st.session_state['acta_lista'] = True
            
            st.success("✅ ¡Fusión realizada! Estos datos ya forman parte del acta final.")
            st.balloons()
    
    elif not relato or not img_file:
        st.info("💡 Para generar la fusión, debe completar el texto y subir una imagen.")

# --- ASÍ SE LLAMA AL MÓDULO ---
modulo_inspeccion_ocular_completo()
