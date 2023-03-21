import cv2
import urllib.request
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input, decode_predictions, VGG16
import numpy as np
# Descargar modelo si no está presente en el directorio
try:
    model = VGG16(weights='imagenet')
except OSError:
    print("Modelo no encontrado en el directorio. Descargando...")
    url = "https://storage.googleapis.com/tensorflow/keras-applications/vgg16/vgg16_weights_tf_dim_ordering_tf_kernels.h5"
    urllib.request.urlretrieve(url, "vgg16_weights_tf_dim_ordering_tf_kernels.h5")
    model = VGG16(weights='imagenet')

# Iniciar cámara
cap = cv2.VideoCapture(0)

while True:
    # Leer cuadro de la cámara
    ret, frame = cap.read()
    
    # Redimensionar imagen para entrada en el modelo
    img = cv2.resize(frame, (224, 224))
    
    # Convertir imagen a tensor y pre-procesar
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # Realizar la predicción del modelo
    preds = model.predict(x)
    pred_class = decode_predictions(preds, top=1)[0][0]

    # Dibujar cuadro de detección en la imagen
    cv2.rectangle(frame, (0, 0), (300, 50), (255, 255, 255), -1)
    cv2.putText(frame, "Prediccion: {}".format(pred_class[1]), (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

    # Mostrar imagen
    cv2.imshow('Video', frame)

    # Salir al presionar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
