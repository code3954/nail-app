import streamlit as st

def show_home():
    st.title("손톱 건강 체크 앱에 오신 것을 환영합니다!")
    st.write("이 앱은 손톱 사진을 분석하여 가능한 건강 상태를 예측합니다.")
    st.write("사용 방법:")
    st.write("1. 왼쪽의 '손톱 분석'메뉴에서 손톱 사진을 업로드하세요")
    st.write("2. '질병 예측'메뉴에서 AI 모델이 분석 결과를 확인하세요.")
