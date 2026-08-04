import asyncio
import httpx

async def fetch(client, url):
    try:
        r = await client.get(url, timeout=10)
        return r.text
    except httpx.RequestError:
        return None

async def main():
    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(
            fetch(client, url1),
            fetch(client, url2),
            fetch(client, url3),
        )

asyncio.run(main())