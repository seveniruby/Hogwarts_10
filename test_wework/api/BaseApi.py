from test_wework.utils.Utils import Utils
import pprint

class BaseApi:
    printer=pprint.PrettyPrinter(indent=2)
    json_data=None

    @classmethod
    def verbose(cls, json_object):
        print(Utils.format(json_object))
        #cls.printer.pprint(json_object)

    @classmethod
    def jsonpath(cls, expr):
        return Utils.jsonpath(cls.json_data, expr)
