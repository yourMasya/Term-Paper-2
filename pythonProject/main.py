import re
import requests
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium_stealth import stealth
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint
import json


def are_identical(str1, str2):
    different_chars = {}
    try:
        for ind, char_1 in enumerate(str1):
            char_2 = str2[ind]
            if char_1 != char_2:
                different_chars[ind] = (char_1, char_2)
    except IndexError:
        pass
    return different_chars if different_chars else True


def url_generator(link_1, alg): #  link_1 = l1, alg = alphabet
    all_urls = {1: link_1}
    part_1, part_2 = link_1[:664], link_1[665:]
    part_1_2 = link_1[:663] + 'h'
    for char_664 in range(1, 64):
        if 1 <= char_664 <= 61:
            all_urls[char_664 + 1] = "".join((part_1, alg[char_664], part_2))
        elif char_664 == 62:
            all_urls[char_664 + 1] = "".join((part_1, "%2B", part_2))
        else:
            all_urls[char_664 + 1] = "".join((part_1, '/', part_2))
    for char_664 in range(0, 58):
        all_urls[char_664 + 65] = "".join((part_1_2, alg[char_664], part_2))
    return all_urls


def get_urls_using_selenium(number, url):
    options = webdriver.FirefoxOptions()
    options.set_preference('general.useragent.override',
                            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.'
                            )

    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    driver = webdriver.Firefox(
            executable_path=r'C:\Users\79603\Desktop\Ucheba\2 курс\Кур сыч\pythonProject\venv\Scripts\geckodriver.exe',
            options=options
        )
    try:
        driver.get(url=url)
        driver.maximize_window()
        with open(rf'page_{number}_selenium.html', 'w') as file:
            file.write(driver.page_source)
            print(driver.page_source)
            # save_as = ActionChains(driver).key_down(Keys.CONTROL).key_down('s').key_up(Keys.CONTROL).key_up('s')
            # print(save_as.perform())
            # file.write(save_as.perform())
        sleep(randint(10, 15))

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def generate_dataframe(func):
    for page in range(1, 123):
        print(f'proccessing page #{page}')
        yield func(page)


def process_html(page_num, lowercase=True):
    path = rf'C:\Users\79603\Desktop\Ucheba\2 курс\Кур сыч\pythonProject\html pages\{page_num}_page.html'
    pages_lst = []
    with open(path, 'r', encoding='utf-8') as f:
        src = f.read()
        html = BS(src, 'lxml')
        texts = html.find_all('li', class_='concordance-item')

        for txt in texts:
            if txt:
                text_obj = re.split(r'\xa0', txt.get_text())
                sentences = [
                    sentence.strip() for sentence
                    in re.split(r'(?<=[.!?]{1, 3})\s+', text_obj[2])
                    if re.search(r'правд', sentence, flags=re.IGNORECASE)
                ]
                unique_sentences = set(sentences)
                for sentence in sentences:
                    if sentence in unique_sentences:
                        neighbours = re.findall(r'(\b\w{1,}\b)?\s?(правд\w*)\s?(\b\w{1,}\b)?',
                                                sentence, flags=re.IGNORECASE)
                        neighbours = list(phrase.lower() if lowercase else phrase for phrase in
                                          map(lambda x: ' '.join(x).strip(), neighbours))
                        inx_str = f'{page_num}.{text_obj[0][:-1]}.{sentences.index(sentence) + 1}'
                        row = {
                            'title': text_obj[1],
                            'sentences': sentence,
                            'neighbours': '; '.join(neighbours),
                            'page-item-sentence_indices': inx_str
                        }
                        unique_sentences.discard(sentence)
                        pages_lst.append(row)
    return pages_lst


