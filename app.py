import streamlit as st

from ui.eda import show_eda
from ui.home import show_home
from ui.ml import show_ml



def main():
    st.write('\n\n')
    st.markdown("<h1 style='text-align: center; color: black;'>네일이미지로 건강 예측</h1>", unsafe_allow_html=True)
    st.write('\n\n')
    st.sidebar.title("네일 건강 확인해보기") 

    # 사이드바에서 라디오 버튼으로 메뉴 항목을 선택
    app_info = st.sidebar.checkbox("앱 소개")
    nail_analysis = st.sidebar.checkbox("네일상태 분석")
    symptom_prediction = st.sidebar.checkbox("증상 예측하기")

    if app_info:
        show_home()
    elif nail_analysis:
        show_eda()
    elif symptom_prediction:
        show_ml()
        

if __name__ == "__main__":
    main()
