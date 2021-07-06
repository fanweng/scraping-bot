#!/usr/bin/env python3

class Product:
    def __init__(self, url=None, name=None, variant=None, part_num=None):
        self.url = url
        self.name = name
        self.variant = variant
        self.part_number = part_num
        self.price = None
        self.currency = None
    
    def setPrice(self, price=None):
        self.price = price[0]
        self.currency = price[1]

FENIX6_URL = "https://buy.garmin.com/en-CA/CA/p/641479/pn/010-02158-10"
FENIX6_NAME = "fēnix® 6 - Pro and Sapphire Editions"
FENIX6_VARIANT = "Sapphire - Carbon Gray DLC with Black Band"
FENIX6_PART_NUMBER = "010-02158-10"

fenix6 = Product(FENIX6_URL, FENIX6_NAME, FENIX6_VARIANT, FENIX6_PART_NUMBER)