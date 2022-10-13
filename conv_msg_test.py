from utility.funcs import get_message_files
from utility.json_str_converter import JsonStrConverter
from utility.long_msg_converter import LongMsgConvertor

from google.protobuf import text_format
from google.protobuf import json_format

from person.Person_pb2 import Person

# Convert long msg to short passed
#  Provide long msg from ./tmq_topic as  input, You can also do some modification on the long msg
#  Output the short msg we use in test cases
def test_convert_long_msg_to_short():
    msg_files = get_message_files()
    for msg_file in msg_files:
        print("")
        print("----------------------------------------------------------------------------------")
        print("Msg file name: " + msg_file)
        lng_msg_conv = LongMsgConvertor(msg_file)
        conv_res = lng_msg_conv.convert()
        print("Result: " + conv_res)
        print("----------------------------------------------------------------------------------")
        print("")
 
# Convert json msg to short debug string passed
# Provide json msg written by yourself , You can do some modification on the raw json file
# Output the short debug string we use in test cases
def test_convert_json_to_debug_string():
    json_files = get_message_files(".json")
    for json_file in json_files:
        print("")
        print("----------------------------------------------------------------------------------")
        print("Msg file name: " + json_file)
        js_msg_conv = JsonStrConverter(json_file)
        conv_res = js_msg_conv.convert()
        conv_res = conv_res.replace("\n", " ").replace('"', '\\"')
        print("Result: " + conv_res)
        print("----------------------------------------------------------------------------------")
        print("")

def test_raw_protobuf_method():
    person = Person()
    person.name = "Zhangsan"
    person.id = 10
    # print(dir(person))

    person_str = str(person)
    print(person_str)
    p1 = Person()

    text = '''name: "Lisi" id: 20 isok: false grade: 3'''
    text_format.Parse(text, p1)

    print(str(p1))

    p2 = Person()
    js_text = '''{"name": "Zhangsan", "id": 20, "isok": true, "grade": 4}'''
    json_format.Parse(js_text, p2)
    res = str(p2) 
    print(res)   

