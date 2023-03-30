"""
# dbclient
A simple but pwerful way to manage local databases in Python!
"""

import os
import threading


class Directory:
    def __init__(self, directory) -> None:
        self.dir = directory
        self.lock = threading.Lock()

    def __getitem__(self, target):

        with self.lock:
            slice_type = type(target)
            if slice_type == str:
                path = os.path.join(self.dir, target)
                if os.path.isdir(path):
                    return Directory(path)
                else:
                    return Data(path)
    
    def __repr__(self) -> str:
        return f"<Directory {self.dir}>"

class Data:
    def __init__(self, path) -> None:
        self.path = path