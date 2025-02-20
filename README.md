# nail-app
- 네일 이미지를 업로드하면 질병을 예측할 수 있는 앱입니다. Teachable Machine의 keras_model.h5 모델을 활용하여 개발했습니다.

## Streamlit URL
- **앱 실행 URL**: `http://[내 스트림릿 URL 주소]`


## 기술 스택
- **Python** == 3.10.16
- **Streamlit** == 1.41.1
- **TensorFlow** == 2.15
- **Pillow** == 11.0.0
- **NumPy** == 1.26.4




## 개발 계기
- 주변 사람들의 네일을 보다가 의문이 생겨, 웹사이트에서 검색하던 중에
- 네일 상태로 질병을 알 수 있다는 사실을 알게 되었습니다. 
- 머신러닝을 활용하여 네일 상태로 질병을 예측할 수 있는 앱을 개발하게 되었습니다.





## 사용한 dataset
- **Kaggle** https://www.kaggle.com
  - Nail Disease Detection: https://www.kaggle.com/datasets/nikhilgurav21/nail-disease-detection-dataset
  - Nail Disease Image Classification Dataset: https://www.kaggle.com/datasets/josephrasanjana/nail-disease-image-classification-dataset





## 인공지능 학습 모델 URL
- **TeachableMachine**: [https://teachablemachine.withgoogle.com/train/image](https://teachablemachine.withgoogle.com/train/image)



## 기능
- **네일 질병 예측**: 네일 이미지를 통해 질병을 예측하는 머신러닝 기반 앱입니다.
- **Streamlit 웹 UI**: 사용자 친화적인 웹 인터페이스를 제공하여 네일 이미지를 업로드하고 네일 상태에 따른 질병을 예측할 수 있습니다.



## 인용한 URL  
- **HiDoc 뉴스**: [https://news.hidoc.co.kr/news/articleView.html?idxno=24372](https://news.hidoc.co.kr/news/articleView.html?idxno=24372)
- **MSD 매뉴얼 일반인용**: [https://www.msdmanuals.com/ko/home/%ED%8F%90-%EB%B0%8F-%EA%B8%B0%EB%8F%84-%EC%9E%A5%EC%95%A0/%ED%8F%90-%EC%9E%A5%EC%95%A0-%EC%A6%9D%EC%83%81/%EA%B3%A4%EB%B4%89%EC%A6%9D](https://www.msdmanuals.com/ko/home/%ED%8F%90-%EB%B0%8F-%EA%B8%B0%EB%8F%84-%EC%9E%A5%EC%95%A0/%ED%8F%90-%EC%9E%A5%EC%95%A0-%EC%A6%9D%EC%83%81/%EA%B3%A4%EB%B4%89%EC%A6%9D)
- **광양사랑병원**: [http://www.gysarang.com/Module/News/Lecture.asp?MODE=V&SRNO=2585](http://www.gysarang.com/Module/News/Lecture.asp?MODE=V&SRNO=2585)







## 개발 과정
1. **데이터 수집**:
    - Kaggle에서 `Nail Disease Detection`과 `Nail Disease Image ClassificationDataset`      
      다운로드하여 사용했습니다.

2. **모델 학습**:
    - `TeachableMachine`의 이미지 프로젝트 표준 모델을 사용하여 6개 클래스(Acral Lentiginous   
      Melanoma, Blue Finger, Clubbing, Healthy Nail, Onychogryphosis, Pitting) 에포크 100, 배치 크기 16으로 `keras_model.h5`모델을 학습했습니다
    - `keras_model.h5`모델을 학습 후, 테스트 이미지를 업로드하여 정확도를 확인했습니다.

3. **데이터 수정**:
    - 한글 라벨링을 위해 네이버 검색을 통해 질병 정보를 수집하고, labels 파일을 수정했습니다. 

4. **프로젝트 설정**:
    - Github에서 `nail-app` 프로젝트를 생성하고, 이를 로컬 PC로 클론하여 개발을 시작했습니다.
    - Python 3.10.16 버전의 가상 환경을 설정한 후, 필요한 패키지들을 `requirements.txt`에 명시하고 설치했습니다.


5. **파일 및 폴더 구성**:
    - `app.py`: 앱의 메인 실행 파일로, Streamlit을 이용해 앱을 실행합니다.
    - `ui` 폴더:
        - `home.py`: 앱 소개 및 사용법을 안내하는 화면을 담당합니다.
        - `eda.py`: 네일 이미지를 업로드하고, 업로드된 이미지에 대한 기본 정보를 제공하는 페이지입니다.
        - `ml.py`: 머신러닝 모델을 로드하고 예측 결과를 사용자에게 보여주는 페이지입니다.
    - `model` 폴더:
        - `keras_model.h5`: 학습된 모델 파일입니다.
        - `labels.txt`: 모델의 예측을 위한 레이블 파일입니다.
    - `nail.ipynb`: Jupyter 노트북으로, 모델을 학습하고 테스트한 코드를 포함하고 있습니다.


6. **로컬에서 실행**:
    - 로컬 환경에서 streamlit run ui/app.py 명령어를 실행해서 테스트했습니다.


7. **streamlit 실행**:
    - streamlit 웹사이트에서 앱이 작동하는지 실행했습니다.




## nail-app 구조   
### ├── README.md
### │ 
### ├── ui/ : 앱의 사용자 인터페이스 관련 파일
### │   ├── app.py              # Streamlit 앱 실행 파일
### │   ├── home.py             # 홈 화면
### │   ├── eda.py              # 데이터 분석 코드
### │   └── ml.py               # 머신러닝 모델 관련 코드
### │ 
### ├── model/ : 학습된 모델과 레이블 파일
### │    ├── keras_model.h5     # 학습된 모델 파일
### │    └── labels.txt         # 모델 학습에 사용된 레이블 파일
### │ 
### ├── nail.ipynb              # 데이터 분석 및 모델 훈련을 위한 Jupyter 노트북
### └── requirements.txt        # 필요한 패키지 목록




## 사용법
1. **앱 실행**:
    - Streamlit URL을 통해 앱을 실행합니다.


2. **네일 이미지 업로드**:
    - '네일 상태 분석' 메뉴에서 네일 이미지를 업로드합니다.
    - 정확한 분석을 위해, 정면에서 찍은 네일 이미지를 사용하는 것이 좋습니다.



3. **질병 예측**:
    - '증상 예측' 메뉴에서 업로드한 이미지를 기반으로 모델이 질병을 예측합니다.
    - 예측 결과와 함께 신뢰도를 제공하여, 사용자에게 네일 상태에 대한 정보를 제공합니다.
