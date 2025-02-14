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

# 모델 및 라벨 로드
model, class_names = load_model_and_labels()
print("모델이 성공적으로 로드되었습니다.")