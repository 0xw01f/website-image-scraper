from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse
import requests
import os

URL = "https://cyberocc.com/"

soup = bs(requests.get(URL).content, "html.parser")
img_urls = []
for img in soup.find_all("img"):
    img_url = URL + img.attrs.get("src")
    img_urls.append(img_url)

image_path = 'images/' + urlparse(URL).netloc

if not os.path.exists(image_path):
    os.makedirs(image_path)

for url in img_urls:
    print(url.split("/")[-1])
    response = requests.get(url)
    size = int(response.headers.get("Content-Length", 0))
    try:
        name = os.path.join(image_path, url.split("/")[-1])
        print(name)
        with open(name, "wb") as f_out:
            f_out.write(response.content)
    except:
        pass