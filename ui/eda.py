from huggingface_hub import InferenceClient
import streamlit as st
from PIL import Image, ImageOps
import numpy as np
import tensorflow as tf
import googlemaps
import folium
from streamlit_folium import folium_static


def get_ai_response(query):
    client = InferenceClient(
        provider="hf-inference", api_key="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"
    )

    medical_query = f"질병 증상 치료 병 질환 {query}"
    simulated_results = [
        f"{query}의 주요 증상",
        f"{query}의 일반적인 치료법",
        f"{query} 관련 주의사항",
    ]
    prompt = f"Query: {medical_query}\n의료 정보 결과:\n" + "\n".join(simulated_results)

    messages = [{"role": "user", "content": prompt}]

    completion = client.chat.completions.create(
        model="Qwen/Qwen2.5-Coder-32B-Instruct",
        messages=messages,
        max_tokens=1024,
    )

    return completion.choices[0].message.content


def show_eda():
    st.subheader("네일 이미지 분석 및 증상 예측")
    st.text("네일 이미지를 업로드하면 네일 정보를 분석하고, 질병을 예측합니다.")
    st.write("\n\n")
    uploaded_file = st.file_uploader(
        "네일 이미지를 업로드하세요.정확한 분석을 위해 밝은 곳에서 정면으로 찍은 이미지를 올려주세요.",
        type=["jpg", "jpeg", "png"],
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="업로드된 이미지", use_column_width=True)

        # 이미지 정보 분석
        st.subheader("이미지 정보")
        st.write(f"파일 이름: {uploaded_file.name}")
        st.write(f"파일 크기: {uploaded_file.size} bytes")
        st.write(f"이미지 크기: {image.size[0]}x{image.size[1]} 픽셀")
        st.write(f"이미지 모드: {image.mode}")

        # 분석된 이미지 데이터를 세션 상태에 저장
        st.session_state["analyzed_image"] = image

        # 질병 예측
        if st.button("질병 예측하기", key="predict_button"):
            with st.spinner("예측 중입니다..."):
                try:
                    model = tf.keras.models.load_model("model/keras_model.h5")
                    class_names = open(
                        "model/labels.txt", "r", encoding="utf-8"
                    ).readlines()

                    # 모델의 입력 크기 확인
                    input_shape = model.input_shape[1:3]

                    image = ImageOps.fit(image, input_shape, Image.Resampling.LANCZOS)
                    image_array = np.asarray(image)
                    normalized_image_array = (
                        image_array.astype(np.float32) / 127.5
                    ) - 1
                    data = np.expand_dims(normalized_image_array, axis=0)

                    prediction = model.predict(data)
                    index = np.argmax(prediction)
                    class_name = class_names[index]
                    confidence_score = prediction[0][index]

                    st.success("예측이 완료되었습니다!")
                    st.info(f"예측 결과: {class_name[2:]}")
                    st.info(f"신뢰도: {confidence_score:.2f}")

                    # 예측 완료 플래그 설정
                    st.session_state["prediction_done"] = True
                except FileNotFoundError as e:  # 파일이 없을 경우
                    st.error(f"모델 파일 또는 레이블 파일을 찾을 수 없습니다: {e}")
                except Exception as e:
                    st.error(f"모델 로딩 또는 예측 중 오류 발생: {e}")
        # else: #이거 주석처리
        #    st.info("이미지 분석 후 '질병 예측하기' 버튼을 눌러주세요.") #이거 주석처리

    # 예측이 완료된 경우에만 AI 질문 섹션 표시
    if "prediction_done" in st.session_state and st.session_state["prediction_done"]:
        st.subheader("질병 증상 질문하기")
        query = st.text_input("질문을 입력해주세요.")
        if st.button("질문 검색"):
            if query:
                with st.spinner("AI가 답변을 생성 중입니다. 잠시만 기다려주세요😎"):
                    response = get_ai_response(query)
                    st.write("답변:")
                    st.write(response)
            else:
                st.warning("질문을 입력해주세요.")

        # 가까운 대형 병원 찾기 섹션 추가
        st.subheader("가까운 대형 병원 찾기")
        search_query = st.text_input("주소나 지역을 입력하세요", "모란역")

        if st.button("병원 검색", key="hospital_search"):
            with st.spinner("검색 중..."):
                try:
                    api_key = "AIzaSyB8mowLjtvuBo08PR928roUhEHs5im-m-c"
                    gmaps = googlemaps.Client(key=api_key)

                    geocode_result = gmaps.geocode(search_query)
                    if geocode_result:
                        lat = geocode_result[0]["geometry"]["location"]["lat"]
                        lng = geocode_result[0]["geometry"]["location"]["lng"]

                        m = folium.Map(location=[lat, lng], zoom_start=14)

                        places_result = gmaps.places_nearby(
                            location=(lat, lng),
                            radius=10000,
                            keyword="대학병원 OR 종합병원 OR 3차병원",
                            type="hospital",
                            language="ko",
                        )

                        large_hospitals = []
                        for place in places_result["results"]:
                            if (
                                "대학병원" in place["name"]
                                or "의과대학병원" in place["name"]
                                or "종합병원" in place["name"]
                            ):
                                large_hospitals.append(place)
                                folium.Marker(
                                    [
                                        place["geometry"]["location"]["lat"],
                                        place["geometry"]["location"]["lng"],
                                    ],
                                    popup=place["name"],
                                    tooltip=place["name"],
                                ).add_to(m)

                        folium_static(m)

                        if large_hospitals:
                            for hospital in large_hospitals:
                                st.write(f"🏥 {hospital['name']}")
                                st.write(f" 주소: {hospital['vicinity']}")
                                st.write(
                                    f" 평점: {hospital.get('rating', '정보 없음')}"
                                )
                                st.write("---")
                        else:
                            st.warning("주변에 대형 병원을 찾을 수 없습니다.")
                    else:
                        st.error("주소를 찾을 수 없습니다.")
                except Exception as e:
                    st.error(f"병원 검색 중 오류가 발생했습니다: {e}")


# 이 파일을 직접 실행하는 경우
if __name__ == "__main__":
    st.warning(
        "이 파일은 모듈로 사용되어야 합니다. Streamlit 앱의 주 진입점으로 사용하지 마세요."
    )
