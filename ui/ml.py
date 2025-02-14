import streamlit as st
import numpy as np
from PIL import Image, ImageOps
from nail import load_model_and_labels, preprocess_image, predict
import requests
import sys
sys.path.append("C:/id/Github/nail-app/ui/nail.py")  # nail.py가 있는 경로를 입력하세요
from nail import load_model_and_labels, preprocess_image, predict

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

            # 병원 찾기 기능
            st.subheader('가까운 병원 찾기')
            lat = st.text_input('위도')
            lon = st.text_input('경도')

            if st.button('병원 검색'):
                api_key = "AIzaSyDBSw98bOQeXN_WLTqac4FKQ3lnlDi_IYU"  # 여기에 Google Maps API 키를 입력하세요
                url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lon}&radius=5000&type=hospital&key={api_key}"
                response = requests.get(url)

                if response.status_code == 200:
                    data = response.json()
                    st.write('검색 결과:')
                    for place in data['results']:
                        st.write(place['name'])
                else:
                    st.write('검색 실패')
    else:
        st.warning("주의! '네일 상태 분석' 메뉴에서 이미지를 업로드하고 확인해주세요.")
