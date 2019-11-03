from test_wework.api.message import Message


class TestMessage:
    message=Message()
    def test_send_text(self):
        self.message.send_text("你的快递已到，请携带工卡前往邮件中心领取。\n出发前可查看<a href=\"http://work.weixin.qq.com\">邮件中心视频实况</a>，聪明避开排队。",
                               users=[ "SiHan"])
        assert self.message.jsonpath("$.errcode")==0
