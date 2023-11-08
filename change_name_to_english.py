import os

# 이미지 파일이 있는 폴더 경로
folder_path = 'img_data'

# 폴더 내의 파일 목록 가져오기
file_list = os.listdir(folder_path)

# 카테고리명 영어
category_dict = {'봄웜톤': 'spring_warm'}
my_category = '봄웜톤'

# 사람 이름 딕셔너리 -> 자신이 설정한 사람 이름을 넣으세요
people_dict = {'송중기': 'sjg', '이정재': 'ljj', '아이유': 'IU', '수지': 'suji', '차태현': 'cth', '전현무': 'jhm'}
people_idx_dict = {'송중기': 0, '이정재': 0, '아이유': 0, '수지': 0, '차태현': 0, '전현무': 0}

# 이미지 파일들만 골라내어 이름 변경
for idx, filename in enumerate(file_list):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):

        person_name = ''
        for j in range(len(my_category), len(filename)):
            print(filename[j])
            if ord(filename[j]) <= 57:
                break
            person_name += filename[j]

        new_filename = f'{category_dict[my_category]}_{people_dict[person_name]}{people_idx_dict[person_name] + 1}.jpg'
        people_idx_dict[person_name] += 1

        # 파일 경로 변경
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)

        # 파일 이름 변경
        os.rename(old_path, new_path)

        print(f'파일 이름 변경: {filename} -> {new_filename}')