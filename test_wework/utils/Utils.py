
import json
class Utils:
    @classmethod
    def format(cls, json_object):
        return json.dumps(json_object, indent=2)