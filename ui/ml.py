import streamlit as st


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


def show_ml():
    st.header("About This App")

    def show_app_info():
        st.markdown(
            '<p class="intro-text">이 앱은 사용자가 업로드한 네일 이미지를 분석하여, 머신러닝 모델이 질병을 예측해서 알려 줍니다.</p>',
            unsafe_allow_html=True,
        )

    def show_development_reason():
        st.markdown(
            "<div class='card-header'> <h5>개발 계기</h5></div>", unsafe_allow_html=True
        )
        st.markdown(
            "<div class='card-body'>이 앱은 주변 사람들의 네일 상태를 보다가 궁금증을 갖게 되어 개발했습니다. 검색을 통해 네일 상태로 건강상태를 파악할 수 있다는 사실을 알게 되었고, 이를 머신러닝 모델로 구현해 보았습니다.</div>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)
        st.write("")

    def show_dataset_info():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(
            "<div class='card-header'> <h5>사용한 dataset</h5></div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            """
        <ul>
        <li><strong>Kaggle:</strong> <a href="https://www.kaggle.com/datasets/nikhilgurav21/nail-disease-detection-dataset" target="_blank">Nail Disease Detection Dataset</a></li>
        <li><strong>Kaggle:</strong> <a href="https://www.kaggle.com/datasets/josephrasanjana/nail-disease-image-classification-dataset" target="_blank">Nail Disease Image Classification Dataset</a></li>
        </ul>
        """,
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)
        st.write("")

    def show_reference_urls():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(
            "<div class='card-header'> <h5>인용한 URL</h5></div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            """
        <ul>
        <li><strong>HiDoc 뉴스</strong><br>
        <a href="https://news.hidoc.co.kr/news/articleView.html?idxno=24372" target="_blank">
        https://news.hidoc.co.kr/news/articleView.html?idxno=24372
        </a>
        </li><br>
        <li><strong>MSD 매뉴얼</strong><br>
        <a href="https://www.msdmanuals.com/ko/home/%ED%94%BC%EB%B6%80-%EC%A7%88%ED%99%98/%EC%86%90%EB%B0%9C%ED%86%B1-%EC%9E%A5%EC%95%A0/%EC%86%90%EB%B0%9C%ED%86%B1%EC%9D%98-%EB%B3%80%ED%98%95-%EC%9D%B4%EC%83%81%EC%A6%9D-%EB%B3%80%EC%83%89" target="_blank">
        https://www.msdmanuals.com/ko/home/%ED%94%BC%EB%B6%80-%EC%A7%88%ED%99%98/%EC%86%90%EB%B0%9C%ED%86%B1-%EC%9E%A5%EC%95%A0/%EC%86%90%EB%B0%9C%ED%86%B1%EC%9D%98-%EB%B3%80%ED%98%95-%EC%9D%B4%EC%83%81%EC%A6%9D-%EB%B3%80%EC%83%89
        </a><br><br>
        <a href="https://www.msdmanuals.com/ko/home/%ED%8F%90-%EB%B0%8F-%EA%B8%B0%EB%8F%84-%EC%9E%A5%EC%95%A0/%ED%8F%90-%EC%9E%A5%EC%95%A0-%EC%A6%9D%EC%83%81/%EA%B3%A4%EB%B4%89%EC%A6%9D" target="_blank">
        https://www.msdmanuals.com/ko/home/%ED%8F%90-%EB%B0%8F-%EA%B8%B0%EB%8F%84-%EC%9E%A5%EC%95%A0/%ED%8F%90-%EC%9E%A5%EC%95%A0-%EC%A6%9D%EC%83%81/%EA%B3%A4%EB%B4%89%EC%A6%9D
        </a>
        </li><br>
        <li><strong>광양사랑병원</strong><br>
        <a href="http://www.gysarang.com/Module/News/Lecture.asp?MODE=V&SRNO=2585" target="_blank">
        http://www.gysarang.com/Module/News/Lecture.asp?MODE=V&SRNO=2585
        </a>
        </li>
        </ul>
        """,
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    show_app_info()
    show_development_reason()
    show_dataset_info()
    show_reference_urls()


if __name__ == "__main__":
    show_ml()
