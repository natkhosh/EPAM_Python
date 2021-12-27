"""
Homework
Ваша задача спарсить информацию о компаниях, находящихся в индексе S&P 500
с данного сайта:
https://markets.businessinsider.com/index/components/s&p_500

Для каждой компании собрать следующую информацию:

Текущая стоимость в рублях (конвертацию производить по текущему курсу,
взятому с сайта центробанка РФ)
Код компании (справа от названия компании на странице компании)
P/E компании (информация находится справа от графика на странице компании)
Годовой рост/падение компании в процентах (основная таблица)
Высчитать какую прибыль принесли бы акции компании (в процентах), если бы
они были куплены на уровне 52 Week Low и проданы на уровне 52 Week High
(справа от графика на странице компании)
Сохранить итоговую информацию в 4 JSON файла:

Топ 10 компаний с самими дорогими акциями в рублях.
Топ 10 компаний с самым низким показателем P/E.
Топ 10 компаний, которые показали самый высокий рост за последний год
Топ 10 комппаний, которые принесли бы наибольшую прибыль, если бы были
куплены на самом минимуме и проданы на самом максимуме за последний год.
Пример формата:
[
{
    "code": "MMM",
    "name": "3M CO.",
    "price" | "P/E" | "growth" | "potential profit" : value,
},
...
]
For scrapping you cans use beautifulsoup4
For requesting aiohttp
"""
# import asyncio
import datetime
import json
import re
from collections import defaultdict
from heapq import nlargest, nsmallest

# import aiohttp
import requests
from bs4 import BeautifulSoup

URL = "https://markets.businessinsider.com/index/components/s&p_500"
COMPANY_INFO = defaultdict(dict)


def current_usd_rate():
    data = datetime.datetime.now()
    url = "http://www.cbr.ru/scripts/XML_daily.asp?date_req=" \
          + data.strftime('%d/%m/%Y')

    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    return float(soup.find("valute", attrs={"id": "R01235"}).
                 value.text.replace(",", "."))


def get_last_page(url):
    # url = "https://markets.businessinsider.com/index/components/s&p_500"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    num_pages = soup.find('div', class_="finando_paging margin-top--small").\
        find_all("a")
    return int(num_pages[-2].text)


def company_list():
    rub = current_usd_rate()
    for i in range(1, 2):
        url = f"https://markets.businessinsider.com/index/" \
              f"components/s&p_500?p={i}"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        table_body = soup.find("tbody", class_="table__tbody")
        table_rows = table_body.find_all("tr")

        for row in table_rows:
            href = row.find("a")["href"]
            company_url = "https://markets.businessinsider.com" + href
            code = re.split(r"/", href)[-1].split("-")[0].upper()
            name = row.find("a").text.strip()
            growth = float(row.find_all("td")[-1].find_all("span")[-1].
                           text[:-1])
            price = float(row.find_all("td")[1].text.split()[0].
                          strip().replace(',', '')) * rub

            COMPANY_INFO[company_url]["code"] = code
            COMPANY_INFO[company_url]["name"] = name
            COMPANY_INFO[company_url]["growth"] = growth
            COMPANY_INFO[company_url]["price"] = price


def get_pe_ratio():

    for company_url in COMPANY_INFO.keys():
        res = requests.get(company_url)
        soup = BeautifulSoup(res.text, 'html.parser')
        try:
            pe_value = float(soup.find("div", string="P/E Ratio").parent
                             .find(text=True).strip().replace(',', ''))
        except AttributeError:
            pe_value = 0

        COMPANY_INFO[company_url]["P/E"] = pe_value


def get_potential_profit():
    for company_url in COMPANY_INFO.keys():
        res = requests.get(company_url)
        soup = BeautifulSoup(res.text, 'html.parser')

        week_high_element = soup.find(
            class_="snapshot__header", text="52 Week High")
        week_low_element = soup.find(
            class_="snapshot__header", text="52 Week Low")
        if week_low_element is None and week_high_element is None:
            profit = 0
        else:
            week_high_value = week_high_element.findParent().text.split()[0]
            week_high = float(week_high_value.replace(",", ""))

            week_low_value = week_low_element.findParent().text.split()[0]
            week_low = float(week_low_value.replace(",", ""))
            potential_profit = week_high / week_low

            profit = round(potential_profit, 2)
        COMPANY_INFO[company_url]["potential profit"] = profit


def save_to_json(filename, value_name, data):
    with open(filename + ".json", "w") as file:
        top_10 = [
            {
                "name": data[i]["name"],
                "code": data[i]["code"],
                f"{value_name}": data[i][value_name],
            }
            for i in range(10)
        ]
        json.dump(top_10, file, indent=4)


def top_10_companies():
    save_to_json("price", "price", nlargest(10,
                                            COMPANY_INFO.values(),
                                            key=lambda x: x["price"]))
    save_to_json("pe", "P/E", nsmallest(10,
                                        COMPANY_INFO.values(),
                                        key=lambda x: x["P/E"]))
    save_to_json("growth", "growth", nlargest(10,
                                              COMPANY_INFO.values(),
                                              key=lambda x: x["growth"]))
    save_to_json("profit", "potential profit",
                 nlargest(10,
                          COMPANY_INFO.values(),
                          key=lambda x: x["potential profit"]))


if __name__ == "__main__":
    company_list()
    get_pe_ratio()
    get_potential_profit()
    # print(COMPANY_INFO)
    top_10_companies()
