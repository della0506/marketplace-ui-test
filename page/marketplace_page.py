# -*- coding: utf-8 -*-
from poium import Page, Element

class MarketplacePage(Page):
    """Marketplace Page"""
    #icon
    icon_link = Element(xpath='//img[starts-with(@class,"MuiBox-root")]')

    #marketplace
    marketplace_tab = Element(xpath='//button[contains(text(),"marketplace")]')

    #inventory
    inventory_tab = Element(xpath='//button[contains(text(),"inventory")]')

    #All Items
    all_items_link = Element(xpath='//button[contains(text(),"All Items")]')

    #Collectibles
    collectibles_link = Element(xpath='//button[contains(text(),"Collectibles")]')

    #Weapon
    weapon_link = Element(xpath='//button[contains(text(),"Weapon")]')

    #Suit
    suit_link = Element(xpath='//button[contains(text(),"Suit")]')

    #Cyberbody
    cyberboy_link = Element(xpath='//button[contains(text(),"Cyberbody")]')

    #Battle Pass
    battle_pass_link = Element(xpath='//button[contains(text(),"Battle Pass")]')

    #Search
    search_input = Element(xpath='//input[@id="mui-4"]')

    #Rarity
    rarity_select = Element(xpath='//*[@id="root"]/div[3]/div/div[3]/div[1]/div[2]/div/div')

    #Rarity list
    rarity_list = Element(xpath='//div[@id="menu-"]/div[3]/ul')

    #Rarity value
    rarity_value = Element(xpath='//*[@id="root"]/div[3]/div/div[3]/div[1]/div[2]/div/div/input')

    #all
    all_select = Element(xpath='//li[contains(text(),"all rarities")]')

    #common
    common_select = Element(xpath='//li[@data-value="Common"]')

    #rare
    rare_select = Element(xpath='//li[@data-value="Rare"]')

    #epic
    epic_select = Element(xpath='//li[@data-value="Epic"]')

    #legendary
    legendary_select = Element(xpath='//li[@data-value="Legendary"]')

    #ultimate
    ultimate_select = Element(xpath='//li[@data-value="Ultimate"]')

    #nft name
    nft_name = Element(xpath='//div[@id="root"]/div[3]/div/div[3]/div[2]/div/a/div/div[1]/p')

    #right
    copyright = Element(xpath='//p[contains(text(),"Copyright")]')