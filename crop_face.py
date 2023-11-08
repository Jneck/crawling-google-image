import cv2
import dlib
import os

# 이미지 파일과 얼굴을 저장할 폴더 경로 설정
input_folder = 'img_data'  # 이미지가 있는 폴더
output_folder = 'cropped_faces'  # 얼굴을 저장할 폴더
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Dlib 얼굴 검출기 초기화
detector = dlib.get_frontal_face_detector()

# 이미지 폴더 내의 모든 이미지 파일에 대해 처리
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
        image_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # 이미지 파일을 읽어옴
        try:
            image = cv2.imread(image_path)
            if image is None:
                raise FileNotFoundError(f"이미지 파일을 읽을 수 없습니다: {image_path}")

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # 얼굴 검출
            faces = detector(gray)

            # 얼굴이 여러 개인 경우, 각 얼굴에 대해 반복
            for i, face in enumerate(faces):
                x, y, w, h = face.left(), face.top(), face.width(), face.height()

                # 얼굴 부분을 크롭
                cropped_face = image[y:y+h, x:x+w]

                # 얼굴 이미지 저장
                cropped_face_path = f"{output_path.split('.')[0]}_{i+1}.jpg"
                cv2.imwrite(cropped_face_path, cropped_face)

                # print(f'얼굴 이미지 저장 완료: {cropped_face_path}')

        except Exception as e:
            print(f"오류 발생: {e}")