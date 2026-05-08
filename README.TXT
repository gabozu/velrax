# Velrax NetAudit v1.0 🛡️

**Velrax NetAudit** es una plataforma SaaS diseñada para automatizar la auditoría técnica y de seguridad en infraestructuras de red, con un enfoque inicial en dispositivos **MikroTik**. 

Esta herramienta permite a administradores de Micro-ISPs y PyMEs validar sus configuraciones en segundos, identificando brechas de seguridad y puntos de optimización sin necesidad de ser expertos en ciberseguridad.

## 🚀 Características Principales

* **Auditoría Instantánea:** Análisis de archivos de configuración `.rsc` mediante motores de expresiones regulares en Python.
* **Security Check:** Detección de puertos vulnerables (Winbox, SSH, API, Web) y protocolos de gestión desprotegidos.
* **Reporte Tipo Semáforo:** Visualización clara de hallazgos críticos, advertencias y recomendaciones de mejora.
* **Cloud-Native:** Desplegado sobre una arquitectura escalable usando Streamlit Cloud y protegida por Cloudflare.

## 🛠️ Stack Tecnológico

* **Lenguaje:** Python 3.9+
* **Framework Web:** [Streamlit](https://streamlit.io/)
* **Infraestructura:** Cloudflare (DNS & SSL)
* **Lógica de Análisis:** Expresiones regulares (Regex) y validación de estándares CIS Benchmarks.

## 📦 Instalación (Entorno Local)

Si deseas ejecutar Velrax localmente para desarrollo:

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/tu-usuario/velrax-netaudit.git](https://github.com/tu-usuario/velrax-netaudit.git)
