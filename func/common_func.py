import os
import random
import yaml

class commonFunc():

    def baseUrl(self):
        """test env"""
        baseUrl = 'https://delysium-market.vercel.app/'
        return baseUrl

    def testText(self):
        """test data"""
        text = random.sample('abcdefghijklmnopqrstuvwxyz',6)
        return ''.join(text)

    def readYaml(self):
        """read yaml"""
        fs = open(os.getcwd()+"/data/data.yaml")
        data = yaml.load(fs,Loader=yaml.FullLoader)
        fs.close()
        return data

    def pageElement(self):
        """Filter element form page"""
        ele = '//div[@id="menu-"]/div[3]/ul'
        return ele
