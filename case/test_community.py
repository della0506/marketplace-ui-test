# -*- coding: utf-8 -*-
import seldom
from seldom import Seldom
from page.community_page import CommunityPage
from func.common_func import commonFunc

class CommunityTest(seldom.TestCase):
    global page
    page = CommunityPage(Seldom.driver)

    def start(self):
        """init"""
        page.open(commonFunc.baseUrl(self))
        self.max_window()
        self.assertText('All Items')
        self.assertText('Connect Wallet')

    def down(self):
        """quit"""
        self.quit()

    @classmethod
    def setUpClass(cls):
        cls().start()

    def test01(self):
        """Check link collection"""
        page.community_tab.click()
        self.assertText('Medium')
        self.assertText('Twitter')
        self.assertText('Discord')
        self.assertText('Telegram')
        self.assertText('YouTube')

    def test02(self):
        """Open medium"""
        page.community_tab.click()
        page.medium_link.click()
        self.switch_to_window(1)
        self.assertUrl(commonFunc.readYaml(self).get('medium_url'))

    def test03(self):
        """Open Twitter"""
        page.community_tab.click()
        page.twitter_link.click()
        self.switch_to_window(2)
        self.assertUrl(commonFunc.readYaml(self).get('twitter_url'))

    def test04(self):
        """Open Discord"""
        page.community_tab.click()
        page.discord_link.click()
        self.switch_to_window(3)
        self.assertUrl(commonFunc.readYaml(self).get('discord_url'))

    def test05(self):
        """Open Telegram"""
        page.community_tab.click()
        page.telegram_link.click()
        self.switch_to_window(4)
        self.assertUrl(commonFunc.readYaml(self).get('telegram_url'))

    def test06(self):
        """Open YouTube"""
        page.community_tab.click()
        page.youtube_link.click()
        self.switch_to_window(5)
        self.assertUrl(commonFunc.readYaml(self).get('youtube_url'))
