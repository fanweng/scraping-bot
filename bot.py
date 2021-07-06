#!/usr/bin/env python3

import time
# import requests
from datetime import datetime
from selenium_driver import driver
from discord_client import client, TOKEN, WEBHOOK_URL
from discord import Webhook, RequestsWebhookAdapter
from items import fenix6

def getWebPrice(driver):
    class Price:
        def __init__(self, webelement=None):
            if webelement:
                self.amount = webelement.text.split()[1]
                self.currency = webelement.text.split()[2]
            else:
                raise ValueError('Invalid WebElement')
    try:
        driver.refresh()
        price = Price(driver.find_element_by_id('js__product__price__main'))
        return price.amount, price.currency
    except Exception as e:
        e_str = str(e)
        print(f'ERROR in getWebPrice(): {e_str}!')

def main():
    driver.get(fenix6.url)

    iteration = 10
    while iteration > 0:
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%y %H:%M:%S")

        fenix6.setPrice(getWebPrice(driver))
        msg = f'{fenix6.name} price is {fenix6.price} {fenix6.currency}'
        print(f'{dt_string} {msg}')


        # TODO: Method 1 - Use Discord client or bot command to send message
        # client.run(TOKEN)

        # Method 2 - Use guild webhook to send message
        webhook = Webhook.from_url(WEBHOOK_URL, adapter=RequestsWebhookAdapter())
        webhook.send(f'{dt_string} {msg}')

        time.sleep(60)
        iteration = iteration - 1

    driver.close()

if __name__ == "__main__":
    main()