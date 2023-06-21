import asyncio
import random
import math

HALF_AN_HOUR_IN_SEC = 60 * 30
HOUR_AND_A_HALF_IN_SEC = 60 * 90


class Scheduler:
    def __init__(self, api_client=None):
        self.api_client = api_client
        self.is_running = False

    async def run(self):
        self.is_running = True

        while self.is_running:
            print(f"- Fetching your listings")
            posts_ids = await self.api_client.get_my_posts_ids()

            if len(posts_ids) == 1:
                print(f"- Starting to share one listing")
            else:
                print(f"- Starting to share {len(posts_ids)} listings")

            for post_id in posts_ids:
                pause_in_sec = random.randint(3, 6)
                await asyncio.sleep(pause_in_sec)

                print(f"- Pausing for: {pause_in_sec} sec")

                await self.api_client.share_post(id=post_id)

                print(
                    f"- Shared post: '{post_id}' successfully")

            pause_in_sec = random.randint(
                HALF_AN_HOUR_IN_SEC, HOUR_AND_A_HALF_IN_SEC)

            minutes_to_sleep = math.floor(pause_in_sec / 60)

            print(f"- Pausing for: {minutes_to_sleep} min")

            await asyncio.sleep(pause_in_sec)

    def stop(self):
        self.is_running = False
