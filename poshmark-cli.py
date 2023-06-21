import asyncio
import sys
from src.api_client import PoshMarkApiClient
from src.scheduler import Scheduler
from argparse import ArgumentParser


parser = ArgumentParser(description='Poshmark CLI')

parser.add_argument('--username', type=str,
                    help='User name', required=True)

args = parser.parse_args()


header_file_path = "./headers.txt"


def load_headers():
    try:
        header_file = open(header_file_path, 'r').readlines()

        result = {}

        for line in header_file:
            split_result = line.split(":")

            if len(split_result) == 2:
                result[split_result[0]] = split_result[1].strip()

        return result
    except:
        print("Failed to load headers from file:", header_file_path)


def dump_headers(headers):
    file_content = ""

    for header_item in headers:
        file_content += header_item + ": " + headers[header_item] + '\n'

    with open(header_file_path, 'w+') as f:
        f.write(file_content)
        f.close()


headers = load_headers()

api_client = PoshMarkApiClient(
    user_name=args.username, headers=headers)

scheduler = Scheduler(api_client=api_client)


async def stop():
    scheduler.stop()
    new_headers = await api_client.dump_headers()
    dump_headers(new_headers)

    await api_client.close()


if __name__ == '__main__':
    print("""
      ___                  ___  
     (o o)                (o o) 
    (  V  ) poshmark cli (  V  )
    --m-m------------------m-m--\n\n""")

    print("- Starting to share your listings")

    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(scheduler.run())
    except KeyboardInterrupt:
        print('\n- Existing ...')

    finally:
        loop.run_until_complete(stop())
        sys.exit()
