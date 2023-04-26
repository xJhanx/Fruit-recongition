import streamlit as st
import cv2
from PIL import Image
import numpy as np
import time 
import matplotlib.pyplot as plt

import altair as alt
import pandas as pd
from PIL import Image


from tensorflow.keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import requests
from bs4 import BeautifulSoup

#Eliminacion de spinner 
def eliminarContainer():
    containerSpinner = st.container()
    with containerSpinner:
        html_code = """
        <style>
        #spinner{
        display: none;
        }
        </style>
        """
        st.markdown(html_code, unsafe_allow_html=True)
        containerSpinner = st.empty()

containerSpinner = st.container()
#preloader 
with containerSpinner:

    html_code = """
    <style>
    #spinner{
    display: flex;
    justify-content:center;
    align-items: center;
    height: 100vh;
    position: relative;
    }
    .lds-roller {
    display: inline-block;
    position: relative;
    width: 80px;
    height: 80px;
    }
    .lds-roller div {
    animation: lds-roller 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
    transform-origin: 40px 40px;
    }
    .lds-roller div:after {
    content: " ";
    display: block;
    position: absolute;
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #fff;
    margin: -4px 0 0 -4px;
    }
    .lds-roller div:nth-child(1) {
    animation-delay: -0.036s;
    }
    .lds-roller div:nth-child(1):after {
    top: 63px;
    left: 63px;
    }
    .lds-roller div:nth-child(2) {
    animation-delay: -0.072s;
    }
    .lds-roller div:nth-child(2):after {
    top: 68px;
    left: 56px;
    }
    .lds-roller div:nth-child(3) {
    animation-delay: -0.108s;
    }
    .lds-roller div:nth-child(3):after {
    top: 71px;
    left: 48px;
    }
    .lds-roller div:nth-child(4) {
    animation-delay: -0.144s;
    }
    .lds-roller div:nth-child(4):after {
    top: 72px;
    left: 40px;
    }
    .lds-roller div:nth-child(5) {
    animation-delay: -0.18s;
    }
    .lds-roller div:nth-child(5):after {
    top: 71px;
    left: 32px;
    }
    .lds-roller div:nth-child(6) {
    animation-delay: -0.216s;
    }
    .lds-roller div:nth-child(6):after {
    top: 68px;
    left: 24px;
    }
    .lds-roller div:nth-child(7) {
    animation-delay: -0.252s;
    }
    .lds-roller div:nth-child(7):after {
    top: 63px;
    left: 17px;
    }
    .lds-roller div:nth-child(8) {
    animation-delay: -0.288s;
    }
    .lds-roller div:nth-child(8):after {
    top: 56px;
    left: 12px;
    }
    @keyframes lds-roller {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
    }
    </style>
    <div id="spinner">
    <div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)
    time.sleep(5)
    eliminarContainer()

#modelos y nombres 


model = load_model('FV.h5')
labels = {0: 'apple', 1: 'banana', 2: 'beetroot', 3: 'bell pepper', 4: 'cabbage', 5: 'capsicum', 6: 'carrot',
          7: 'cauliflower', 8: 'chilli pepper', 9: 'corn', 10: 'cucumber', 11: 'eggplant', 12: 'garlic', 13: 'ginger',
          14: 'grapes', 15: 'jalepeno', 16: 'kiwi', 17: 'lemon', 18: 'lettuce',
          19: 'mango', 20: 'onion', 21: 'orange', 22: 'paprika', 23: 'pear', 24: 'peas', 25: 'pineapple',
          26: 'pomegranate', 27: 'potato', 28: 'raddish', 29: 'soy beans', 30: 'spinach', 31: 'sweetcorn',
          32: 'sweetpotato', 33: 'tomato', 34: 'turnip', 35: 'watermelon'}

fruits = ['Apple', 'Banana', 'Bello Pepper', 'Chilli Pepper', 'Grapes', 'Jalepeno', 'Kiwi', 'Lemon', 'Mango', 'Orange',
          'Paprika', 'Pear', 'Pineapple', 'Pomegranate', 'Watermelon']
vegetables = ['Beetroot', 'Cabbage', 'Capsicum', 'Carrot', 'Cauliflower', 'Corn', 'Cucumber', 'Eggplant', 'Ginger',
              'Lettuce', 'Onion', 'Peas', 'Potato', 'Raddish', 'Soy Beans', 'Spinach', 'Sweetcorn', 'Sweetpotato',
              'Tomato', 'Turnip']



#variables 
objeto = ""


# Crear una aplicación Streamlit
st.title("𝔻𝕖𝕥𝕖𝕔𝕥𝕠𝕣 𝕕𝕖 𝕗𝕣𝕦𝕥𝕒𝕤")


#sidebar set()
with st.sidebar:

    # Cargar una imagen desde el disco
    img = Image.open("Assets/logo_unipaz.png")


    # Mostrar la imagen en Streamlit
    st.image(img, width=300, caption="Logo")

    st.info('**Category : Vegetables**'+objeto)
    st.info('**Category : Fruit**')
    st.success("**Predicted : "  + '*Es una fruta *')
    st.success("**Predicted : "  + '*Es un vegetal*')
    # Generar datos de ejemplo
    # x = np.linspace(0, 10, 100)
    # y = np.sin(x)

    # # Carga la imagen
    img = Image.open('nombre_de_la_imagen.jpg')

    # Convierte la imagen a un arreglo de numpy y lo normaliza
    img_data = np.asarray(img) / 255

    # Crea un DataFrame de Pandas a partir del arreglo de numpy
    df = pd.DataFrame(img_data.reshape(-1, 3), columns=['R', 'G', 'B'])

    # Crea un gráfico de barras horizontal con los valores promedio de cada canal de color
    chart = alt.Chart(df).mark_bar().encode(
    y=alt.Y('channel:N', axis=None),
    x=alt.X('mean(value):Q', scale=alt.Scale(domain=(0, 1))),
    color=alt.Color('channel:N', scale=alt.Scale(range=['red', 'green', 'blue']))
    ).transform_fold(
    ['R', 'G', 'B'],
    as_=['channel', 'value']
    )
    # Muestra el gráfico
    st.altair_chart(chart,theme=None, use_container_width=True)



def fetch_calories(prediction):
    try:
        url = 'https://www.google.com/search?&q=calories in ' + prediction
        req = requests.get(url).text
        scrap = BeautifulSoup(req, 'html.parser')
        calories = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
        return calories
    except Exception as e:
        st.error("Can't able to fetch the Calories")
        print(e)


def processed_img(img_path):
    img = load_img(img_path, target_size=(224, 224, 3))
    img = img_to_array(img)
    img = img / 255
    img = np.expand_dims(img, [0])
    answer = model.predict(img)
    y_class = answer.argmax(axis=-1)
    print(y_class)
    y = " ".join(str(x) for x in y_class)
    y = int(y)
    res = labels[y]
    print(res)
    return res.capitalize()










img_file_buffer = st.camera_input("Capturar Objeto")
if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    
    # Save the image to disk
    img_file = cv2.imwrite("nombre_de_la_imagen.jpg", cv2_img)
    
    objeto = "tome una foto , actualizate"
    # Check the type of cv2_img:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(cv2_img))
    st.write(objeto)
    # Check the shape of cv2_img:
    # Should output shape: (height, width, channels)
    st.write(cv2_img.shape)

    st.title("Frutas🍍-Vegetables🍅 ")

    if img_file_buffer is not None:
        save_image_path = './nombre_de_la_imagen.jpg'
        with open(save_image_path, "wb") as f:
            f.write(img_file_buffer.getbuffer())

        # if st.button("Predict"):
        if img_file_buffer is not None:
            result = processed_img(save_image_path)
            print(result)
            if result in vegetables:
                st.info('**Category : Vegetables**')
            else:
                st.info('**Category : Fruit**')
            st.success("**Predicted : " + result + '**')
            cal = fetch_calories(result)
            if cal:
                st.warning('**' + cal + '(100 grams)**')
