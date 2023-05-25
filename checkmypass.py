import requests
import hashlib
from getpass import getpass


def request_api_data(query_characters):
    url = 'https://api.pwnedpasswords.com/range/' + query_characters
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Error fetching: {response.status_code}, check the API and try again.')
    return response


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main():
    password = getpass(prompt='Enter a password: ', stream=None)
    count = pwned_api_check(password)
    if count:
        print(f'{password} was found {count} times. Change your password!')
    else:
        print(f'{password} was not found.')


if __name__ == '__main__':
    main()
