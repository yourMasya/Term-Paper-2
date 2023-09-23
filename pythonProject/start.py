from bs4 import BeautifulSoup as BS
import pandas as pd
from main import url_generator, get_urls_using_selenium, process_html, generate_dataframe
import json
import re
import requests
from time import sleep
from random import randint
a = {
    "seed_urls": [],
    "headers": {"accept": "application/json, text/plain, */*", 
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control": "no-cache",
                "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control": "no-cache",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"},
    "total_articles_to_find_and_parse": 5,
    "encoding": "utf-8",
    "timeout": 5,
    "should_verify_certificate": "true",
    "headless_mode": "true"
}

headers = {'Accept': '*/*',
      'Accept-Encoding': 'gzip, deflate, br',
      'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
      'Connection': 'keep-alive',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.'
      }

#   'accept': '*/*',
# 'accept-encoding': 'gzip, deflate, br',
# 'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
# 'cache-control': 'no-cache',
# 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'

l1 = 'https://ruscorpora.ru/results?search=CtwDEisKKRInChUKA2xleBIOCgzQv9GA0LDQstC00LAKDgoFZ3JhbW0SBQoDKFMpIpUDCpIDCioKJHByaV9jYXQ60YXRg9C00L7QttC10YHRgtCy0LXQvdC90LDRjxoCCAEKrAIKIXR5cGU60YXRg9C00L7QttC10YHRgtCy0LXQvdC90LDRjxKGAgqDAtC00L3QtdCy0L3QuNC6LCDQt9Cw0L/QuNGB0L3Ri9C1INC60L3QuNC20LrQuCB8INC70LXQs9C10L3QtNCwIHwg0L7Rh9C10YDQuiB8INC/0LjRgdGM0LzQviDQu9C40YLQtdGA0LDRgtGD0YDQvdC%2B0LUgfCDQv9C%2B0LLQtdGB0YLRjCB8INC/0L7RjdC80LAgfCDQv9GA0LjRgtGH0LAgfCDQv9GM0LXRgdCwIHwg0YDQsNGB0YHQutCw0LcgfCDRgNC%2B0LzQsNC9IHwg0YHQutCw0LfQutCwIHwg0YHQutCw0LcgfCDRgdGG0LXQvdCw0YDQuNC5IHwg0YbQuNC60LsKNQoQdGV4dF9vcnRob2dyYXBoeRIhCh/QndC%2B0LLQsNGPINC%2B0YDRhNC%2B0LPRgNCw0YTQuNGPKg4KCAgAEDIYMiAyIABABTICCAE6AQEwAQ=='
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

if __name__ == "__main__":

    # urls = url_generator(l1, alphabet)
    # print(get_urls_using_selenium(1, l1))
    # for number in urls:
    #    get_urls_using_selenium(number, urls[number])

    # with open('urls.txt', 'w') as f:
    #     f.write("\n".join(urls.values()))
    #     sentences = []
    #     counter = 0
    #
    #     r = requests.get(l1, headers=headers)
    #     src = r.text
    #     html = BS(r.content, 'lxml')
    #     print(html)

    #pages_dict = open_html()
    #print(list(pages_dict))

    df = []
    for i in generate_dataframe(process_html):
        df += i
    out_file = open('df_pravda.json', 'w', encoding='utf-8')
    json.dump(df, out_file, ensure_ascii=False, indent=6)
    out_file.close()
    # df.to_json(orient='records')
    # '[{"col 1":"a","col 2":"b"},{"col 1":"c","col 2":"d"}]'
    # pd.read_json(_, orient='records')

    # for i in urls.values():
    #     counter += 1
    #     r = requests.get(i)
    #     html = BS(r.content, 'lxml')
    #     page = html.find_all('div', class_='concordance-item__group')
    #     sleep(randint(2, 4))
    #     for sentence in page:
    #         if sentence:
    #             sentences.append(sentence.text.strip())
    #     print(f"Iterations made: #{counter}")
    #     if counter % 10 == 0:
    #         print(sentences)
