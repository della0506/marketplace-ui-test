# -*- coding: utf-8 -*-
import seldom
from seldom import Seldom
from page.marketplace_page import MarketplacePage
from func.common_func import commonFunc

class MarketplaceTest(seldom.TestCase):
    global page
    page = MarketplacePage(Seldom.driver)

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
        """Click logo"""
        page.icon_link.click()
        self.switch_to_window(1)
        self.refresh()
        self.sleep(1)
        self.assertUrl(commonFunc.readYaml(self).get('delysium_url'))

    def test02(self):
        """Click Collectibles type"""
        page.collectibles_link.click()
        self.assertText(commonFunc.readYaml(self).get('collectibles_name'))
        self.assertNotText(commonFunc.readYaml(self).get('weapon_name'))

    def test03(self):
        """Click Weapon type"""
        page.weapon_link.click()
        self.assertText(commonFunc.readYaml(self).get('weapon_name'))
        self.assertNotText(commonFunc.readYaml(self).get('collectibles_name'))

    def test04(self):
        """Click All Items type"""
        page.all_items_link.click()
        self.assertText(commonFunc.readYaml(self).get('weapon_name'))
        self.assertText(commonFunc.readYaml(self).get('collectibles_name'))

    def test05(self):
        """Click Suit type"""
        page.suit_link.click()
        self.assertText(commonFunc.readYaml(self).get('comming_soon'))

    def test06(self):
        """Click Cuberbody type"""
        page.cyberboy_link.click()
        self.assertText(commonFunc.readYaml(self).get('comming_soon'))

    def test07(self):
        """Click Battle Pass type"""
        page.battle_pass_link.click()
        self.assertText(commonFunc.readYaml(self).get('comming_soon'))

    def test08(self):
        """Search no result"""
        page.search_input.input(commonFunc.testText(self))
        self.assertText(commonFunc.readYaml(self).get('no_nft'))

    def test09(self):
        """Clear search key"""
        page.search_input.input(commonFunc.testText(self))
        page.search_input.select_all()
        page.search_input.delete()
        self.assertNotText(commonFunc.readYaml(self).get('no_nft'))

    def test10(self):
        """Search have result"""
        page.search_input.input(commonFunc.readYaml(self).get('weapon_name'))
        self.assertText(commonFunc.readYaml(self).get('weapon_name'))
        self.assertEqual(page.nft_name.text,commonFunc.readYaml(self).get('weapon_name'))

    def test11(self):
        """Open rarity select"""
        page.rarity_select.click()
        self.wait(1)
        self.assertElement(xpath=commonFunc.pageElement(self))

    def test12(self):
        """Filter rarity-common"""
        page.rarity_select.click()
        page.common_select.click()
        self.assertEqual(page.rarity_value.get_attribute('value'), 'Common')

    def test13(self):
        """Filter rarity-rare"""
        page.rarity_select.click()
        page.rare_select.click()
        self.assertEqual(page.rarity_value.get_attribute('value'), 'Rare')

    def test14(self):
        """Filter rarity-epic"""
        page.rarity_select.click()
        page.epic_select.click()
        self.assertEqual(page.rarity_value.get_attribute('value'), 'Epic')

    def test15(self):
        """Filter rarity-legendary"""
        page.rarity_select.click()
        page.legendary_select.click()
        self.assertEqual(page.rarity_value.get_attribute('value'), 'Legendary')

    def test16(self):
        """Filter rarity-ultimate"""
        page.rarity_select.click()
        page.ultimate_select.click()
        self.assertEqual(page.rarity_value.get_attribute('value'), 'Ultimate')

    def test17(self):
        """Filter items and rarity"""
        page.rarity_select.click()
        page.common_select.click()
        self.assertEqual(page.rarity_value.get_attribute('value'), 'Common')
        page.weapon_link.click()
        self.assertText(commonFunc.readYaml(self).get('weapon_name'))
        self.assertNotText(commonFunc.readYaml(self).get('collectibles_name'))
        page.collectibles_link.click()
        self.assertEqual(page.rarity_value.get_attribute('value'), 'Common')
        page.rarity_select.click()
        page.rare_select.click()
        self.assertEqual(page.rarity_value.get_attribute('value'), 'Rare')
        self.assertEqual(page.collectibles_link.get_attribute('aria-selected'),'true')

    def test18(self):
        """Search in items"""
        page.weapon_link.click()
        self.assertText(commonFunc.readYaml(self).get('weapon_name'))
        page.search_input.input(commonFunc.testText(self))
        self.assertText(commonFunc.readYaml(self).get('no_nft'))
        page.search_input.select_all()
        page.search_input.delete()
        page.search_input.input(commonFunc.readYaml(self).get('weapon_name'))
        self.assertText(commonFunc.readYaml(self).get('weapon_name'))
        self.assertNotText(commonFunc.readYaml(self).get('collectibles_name'))


    def test19(self):
        """Search in rarity"""
        page.rarity_select.click()
        page.common_select.click()
        self.assertEqual(page.rarity_value.get_attribute('value'), 'Common')
        page.search_input.input(commonFunc.readYaml(self).get('weapon_name'))
        self.assertText(commonFunc.readYaml(self).get('weapon_name'))
        self.assertNotText(commonFunc.readYaml(self).get('collectibles_name'))

    def test20(self):
        """Search in items and rarity"""
        page.weapon_link.click()
        self.assertText(commonFunc.readYaml(self).get('weapon_name'))
        page.search_input.input(commonFunc.testText(self))
        self.assertText(commonFunc.readYaml(self).get('no_nft'))
        page.search_input.select_all()
        page.search_input.delete()
        page.search_input.input(commonFunc.readYaml(self).get('weapon_name'))
        self.assertText(commonFunc.readYaml(self).get('weapon_name'))
        self.assertNotText(commonFunc.readYaml(self).get('collectibles_name'))
        page.rarity_select.click()
        page.rare_select.click()
        self.assertText(commonFunc.readYaml(self).get('no_nft'))
        page.rarity_select.click()
        page.common_select.click()
        self.assertText(commonFunc.readYaml(self).get('weapon_name'))
        self.assertNotText(commonFunc.readYaml(self).get('collectibles_name'))

    def test21(self):
        """Scroll page"""
        self.window_scroll(width=0, height=10000)
        self.wait(1)
        self.window_scroll(width=0, height=10000)
        self.assertText(commonFunc.readYaml(self).get('scroll_nft'))

    def test22(self):
        """Check copyright"""
        self.assertText('All rights reserved.')
