import streamlit as st
import numpy as np
from PIL import Image, ImageOps
from keras.models import load_model

def load_model_and_labels():
    model = load_model("model/keras_model.h5", compile=False)
    class_names = open("model/labels.txt", "r", encoding='utf-8').readlines()
    return model, class_names

def preprocess_image(image):
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array
    return data

def predict(model, data, class_names):
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    return class_name[2:], confidence_score

def show_ml():
    st.subheader('네일 건강 상태 예측')
    st.text('아래의 질병 예측하기 버튼을 눌러주세요.')
    
    if 'analyzed_image' in st.session_state:
        image = st.session_state['analyzed_image']
        st.image(image, caption="업로드 이미지", width=250)
        
        if st.button("질병 예측하기"):
            model, class_names = load_model_and_labels()
            processed_image = preprocess_image(image)
            class_name, confidence_score = predict(model, processed_image, class_names)
            
            st.success("예측이 완료되었습니다!")
            st.info(f'예측 결과: {class_name}')
            st.info(f'신뢰도: {confidence_score:.2f}')
    else:
        st.warning("잠깐! '네일 상태 분석' 메뉴에서 이미지를 업로드하고 확인해주세요.")
