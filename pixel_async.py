import asyncio
import httpx
from key import keys


async def downloadd(query, current_page):
    header = keys
    params = {"query": query, "per_page": 1, "page": current_page}
    url = 'https://api.pexels.com/v1/search'

    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=header, params=params)
        if r.status_code == 200:
            _r = r.json()
            for item in _r.get("photos"):
                print(item.get("src").get("original"))
        else:
            print(r.status_code)
    print(f'{query} = {current_page}')


async def main():
    queve = asyncio.Queue()

    query = input('введите раздел картинок которые вы хотите загрузить: ')
    page_count = int(input('введите количество картинок которые вы хотите загрузить: '))

    current_page = 0
    task_list = []

    while current_page < page_count:
        current_page += 1
        task = asyncio.create_task(downloadd(query, current_page))
        task_list.append(task)
    await queve.join()

    await asyncio.gather(*task_list, return_exceptions=True)  # <-- return_exceptions = возврат исключений


asyncio.run(main())

