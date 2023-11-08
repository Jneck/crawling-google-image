# crawling-google-image
셀레니움4를 사용한 구글 이미지 크롤링 및 얼굴 사진 크롭

## 라이브러리 설치
### 크롤링에
- pip install selenium
- pip install --upgrade selenium
- pip install webdriver-manager

### 기존에 저장된 이미지 파일 crop하여 재저장
- opencv 및 dlib: pip install opencv-python dlib

## crawling.py
셀리니움4를 이용해서 구글 이미지 검색기에서 검색어에 
해당하는 이미지들을 개수만큼 크롤링하여 해당 폴더에 저장해줍니다.

## crop_face.py
저장되어 있는 img파일에서 얼굴 부분만 crop하여 재저장해줍니다

## change_name_to_english.py
저장되어 있는 파일들이 한글명일 경우 <b>crop_face.py</b>가 제대로 작동하지
않기 때문에 인물명에 맞게 이름을 변환합니다.  
  
**되도록이면 크롤링시 이름을 영어로 저장하길 권장드립니다.**
