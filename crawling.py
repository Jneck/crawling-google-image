from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import urllib.request
import os
basic = os.getcwd()

#######
####### 설정해야 할 부분
search = "전현무"   # 이미지 이름
count = 100    # 크롤링할 이미지 개수

folder_name = "img_data"
saveurl = basic+f"/{folder_name}/"  # 이미지들을 저장할 폴더 주소
category = '봄웜톤'

#######
#######

# 폴더 없으면 생성해주기
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f'폴더 생성: {folder_name}')
else:
    print(f'폴더 이미 존재: {folder_name}')


## 셀레니움으로 구글 이미지 접속 후 이미지 검색

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl")
elem = driver.find_element(By.NAME,"q")
elem.send_keys(search)

elem.send_keys(Keys.RETURN)

# 페이지 끝까지 스크롤 내리기
SCROLL_PAUSE_TIME = 1
# 스크롤 깊이 측정하기
last_height = driver.execute_script("return document.body.scrollHeight")

# 스크롤 끝까지 내리기
# 이미지 스크롤링
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') # 브라우저 끝까지 스크롤
    time.sleep(1) # 쉬어주기
    try:
        button = driver.find_element(By.XPATH, '//*[@id="islmp"]/div/div/div/div/div[1]/div[2]/div[2]/input')
        button.click() # 스크롤을 내리다보면 '결과 더보기'가 있는 경우 버튼 클릭
        time.sleep(1)
    except:
        pass
    if driver.find_element(By.CLASS_NAME, 'OuJzKb.Yu2Dnd').text == '더 이상 표시할 콘텐츠가 없습니다.': # class 이름으로 가져오기
        break

#이미지 찾고 다운받기
images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")

for i in range(count):
    try:
        images[i].click() # 이미지 클릭
        #print('here1')
        time.sleep(1)

        imgUrl = driver.find_element(By.XPATH,
            '//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]').get_attribute("src")
        imgUrl = imgUrl.replace('https', 'http')
        #print('here2')

        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent', 'Mozilla/5.0')]  # https://docs.python.org/3/library/urllib.request.html 참고
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(imgUrl, saveurl + category + search + str(i) + ".jpg")    # 이미지 다운
        #print(imgUrl, saveurl + search + str(i))
    except:
        pass
driver.close()