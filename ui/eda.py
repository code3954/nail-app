import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

def show_eda():
    st.title("손톱 이미지 분석")
    st.write("손톱 사진을 업로드하면 이미지 정보를 분석합니다.")
    
    uploaded_file = st.file_uploader("손톱 이미지를 업로드하세요", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="업로드된 이미지", use_column_width=True)
        
        # 이미지 정보 분석
        st.subheader("이미지 정보")
        st.write(f"파일 이름: {uploaded_file.name}")
        st.write(f"파일 크기: {uploaded_file.size} bytes")
        st.write(f"이미지 크기: {image.size[0]}x{image.size[1]} 픽셀")
        st.write(f"이미지 모드: {image.mode}")
        
        # 히스토그램 표시
        st.subheader("이미지 히스토그램")
        fig, ax = plt.subplots()
        ax.hist(list(image.getdata()), bins=256, range=(0,256), color='gray')
        ax.set_title("Pixel Value Distribution")
        ax.set_xlabel("Pixel Value")
        ax.set_ylabel("Frequency")
        st.pyplot(fig)
        
        # 분석된 이미지 데이터를 세션 상태에 저장
        st.session_state['analyzed_image'] = image
        
        st.success("이미지 분석이 완료되었습니다. '질병 예측' 메뉴에서 결과를 확인하세요.")