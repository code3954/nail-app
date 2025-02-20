import streamlit as st

st.set_page_config(page_title="네일 건강 상태 예측", layout="wide")

from ui.home import show_home
from ui.eda import show_eda
from ui.ml import show_ml


def main():
    st.markdown(
        """
    <style>
    @keyframes blink {
        0% { opacity: 1; }
        50% { opacity: 0; }
        100% { opacity: 1; }
    }
    .blinking-text {
        animation: blink 1s linear infinite;
    }
    a {
        color: gray !important;
        text-decoration: underline;
    }
    .menu-link {
        display: block;
        padding: 10px 20px;
        text-align: center;
        color: black;
        text-decoration: none;
        border: 1px solid #ccc;
        border-radius: 5px;
        margin-bottom: 5px;
    }
    .menu-link:hover {
        background-color: #f0f0f0;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "<h1 style='text-align: center; color: black;'><span class='blinking-text'>네일이미지로 건강 예측</span></h1>",
        unsafe_allow_html=True,
    )
    st.write("\n\n")
    st.sidebar.title("메뉴 목록")

    # 메뉴 아이템 정의
    menu_items = {
        "앱 소개": show_home,
        "네일상태 분석": show_eda,
        "증상 예측하기": show_ml,
    }

    # 선택된 페이지를 세션 상태에 저장
    if "page" not in st.session_state:
        st.session_state["page"] = "앱 소개"  # 기본 페이지 설정

    # 사이드바 메뉴 생성 (목차 스타일)
    with st.sidebar:
        for label in menu_items.keys():
            if st.button(label, key=f"menu_{label}"):
                st.session_state["page"] = label

    # 페이지 내용 표시
    selected_page = st.session_state["page"]
    if selected_page in menu_items:
        menu_items[selected_page]()  # 선택된 페이지의 함수 호출
    else:
        st.write("페이지를 찾을 수 없습니다.")  # 예외 처리


def show_app_info():
    st.markdown(
        '<p class="intro-text">이 앱은 사용자가 업로드한 네일 이미지를 분석하여, 머신러닝 모델이 질병을 예측해서 알려 줍니다.</p>',
        unsafe_allow_html=True,
    )




if __name__ == "__main__":
    main()
