import requests
from PIL import Image
from io import BytesIO
from key import keys


def dowload(qury: str, page: int):
    my_key = keys
    i = 1
    while i <= page:
        url = f"https://api.pexels.com/v1/search?query={qury}&per_page=1&page={i}"
        resp = requests.get(url, headers=my_key)
        if resp.status_code == 200:
            _r = resp.json()
            for item in _r.get("photos"):
                print(item.get("url"))
        else:
            print(resp.text)
        i += 1


def main():
    q = input("Введите раздел картинки: ")
    p = int(input("Введите количество картинок: "))
    dowload(q, p)


if __name__ == '__main__':
    main()