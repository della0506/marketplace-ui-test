# -*- coding: utf-8 -*-
from poium import Page, Element

class CommunityPage(Page):
    """Community Page"""
    #community
    community_tab = Element(xpath='//div[contains(text(),"community")]')

    #medium
    medium_link = Element(xpath='//*[@id="mui-1"]/div/a[1]')

    #twitter
    twitter_link = Element(xpath='//*[@id="mui-1"]/div/a[2]')

    #discord
    discord_link = Element(xpath='//*[@id="mui-1"]/div/a[3]')

    #telegram
    telegram_link = Element(xpath='//*[@id="mui-1"]/div/a[4]')

    #youtube
    youtube_link = Element(xpath='//*[@id="mui-1"]/div/a[5]')