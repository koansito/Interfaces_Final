import streamlit as st
import paho.mqtt.client as mqtt

def enviar_comando(topic, msg):
    client = mqtt.Client()
    client.connect("broker.hivemq.com", 1883)
    client.publish(topic, msg)
    client.disconnect()

st.title("Gestión de Ambientes")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Iluminación")
    if st.button("💡 Encender Sala"):
        enviar_comando("casa/sala/luz", "ON")
    if st.button("🌑 Apagar Sala"):
        enviar_comando("casa/sala/luz", "OFF")

with col2:
    st.subheader("Simulación Física")
    # Un slider para simular intensidad o temperatura
    nivel = st.slider("Brillo de luz (Simulado)", 0, 100, 50)
    st.write(f"Nivel actual: {nivel}%")
    
st.success("Interactuando con el mundo físico vía MQTT")
