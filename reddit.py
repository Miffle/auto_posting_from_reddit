import asyncio

import asyncpraw

reddit = asyncpraw.Reddit(
    user_agent="XXXX",
    client_id='XXXXXXXXX',
    client_secret='XXXXXXXX')

cod = ''
url = ''
submission = ''
title = ''
witcher = ''
subred1 = ''
dot = ''
dot1 = ''


async def sravn():
    with open("witcher.txt", 'r') as file:
        old = file.read()
    while url == old:
        print("url is old")
        await asyncio.sleep(360)
        asyncio.create_task(obnov())
    print("url updates")


async def lol():
    print(url)


async def obnov():
    global cod, url, submission, title, witcher, subred1, dot, dot1
    subred1 = await reddit.subreddit("Group_Name")
    witcher = subred1.top("hour", limit=1)
    async for submission in witcher:
        cod = (submission.url[0 - 3] + submission.url[0 - 2] + submission.url[0 - 1])
        dot = submission.url[0 - 4]
        dot1 = submission.url[0 - 5]
        url = submission.url
        title = submission.title


def zapis():
    with open("witcher.txt", "w") as f:
        f.write(url)
