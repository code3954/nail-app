import streamlit as st
from PIL import Image

def show_eda():
    st.subheader("네일 이미지 분석")
    st.text("네일 이미지를 업로드하면 네일 정보를 분석해서 건강상태를 알려드립니다.")
    st.write('\n\n')
    uploaded_file = st.file_uploader("네일 이미지를 업로드하세요.정확한 분석을 위해 밝은 곳에서 정면으로 찍은 이미지를 올려주세요.", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="업로드된 이미지", use_container_width=True)
        
        # 이미지 정보 분석
        st.subheader("이미지 정보")
        st.write(f"파일 이름: {uploaded_file.name}")
        st.write(f"파일 크기: {uploaded_file.size} bytes")
        st.write(f"이미지 크기: {image.size[0]}x{image.size[1]} 픽셀")
        st.write(f"이미지 모드: {image.mode}")
        
        # 분석된 이미지 데이터를 세션 상태에 저장
        st.session_state['analyzed_image'] = image
        st.success("이미지 분석이 완료되었습니다. '질병 예측' 메뉴에서 결과를 확인하세요.")