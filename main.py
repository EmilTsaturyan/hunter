import aiohttp
import asyncio

from sites import sites


async def check_username_availability(username: str, sites: dict) -> dict:
    username_availability = {}
    for site, site_info in sites.items():
        print(f'Checking on {site}')
        try:
            url = site_info['url'].format(username)
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        username_availability[site] = url
                        print(f'[+] {site}: {url}')
                        continue
        except:
            continue

    return username_availability


def print_username_availability(username: str, username_availability: dict) -> None:
    for site, url in username_availability.items():
        print(f'Username {username} is available on {site}: {url}')


async def main():
    username = input('Enter username: ')
    print(f'[*] Checking username {username} on:')
    username_availability = await check_username_availability(username, sites)
    print_username_availability(username, username_availability)


if __name__ == '__main__':
    asyncio.run(main())