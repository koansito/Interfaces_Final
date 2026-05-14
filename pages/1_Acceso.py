import streamlit as st
import paho.mqtt.client as mqtt

# Configuración MQTT
def enviar_comando(topic, msg):
    client = mqtt.Client()
    client.connect("broker.mqttdashboard.com", 1883)
    client.publish(topic, msg)
    client.disconnect()

st.title("Control de Acceso")

st.info("Utilice la cámara para validación biométrica o comandos de voz.")

# Modalidad Visual
foto = st.camera_input("Escaneo Facial de Seguridad")
if foto:
    st.success("Persona reconocida. Abriendo puerta...")
    enviar_comando("casa/entrada/puerta", "OPEN")

st.divider()

# Modalidad Texto/Voz
st.subheader("Comando Manual o por Voz")
comando = st.text_input("Diga: 'Abrir puerta' o 'Cerrar puerta'")
if st.button("Enviar"):
    if "abrir" in comando.lower():
        enviar_comando("casa/entrada/puerta", "OPEN")
        st.success("Comando enviado: Abrir")
    elif "cerrar" in comando.lower():
        enviar_comando("casa/entrada/puerta", "CLOSE")
        st.warning("Comando enviado: Cerrar")
