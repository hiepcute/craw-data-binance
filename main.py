import sys
import time
import sqlite3
import requests
from help import setup_logging

logger = setup_logging()
import pandas as pd
import matplotlib.pyplot as plt
from help import setup_logging
arr_day = []
arr_price = []
logger=setup_logging()

def main(name):
    print(f"Hello {name}")

url=" https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"
def get_respone_from_website(urlx):
    endpoint = url
    body = {
        "page": 1,
        "rows": 10,
        "payTypes": [],
        "asset": "USDT",
        "tradeType": "BUY",
        "fiat": "VND",
        "publisherType": "merchant"
    }
    # Dinh dang data
    headers = {
        "Content-Type": "application/json"
    }

    reponse = requests.post(url=endpoint, headers=headers, json=body)
    if reponse:
        logger.info("get reponse")
    else:
        logger.info(" cant connect")
        return 0
    return reponse


def cal_avg_price_coin_in_website(reponse):
    content = reponse.json()['data']
    try:
        with sqlite3.connect('price.db') as conn:
            curs = conn.cursor()
            curs.execute("CREATE TABLE IF NOT EXISTS price (Price REAL)")
            logger.info("CREATE TABLE")
            price = 0
            for each in content:
                price = float(each['adv']['price'])
                arr_price.append(price)
                arr_day.append(datetime.now())
                curs.execute("INSERT INTO price VALUES (?)", (price,))
                logger.info("INSERT DATA TO DATABASE")
            data = {'day': arr_day, 'price': arr_price}
            df = pd.DataFrame(data)
            print(price)
        return df,data
    except Exception as er:
        print(er)
        return 0


def draw_price_coin_binance(df,data):
    df = pd.DataFrame(data, columns=['day', 'price'])
    print(df)
    df.plot(x='day', y='price', kind='scatter')
    plt.show()










if __name__ == '__main__':
    print("Running!")
    logger.info("----------")
    respone=get_respone(url)
    df,data=cal_avg(respone)
    draw(df,data)
    print("end")


