import os
import requests
from uuid import uuid4
import time
from urllib import parse
import asyncio
from aiohttp import ClientSession
import aiofiles

def save_post_image(url):
    start = time.time()
    for _ in range(25):
        response = requests.get(url)
        extension = os.path.splitext(parse.urlsplit(response.url).path)[-1]
        image_name = f'{uuid4()}{extension}'
        path = f'images/{image_name}'
        with open(path, mode='wb') as f:
            f.write(response.content)

    elapsed = time.time() - start
    print(f'{elapsed} s')

async def make_request(session):
    try:
        resp = await session.request(method="GET", url=url)
    except Exception as ex:
        print(ex)
        return

    if resp.status == 200:
        image_name = f'{uuid4()}.jpg'
        path = f'async_images/{image_name}'

        async with aiofiles.open(path, 'wb') as f:
            await f.write(await resp.read())


async def bulk_request():
    """Make requests concurrently"""
    async with ClientSession() as session:
        tasks = []
        for _ in range(25):
            tasks.append(
                make_request(session)
            )
        await asyncio.gather(*tasks)


def download_images():
    start = time.time()
    asyncio.run(bulk_request())
    print('{} s'.format(time.time() - start))