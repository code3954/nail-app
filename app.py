import streamlit as st

from ui.home import home
from ui.eda import eda
from ui.ml import ml

def main():
    st.markdown("<h1 style='text-align: center; color: black;'>손톱 증상 예측 앱</h1>", unsafe_allow_html=True)
    st.text('손톱 사진을 업로드하여 증상을 확인하세요.')
    st.sidebar.title("네일 건강 확인해보기") 

    menu = ["앱 소개", "손톱상태 분석", "증상 예측하기"]
    choice = st.sidebar.selectbox("메뉴 선택", menu)

    if choice == menu[0]:
        home()
    elif choice == menu[1]:
        eda()
    elif choice == menu[2]:
        ml()

if __name__ == "__main__":
    main()