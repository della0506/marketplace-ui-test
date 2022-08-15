# -*- coding: utf-8 -*-
import os
import requests
import json

def testReport():
    """send report to Feishu"""
    path = os.getcwd() + '/reports'
    name = os.listdir(path)
    print(type(name),name)
    fileName = list(filter(lambda a:a.find("result") >= 0,name))
    print(fileName)
    #return ''.join(fileName)

    p = {
    "msg_type": "interactive",
    "card": {
        "config": {
                "wide_screen_mode": True,
                "enable_forward": True
        },
        "elements": [{
                "actions": [{
                        "tag": "button",
                        "text": {
                                "content": "Click For Details 🔍",
                                "tag": "lark_md"
                        },
                        "url": "https://jenkins.dev-metaverse.fun/view/test/job/test-pegasus-ui-automation/_e5afb9_e8af9d_e7b3bb_e7bb9fUI_e887aa_e58aa8_e58c96_e6b58b_e8af95_e68aa5_e5918a/",
                        "type": "default",
                        "value": {}
                }],
                "tag": "action"
        }],
        "header": {
                "title": {
                        "content": "🔔 Marketplace UI Automation Testing Report",
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
