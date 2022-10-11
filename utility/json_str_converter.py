import json 
from collections import OrderedDict


class RetObj(object):
    def __init__(self, long_res, level=0):
        self.long_res = long_res
        self.level = level

# Converter convert from json object to  short debug string
class JsonStrConverter(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def convert(self):
        json_obj = None
        with open(self.file_name) as f:
            json_obj = json.load(f, object_pairs_hook=OrderedDict)
        ret_obj = RetObj("", -1)
        self.convert_from_json_obj(json_obj,  ret_obj)
        return ret_obj.long_res
  
    
    def convert_from_json_obj(self, json_obj, ret_obj):
        for key, value in json_obj.items():
            #  Single dict add 1 level to pretty print the dict
            if isinstance(value, OrderedDict):
                ret_obj.level += 1
                ret_obj.long_res  += " "*(2*ret_obj.level)
                ret_obj.long_res += key
                ret_obj.long_res += " "
                ret_obj.long_res += "{\n"
                self.convert_from_json_obj(value, ret_obj)
                ret_obj.long_res  += " "*(2*ret_obj.level)
                ret_obj.long_res += "}\n"
            #  Multiple element in 1 list, only need to add 1 level, since multiple elements are in the same level
            elif isinstance(value, list):
                ret_obj.level += 1
                for single_value in value:
                    ret_obj.long_res  += " "*(2*ret_obj.level)
                    ret_obj.long_res += key
                    ret_obj.long_res += " "
                    ret_obj.long_res += "{\n"
                    self.convert_from_json_obj(single_value, ret_obj)
                    ret_obj.long_res  += " "*(2*ret_obj.level)
                    ret_obj.long_res += "}\n"
            else:
                #  Single key value add 1 level
                ret_obj.level += 1
                ret_obj.long_res  += " "*(2*ret_obj.level)
                ret_obj.long_res += key
                ret_obj.long_res += ": "
                ret_obj.long_res += str(value) 
                ret_obj.long_res += "\n"
            #  After each level has been printed to the str, we need to reset the current level
            ret_obj.level -= 1
                