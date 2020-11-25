import requests

from test_wework.api.base_api import BaseApi
from test_wework.api.wework import WeWork


class Message(BaseApi):
    _send_url = "https://qyapi.weixin.qq.com/cgi-bin/message/send"

    def send_text(self, msg=None, users=[], parties=[], tags=[]):

        self.json_data = requests.post(
            self._send_url,
            params={"access_token": WeWork.get_app_token()},
            # 需要设置UTF8编码
            headers={'content-type': 'application/json; charset=utf-8'},
            json={
                "touser": "|".join(users),
                "toparty": "|".join(parties),
                "totag": "|".join(tags),
                "msgtype": "text",
                "agentid": WeWork.agent_id,
                "text": {
                    "content": msg
                },
                "safe": 0,
                "enable_id_trans": 0
            },
            # proxies=self.proxies,
            verify=False
        ).json()
        self.verbose(self.json_data)

    def send_voice(self):
        pass

    def send_video(self):
        pass
