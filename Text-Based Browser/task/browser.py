import argparse
import requests
import collections
import os
from bs4 import BeautifulSoup
from colorama import Fore

nytimes_com = r'''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = """
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
"""

history_stack = []  # Stack for browser history in current session


def save_page(name, site):
    file = open(save_dir + '\\' + name, 'w', encoding='utf-8')
    file.write(site)
    file.close()


def print_page(name):
    file = open(save_dir + '\\' + name, 'r')
    print(*file.readlines())
    file.close()


def extract_content(url):
    site_content = ''
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    site_content = soup.get_text()
    site_list = site_content.split('\n')
    site_content = ''
    for line in site_list:
        if line == '':
            pass
        else:
            site_content += line + '\n'
    return site_content


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
            # r = requests.get(prefix + url).content
            # r = requests.get(prefix + url)
            site_text = extract_content(prefix + url)
            print(site_text)
            save_page(url[:url.find('.')], site_text)
            prev_url = url
