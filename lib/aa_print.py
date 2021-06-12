#python3
#
#this is AA print Class file
#
# 2021/06/08
# author hirokazu niimoto

#色付けライブラリ（Windows初期化）
from colorama import init
init()
#色付けライブラリ
from colorama import Fore, Back, Style

class AA_PRINT(object):
    """docstring forAA_PRINT."""

    def __init__(self):
        self.welcomeAA = '''

        #    # ###### #       ####   ####  #    # ######
        #    # #      #      #    # #    # ##  ## #
        #    # #####  #      #      #    # # ## # #####
        # ## # #      #      #      #    # #    # #
        ##  ## #      #      #    # #    # #    # #
        #    # ###### ######  ####   ####  #    # ######

        '''

        self.toAA = '''
        #####  ####
          #   #    #
          #   #    #
          #   #    #
          #   #    #
          #    ####
        '''

        self.nameAA = '''
        #    #  ####  #    #          ####  # ##### #    # #    # #####
        ##   # #    # #    #         #    # #   #   #    # #    # #    #
        # #  # #    # #    #         #      #   #   ###### #    # #####
        #  # # #    # # ## #         #  ### #   #   #    # #    # #    #
        #   ## #    # ##  ##         #    # #   #   #    # #    # #    #
        #    #  ####  #    #          ####  #   #   #    #  ####  #####

        '''

    def AA_print(self):
        #AAの出力
        print(Fore.CYAN + self.welcomeAA)

        print(Fore.CYAN + self.toAA)

        print(Fore.BLUE + self.nameAA)

        #カラーをリセット
        print(Style.RESET_ALL)
        print("\n\n")
