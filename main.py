from hashlib import md5
import requests
import json
from bs4 import BeautifulSoup
from datetime import date
import excel2img
from PIL import Image



user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
session = requests.Session()
session.headers.update({'User-Agent': user_agent})

url = "https://fms.eljur.ru/authorize"
session.headers.update({'Referer': url})

data = {
    "username": '89504075585',
    "password": '89504075585'
}
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

# авторизация
ss = session.post("https://fms.eljur.ru/ajaxauthorize", data=data, headers=headers)
date = str(date.today()).split('-')
# date = f'{date[2]}.{date[1]}'
date = f'20.12'

json_string = session.get('https://fms.eljur.ru/journal-board-action')
bs = BeautifulSoup(json_string.text, "html.parser")
d = [el['href'] for el in bs.find_all("a", {"title": f"{date}.xlsx"})]
if not d:
    print('рассписание отсутствует')
    exit()


response = session.get(d[0])
file_Path = 'Sample.xlsx'

if response.status_code == 200:
    with open(file_Path, 'wb') as file:
        file.write(response.content)
    print('File downloaded successfully')
else:
    print('Failed to download file')


excel2img.export_img("Sample.xlsx", f"{date}-10.png",'10',None)
try:
 excel2img.export_img("Sample.xlsx", f"{date}-11.png",'11',None)
except:
    excel2img.export_img("Sample.xlsx", f"{date}-11.png", '11 ', None)


Image.open(f'{date}-11.png').save(f'{date}-11.jpg')
Image.open(f'{date}-10.png').save(f'{date}-10.jpg')



_TOKEN = "5724039823:AAHzq9Fp4JK4PAerNWYkyKtCV5CmY7ZARWg"


def send_photo(chat_id, image_path, image_caption=""):
    data = {"chat_id": chat_id, "caption": image_caption}
    url = f"https://api.telegram.org/bot{_TOKEN}/sendDocument?chat_id={chat_id}"
    print(url)
    with open(image_path, "rb") as image_file:
        ret = requests.post(url, data=data, files={"document": image_file})
    return ret.json()
send_photo('5480167477',f'{date}-11.jpg')

session.close()
