import json
import asyncio
import aiohttp
from typing import Union, Tuple

from loguru import logger

import helpers


class Weather:
    def __init__(self, urls) -> None:
        self.urls = urls
        self.all_data = []
        asyncio.run(self.main())

    async def fetch(self, session, url) -> Union[Tuple[str, str] or None]:
        retry_delay = 5
        try:
            async with session.get(url) as response:
                resp = await response.json()
                return resp, url
        except Exception as e:
            await asyncio.sleep(retry_delay)
            logger.error(e)

    async def main(self) -> None:
        """Асинхронный запуск парсера json"""
        tasks = []
        async with aiohttp.ClientSession() as session:
            for url in self.urls:
                tasks.append(self.fetch(session, url))
            json_response = await asyncio.gather(*tasks)
            self.all_data.extend(json_response)
            self.save_to_json_file()

    def save_to_json_file(self) -> None:
        with open('weather.json', 'a') as outfile:
            json.dump(self.all_data, outfile)


urls = helpers.generate_new_urls()
Weather(urls)

