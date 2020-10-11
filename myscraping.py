import os
import time
from io import BytesIO, StringIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from bs4 import BeautifulSoup
import urllib.request
import ulid

abs_path = os.getcwd()

ScrapingTime = 3
waittime = 0.5
driver_path = "driver\chromedriver86.exe"
# driver_path = chromedriver_binary.chromedriver_filename
print(driver_path)

options = webdriver.chrome.options.Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--user-agent=hogehoge')
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--no-sandbox')
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"

#特定のWEBページからURLリストを取得する
def getScrapingImageURLs(url, Selector, num=100):
    time.sleep(ScrapingTime)
    driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
    #driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Selector))
    )
    leng = 0
    for i in range(num):
        print(i)
        driver.execute_script(
            "window.scrollTo(0, document.getElementsByClassName('justified-gallery')[0].scrollHeight)")
        soup = BeautifulSoup(driver.page_source, features="html.parser")
        time.sleep(waittime*i)
        imgs = soup.find_all('img')
        if i>10 and leng == len(imgs):
            break
        leng = len(imgs)
        print(len(imgs))
    print("合計アクセス数：", len(imgs), "枚です。")
    image_urls = []
    for img in imgs:
        image_urls.append(img["src"])

    time.sleep(1)
    return image_urls

#画像のURLリストから指定ディレクトリに保存する
def saveImageFromURLs(image_urls, save_dir, save_type="local"):
    save_urls = []
    for index, image_url in enumerate(image_urls):
        filename = getULIDStr() + ".jpg"
        save_path = convDirAddName(save_dir, filename)
        try:
            time.sleep(0.1)
            pil_image = urlToPILImage(image_url)
            save_url = savePILImageInLocal(save_path, pil_image)
        except Exception as e:
            print("saveImageFromURLs Error")
            print(e)
            if os.path.exists(save_path):
                os.remove(save_path)
    return save_urls

def convDirAddName(dirname, filename):
    if dirname[-1] == "/" or dirname[-1] == "\\":
        return dirname+filename
    return dirname + "/" + filename

def urlToPILImage(url):
    f = BytesIO(urllib.request.urlopen(url).read())
    return Image.open(f)

def savePILImageInLocal(save_path, pil_image):
    pil_image.save(save_path)
    return save_path

def getULIDStr():
    id1 = ulid.new()
    return id1.str

if __name__ == "__main__":
    save_dir = "images"
    keyword = "海"
    save_dir = "images/"+keyword
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    url = 'https://500px.com/search?submit=送信q=%s&type=photos' % keyword
    Selector = ".photo_link"

    image_urls = getScrapingImageURLs(url, Selector, 200)

    print(image_urls)
    save_urls = saveImageFromURLs(image_urls, save_dir)
    print("save complete")