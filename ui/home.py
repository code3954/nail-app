import streamlit as st


def show_home():
    st.markdown(
        """
<style>
.big-font {
font-size: 50px !important;
color: #1E90FF;
text-align: center;
font-weight: bold;
}
.medium-font {
font-size: 30px !important;
color: #4682B4;
text-align: center;
}
.intro-text {
font-size: 18px !important;
color: #333;
text-align: justify;
margin: 20px 0;
}
.card {
background-color: #F0F8FF;
border-radius: 10px;
padding: 20px;
margin: 20px 0;
box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}
.card-header {
font-size: 24px;
font-weight: bold;
color: #4169E1;
margin-bottom: 10px;
}
ul {
list-style-type: none;
padding-left: 0;
}
li {
margin-bottom: 10px;
}
</style>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        '<p class="big-font">네일이미지로 내 건강상태 확인</p>', unsafe_allow_html=True
    )
    st.markdown(
        '<p class="medium-font">사용자의 네일 이미지를 분석하여 관련된 병증을 확인할 수 있습니다.</p>',
        unsafe_allow_html=True,
    )

    st.image(
        "https://images.unsplash.com/photo-1500322865251-52cc7d1e8a3d",
        use_container_width=True,
        caption="네일 건강 체크",
    )

    st.markdown(
        '<p class="intro-text">이 앱은 사용자가 업로드한 네일 이미지를 분석하여, 머신러닝 모델이 질병을 예측해서 알려 줍니다. 간단한 이미지 업로드만으로 당신의 건강 상태를 확인해보세요.</p>',
        unsafe_allow_html=True,
    )

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-header'>사용 방법</div>", unsafe_allow_html=True)
    st.markdown(
        """
    <ul>
    <li>1. 왼쪽 사이드바의 '네일상태 분석' 메뉴를 선택하세요.</li>
    <li>2. 네일 이미지를 업로드하세요. (밝은 곳에서 정면에서 촬영한 선명한 이미지가 좋습니다)</li>
    <li>3. '증상 예측하기' 메뉴에서 AI 모델이 분석한 결과를 확인하세요.</li>
    <li>4. 필요한 경우, 가까운 병원 찾기 기능을 이용해보세요.</li>
    </ul>
    """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-header'>주의사항</div>", unsafe_allow_html=True)
    st.markdown(
        """
    <ul>
    <li>이 앱의 예측 결과는 참고용이며, 정확한 진단을 위해서는 반드시 전문의와 상담하세요.</li>
    <li>업로드된 이미지는 분석 후 즉시 삭제됩니다.</li>
    <li>정확한 분석을 위해 깨끗하고 선명한 네일 이미지를 사용해주세요.</li>
    </ul>
    """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    show_home()
