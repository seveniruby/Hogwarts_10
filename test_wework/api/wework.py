import requests

from test_wework.api.BaseApi import BaseApi


class WeWork(BaseApi):
    corpid="wwd6da61649bd66fea"
    agent_id="1000010"
    agent_secret="pAF_eP3FlN3d6-GxGFESaEwL1G5or1UQmHjkc9rtTj8"
    contact_secret="C7uGOrNyxWWzwBsUyWEbLdbZBDrc71PNOhyQ_YYPhts"
    access_token=None

    @classmethod
    def get_token(cls):
        if cls.access_token==None:
            url="https://qyapi.weixin.qq.com/cgi-bin/gettoken"
            r=requests.get(url, params={ "corpid": cls.corpid, "corpsecret": cls.contact_secret}).json()
            print("first get token")
            cls.verbose(r)
            cls.access_token=r["access_token"]

        return WeWork.access_token