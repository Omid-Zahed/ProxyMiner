import requests
import json


def ProxyTest(proxy, myIp=0):
    proxies = {
        'http': proxy,
        'https': proxy,

    }
    testIpUrl = 'https://api64.ipify.org/?format=json'
    try:
        if myIp == 0:
            firstReq = requests.get(testIpUrl)
            if firstReq.status_code == 200:
                myIp = json.loads(firstReq.text)["ip"]

        nextReq = requests.get(testIpUrl, proxies=proxies)
        if nextReq.status_code == 200:
            nextIp = json.loads(nextReq.text)["ip"]

            if nextIp != myIp:
                return True
            else:
                return False
        else:
            return False


    except IOError:
        return False
