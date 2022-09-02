# -*- coding: utf-8 -*-
from poium import Page, Element

class LoginPage(Page):
    """Website Page"""
    #play button
    play_but = Element(xpath='//span[contains(text(),"Play")]')

    #email
    email_input = Element(xpath='//label[contains(text(),"Email")]/following-sibling::div/div/input')

    #password
    password_input = Element(xpath='//label[contains(text(),"Password")]/following-sibling::div/div/input')
    
    #close
    close = Element(xpath='//div[@class="dialog-close"]')
