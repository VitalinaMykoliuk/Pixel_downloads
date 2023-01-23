import requests
from PIL import Image
from io import BytesIO
from key import keys


def dowload(qury: str, page: int):
    my_key = keys
    params = {"query": qury, "per_page": 1}
    url = f"https://api.pexels.com/v1/search"
    i = 1
    while i <= page:
        params["page"] = i
        resp = requests.get(url, headers=my_key, params=params)
        if resp.status_code == 200:
            _r = resp.json()
            for item in _r.get("photos"):
                _img_url = item.get("src").get("original")
                rezalt = requests.get(_img_url)
                print(_img_url)
                image = Image.open(BytesIO(rezalt.content))
                image.save(f"media/{qury}_{i}.{_img_url.split('.')[-1]}")

        else:
            print(resp.text)
        i += 1


def main():
    q = input("Введите раздел картинки: ")
    p = int(input("Введите количество картинок: "))
    dowload(q, p)


if __name__ == '__main__':
    main()