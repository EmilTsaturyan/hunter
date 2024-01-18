from sites import sites
import requests


def check_username_availability(username: str, sites: dict) -> dict:
    username_availability = {}
    for site, site_info in sites.items():
        try:
            url = site_info['url'].format(username)
            response = requests.get(url)
            if response.status_code == 200:
                username_availability[site] = url
                print(f'[+] {site}: {url}')
                continue
        except:
            continue

    return username_availability


def print_username_availability(username: str, username_availability: dict) -> None:
    for site, url in username_availability.items():
        print(f'Username {username} is available on {site}: {url}')


def main():
    username = input('Enter username: ')
    print(f'[*] Checking username {username} on:')
    username_availability = check_username_availability(username, sites)
    print_username_availability(username, username_availability)


if __name__ == '__main__':
    main()