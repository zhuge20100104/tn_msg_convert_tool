import os 
from .consts import DATA_DIR

def get_message_files(ext=".txt"):
    paths = list()
    for file_ in os.listdir(DATA_DIR):
        # Only consider files ends with .txt as long message files
        if file_.endswith(ext):
            path_ = os.path.join(DATA_DIR, file_)
            paths.append(path_)
    return paths
    