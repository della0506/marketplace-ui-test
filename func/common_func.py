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

    def pageToString(self,page):
        """Transfer element to string"""
        ele = str(page)[8:-1]
        return ele