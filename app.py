import streamlit as st
import re

st.set_page_config(page_title="Velrax NetAudit", page_icon="🛡️", layout="wide")

# Estilo Velrax
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stAlert { border-radius: 10px; }
    .status-box { padding: 15px; border-radius: 10px; border: 1px solid #ddd; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Velrax | Network Audit Professional")
st.markdown("---")
st.caption("Velrax NetAudit v1.0 | Infraestructura de red segura y optimizada. | © 2026 Velrax Tech | Medellín, Colombia")

uploaded_file = st.file_uploader("Cargar configuración de Switch/Router (.txt)", type=['txt'])

if uploaded_file:
    content = uploaded_file.read().decode("utf-8")
    lines = content.splitlines()
    
    # --- MOTOR DE AUDITORÍA TÉCNICA ---
    results = []

    # 1. Auditoría de MTU (Viste que tienes 2000)
    if "mtu=2000" in content:
        results.append({"clase": "info", "msg": "MTU Personalizado (2000) detectado. Validar que toda la ruta de capa 2 soporte Baby Giants para evitar fragmentación."})

    # 2. Auditoría de SNMP
    if "/snmp" in content and "enabled=yes" in content:
        if "addresses=0.0.0.0/0" in content:
            results.append({"clase": "error", "msg": "SNMP abierto globalmente (0.0.0.0/0). Riesgo de exfiltración de topología."})
        else:
            results.append({"clase": "warning", "msg": "SNMP activo. Verificar que la Community 'name_community' no sea la de fábrica."})

    # 3. Auditoría de Seguridad de Acceso (AAA)
    if "use-radius=yes" in content:
        results.append({"clase": "success", "msg": "Autenticación centralizada RADIUS detectada. Excelente práctica de seguridad B2B."})
    
    # 4. Auditoría de Firewall (Address Lists)
    if "list=MGMT" in content:
        results.append({"clase": "success", "msg": "Uso de Address List 'MGMT' para acceso restringido detectado. Filtrado de capa 3 correcto."})

    # 5. Auditoría de NAT
    if "action=masquerade" in content and "out-interface=ether1" in content:
        results.append({"clase": "info", "msg": "NAT Masquerade detectado en ether1 (CPE Mode)."})

    # --- RENDERIZADO DE RESULTADOS ---
    st.subheader("Análisis de Infraestructura")
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.markdown("### Hallazgos de Seguridad")
        for r in results:
            if r['clase'] == "error": st.error(f"**CRÍTICO:** {r['msg']}")
            if r['clase'] == "warning": st.warning(f"**RIESGO:** {r['msg']}")
            if r['clase'] == "success": st.success(f"**CUMPLIMIENTO:** {r['msg']}")
            if r['clase'] == "info": st.info(f"**NOTA:** {r['msg']}")
            
    with col2:
        st.markdown("### Configuración Detectada")
        with st.expander("Ver código fuente analizado"):
            st.code(content, language="bash")
else:
    st.info("Por favor carga el archivo de configuración para iniciar.")

if st.button("Generar Reporte PDF Profesional"):
    st.info("🚀 Funcionalidad disponible próximamente en la versión Pro.")