import streamlit as st

from ui.eda import show_eda
from ui.home import show_home
from ui.ml import show_ml



def main():
    st.write('\n\n')
    st.markdown("<h1 style='text-align: center; color: black;'>네일 건강 예측 앱</h1>", unsafe_allow_html=True)
    st.write('\n\n')
    st.sidebar.title("네일 건강 확인해보기") 

    # 사이드바에서 라디오 버튼으로 메뉴 항목을 선택
    menu = ["앱 소개", "네일상태 분석", "증상 예측하기"]
    choice = st.sidebar.radio("메뉴", menu)
    
    if choice == menu[0]:
        show_home()
    elif choice == menu[1]:
        show_eda()
    elif choice == menu[2]:
        show_ml()
        

if __name__ == "__main__":
    main()
