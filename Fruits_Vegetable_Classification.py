import streamlit as st
import cv2



# Configurar la captura de video desde la cámara
cap = cv2.VideoCapture(0)

# Crear una función para mostrar el video de la cámara
def show_camera():
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return frame

# Crear una nueva página en Streamlit para mostrar el último fotograma guardado

def show_phogram(imagen):
     st.image(imagen, channels="RGB")
     st.title("Objeto identificado")

# Crear una aplicación Streamlit
st.title("Aplicación de Streamlit para mostrar la cámara")

# Crear un elemento Streamlit para mostrar el video
video_element = st.empty()

# Crear el botón para guardar el último fotograma
save_button = st.button("Guardar el último fotograma")

# Variable para almacenar el último fotograma
last_frame = None

#sidebar set()
with st.sidebar:
  st.write("Elemento sidebar")

# Loop para mostrar el video de la cámara en tiempo real
while True:
    # Obtener el fotograma actual
    frame = show_camera()

    # Mostrar el fotograma en el elemento Streamlit
    video_element.image(frame, channels="RGB")

    # Guardar el fotograma actual si se presiona el botón "Guardar el último fotograma"
    if save_button:
        last_frame = frame
        show_phogram(last_frame)

    # Actualizar el estado del botón
    save_button = st.session_state.get("save_button", False)

    # Salir del while loop si se ha guardado el último fotograma
    if last_frame is not None:
       break
   
# Liberar recursos (cerrar todo con respectoa  la liberia cap)
cap.release()


