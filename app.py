<<<<<<< HEAD
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np

st.title("Detector de Mascarillas")

@st.cache_resource
def cargar_modelo():
    modelo = load_model('modelo_mascarillas_30epocas.h5')
    return modelo

modelo = cargar_modelo()

# Cargar la imagen
archivo_imagen = st.file_uploader("Sube una imagen para analizar (JPG o PNG)", type=["jpg", "jpeg", "png"])

if archivo_imagen is not None:
    # Mostrar la imagen en la interfaz
    st.image(archivo_imagen, caption="Imagen seleccionada", use_column_width=True)

    # Preprocesar la imagen
    img = load_img(archivo_imagen, target_size=(128, 128))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Hacer la prediccion
    prediccion = modelo.predict(img_array)[0][0]
    st.write(f"Valor crudo de la prediccion: {prediccion}")

    # Clasificacion final usando el umbral
    umbral = 0.5
    if prediccion <= umbral:
        st.success("La persona lleva mascarilla")
    else:
        st.error("La persona NO lleva mascarilla")

=======
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np

# T�tulo de la aplicaci�n
st.title("Detector de Mascarillas")

# Funci�n para cargar el modelo una sola vez
@st.cache_resource
def cargar_modelo():
    modelo = load_model('modelo_mascarillas_30epocas.h5')
    return modelo

modelo = cargar_modelo()

# Cargar la imagen
archivo_imagen = st.file_uploader("Sube una imagen para analizar (JPG o PNG)", type=["jpg", "jpeg", "png"])

if archivo_imagen is not None:
    # Mostrar la imagen en la interfaz
    st.image(archivo_imagen, caption="Imagen seleccionada", use_column_width=True)

    # Preprocesar la imagen
    img = load_img(archivo_imagen, target_size=(128, 128))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Hacer la predicci�n
    prediccion = modelo.predict(img_array)[0][0]
    st.write(f"Valor crudo de la predicci�n: {prediccion}")

    # Clasificaci�n final usando el umbral
    umbral = 0.5
    if prediccion <= umbral:
        st.success("�La persona lleva mascarilla!")
    else:
        st.error("�La persona NO lleva mascarilla!")

>>>>>>> 441fcc30591fd80fc296f987a8aa2b73c10b323d
