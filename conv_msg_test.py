from utility.funcs import get_message_files
from utility.json_str_converter import JsonStrConverter
from utility.long_msg_converter import LongMsgConvertor

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

