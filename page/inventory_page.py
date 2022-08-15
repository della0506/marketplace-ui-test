# -*- coding: utf-8 -*-
from poium import Page, Element


class InventoryPage(Page):
    """Inventory Page"""
    #url
    inventory_url = 'inventory'

    #wallet
    connect_wallet = Element(xpath='//p[contains(text(),"Connect Wallet")]')

    #cancel
    cancel_button = Element(xpath='//div[starts-with(@class,"MuiDialogContent-root")]/button')

    #discord
    discord_link = Element(xpath='//a[starts-with(@class,"MuiTypography-root MuiTypography-caption")]')
