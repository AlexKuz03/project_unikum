import time
import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import socks
import socket
import re

socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket
#https://cyberleninka.ru/article/c/fizika
def get_html(url):
    response = requests.get(url)
    return response.text


def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')
    lis = soup.find('div', class_='content').find('div', class_="main").find('div', class_='visible').find_all('li')
    links = []
    for li in lis:
        if len(li.find('p')) != 0:
            a = li.find('a').get('href')
            link = 'https://cyberleninka.ru/' + a
            links.append(link)
    return links


def text_before_word(text, word):
    line = text.split(word)[0].strip()
    return line


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        name = soup.find('i', itemprop='headline').text
    except:
        name = ''
    try:
        thisText = soup.find('p',
itemprop='description').text
    except:
        thisText = ''
    data = {'name': name,
            'text': thisText}
    return data


def write_csv(i, data):
    with open('1234234.csv', 'a', encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerow((re.sub('[Ёё]', 'е', data['name']),
                         re.sub('[Ёё]', 'е', data['text'])))
        print(i, data['name'], 'parsed')


def main():
    start = datetime.now()
    url = 'https://cyberleninka.ru/article/c/fizika'
    all_links = get_all_links(get_html(url))
    for i, link in enumerate(all_links):
        html = get_html(link)
        data = get_page_data(html)
        write_csv(i, data)
    for j in range(2, 16):
        url = 'https://cyberleninka.ru/article/c/fizika/' + str(j)
        print(url)
        all_links = get_all_links(get_html(url))
        for i, link in enumerate(all_links):
            html = get_html(link)
            data = get_page_data(html)
            if not([s for s in data['name'] if s in 'qwertyuiopasdfghjklzxcvbnm'] or [s for s in data['text'] if s in 'qwertyuiopasdfghjklzxcvbnm']):
                write_csv(i, data)
            else:
                print('not')
        time.sleep(5)
    end = datetime.now()
    total = end - start
    print(str(total))
    a = input()

if __name__ == '__main__':
    main()