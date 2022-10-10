import os 

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")
print("ROOT_DIR: " + ROOT_DIR)
print("DATA_DIR:" + DATA_DIR)