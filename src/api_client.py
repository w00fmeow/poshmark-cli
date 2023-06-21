
import aiohttp
from bs4 import BeautifulSoup

DOMAIN = "https://poshmark.com"


def make_soup(html):
    return BeautifulSoup(html, 'html.parser')


class PoshMarkApiClient:
    def __init__(self, headers=None, user_name=None):
        self.user_name = user_name
        self.session = aiohttp.ClientSession(headers=headers)

    async def share_post(self, id=None):
        url = f"{DOMAIN}/vm-rest/users/self/shared_posts/{id}?pm_version=249.0.0"
        response = await self.session.put(url, json=dict())

        data = await response.json()

        return data

    async def get_my_posts_ids(self):
        url = f"{DOMAIN}/closet/{self.user_name}"
        response = await self.session.get(url)

        html = await response.text()

        return self.parse_posts_response(html=html)

    def parse_posts_response(self, html=None):
        ids = set()
        soup = make_soup(html)

        posts_elements = soup.select('[data-et-prop-listing_id]')

        for post in posts_elements:
            ids.add(post["data-et-prop-listing_id"])

        return list(ids)

    async def close(self):
        try:
            await self.session.close()
        except:
            pass

    async def dump_headers(self):
        return self.session.headers
