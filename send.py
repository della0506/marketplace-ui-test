# -*- coding: utf-8 -*-
import os
import requests
import json
from bs4 import BeautifulSoup

def testReport():
    """Read test report html"""
    path = os.getcwd() + '/reports'
    name = os.listdir(path)
    print(type(name),name)
    fileName = list(filter(lambda a:a.find("result") >= 0,name))
    print(fileName)
    print(path+'/'+''.join(fileName))
    with open('/var/lib/jenkins/workspace/test-marketplace-ui-automation/reports/'+''.join(fileName),'r') as f:
        soup = BeautifulSoup(f.read(),'html.parser')
        passNum = soup.select('span[class="badge badge-pill bg-soft-success text-success me-2"]')[0].text
        failNum = soup.select('span[class="badge badge-pill bg-soft-warning text-warning me-2"]')[0].text
        errNum = soup.select('span[class="badge badge-pill bg-soft-danger text-danger me-2"]')[0].text
        
    """Send report to Feishu"""
    p = {
    "msg_type": "interactive",
    "card": {
        "config": {
                "wide_screen_mode": True,
                "enable_forward": True
        },
        "elements": [
            {
                "tag": "div",
                "text": {
                    "content": f"{passNum}     ｜     {failNum}     ｜     {errNum}",
                    "tag": "lark_md"
                }
            }, {
                    "actions": [{
                            "tag": "button",
                            "text": {
                                    "content": "🔍 CLICK HERE FOR DETAILS",
                                    "tag": "lark_md"
                            },
                            "url": "https://jenkins.dev-metaverse.fun/view/test/job/test-marketplace-ui-automation/Marketplace_20Test_20Report/",
                            "type": "default",
                            "value": {}
                    }],
                    "tag": "action"
            }],
            "header": {
                    "title": {
                            "content": f"🔔 Marketplace UI Automation Test Report",
                            "tag": "plain_text"
                    }
            }
        }
    }
    toFS = requests.post('https://open.feishu.cn/open-apis/bot/v2/hook/1eba2ae5-9ad4-4acc-b3fe-3b53ce9f97a7',json.dumps(p))
    print(toFS.status_code, toFS.json())
    return toFS

if __name__ == '__main__':
    testReport()
