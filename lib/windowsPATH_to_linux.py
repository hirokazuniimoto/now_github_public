#python3

#
# this is the program which change windows path such as '\'
# to linux path ( for programm can use)
#
# 2021/06/08
# author hirokazu niimoto
#

import sys

class WindowPATH_to_linux(object):
    """docstring forWindowPATH_to_linux."""

    def __init__(self,path):
        self.path = path

    def windowsPATH_to_linux(self):
        new_path = self.path.replace('\\','/')
        return new_path
