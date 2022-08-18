# -*- coding: utf-8 -*-
import seldom
from seldom import Seldom
from page.inventory_page import InventoryPage
from page.marketplace_page import MarketplacePage
from func.common_func import commonFunc

class InventoryTest(seldom.TestCase):
    global page,m_page
    page = InventoryPage(Seldom.driver)
    m_page = MarketplacePage(Seldom.driver)

    def start(self):
        """init"""
        page.open(commonFunc.baseUrl(self)+page.inventory_url)
        self.max_window()
        self.assertText(commonFunc.readYaml(self).get('inventory_no_nft'))

    def down(self):
        """quit"""
        self.quit()

    @classmethod
    def setUpClass(cls):
        cls().start()

    def test01(self):
        """Connect wallet and cancel """
        page.connect_wallet.click()
        self.assertText(commonFunc.readYaml(self).get('connect_title'))
        self.assertText('MetaMask')
        page.cancel_button.click()
        self.assertNotText(commonFunc.readYaml(self).get('connect_title'))
        self.assertNotText('MetaMask')
        self.assertText(commonFunc.readYaml(self).get('inventory_no_nft'))

    def test02(self):
        """Click discord"""
        page.connect_wallet.click()
        self.assertText(commonFunc.readYaml(self).get('connect_title'))
        self.assertText('MetaMask')
        page.discord_link.click()
        self.assertUrl(commonFunc.readYaml(self).get('wallet_discord_url'))

    def test03(self):
        """Click Collectibles type"""
        m_page.collectibles_link.click()
        self.assertEqual(m_page.collectibles_link.get_attribute('aria-selected'),'true')
        self.assertText(commonFunc.readYaml(self).get('inventory_no_nft'))

    def test04(self):
        """Click Weapon type"""
        m_page.weapon_link.click()
        self.assertEqual(m_page.weapon_link.get_attribute('aria-selected'),'true')
        self.assertText(commonFunc.readYaml(self).get('inventory_no_nft'))

    def test05(self):
        """Click All Items type"""
        m_page.all_items_link.click()
        self.assertEqual(m_page.all_items_link.get_attribute('aria-selected'),'true')
        self.assertText(commonFunc.readYaml(self).get('inventory_no_nft'))

    def test06(self):
        """Click Suit type"""
        m_page.suit_link.click()
        self.assertText(commonFunc.readYaml(self).get('comming_soon'))

    def test07(self):
        """Click Cuberbody type"""
        m_page.cyberboy_link.click()
        self.assertText(commonFunc.readYaml(self).get('comming_soon'))

    def test08(self):
        """Click Battle Pass type"""
        m_page.battle_pass_link.click()
        self.assertText(commonFunc.readYaml(self).get('comming_soon'))

    def test09(self):
        """Search in search bar"""
        m_page.search_input.input(commonFunc.testText(self))
        self.assertText(commonFunc.readYaml(self).get('inventory_no_nft'))

    def test10(self):
        """Clear search key"""
        m_page.search_input.input(commonFunc.readYaml(self).get('weapon_name'))
        m_page.search_input.select_all()
        m_page.search_input.delete()
        self.assertText(commonFunc.readYaml(self).get('inventory_no_nft'))

    def test11(self):
        """Open rarity select"""
        m_page.rarity_select.click()
        self.wait(1)
        self.assertElement(m_page.rarity_list)

    def test12(self):
        """Filter rarity-common"""
        m_page.rarity_select.click()
        m_page.common_select.click()
        self.assertEqual(m_page.rarity_value.get_attribute('value'),'Common')

    def test13(self):
        """Filter rarity-rare"""
        m_page.rarity_select.click()
        m_page.rare_select.click()
        self.assertEqual(m_page.rarity_value.get_attribute('value'), 'Rare')

    def test14(self):
        """Filter rarity-epic"""
        m_page.rarity_select.click()
        m_page.epic_select.click()
        self.assertEqual(m_page.rarity_value.get_attribute('value'), 'Epic')

    def test15(self):
        """Filter rarity-legendary"""
        m_page.rarity_select.click()
        m_page.legendary_select.click()
        self.assertEqual(m_page.rarity_value.get_attribute('value'), 'Legendary')

    def test16(self):
        """Filter rarity-ultimate"""
        m_page.rarity_select.click()
        m_page.ultimate_select.click()
        self.assertEqual(m_page.rarity_value.get_attribute('value'), 'Ultimate')

    def test17(self):
        """Filter items and rarity"""
        m_page.rarity_select.click()
        m_page.rare_select.click()
        self.assertEqual(m_page.rarity_value.get_attribute('value'), 'Rare')
        m_page.weapon_link.click()
        self.assertEqual(m_page.weapon_link.get_attribute('aria-selected'),'true')
        self.assertEqual(m_page.rarity_value.get_attribute('value'), 'Rare')
        self.assertText(commonFunc.readYaml(self).get('inventory_no_nft'))

    def test18(self):
        """Search in items"""
        m_page.weapon_link.click()
        self.assertEqual(m_page.weapon_link.get_attribute('aria-selected'),'true')
        self.assertText(commonFunc.readYaml(self).get('inventory_no_nft'))
        m_page.search_input.input(commonFunc.readYaml(self).get('weapon_name'))
        self.assertText(commonFunc.readYaml(self).get('inventory_no_nft'))

    def test19(self):
        """Search in rarity"""
        m_page.rarity_select.click()
        m_page.ultimate_select.click()
        self.assertEqual(m_page.rarity_value.get_attribute('value'), 'Ultimate')
        m_page.search_input.input(commonFunc.readYaml(self).get('weapon_name'))
        self.assertText(commonFunc.readYaml(self).get('inventory_no_nft'))
        self.assertEqual(m_page.rarity_value.get_attribute('value'), 'Ultimate')

    def test20(self):
        """Search in items and rarity"""
        m_page.weapon_link.click()
        self.assertEqual(m_page.weapon_link.get_attribute('aria-selected'),'true')
        m_page.search_input.input(commonFunc.testText(self))
        self.assertText(commonFunc.readYaml(self).get('inventory_no_nft'))
        self.assertEqual(m_page.weapon_link.get_attribute('aria-selected'), 'true')
        m_page.search_input.select_all()
        m_page.search_input.delete()
        m_page.search_input.input(commonFunc.readYaml(self).get('weapon_name'))
        self.assertText(commonFunc.readYaml(self).get('inventory_no_nft'))
        self.assertEqual(m_page.weapon_link.get_attribute('aria-selected'), 'true')
        m_page.rarity_select.click()
        m_page.rare_select.click()
        self.assertText(commonFunc.readYaml(self).get('inventory_no_nft'))
        self.assertEqual(m_page.weapon_link.get_attribute('aria-selected'), 'true')
        self.assertEqual(m_page.rarity_value.get_attribute('value'), 'Rare')

    def test21(self):
        """Check copyright"""
        self.assertText('All rights reserved.')
