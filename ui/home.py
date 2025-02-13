import streamlit as st

def show_home():
    st.markdown("""
    <style>
    .big-font {
        font-size: 50px !important;
        color: black;
        text-align: center;
    }
    .medium-font {
        font-size: 30px !important;
        color: black;
        text-align: center;
    }
    .small-font {
        font-size: 20px !important;
        color: black;
    }
    .intro-text {
        font-size: 18px !important;
        color: black;
        text-align: justify;
    }

    </style>
    """, unsafe_allow_html=True)

    
    st.markdown('<p class="big-font"> 네일이미지로 내 건강상태 확인</p>', unsafe_allow_html=True)
    st.markdown('<p class="medium-font">사용자의 네일 이미지를 분석하여 관련된 병증을 확인할 수 있습니다.</p>', unsafe_allow_html=True)


    st.image("https://images.unsplash.com/photo-1500322865251-52cc7d1e8a3d", use_container_width=True)


    st.markdown('<p class="intro-text">이 앱은 사용자가 업로드한 네일 이미지를 분석하여, 머신러닝 모델이 질병을 예측해서 알려 줍니다.</p>', unsafe_allow_html=True)


    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-header'> 사용 방법</div>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li>왼쪽의 '네일 분석' 메뉴에서 네일 이미지를 업로드하세요.</li>
        <li>'증상 예측' 메뉴에서 AI 모델이 분석한 결과를 확인하세요.</li>
    </ul>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

 
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-header'> 개발 계기</div>", unsafe_allow_html=True)
    st.markdown("<div class='card-body'>이 앱은 주변 사람들의 네일 상태를 보다가 궁금증을 갖게 되어 개발했습니다.검색을 통해 네일 상태로 건강상태를 파악할 수 있다는 사실을 알게 되었고, 이를 머신러닝 모델로 구현해 보았습니다.</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-header'> 사용한 데이터</div>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li><strong>Kaggle:</strong> Nail Disease Detection Dataset</li>
        <a href="https://www.kaggle.com/datasets/nikhilgurav21/nail-disease-detection-dataset">https://www.kaggle.com/datasets/nikhilgurav21/nail-disease-detection-dataset</a><br>
        <br>
        <li><strong>Kaggle:</strong> Nail Disease Image Classification Dataset</li>
        <a href="https://www.kaggle.com/datasets/josephrasanjana/nail-disease-image-classification-dataset">https://www.kaggle.com/datasets/josephrasanjana/nail-disease-image-classification-dataset</a><br>
    </ul>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("&nbsp;")
  
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-header'> 인용한 URL</div>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li><strong>HiDoc 뉴스</strong><br>
        <a href="https://news.hidoc.co.kr/news/articleView.html?idxno=24372">https://news.hidoc.co.kr/news/articleView.html?idxno=24372</a></li>
        <br>
        <li><strong>MSD 매뉴얼</strong><br>
        <a href="https://www.msdmanuals.com/ko/home/%ED%8F%90-%EB%B0%8F-%EA%B8%B0%EB%8F%84-%EC%9E%A5%EC%95%A0/%ED%8F%90-%EC%9E%A5%EC%95%A0-%EC%A6%9D%EC%83%81/%EA%B3%A4%EB%B4%89%EC%A6%9D">https://www.msdmanuals.com/ko/home/%ED%8F%90-%EB%B0%8F-%EA%B8%B0%EB%8F%84-%EC%9E%A5%EC%95%A0/%ED%8F%90-%EC%9E%A5%EC%95%A0-%EC%A6%9D%EC%83%81/%EA%B3%A4%EB%B4%89%EC%A6%9D</a></li>
        <br>
        <li><strong>광양사랑병원</strong><br>
        <a href="http://www.gysarang.com/Module/News/Lecture.asp?MODE=V&SRNO=2585">http://www.gysarang.com/Module/News/Lecture.asp?MODE=V&SRNO=2585</a></li>
    </ul>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)



if __name__ == "__main__":
    show_home()

