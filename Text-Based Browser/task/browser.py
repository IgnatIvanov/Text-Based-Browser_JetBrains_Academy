import argparse
import requests
import os
from bs4 import BeautifulSoup
from colorama import Fore, init


history_stack = []  # Stack for browser history in current session


def save_page(name, site):
    file = open(save_dir + '\\' + name, 'w', encoding='utf-8')
    file.write(str(site))
    file.close()


def print_page(name):
    file = open(save_dir + '\\' + name, 'r')
    soup_string = ''
    for line in file.readlines():
        soup_string += line
    soup = BeautifulSoup(soup_string, 'html.parser')
    site_content = soup.find_all(["p", 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li'])
    print_text(site_content)
    file.close()


def extract_content(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    site_content = soup.find_all(["p", 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li'])
    return site_content


def print_text(site_content):
    init(autoreset=True)
    for line in site_content:
        print(line)
        if str(line).find('href') >= 0:
            print(Fore.BLUE + line.get_text(), sep='\n')
        else:
            print(line.get_text(strip=True), sep='\n')
            print(line.get_text(), sep='\n')


parser = argparse.ArgumentParser()  # Need parser for handling run parameters
parser.add_argument('current_dir')  # Create positional argument for sites pages directory
args = parser.parse_args()
os.makedirs(os.getcwd() + '/' + args.current_dir, exist_ok=True)


script_dir = os.getcwd()
save_dir = os.getcwd() + '\\' + args.current_dir

url = ''
prev_url = ''
while url != 'exit':
    url = str(input())
    if url == 'back':
        if len(history_stack) == 0:
            pass
        else:
            url = history_stack.pop()
    else:
        history_stack.append(prev_url)
    try:
        print_page(url[:url.find('.')])
        prev_url = url
    except FileNotFoundError:
        if '.' not in url:
            # print('Error: Incorrect URL')
            print('Incorrect URL')
        elif url == 'exit':
            pass
        else:
            prefix = ''
            if url[8:] != 'https://':
                prefix = 'https://'
            site_text = extract_content(prefix + url)
            print_text(site_text)
            save_page(url[:url.find('.')], site_text)
            prev_url = url
