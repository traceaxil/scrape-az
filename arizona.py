import sys
import os
from bs4 import BeautifulSoup

def decode_cloudflare_email(encoded_email):
    r = int(encoded_email[:2],16)
    email = ''.join([chr(int(encoded_email[i:i+2], 16) ^ r) for i in range(2, len(encoded_email), 2)])
    return email

def parse_page():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'arizona.html')
    page = open(file_path, 'r')
    soup = BeautifulSoup(page.read(), 'html.parser')
    tags = soup.find_all('a')
    for tag in tags:
        if 'data-cfemail' in tag.attrs:
            print(decode_cloudflare_email(tag.attrs['data-cfemail']))

def main(argv):
    parse_page()

if __name__ == '__main__':
    main(sys.argv[1:])


