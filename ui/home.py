import streamlit as st

def show_home():
    st.write('\n\n')
    st.markdown("<h4 style='text-align: center; color: black;'>네일이미지 건강 확인 앱.</h4>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: black;'>이 앱은 사용자의 네일 이미지를 분석하여</h4>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: black;'>건강 상태를 알려드립니다.</h4>", unsafe_allow_html=True)


    st.write('\n\n')

    # "사용방법" 섹션에 빨간색 라운드 테두리 추가
    st.markdown("""
    <div style="border: 2px solid red; border-radius: 15px; padding: 20px; background-color: white;">
        <h4>사용방법</h4>
        <ul>
            <li>왼쪽의 '네일 분석' 메뉴에서 네일 이미지를 업로드하세요</li>
            <li>'증상 예측' 메뉴에서 AI 모델이 분석 결과를 확인하세요.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('&nbsp;')

    # "개발 계기" 섹션에 주황색 라운드 테두리 추가
    st.markdown("""
    <div style="border: 2px solid orange; border-radius: 15px; padding: 20px;">
        <h4>개발 계기</h4>
        <p>주변 사람들의 네일을 보다가 궁금증이 생겨, 웹사이트에서 검색하던 중에 네일 상태로 질병을 알 수 있다는 사실을 알게 되었습니다.</p>
        <p>머신러닝을 활용하여 네일 상태로 질병을 예측할 수 있는 앱을 개발하면 유용할 것 같다는 생각이 들어 개발하게 되었습니다.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('&nbsp;')

    st.markdown("""
    <div style="border: 2px solid green; border-radius: 15px; padding: 10px;">
        <h4>사용한 data</h4>
        <ul><li>Kaggle</strong></li></ul>              
        · Nail Disease Detection</li><br>
        <a href="https://www.kaggle.com/datasets/nikhilgurav21/nail-disease-detection-dataset">https://www.kaggle.com/datasets/nikhilgurav21/nail-disease-detection-dataset</a><br>
        <br>
        · Nail Disease Image Classification Dataset<br>
        <a href="https://www.kaggle.com/datasets/josephrasanjana/nail-disease-image-classification-dataset">https://www.kaggle.com/datasets/josephrasanjana/nail-disease-image-classification-dataset</a><br>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('&nbsp;')


    st.markdown("""
    <div style="border: 2px solid blue; border-radius: 15px; padding: 10px;">
        <h4>인용한 site</h4>
        <strong>· HiDoc 뉴스</strong></li></ul>
        <a href=" https://news.hidoc.co.kr/news/articleView.html?idxno=24372">https://news.hidoc.co.kr/news/articleView.html?idxno=24372</a><br>
        <br>
        <strong>·  MSD 매뉴얼 일반인용</strong><br>
        <a href="https://www.msdmanuals.com/ko/home/%ED%8F%90-%EB%B0%8F-%EA%B8%B0%EB%8F%84-%EC%9E%A5%EC%95%A0/%ED%8F%90-%EC%9E%A5%EC%95%A0-%EC%A6%9D%EC%83%81/%EA%B3%A4%EB%B4%89%EC%A6%9D">https://www.msdmanuals.com/ko/home/%ED%8F%90-%EB%B0%8F-%EA%B8%B0%EB%8F%84-%EC%9E%A5%EC%95%A0/%ED%8F%90-%EC%9E%A5%EC%95%A0-%EC%A6%9D%EC%83%81/%EA%B3%A4%EB%B4%89%EC%A6%9D</a><br>
        <br>
        <strong>·  광양사랑병원</strong><br>
        <a href="http://www.gysarang.com/Module/News/Lecture.asp?MODE=V&SRNO=2585">http://www.gysarang.com/Module/News/Lecture.asp?MODE=V&SRNO=2585Link</a><br>
    </div>
    """, unsafe_allow_html=True)