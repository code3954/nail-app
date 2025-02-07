import streamlit as st

def show_home():
    st.markdown('&nbsp;')
    st.subheader("네일 건강 확인 앱에 오신 것을 환영합니다!")
    st.write('\n\n')
    st.text("이 앱은 사용자의 네일 이미지를 분석하여 건강 상태를 예측합니다.")
    st.write('\n\n')
    st.markdown("""
    <div style="border: 2px solid #000080; border-radius: 15px; padding: 20px; background-color: #FFFFFF;">
        <h3>사용방법</h3>
        <ul>
            <li>왼쪽의 '네일 분석' 메뉴에서 네일 이미지를 업로드하세요</li>
            <li>'증상 예측' 메뉴에서 AI 모델이 분석 결과를 확인하세요.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('&nbsp;')
 
    st.markdown("### 개발 계기")
    st.text("주변 사람들의 네일을 보다가 웹사이트 검색하던 중,")
    st.text("네일 상태로 질병을 알 수 있다는 사실을 알게 되었습니다.")
    st.text("머신러닝을 활용하여 네일 상태로 질병을 예측할 수 있는 앱을 개발하면")
    st.text("유용할 것 같다는 생각이 들어 개발하게 되었습니다..")
    st.markdown('&nbsp;')

    st.markdown("### 사용한 data")
    st.markdown('**Kaggle**')
    st.text('·Nail Disease Detection')
    st.markdown('ㄴ https://www.kaggle.com/datasets/nikhilgurav21/nail-disease-detection-dataset')                
    st.markdown('·Nail Disease Image Classification Dataset')
    st.markdown('ㄴ https://www.kaggle.com/datasets/josephrasanjana/nail-disease-image-classification-dataset')
    st.markdown('&nbsp;')
     
    st.markdown('### 인용한 site')  
    st.markdown('**HiDoc 뉴스**')
    st.markdown('ㄴ https://news.hidoc.co.kr/news/articleView.html?idxno=24372')
    st.markdown('**MSD 매뉴얼 일반인용**')
    st.markdown('ㄴ https://www.msdmanuals.com/ko/home/%ED%8F%90-%EB%B0%8F-%EA%B8%B0%EB%8F%84-%EC%9E%A5%EC%95%A0/%ED%8F%90-%EC%9E%A5%EC%95%A0-%EC%A6%9D%EC%83%81/%EA%B3%A4%EB%B4%89%EC%A6%9D')
    st.markdown('**광양사랑병원**')
    st.markdown('ㄴ http://www.gysarang.com/Module/News/Lecture.asp?MODE=V&SRNO=2585')
