# -*- coding: utf-8 -*-
import seldom
from seldom import Seldom
from page.login_page import LoginPage

class LoginTest(seldom.TestCase):
    global page
    page = LoginPage(Seldom.driver)

    def start(self):
        """init"""
        page.open('https://www.delysium.com/account/login')
        self.max_window()
        self.assertText('Play on the Web')

    def end_class(self):
        """quit"""
        self.close()

    @classmethod
    def setUpClass(cls):
        cls().start()

    def test01(self):
        """login"""
        page.play_but.click()
        self.assertText('Forget Password')
        page.email_input.input('linyunong@rct.ai')
        page.password_input.input('Mywork-0')
        page.play_but.click()
        page.close.click()
        self.wait(2)
        self.assertText('Server Browser')
