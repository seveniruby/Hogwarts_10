from time import sleep, time

from selenium import webdriver

from test_po.contact_page import ContactPage
from test_po.wework_page import Wework


class TestContact:

    def setup(self):
        self.work=Wework()
        self.contact=ContactPage(self.work)

    def teardown(self):
        sleep(20)
        self.work.quit()
    def test_add_member(self):

        self.contact.add_member("seveniruby", "seveniruby", "seveniruby", "15600534700")
        assert self.contact.get_tips() == "OK"

    def test_add_member_chinese(self):
        self.contact.add_member("思寒", "思寒", "seveniruby_1", "15600534701")
        assert self.contact.get_tips() == "OK"

    def test_delete(self):
        udid=str(time())
        self.contact\
            .add_member("思寒"+udid, "思寒"+udid, "seveniruby_1"+udid, "15600534701")

    def test_update_profile(self):
        self.contact.search("seveniruby").update( name="seveniruby %s" % str(time()))


